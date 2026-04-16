# 🏭 IndustriAI : Système de Maintenance Prédictive IoT

[![Python](https://img.shields.io/badge/Python-3.13-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-Framework-009688.svg)](https://fastapi.tiangolo.com/)
[![Docker](https://img.shields.io/badge/Docker-Ready-2496ED.svg)](https://www.docker.com/)
[![Machine Learning](https://img.shields.io/badge/ML-Isolation_Forest-FF6F00.svg)](https://scikit-learn.org/)

> Une solution complète de détection d'anomalies industrielles en temps réel, alliant IoT, Intelligence Artificielle et monitoring interactif.

---

## 🌟 Aperçu du Projet

Ce projet simule un environnement industriel où des capteurs (Température & Vibration) envoient des flux de données constants. Une Intelligence Artificielle analyse ces flux pour prédire les pannes avant qu'elles n'arrivent, le tout visualisable sur une tour de contrôle interactive.

### 📸 Capture d'écran
*(Ajoute ici ton GIF ou ton image `image_a43042.png` pour l'effet "Wow")*
![Dashboard Preview](votre_lien_image_ou_chemin_relatif)

---

## 🧠 Intelligence Artificielle Expliquable (XAI)

Contrairement aux modèles "boîtes noires", **IndustriAI** intègre une couche d'explicabilité. L'algorithme **Isolation Forest** détecte les comportements anormaux, et le système identifie instantanément la cause :
- 🌡️ **Surchauffe critique**
- 🫨 **Vibrations mécaniques anormales**
- 📉 **Rapports Temp/Vib inhabituels**

---

## 🛠️ Architecture Technique

Le projet est découpé en micro-services conteneurisés :

1.  **Le Simulateur (IoT)** : Génère des données réalistes de capteurs avec injection aléatoire d'anomalies.
2.  **L'API (FastAPI)** : Le cœur du système. Reçoit les données, interroge l'IA et archive les résultats.
3.  **Le Cerveau (Scikit-Learn)** : Modèle de Machine Learning entraîné pour la détection d'outliers.
4.  **La Base de Données (SQLite)** : Persistance de l'historique des performances machine.
5.  **Le Dashboard (Streamlit & Plotly)** : Interface utilisateur fluide avec rafraîchissement en temps réel et gestion intelligente du zoom (Sliding Window).

---

## 🚀 Installation Rapide (Mode Docker)

C'est l'avantage d'IndustriAI : **une seule commande suffit** pour lancer toute l'usine sur votre machine.

**Pré-requis :** [Docker Desktop](https://www.docker.com/products/docker-desktop/) installé et lancé.

```bash
# 1. Cloner le projet
git clone [https://github.com/votre-pseudo/detecteur-anomalies-production.git](https://github.com/votre-pseudo/detecteur-anomalies-production.git)
cd detecteur-anomalies-production

# 2. Lancer l'architecture complète
docker-compose up --build -d
