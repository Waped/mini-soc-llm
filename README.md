# Mini SOC LLM

## Présentation

Mini SOC LLM est un projet personnel développé dans le cadre de ma formation en Mastère Cybersécurité & Cloud à l'EFREI Paris.

L'objectif est de simuler un assistant IA capable d'aider un analyste SOC à analyser automatiquement une alerte de sécurité grâce à un Large Language Model (LLM).

Le projet s'inspire des assistants IA utilisés dans les Security Operations Centers pour accélérer les premières phases d'investigation.

---

## Fonctionnalités

* Analyse d'une alerte de sécurité au format JSON
* Génération automatique d'un rapport d'analyse
* Classification de la menace
* Référence aux techniques MITRE ATT&CK
* Recommandations d'investigation
* Recommandations de remédiation
* Mini-RAG basé sur une base de connaissances locale
* API REST développée avec FastAPI
* Conteneurisation avec Docker
* Pipeline CI/CD avec GitHub Actions
* Gestion des erreurs avec retry et fallback

---

## Architecture

```text
Client
   │
POST /analyze
   │
FastAPI
   │
Agent SOC
   │
Mini RAG
   │
Gemini 2.5 Flash
   │
Réponse JSON
```

---

## Technologies

* Python
* FastAPI
* Google Gemini 2.5 Flash
* Docker
* GitHub Actions
* JSON
* Git

---

## Installation

Créer un environnement virtuel :

```bash
python -m venv .venv
```

Activer l'environnement :

Linux / WSL :

```bash
source .venv/bin/activate
```

Installer les dépendances :

```bash
pip install -r requirements.txt
```

Créer un fichier `.env` :

```text
GEMINI_API_KEY=your_api_key
```

---

## Lancer l'API

```bash
uvicorn app.api:app --reload
```

Documentation interactive :

```
http://127.0.0.1:8000/docs
```

---

## Exemple de requête

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

## Exemple de réponse

```json
{
  "incident_type": "Brute Force",
  "severity": "High",
  "mitre_technique": "T1110",
  "confidence": 0.95,
  "summary": "...",
  "investigation_steps": [],
  "remediation_actions": []
}
```

---

## Évolutions possibles

* Intégration d'un SIEM
* RAG avec base vectorielle
* Déploiement sur Azure
* Support de plusieurs fournisseurs de LLM
