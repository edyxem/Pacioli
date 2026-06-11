// ===== NAVIGATION ENTRE VUES =====
const viewTitles = {
  tableau:      'Tableau de bord',
  recettes:     'Recettes',
  depenses:     'Dépenses',
  clients:      'Clients',
  fournisseurs: 'Fournisseurs',
  journal:      'Journal',
  bilan:        'Bilan',
};

function switchView(viewName) {
  // Cacher toutes les vues
  document.querySelectorAll('.view').forEach(v => v.classList.remove('active'));

  // Afficher la vue cible
  const target = document.querySelector(`[data-view="${viewName}"]`);
  if (target) target.classList.add('active');

  // Mettre à jour le titre
  const titleEl = document.getElementById('pageTitle');
  if (titleEl) titleEl.textContent = viewTitles[viewName] || viewName;

  // Mettre à jour le dock
  document.querySelectorAll('nav.dock button').forEach(btn => {
    btn.classList.toggle('active', btn.dataset.go === viewName);
  });

  window.scrollTo({ top: 0, behavior: 'smooth' });
}

document.querySelectorAll('nav.dock button').forEach(btn => {
  btn.addEventListener('click', () => switchView(btn.dataset.go));
});

// ===== TOGGLE GRAPHIQUE =====
document.querySelectorAll('.toggle button').forEach(btn => {
  btn.addEventListener('click', () => {
    btn.parentElement.querySelectorAll('button').forEach(b => b.classList.remove('on'));
    btn.classList.add('on');
  });
});

// ===== RECHERCHE CLIENT EN TEMPS RÉEL =====
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

// ===== MESSAGES DJANGO — AUTO FERMETURE =====
document.querySelectorAll('.messages li').forEach(msg => {
  setTimeout(() => {
    msg.style.transition = 'opacity .5s';
    msg.style.opacity = '0';
    setTimeout(() => msg.remove(), 500);
  }, 4000);
});

// ===== CONFIRMATION SUPPRESSION =====
document.querySelectorAll('.btn-delete-confirm').forEach(btn => {
  btn.addEventListener('click', function (e) {
    if (!confirm('Confirmer la suppression ?')) {
      e.preventDefault();
    }
  });
});