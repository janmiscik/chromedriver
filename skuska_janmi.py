import requests
import random
import time
from concurrent.futures import ThreadPoolExecutor

# URL tvojho webu (hlavná stránka a podstránky)
urls = [
    "http://janmi.sk",
    "http://janmi.sk/aboutme",
    "http://janmi.sk/contact",
]

# Funkcia, ktorá pošle jednu požiadavku na náhodnú stránku
def send_request():
    url = random.choice(urls)
    try:
        r = requests.get(url)
        print(f"[{url}] Status: {r.status_code}")
    except Exception as e:
        print(f"[{url}] Chyba: {e}")
    # Malé náhodné oneskorenie medzi požiadavkami
    time.sleep(random.uniform(0.1, 0.5))

# Počet súbežných "návštevníkov"
threads = 50
# Počet požiadaviek na návštevníka
requests_per_thread = 20

with ThreadPoolExecutor(max_workers=threads) as executor:
    for _ in range(requests_per_thread):
        executor.submit(send_request)
