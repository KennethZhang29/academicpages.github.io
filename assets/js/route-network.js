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
  let animationId = 0;

  const colors = () => darkMode()
    ? {
        edge: 'rgba(174, 132, 230, 0.13)',
        route: 'rgba(201, 160, 255, 0.58)',
        node: 'rgba(228, 211, 255, 0.64)',
      }
    : {
        edge: 'rgba(103, 64, 151, 0.09)',
        route: 'rgba(111, 68, 167, 0.38)',
        node: 'rgba(91, 57, 135, 0.42)',
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
    context.clearRect(0, 0, width, height);
    const palette = colors();
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
