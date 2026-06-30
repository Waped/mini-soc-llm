# 🛡️ Mini SOC LLM

Un mini-agent conversationnel destiné à assister un Security Operations Center (SOC) dans l'analyse d'alertes de sécurité.

Le projet reçoit une alerte de sécurité au format JSON, enrichit son analyse grâce à une base de connaissances (RAG simple) et utilise Gemini 2.5 Flash pour produire une analyse structurée comprenant :

- Classification de la menace
- Niveau de sévérité
- Contexte MITRE ATT&CK
- Recommandations d'investigation
- Actions de remédiation

Ce projet a été réalisé dans le cadre d'un projet personnel afin d'approfondir les technologies LLM appliquées à la cybersécurité.

---

#  Fonctionnalités

- Analyse automatique d'alertes de sécurité
- API REST avec FastAPI
- RAG simple basé sur des fichiers texte
- Intégration de Gemini 2.5 Flash
- Réponses JSON structurées
- Retry automatique en cas d'erreur
- Fallback si le modèle n'est pas disponible
- Conteneurisation avec Docker
- Pipeline CI avec GitHub Actions

---

#  Technologies utilisées

- Python 3.10
- FastAPI
- Google Gemini 2.5 Flash
- Docker
- GitHub Actions
- python-dotenv

---

#  Structure du projet

```
mini-soc-llm/
│
├── app/
│   ├── api.py
│   ├── llm.py
│   ├── parser.py
│   ├── prompts.py
│   ├── rag.py
│   ├── utils.py
│   ├── main.py
│   └── __init__.py
│
├── alerts/
│   └── alert1.json
│
├── knowledge/
│   ├── mitre_attack.txt
│   └── soc_playbook.txt
│
├── .github/
│   └── workflows/
│
├── Dockerfile
├── requirements.txt
└── README.md
```

---

#  Installation

## 1. Cloner le dépôt

```bash
git clone https://github.com/<ton-utilisateur>/mini-soc-llm.git

cd mini-soc-llm
```

---

## 2. Créer un environnement virtuel

Sous Linux / WSL :

```bash
python3 -m venv .venv
```

Activer l'environnement :

```bash
source .venv/bin/activate
```

Sous Windows PowerShell :

```powershell
python -m venv .venv

.venv\Scripts\Activate.ps1
```

---

## 3. Installer les dépendances

```bash
pip install -r requirements.txt
```

---

## 4. Configurer la clé API Gemini

Créer un fichier `.env` à la racine du projet.

```
GEMINI_API_KEY=VotreCleAPI
```

---

#  Exécution en local

## Mode CLI

```bash
python -m app.main
```

---

## Mode API

Lancer FastAPI :

```bash
uvicorn app.api:app --reload
```

Puis ouvrir :

```
http://localhost:8000/docs
```

---

#  Exécution avec Docker

## Construire l'image

```bash
docker build -t mini-soc-llm .
```

## Lancer le conteneur

```bash
docker run --env-file .env -p 8000:8000 mini-soc-llm
```

L'API sera disponible à l'adresse :

```
http://localhost:8000/docs
```

---

#  Exemple de requête

POST `/analyze`

```json
{
  "timestamp": "2026-06-29T14:00:00Z",
  "event": "Multiple failed login attempts",
  "source_ip": "192.168.1.50",
  "destination_host": "DC01",
  "user": "administrator"
}
```

---

#  Exemple de réponse

```json
{
  "incident_type": "Brute Force Attempt",
  "severity": "High",
  "mitre_technique": "T1110",
  "confidence": 0.94,
  "recommendation": [
    "Block the source IP",
    "Investigate authentication logs",
    "Reset the impacted account password"
  ]
}
```

---

#  Pipeline CI

À chaque `git push` sur la branche `main`, GitHub Actions :

- installe les dépendances
- exécute le projet
- vérifie que le build est valide

---

#  Améliorations possibles

- Intégration avec un SIEM (Microsoft Sentinel, Splunk...)
- Utilisation d'une base vectorielle pour le RAG
- Authentification de l'API
- Déploiement sur Azure
- Analyse de plusieurs alertes simultanément

---

# 👤 Auteur

**Alioune Thiaw**

Étudiant en Mastère Cybersécurité & Cloud – EFREI Paris

Projet personnel réalisé dans le cadre d'un apprentissage des LLM appliqués au SOC.