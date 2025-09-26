import os, requests

def transfer_to_moniepoint(account_number, bank_code, amount_ngn):
    api_key = os.getenv("MONIEPOINT_API_KEY")
    secret = os.getenv("MONIEPOINT_SECRET")

    url = "https://api.moniepoint.com/v1/transfers"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}",
        "x-secret-key": secret
    }
    payload = {
        "account_number": account_number,
        "bank_code": bank_code,
        "amount": amount_ngn
    }

    response = requests.post(url, headers=headers, json=payload)
    return response.json()
