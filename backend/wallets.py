wallets = []

def insert_wallet(address, balance=0):
    wallets.append({"address": address, "balance": balance})

def get_wallet(address):
    return next((w for w in wallets if w["address"] == address), None)

def update_balance(address, amount):
    wallet = get_wallet(address)
    if wallet:
        wallet["balance"] += amount
        return wallet
    return None
