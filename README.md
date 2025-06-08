# 📈 Temps réel FX – Pipeline Kafka → Elasticsearch → Kibana

Ce projet met en place un pipeline de streaming pour les données de taux de change (forex) en temps réel, utilisant Kafka, Kafka Connect, Elasticsearch et Kibana.

---

## 🔧 Architecture

- **Kafka** : réception des messages forex.
- **Kafka Connect** : exporte les données vers Elasticsearch.
- **Elasticsearch** : indexe les données.
- **Kibana** : visualisation des taux de change.
- **Producteur `fx-producer`** : génère des messages JSON dans le topic `forex`.

---

## 📁 Structure du projet


temps_reel_fx/
│
├── docker-compose.yml
├── Dockerfile.connect
├── init-connect.sh
├── connectors/
│ └── es-forex.json
├── fx-producer/
│ ├── Dockerfile
│ └── producer.py (exemple Python)

---

## 🚀 Lancer le projet

1. **Cloner le repo**
   ```bash
   git clone <url-du-repo>
   cd temps_reel_fx


Démarrer l’environnement

bash
Copier
Modifier
docker-compose up --build -d
Initialiser le connecteur Kafka Connect


bash init-connect.sh
🔍 Vérifications
✅ Vérifier que les messages sont bien produits :



docker exec -it <container-kafka> \
  kafka-console-consumer \
  --bootstrap-server localhost:9092 \
  --topic forex \
  --from-beginning
✅ Vérifier que l’index forex a été créé :


curl http://localhost:9200/_cat/indices?v
✅ Afficher les documents indexés :


curl http://localhost:9200/forex/_search?pretty
📊 Accéder à Kibana
Interface Kibana : http://localhost:5601

Rechercher l’index forex* dans "Stack Management > Index Patterns"

📝 Exemple de message JSON




{
  "amount": 1.0,
  "base": "EUR",
  "date": "2025-06-06",
  "rates": {
    "USD": 1.1411,
    "JPY": 164.62,
    "GBP": 0.8426
  }
}



📌 Prérequis
Docker + Docker Compose

Ports libres : 9092, 8083, 9200, 5601

Machine avec au moins 4 Go RAM

✍️ Auteur
Projet réalisé par moi – M1 Big Data 2025
