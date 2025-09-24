// Simple tilt interaction for elements with [data-tilt]
(() => {
  document.querySelectorAll('[data-tilt]').forEach(el => {
    const inner = el.querySelector('.card-inner') || el;
    el.addEventListener('mousemove', (e) => {
      const rect = el.getBoundingClientRect();
      const x = (e.clientX - rect.left) / rect.width - 0.5;
      const y = (e.clientY - rect.top) / rect.height - 0.5;
      const ry = x * 10; const rx = -y * 8;
      inner.style.transform = `rotateX(${rx}deg) rotateY(${ry}deg) translateZ(6px)`;
    });
    el.addEventListener('mouseleave', () => { inner.style.transform = '' });
  });

  // Contact buttons (mailto / open link)
  document.querySelectorAll('.btn').forEach(btn => {
    btn.addEventListener('click', (e) => {
      const mailto = btn.dataset.mailto;
      const link = btn.dataset.link;
      if (mailto) {
        window.location.href = `mailto:${mailto}`;
      } else if (link) {
        window.open(link, '_blank', 'noopener');
      }
    });
  });

  // Hobbies chips: toggle selected state and persist
  const STORAGE_KEY = 'portfolio_hobbies_v1';
  const saved = JSON.parse(localStorage.getItem(STORAGE_KEY) || '[]');
  document.querySelectorAll('.chip').forEach(chip => {
    const hobby = chip.dataset.hobby;
    if (saved.includes(hobby)) { chip.classList.add('selected'); chip.setAttribute('aria-pressed','true') }
    chip.addEventListener('click', () => {
      const selected = chip.classList.toggle('selected');
      chip.setAttribute('aria-pressed', selected ? 'true' : 'false');
      let cur = JSON.parse(localStorage.getItem(STORAGE_KEY) || '[]');
      if (selected) { if (!cur.includes(hobby)) cur.push(hobby) }
      else { cur = cur.filter(h => h !== hobby) }
      localStorage.setItem(STORAGE_KEY, JSON.stringify(cur));
    });
  });
})();