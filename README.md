# Sui Swarm Marketplace

Web dashboard for P2P Swarm Agent — displays swarm state transactions recorded on Sui blockchain.

## Features
- View smart contract info
- List last transactions
- Real swarm state hashes from Sui testnet

## Smart Contract
- **Package ID:** `0xa15a9d830198166cadc053a0d7316a212dfb10c5d13cbb5a4a062a0858c3f0e6`
- **Module:** `swarm_state`
- **Function:** `record_state(state_hash, leader)`

## Run
```bash
pip install flask requests
python app.py
Open http://localhost:5001

Links
Main project: https://github.com/rudimentall1/p2p-swarm-agent

Demo video: https://youtu.be/510ubVJ6yJE
