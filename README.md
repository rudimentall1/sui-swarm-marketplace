# Sui Swarm Marketplace

Web dashboard for inspecting swarm state hashes and transactions anchored to the Sui testnet.

## Purpose

The project complements the P2P Swarm Agent by providing a lightweight interface for viewing blockchain-backed swarm state.

## Features

- Smart-contract information
- Recent recorded transactions
- Swarm state hashes from Sui testnet

## Contract Interface

- Module: `swarm_state`
- Function: `record_state(state_hash, leader)`

The package identifier currently documented by the project is:

`0xa15a9d830198166cadc053a0d7316a212dfb10c5d13cbb5a4a062a0858c3f0e6`

## Run

```bash
pip install flask requests
python app.py
```

Open `http://localhost:5001`.

## Status

Prototype dashboard / companion component for the P2P Swarm Agent project.
