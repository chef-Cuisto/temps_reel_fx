import os, json, time, logging
from datetime import datetime, timedelta
from kafka import KafkaProducer
from kafka.errors import NoBrokersAvailable

logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s %(levelname)s %(message)s")

BOOTSTRAP = os.getenv("KAFKA_BOOTSTRAP_SERVERS", "kafka:9092")

# ↘︎ petite boucle de retry pour attendre Kafka
while True:
    try:
        producer = KafkaProducer(
            bootstrap_servers=BOOTSTRAP,
            value_serializer=lambda v: json.dumps(v).encode("utf-8"),
        )
        break
    except NoBrokersAvailable:
        logging.warning("Kafka not ready on %s, retry in 5 s…", BOOTSTRAP)
        time.sleep(5)

# ⏱ Simulation de 30 jours de données historiques
BASE_DATE = datetime(2025, 6, 1)

for i in range(30):
    fake_date = (BASE_DATE + timedelta(days=i)).strftime("%Y-%m-%d")

    data = {
        "amount": 1.0,
        "base": "EUR",
        "date": fake_date,
        "rates": {
            "USD": round(1.10 + i * 0.001, 4),
            "JPY": round(160.00 + i, 2),
            "GBP": round(0.85 - i * 0.001, 4),
            "CAD": round(1.50 + i * 0.002, 4),
            "AUD": round(1.70 + i * 0.0015, 4),
        }
    }

    try:
        producer.send("forex", value=data)
        logging.info("Pushed simulated rates for %s", fake_date)
    except Exception as e:
        logging.error("Kafka send failed: %s", e)

    time.sleep(1)  # délai facultatif
