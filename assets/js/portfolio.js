(() => {
  const reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)');
  const tabButtons = Array.from(document.querySelectorAll('[data-folio-tab]'));
  const tabPanels = Array.from(document.querySelectorAll('[data-folio-panel]'));

  const selectTab = (button) => {
    const target = button.dataset.folioTab;

    tabButtons.forEach((item) => {
      const active = item === button;
      item.classList.toggle('is-active', active);
      item.setAttribute('aria-selected', String(active));
      item.tabIndex = active ? 0 : -1;
    });

    tabPanels.forEach((panel) => {
      const active = panel.dataset.folioPanel === target;
      panel.hidden = !active;
      panel.classList.toggle('is-active', active);
    });
  };

  tabButtons.forEach((button, index) => {
    button.addEventListener('click', () => selectTab(button));
    button.addEventListener('keydown', (event) => {
      if (!['ArrowDown', 'ArrowUp', 'ArrowLeft', 'ArrowRight'].includes(event.key)) return;
      event.preventDefault();
      const direction = ['ArrowDown', 'ArrowRight'].includes(event.key) ? 1 : -1;
      const nextIndex = (index + direction + tabButtons.length) % tabButtons.length;
      tabButtons[nextIndex].focus();
      selectTab(tabButtons[nextIndex]);
    });
  });

  const revealItems = document.querySelectorAll('.folio-reveal');
  if (reducedMotion.matches || !('IntersectionObserver' in window)) {
    revealItems.forEach((item) => item.classList.add('is-visible'));
    return;
  }

  const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (!entry.isIntersecting) return;
      entry.target.classList.add('is-visible');
      observer.unobserve(entry.target);
    });
  }, { rootMargin: '0px 0px -8% 0px', threshold: 0.12 });

  revealItems.forEach((item) => observer.observe(item));
})();
