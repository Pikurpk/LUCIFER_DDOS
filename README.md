# 🔥 **LUCIFER DDOS – Professional Edition**
### ⚡ Advanced Network Stress-Testing & Load Evaluation Toolkit  
<div align="center">

![LUCIFER DDOS](https://img.shields.io/badge/LUCIFER-DDOS-red?style=for-the-badge&logo=apache)
![Version](https://img.shields.io/badge/Version-2.0_Professional-blue?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.6+-yellow?style=for-the-badge&logo=python)
![Status](https://img.shields.io/badge/Build-Stable-success?style=for-the-badge)

**A high-performance DDoS testing toolkit built for learning, research,  
and authorized penetration testing only.**

</div>

---

## 🎯 **Key Features**

| Feature | Description | Status |
|--------|-------------|--------|
| 🔥 **HTTP Flood Attack** | High-volume HTTP request flooding with full proxy support | ✅ Active |
| ⚡ **TCP Flood Attack** | Raw TCP socket-based flood stress tests | ✅ Active |
| 🌊 **UDP Flood Attackk** | Connectionless UDP packet bombardment | ✅ Active |
| 🐢 **Slowloris Attackk** | Partial connection exhaustion attack | ✅ Active |
| 📡 **ICMP Flood Attack** | ICMP/Ping flood for network testing | ✅ Active |
| 🎭 **Mixed Attack** | Combined HTTP+TCP+UD | ✅ Active |
| 🔄 **Proxy Rotation** | Supports HTTP/SOCKS4/SOCKS5 + authentication proxies | ✅ Active |
| 🌐 **User-Agent Rotation** | Random user-agents on each request for evasion | ✅ Active |
| 🧵 **Multi-Threading Engine** | Ultra-fast parallel attack execution | ✅ Active |
| 📊 **Live Attack Stats** | Requests per second, successes, fails, etc. | ✅ Active |
| 🔐 **Password Authentication** | Secure access to protect tool usage | ✅ Active |

---

## 🛠️ **Installation Guide**

---

### 📱 **Termux (Android)**  
```bash
pkg update && pkg upgrade -y
pkg install python git -y
git clone https://github.com/pikurpk/LUCIFER_DDOS.git
cd LUCIFER_DDOS
pip install -r requirements.txt
LUCIFER_DDOS.py
```

---

### 🐉 **Kali Linux / Parrot OS**
```bash
sudo apt update && sudo apt upgrade -y
sudo apt install python3 python3-pip git -y
git clone https://github.com/pikurpk/LUCIFER_DDOS.git
cd LUCIFER_DDOS
pip3 install -r requirements.txt
LUCIFER_DDOS.py
```

---

### 🪟 **Windows (CMD / PowerShell)**
```bash
git clone https://github.com/pikurpk/LUCIFER_DDOS.git
cd LUCIFER_DDOS
pip install -r requirements.txt
LUCIFER_DDOS.py
```

---

## 🚀 **Usage Guide**

1️⃣ **Run the Tool**  
```bash
python LUCIFER_DDOS.py
```

2️⃣ **Authentication**  
```
Enter password: ********
```

3️⃣ **Choose Attack Type**
- HTTP Flood Attack  
- TCP Flood Attack  
- Load Proxies  
- System Statistics  
- About Tool  

4️⃣ **Configure Attack**
- Set Target URL/IP  
- Set Duration  
- Set Thread Count  
- Load Proxy List (Optional)

---

## 📂 **Project Structure**

```
LUCIFER_DDOS/
│── install.py
│── LUCIFER_DDOS.py
│── proxies.txt
│── requirements.txt
│── README.md
└── modules/
    ├── http_flood.py
    ├── tcp_flood.py
    ├── utils.py
    └── auth.py
```

---

## ⚠️ **Legal Disclaimer**

> This tool is strictly for **educational**, **research**, and  
> **authorized penetration testing** purposes only.  
> **Misuse is illegal.** The developer is not responsible for any damage caused.

---

## 📞 **Support & Contact**
<div align="center">

| Platform | Link | Status |
|----------|-------|---------|
| **Telegram** | `@pk_the_lucifer` | 🟢 Active |
| **Facebook** | www.facebook.com/pk_the_lucifer | 🟢 Active |

**Made with ❤️ by Foysal**

</div>
