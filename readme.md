# 📚 LITReview

LITReview est une application web construite avec Django, qui permet aux utilisateurs de publier ou demander des critiques de livres et d’articles, de suivre d’autres membres, et de gérer leurs publications dans un flux personnalisé.

---

## 🔍 Fonctionnalités principales

### Utilisateurs
- Inscription / Connexion / Déconnexion
- Suivre et se désabonner d'autres utilisateurs
- Voir la liste des utilisateurs suivis

### Billets (Tickets)
- Créer un billet pour demander une critique
- Ajouter une image facultative
- Voir, modifier et supprimer ses billets

### Critiques (Reviews)
- Répondre à un billet en publiant une critique
- Créer une critique indépendamment d’un billet (critique “à partir de zéro”)
- Voir, modifier et supprimer ses critiques
- Notation de 0 à 5

### Flux personnalisé
- Affiche les billets et critiques :
  - De l’utilisateur connecté
  - Des utilisateurs suivis
  - Les critiques reçues sur les billets de l’utilisateur connecté
- Ordonné de manière antéchronologique

---

## 🛠️ Technologies utilisées

- **Framework** : Django 
- **Base de données** : SQLite
- **Frontend** : HTML/CSS 
- **Authentification** : Système intégré de Django
- **Gestion des médias** : `ImageField` de Django

---


## 🚀 Installation et démarrage

### 1. Cloner le dépôt

```bash
git clone git@github.com:Caroleloop/oc_python_9_Developpez_une_application_Web_en_utilisant_Django.git
cd LITReview
```

### 2. Créer et activer un environnement virtuel

```bash
python -m venv env
source env/bin/activate ou env\Scripts\activate 
```

### 3. Installer les dépendances

```bash
pip install -r requirements.txt
```

### 4. Appliquer les migrations

```bash
python manage.py migrate
```

### 5. Démarrer le serveur

```bash
python manage.py runserver
```

### 6. Accéder au site

Ouvrir [http://127.0.0.1:8000](http://127.0.0.1:8000) dans un navigateur.

---