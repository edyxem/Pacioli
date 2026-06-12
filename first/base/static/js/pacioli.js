// ===== MESSAGES DJANGO — AUTO FERMETURE =====
document.addEventListener('DOMContentLoaded', () => {
  document.querySelectorAll('.messages li').forEach(msg => {
    setTimeout(() => {
      msg.style.transition = 'opacity .5s';
      msg.style.opacity = '0';
      setTimeout(() => msg.remove(), 500);
    }, 4000);
  });
});


// ===== RECHERCHE TIERS EN TEMPS RÉEL =====
const searchInput = document.getElementById('searchClient');
if (searchInput) {
  searchInput.addEventListener('input', function () {
    const query = this.value.toLowerCase();
    document.querySelectorAll('.client').forEach(card => {
      const name = card.querySelector('h3')?.textContent.toLowerCase() || '';
      card.style.display = name.includes(query) ? '' : 'none';
    });
  });
}

// ===== THEME SWITCH =====
document.addEventListener('DOMContentLoaded', () => {
  const btn = document.getElementById('themeToggle');
  const root = document.documentElement;

  if (!btn) return;

  // Appliquer le thème sauvegardé (le script inline dans <head> l'a déjà posé,
  // mais on s'assure que l'icône s'affiche correctement dès le rendu)
  const saved = localStorage.getItem('pacioli-theme') || 'light';
  root.setAttribute('data-theme', saved);

  btn.addEventListener('click', () => {
    const current = root.getAttribute('data-theme') || 'light';
    const next = current === 'dark' ? 'light' : 'dark';
    root.setAttribute('data-theme', next);
    localStorage.setItem('pacioli-theme', next);

    // Petite animation de rotation au clic
    btn.style.transition = 'transform .35s cubic-bezier(.34,1.56,.64,1), box-shadow .2s';
    btn.style.transform = 'rotate(360deg) scale(1.12)';
    setTimeout(() => { btn.style.transform = ''; }, 350);
  });
});