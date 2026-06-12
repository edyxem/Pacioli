# 📒 Pacioli

> *"Luca Pacioli a inventé la comptabilité en 1494. Nous, on a juste fait une app cool avec."*

Pacioli est un logiciel de comptabilité simple, propre et sans prise de tête, conçu pour les petites entreprises qui veulent garder un œil sur leur argent sans se noyer dans des tableurs Excel de 47 colonnes.

---

## ✨ Ce que Pacioli sait faire

- 💰 **Recettes & Dépenses** — Enregistre, modifie, supprime. Simple comme bonjour.
- 👥 **Clients & Fournisseurs** — Ton annuaire business, propre et searchable.
- 📊 **Tableau de bord** — Solde en temps réel, graphique de flux de trésorerie sur la semaine, les 7 dernières semaines ou les 6 derniers mois.
- 📄 **Rapports** — Journal des opérations, bilan simplifié, état des recettes/dépenses, rapport global. Tout ça exportable en PDF.
- 🔐 **Authentification** — Deux rôles : Administrateur et Comptable. Chacun à sa place.
- 🗂️ **Catégories** — Classe tes opérations pour t'y retrouver facilement.
- 🖥️ **Application Desktop** — Disponible en tant qu'app Windows native grâce à Electron.

---

## 🛠️ Stack technique

| Élément | Technologie |
|---|---|
| Backend | Django 5 + Django REST Framework |
| Base de données | PostgreSQL |
| Frontend | HTML / CSS / JS vanilla |
| Police | Ubuntu (Google Fonts) |
| PDF | ReportLab |
| Authentification | Sessions Django natives |
| Desktop | Electron |

---

## 🚀 Installation

### Prérequis

- Python 3.10+
- Node.js 18+ et npm
- PostgreSQL

---

### Mode Web (navigateur)

#### 1. Clone le projet

```bash
git clone https://github.com/ton-repo/pacioli.git
cd pacioli
```

#### 2. Crée et active l'environnement virtuel

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Mac / Linux
source venv/bin/activate
```

#### 3. Installe les dépendances Python

```bash
pip install django djangorestframework psycopg2-binary reportlab
```

#### 4. Configure la base de données

Crée une base PostgreSQL :

```sql
CREATE DATABASE pacioli_db;
CREATE USER pacioli_user WITH PASSWORD '';
GRANT ALL PRIVILEGES ON DATABASE pacioli_db TO pacioli_user;
```

Puis dans `first/settings.py`, ajuste les identifiants si besoin.

#### 5. Applique les migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

#### 6. Crée un superutilisateur

```bash
python manage.py createsuperuser
```

#### 7. Lance le serveur

```bash
python manage.py runserver
```

Ouvre **http://localhost:8000** et profite. 🎉

---

### Mode Desktop (Electron)

> Assure-toi que PostgreSQL tourne et que le venv Django est configuré avant de lancer Electron.

#### 1. Installe les dépendances Node

```bash
cd electron
npm install
```

#### 2. Lance l'application desktop

```bash
npm start
```

Electron démarre Django en arrière-plan et ouvre l'application dans une fenêtre native. Aucun navigateur nécessaire.

#### 3. Générer le fichier `.exe` (Windows)

```bash
npm run build
```

L'installateur Windows sera généré dans `electron/dist/`. Il peut être distribué et installé sur n'importe quelle machine Windows disposant de Python et PostgreSQL.

---

## 📁 Structure du projet

```
pacioli/
├── base/           → Layout principal, dashboard, statiques
├── users/          → Authentification (login, signup, logout)
├── recettes/       → Gestion des recettes
├── depenses/       → Gestion des dépenses
├── tiers/          → Clients et fournisseurs
├── rapports/       → Journal, bilan, exports PDF
├── first/          → Configuration Django (settings, urls)
└── electron/       → Wrapper Electron (app desktop)
    ├── index.js    → Processus principal Electron
    └── package.json
```

---

## 🎨 Design

Le design s'inspire des apps fintech modernes — fond clair, noir profond `#0a0a0a`, typographie Ubuntu, dock de navigation fixe en bas, cartes arrondies avec ombres douces. Sobre mais pas ennuyeux.

---

## 👤 Rôles utilisateurs

| Rôle | Accès |
|---|---|
| **Administrateur** | Tout — utilisateurs, rapports, sauvegarde |
| **Comptable** | Recettes, dépenses, clients, fournisseurs, rapports |

---

## 📊 Graphique de trésorerie

Le dashboard affiche un graphique de flux de trésorerie avec trois vues :

- **Semaine** — du lundi au dimanche de la semaine courante
- **7 semaines** — les 7 dernières semaines glissantes
- **6 mois** — les 6 derniers mois

Les données sont calculées en temps réel depuis la base de données. Pas de données statiques, pas de mensonges.

---

## 📄 Export PDF

Le bilan est exportable en PDF directement depuis l'interface. Le PDF inclut :

- Les KPIs (recettes, dépenses, résultat net)
- Le tableau complet des recettes
- Le tableau complet des dépenses
- Le résultat final avec indicateur bénéfice / déficit

---

## 🗺️ Roadmap

- [x] Authentification et gestion des rôles
- [x] CRUD Recettes / Dépenses / Clients / Fournisseurs
- [x] Catégories d'opérations
- [x] Dashboard avec graphique multi-vues
- [x] Journal des opérations avec filtres par date
- [x] Bilan simplifié + export PDF
- [x] Packaging Electron (app desktop Windows)
- [ ] Sauvegarde automatique
- [ ] Export Excel
- [ ] Historique des connexions
- [ ] Restauration d'une sauvegarde

---

## 👨‍💻 Auteur

**Elidjé Emmanuel Marie-Edgar Tossou**
Licence 2 Informatique — IIT VITIB, Grand-Bassam, Côte d'Ivoire

> Projet académique réalisé dans le cadre du cours de développement logiciel — 2026

---

## 📜 Licence

Ce projet est à usage académique. Fais-en bon usage. 🤝
