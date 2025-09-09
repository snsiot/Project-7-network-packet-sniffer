# Network Packet Sniffer with Alert System

## Overview
This project is a Python-based network packet sniffer that captures network traffic in real-time, logs packet information into a SQLite database, and supports anomaly detection and alerting (to be implemented). 

## Features
- Captures packets and logs IP, ports, length, and TCP flags.
- Stores packet data in a SQLite database.
- Provides scripts to check logged data.
- Detects anomalies and sends alerts (future work).
- Can be extended with live traffic visualization.

## How to Use
1. Run `setup_db.py` to create the database and table.
2. Run `sniffer.py` to start capturing packets and logging data.
3. Use `check_db.py` to view recent logged packets.

## Requirements
- Python 3.x
- scapy (`pip install scapy`)
- matplotlib (optional, for graphing)

## Notes
- This project does not run directly on GitHub; you need to run it locally or in an online IDE.
- Use an online IDE like [Replit](https://replit.com/) to run this code in the browser.

## License
MIT License

