
import requests
from concurrent.futures import ProcessPoolExecutor

with ProcessPoolExecutor(max_workers=16) as executor:
    for i in range(0, 10000):
        requests.get("http://127.0.0.1:8000")
