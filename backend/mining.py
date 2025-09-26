import threading, time, os
from wallets import wallets

MINING_RATE = int(os.getenv("MINING_RATE", 200))

def mine():
    while True:
        for w in wallets:
            w["balance"] += MINING_RATE
        print(f"⛏️ Mining: +{MINING_RATE} SKD to all wallets")
        time.sleep(1)

# Start mining in background thread
threading.Thread(target=mine, daemon=True).start()
