# 🚀 Strict Python 3 lock
import sys
required_version = (3, 10)
if sys.version_info[:2] != required_version:
    print(f"❌ Wrong Python version! Required {required_version[0]}.{required_version[1]}, but running {sys.version_info.major}.{sys.version_info.minor}")
    sys.exit(1)

from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import os

from wallets import wallets, insert_wallet, update_balance
import mining
from transfer import transfer_to_moniepoint
from exchange import usd_to_ngn

# ✅ Load environment
load_dotenv()

app = Flask(__name__)
CORS(app)

# ✅ Route: all wallets
@app.route("/wallets", methods=["GET"])
def get_wallets():
    return jsonify(wallets)

# ✅ Route: create wallet
@app.route("/wallets", methods=["POST"])
def create_wallet():
    data = request.json
    insert_wallet(data["address"])
    return jsonify({"success": True, "message": "Wallet created"})

# ✅ Route: update balance
@app.route("/wallets/update", methods=["POST"])
def update_wallet():
    data = request.json
    wallet = update_balance(data["address"], data["amount"])
    return jsonify(wallet or {"error": "Wallet not found"})

# ✅ Route: transfer SKD → NGN → Moniepoint
@app.route("/transfer", methods=["POST"])
def transfer():
    data = request.json
    amount_ngn = usd_to_ngn(data["amountUSD"])
    response = transfer_to_moniepoint(data["accountNumber"], data["bankCode"], amount_ngn)
    return jsonify(response)

if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    print(f"🚀 Mine App running at http://localhost:{port} on Python {sys.version.split()[0]}")
    app.run(host="0.0.0.0", port=port)
