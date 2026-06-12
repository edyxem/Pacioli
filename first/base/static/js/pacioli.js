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