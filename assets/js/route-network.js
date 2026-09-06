(() => {
  const canvas = document.getElementById('route-network');

  if (!canvas) return;

  const context = canvas.getContext('2d');
  if (!context) return;

  const reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)');
  const darkMode = () => document.documentElement.dataset.theme === 'dark';
  let width = 0;
  let height = 0;
  let scale = 1;
  let nodes = [];
  let frame = 0;
  let lastPaint = 0;
  let animationId = 0;

  const colors = () => darkMode()
    ? {
        background: ['#100a1b', '#21143a', '#102b31', '#321626'],
        violet: 'rgba(157, 104, 234, 0.32)',
        aqua: 'rgba(51, 181, 177, 0.24)',
        coral: 'rgba(222, 104, 122, 0.18)',
        edge: 'rgba(220, 197, 255, 0.1)',
        route: 'rgba(227, 207, 255, 0.42)',
        node: 'rgba(239, 226, 255, 0.52)',
      }
    : {
        background: ['#faf7ff', '#e6ddf7', '#d7efeb', '#f6e0e5'],
        violet: 'rgba(116, 70, 194, 0.2)',
        aqua: 'rgba(18, 139, 143, 0.16)',
        coral: 'rgba(211, 102, 118, 0.12)',
        edge: 'rgba(81, 50, 126, 0.075)',
        route: 'rgba(93, 53, 153, 0.3)',
        node: 'rgba(72, 45, 112, 0.34)',
      };

  const seededValue = (index, offset) => {
    const value = Math.sin((index + 1) * 12.9898 + offset * 78.233) * 43758.5453;
    return value - Math.floor(value);
  };

  const createNodes = () => {
    const count = Math.max(16, Math.min(30, Math.floor(width / 55)));

    nodes = Array.from({ length: count }, (_, index) => ({
      x: seededValue(index, 1) * width,
      y: seededValue(index, 2) * height,
      radius: 1.1 + seededValue(index, 3) * 1.5,
      phase: seededValue(index, 4) * Math.PI * 2,
      driftX: (seededValue(index, 5) - 0.5) * 7,
      driftY: (seededValue(index, 6) - 0.5) * 6,
    }));
  };

  const resize = () => {
    width = window.innerWidth;
    height = window.innerHeight;
    scale = Math.min(window.devicePixelRatio || 1, 1.5);
    canvas.width = Math.floor(width * scale);
    canvas.height = Math.floor(height * scale);
    canvas.style.width = `${width}px`;
    canvas.style.height = `${height}px`;
    context.setTransform(scale, 0, 0, scale, 0, 0);
    createNodes();
    draw();
  };

  const positionAt = (node, time) => ({
    x: node.x + Math.sin(time * 0.00017 + node.phase) * node.driftX,
    y: node.y + Math.cos(time * 0.00015 + node.phase) * node.driftY,
  });

  const drawFlowBand = ({ center, thickness, amplitude, frequency, speed, phase, color }, time) => {
    const step = Math.max(36, width / 28);
    const offset = reducedMotion.matches ? 0 : time * speed;

    context.beginPath();
    for (let x = -step; x <= width + step; x += step) {
      const y = center
        + Math.sin(x * frequency + offset + phase) * amplitude
        + Math.sin(x * frequency * 0.43 - offset * 0.7 + phase) * amplitude * 0.35;
      if (x === -step) context.moveTo(x, y - thickness);
      else context.lineTo(x, y - thickness);
    }

    for (let x = width + step; x >= -step; x -= step) {
      const y = center
        + Math.sin(x * frequency + offset + phase) * amplitude
        + Math.sin(x * frequency * 0.43 - offset * 0.7 + phase) * amplitude * 0.35;
      context.lineTo(x, y + thickness);
    }

    context.closePath();
    context.fillStyle = color;
    context.fill();
  };

  const drawFlowField = (palette, time) => {
    const shift = reducedMotion.matches ? 0 : Math.sin(time * 0.000055) * width * 0.18;
    const gradient = context.createLinearGradient(-width * 0.2 + shift, 0, width * 1.2 + shift, height);
    gradient.addColorStop(0, palette.background[0]);
    gradient.addColorStop(0.34, palette.background[1]);
    gradient.addColorStop(0.67, palette.background[2]);
    gradient.addColorStop(1, palette.background[3]);
    context.fillStyle = gradient;
    context.fillRect(0, 0, width, height);

    context.save();
    context.filter = `blur(${Math.max(42, Math.min(90, width * 0.055))}px)`;
    context.globalCompositeOperation = darkMode() ? 'screen' : 'multiply';
    drawFlowBand({
      center: height * 0.2,
      thickness: height * 0.17,
      amplitude: height * 0.11,
      frequency: 0.0033,
      speed: 0.00017,
      phase: 0.8,
      color: palette.violet,
    }, time);
    drawFlowBand({
      center: height * 0.58,
      thickness: height * 0.2,
      amplitude: height * 0.14,
      frequency: 0.0025,
      speed: -0.00012,
      phase: 2.1,
      color: palette.aqua,
    }, time);
    drawFlowBand({
      center: height * 0.9,
      thickness: height * 0.14,
      amplitude: height * 0.09,
      frequency: 0.0041,
      speed: 0.0001,
      phase: 4.4,
      color: palette.coral,
    }, time);
    context.restore();
  };

  const drawNetwork = (positions, palette) => {
    context.lineWidth = 0.7;
    context.strokeStyle = palette.edge;

    positions.forEach((point, index) => {
      const nearest = positions
        .map((candidate, candidateIndex) => ({
          candidate,
          candidateIndex,
          distance: Math.hypot(point.x - candidate.x, point.y - candidate.y),
        }))
        .filter(({ candidateIndex, distance }) => candidateIndex !== index && distance < 230)
        .sort((a, b) => a.distance - b.distance)
        .slice(0, 2);

      nearest.forEach(({ candidate, candidateIndex }) => {
        if (candidateIndex < index) return;
        context.beginPath();
        context.moveTo(point.x, point.y);
        context.lineTo(candidate.x, candidate.y);
        context.stroke();
      });
    });
  };

  const drawRoute = (positions, palette, time) => {
    const route = positions.filter((_, index) => index % 3 === 0).slice(0, 8);
    const visibleSegments = reducedMotion.matches
      ? route.length - 1
      : Math.min(route.length - 1, Math.floor((time / 900) % (route.length + 3)));

    context.lineWidth = 1.8;
    context.strokeStyle = palette.route;
    context.beginPath();

    route.forEach((point, index) => {
      if (index > visibleSegments) return;
      if (index === 0) context.moveTo(point.x, point.y);
      else context.lineTo(point.x, point.y);
    });

    context.stroke();
  };

  const drawNodes = (positions, palette, time) => {
    positions.forEach((point, index) => {
      const pulse = reducedMotion.matches ? 1 : 0.75 + Math.sin(time * 0.0015 + index) * 0.25;
      context.fillStyle = palette.node;
      context.beginPath();
      context.arc(point.x, point.y, nodes[index].radius * pulse, 0, Math.PI * 2);
      context.fill();
    });
  };

  const draw = (time = 0) => {
    if (!reducedMotion.matches && time && time - lastPaint < 32) {
      animationId = window.requestAnimationFrame(draw);
      return;
    }

    lastPaint = time;
    context.clearRect(0, 0, width, height);
    const palette = colors();
    drawFlowField(palette, time);
    const positions = nodes.map((node) => positionAt(node, time));
    drawNetwork(positions, palette);
    drawRoute(positions, palette, time);
    drawNodes(positions, palette, time);

    if (!reducedMotion.matches && !document.hidden) {
      frame = time;
      animationId = window.requestAnimationFrame(draw);
    }
  };

  const restart = () => {
    window.cancelAnimationFrame(animationId);
    draw(frame);
  };

  window.addEventListener('resize', resize, { passive: true });
  reducedMotion.addEventListener('change', restart);
  document.addEventListener('visibilitychange', restart);
  new MutationObserver(restart).observe(document.documentElement, {
    attributes: true,
    attributeFilter: ['data-theme'],
  });

  resize();
})();
