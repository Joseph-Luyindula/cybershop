# Mini Système de Recommandation de Produits

Un projet Django simple qui recommande automatiquement des produits à un utilisateur en fonction de :

- ses 10 dernières consultations,
- ses préférences de catégories,
- sa moyenne de prix habituelle,
- et les produits similaires lorsqu’il consulte un article.

---

## Fonctionnalités

- Recommandations personnalisées (catégories + prix + historique)
- Détection automatique d’une vue après 5 secondes via Swiper.js
- Produits similaires sur la fiche produit
- Interface simple, orientée logique

---

## Installation

### 1. Cloner le projet

```bash
git clone https://github.com/joseph-luyindula/cybershop.git
cd cybershop
```

### 2. Créer et activer un environnement virtuel

```bash
python -m venv env
source env/bin/activate  # sous Windows : env\Scripts\activate
```

### 3. Installer les dépendances

```bash
pip install -r requirements.txt
```

> Si le fichier `requirements.txt` n’existe pas, tu peux l’auto-générer :
> `pip freeze > requirements.txt`

### 4. Appliquer les migrations

```bash
python manage.py migrate
```

### 5. Créer un super utilisateur

```bash
python manage.py createsuperuser
```

### 6. Lancer le serveur

```bash
python manage.py runserver
```

Accède ensuite à `http://127.0.0.1:8000`.

---

## Structure des recommandations

### Recommandation personnalisée (`global_recommendations`)
- Se base sur les 10 derniers produits consultés
- Récupère les catégories dominantes
- Calcule la moyenne de prix
- Filtre des produits similaires non encore consultés
> À savoir au début il peut arriver qu'il recommande un produit d'une autre catégorie mais dont le prix et assez proche des prix que vous observez 

### Produits similaires (`mini_recommendation`)
- Recommande des produits partageant les mêmes catégories qu’un produit donné
> Fonctionnalités utiliser dans la page d'un article 
 
---

## Vue automatique après 3 secondes (Swiper.js)

Quand un utilisateur fait défiler horizontalement les produits :

- Le produit actuellement visible est détecté
- Après 3 secondes, une requête AJAX POST est envoyée vers `/register-view/`
- Cela enregistre une nouvelle `ProductView` côté Django

```javascript
// Exemple de logique JS
viewTimers[currentSlideIndex] = setTimeout(() => {
  registerView(productId);
}, 3000);
```

---

## Modèles de base

- `Category` : Catégorie de produit
- `Product` : Produit avec prix et description
- `UserProfile` : Préférences de l’utilisateur (catégories et prix moyen)
- `ProductView` : Historique des consultations

---

## Fichiers importants

| Fichier | Rôle |
|--------|------|
| `models.py` | Structure de la base de données |
| `views.py` | Vues Django pour recommandations |
| `templates/` | Interface HTML minimaliste |
| `utils.py` | Fonctions de logique de recommandation |

---

## À venir (suggestions d'évolution)

- récupérer certaines des données des utilisateurs (toute en ce rassurant que les identités, les informations de payement soit protégé) pour créer plus tard un modèle de machines learnning.

---

## Auteur

Projet réalisé par Joseph Luyindula 
Contact : josephluyindula00@gmail.com

