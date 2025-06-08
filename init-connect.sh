#!/bin/bash

echo "⏳ Attente de Kafka Connect sur le port 8083..."

until curl -s -o /dev/null -w "%{http_code}" http://localhost:8083 | grep -q "200"; do
  echo "Kafka Connect pas encore prêt... nouvelle tentative dans 5 secondes"
  sleep 5
done

echo "✅ Kafka Connect est prêt."

if curl -s http://localhost:8083/connectors | grep -q "es-forex"; then
  echo "➡️ Connecteur 'es-forex' déjà présent."
else
  echo "🚀 Création du connecteur 'es-forex'..."
  curl -X POST -H "Content-Type: application/json" \
       --data @connectors/es-forex.json \
       http://localhost:8083/connectors
fi
