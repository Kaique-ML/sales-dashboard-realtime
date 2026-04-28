"""Kafka producer simulando eventos de venda em tempo real."""
import json
import random
import time
from datetime import datetime
from kafka import KafkaProducer

producer = KafkaProducer(
    bootstrap_servers=["localhost:9092"],
    value_serializer=lambda v: json.dumps(v).encode("utf-8"),
)

produtos = ["Notebook", "Smartphone", "Tablet", "Monitor", "Teclado"]

def gerar_venda():
    return {
        "id": random.randint(1000, 9999),
        "produto": random.choice(produtos),
        "valor": round(random.uniform(50, 5000), 2),
        "quantidade": random.randint(1, 5),
        "timestamp": datetime.now().isoformat(),
    }

if __name__ == "__main__":
    print("Iniciando producer de vendas...")
    while True:
        venda = gerar_venda()
        producer.send("vendas", venda)
        print(f"Venda enviada: {venda}")
        time.sleep(random.uniform(0.5, 3))
