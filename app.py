from flask import Flask, render_template, jsonify
import requests
import os

app = Flask(__name__)

# Sui testnet RPC
SUI_RPC = "https://fullnode.testnet.sui.io:443"
CONTRACT_ID = "0xa15a9d830198166cadc053a0d7316a212dfb10c5d13cbb5a4a062a0858c3f0e6"

def get_last_transactions():
    """Получает последние транзакции контракта"""
    # Симуляция, т.к. реальные транзакции требуют индексатора
    return [
        {"hash": "0x8gFzvtpaCZ54yVyunEZYozMYHwf9yr9yUtbMvmVzZcx8", "state_hash": "f92e93cd51a79807...", "leader": "0x0d98de5b...", "time": "2026-03-24 20:30:00"},
        {"hash": "0x7hGzvtpaCZ54yVyunEZYozMYHwf9yr9yUtbMvmVzZcx7", "state_hash": "dae854512507b9aa...", "leader": "0x0d98de5b...", "time": "2026-03-24 20:00:00"},
    ]

@app.route('/')
def index():
    return render_template('index.html', contract=CONTRACT_ID)

@app.route('/api/transactions')
def api_transactions():
    txs = get_last_transactions()
    return jsonify(txs)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
