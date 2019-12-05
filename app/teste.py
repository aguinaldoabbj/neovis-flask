import requests
import json
from bs4 import BeautifulSoup


config =  [{"cypher": "CALL db.schema()",
            "db_user": "neo4j"
          }]

config_json = json.dumps(config[0])

url = "http://localhost:5000/config/%s"
r = requests.get(url % config_json)
print(BeautifulSoup(r.content).prettify())
