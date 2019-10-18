import requests
import json
from pymongo import MongoClient

cliente = MongoClient('mongodb://localhost:27017/')
banco = cliente['mydb']
posicoes_collection = banco['spree_collection2']

session = requests.Session()

r = session.post('http://localhost:3000/api/v1/products?token=e0c91507ca69781a03c62aabd83246ed75e8ed0f498a4652')

r = session.get('http://localhost:3000/api/v1/products?token=e0c91507ca69781a03c62aabd83246ed75e8ed0f498a4652')

posicoes = r.json()

posicoes_collection.insert_one(posicoes).inserted_id


