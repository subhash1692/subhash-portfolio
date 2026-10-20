(() => {
  'use strict';
  const toggle = document.querySelector('.menu-toggle');
  const menu = document.querySelector('#site-links');
  if (toggle && menu) {
    const closeMenu = () => {
      toggle.setAttribute('aria-expanded', 'false');
      toggle.setAttribute('aria-label', 'Open navigation');
      menu.classList.remove('is-open');
    };
    toggle.addEventListener('click', () => {
      const opened = toggle.getAttribute('aria-expanded') !== 'true';
      toggle.setAttribute('aria-expanded', String(opened));
      toggle.setAttribute('aria-label', opened ? 'Close navigation' : 'Open navigation');
      menu.classList.toggle('is-open', opened);
    });
    menu.querySelectorAll('a').forEach(link => link.addEventListener('click', closeMenu));
    document.addEventListener('keydown', event => { if (event.key === 'Escape') closeMenu(); });
    document.addEventListener('click', event => { if (!menu.contains(event.target) && !toggle.contains(event.target)) closeMenu(); });
  }

  const copyButton = document.querySelector('[data-copy-email]');
  if (copyButton) {
    copyButton.addEventListener('click', async () => {
      const email = copyButton.getAttribute('data-copy-email');
      const oldText = copyButton.textContent;
      try {
        if (!navigator.clipboard || !window.isSecureContext) throw new Error('Clipboard unavailable');
        await navigator.clipboard.writeText(email);
        copyButton.textContent = 'Email copied ✓';
        setTimeout(() => { copyButton.textContent = oldText; }, 2200);
      } catch (error) {
        window.location.href = `mailto:${email}`;
      }
    });
  }
  const year = document.getElementById('year');
  if (year) year.textContent = String(new Date().getFullYear());
})();
