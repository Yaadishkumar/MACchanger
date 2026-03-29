# 🔐 MAC Address Changer (Python)

A simple Python-based tool to change the MAC (Media Access Control) address of a network interface on Linux systems.

## 📌 Features

- Change MAC address of any network interface
- Display current MAC address
- User-friendly CLI interface
- Lightweight and fast
- Works on most Linux distributions

## ⚙️ Requirements

- Python 3.x
- Linux OS
- `ifconfig` or `ip` command available
- Root privileges (sudo)

## 📥 Installation

Clone the repository:

```bash
git clone https://github.com/Yaadishkumar/MACchanger.git
cd MACchanger

## Run Script
```bash
sudo python3 mac_changer.py -i <interface> -m <new_mac>
