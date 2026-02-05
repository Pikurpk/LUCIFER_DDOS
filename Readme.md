# 🔥 LUCIFER DDOS - Professional Edition

<div align="center">

![LUCIFER DDOS](https://img.shields.io/badge/LUCIFER-DDOS-red?style=for-the-badge&logo=security)
![Version](https://img.shields.io/badge/Version-2.0_Professional-blue?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.6+-green?style=for-the-badge&logo=python)

**A powerful DDoS testing toolkit for educational purposes and authorized penetration testing**

</div>
🚀 Features
<div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 20px; border-radius: 10px; margin: 20px 0; box-shadow: 0 10px 20px rgba(0,0,0,0.2);"> 🔥 HTTP Flood Attack - High-volume HTTP requests with proxy support | ✅ Active<br> ⚡ TCP Flood Attack - Raw TCP packet flooding for network stress testing | ✅ Active<br> 🌊 UDP Flood Attack - Connectionless UDP packet bombardment | ✅ Active<br> 🐢 Slowloris Attack - Partial connection exhaustion attack | ✅ Active<br> 📡 ICMP Flood Attack - ICMP/Ping flood for network testing | ✅ Active<br> 🎭 Mixed Attack - Combined HTTP+TCP+UDP attack | ✅ Active<br> 🔄 Proxy Rotation - Multiple proxy formats with authentication support | ✅ Active<br> 🌐 User Agent Rotation - Randomized user agents for each request | ✅ Active<br> 🧵 Multi-threading - High-performance concurrent attacks | ✅ Active<br> 📊 Real-time Statistics - Live attack metrics and progress monitoring | ✅ Active </div>
⚠️ Disclaimer
<div style="background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%); padding: 20px; border-radius: 10px; margin: 20px 0; box-shadow: 0 10px 20px rgba(0,0,0,0.2); border: 3px solid #ff0000;"> ⚠️ <strong>WARNING:</strong> This tool is designed for <strong>educational purposes only</strong>. Use only on systems you own or have explicit permission to test. The developer is not responsible for any misuse or damage caused by this tool. </div>
🛠 Installation
<div style="background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%); padding: 20px; border-radius: 10px; margin: 20px 0; box-shadow: 0 10px 20px rgba(0,0,0,0.2);"> <div style="background: #1a1a1a; padding: 15px; border-radius: 8px; margin: 10px 0;"> <strong style="color: #00ff00;">📱 Termux (Android)</strong><br> <code style="color: #ffffff;">pkg update && pkg upgrade<br> pkg install python git -y<br> git clone https://github.com/pikurpk/LUCIFER_DDOS.git<br> cd LUCIFER_DDOS<br> pip install -r requirements.txt<br> python main.py</code> </div><div style="background: #1a1a1a; padding: 15px; border-radius: 8px; margin: 10px 0;"> <strong style="color: #00ff00;">🐉 Kali Linux</strong><br> <code style="color: #ffffff;">sudo apt update && sudo apt upgrade -y<br> sudo apt install python3 python3-pip git -y<br> git clone https://github.com/pikurpk/LUCIFER_DDOS.git<br> cd LUCIFER_DDOS<br> pip3 install -r requirements.txt<br> python3 main.py</code> </div><div style="background: #1a1a1a; padding: 15px; border-radius: 8px; margin: 10px 0;"> <strong style="color: #00ff00;">🪟 Windows</strong><br> <code style="color: #ffffff;">git clone https://github.com/pikurpk/LUCIFER_DDOS.git<br> cd LUCIFER_DDOS<br> pip install -r requirements.txt<br> python main.py</code> </div><div style="background: #1a1a1a; padding: 15px; border-radius: 8px; margin: 10px 0;"> <strong style="color: #00ff00;">📦 Requirements</strong><br> <code style="color: #ffffff;">pip install -r requirements.txt</code><br> <em style="color: #cccccc;">*Make sure requirements.txt contains all necessary dependencies.*</em> </div> </div>
📖 Usage Guide
<div style="background: linear-gradient(135deg, #fa709a 0%, #fee140 100%); padding: 20px; border-radius: 10px; margin: 20px 0; box-shadow: 0 10px 20px rgba(0,0,0,0.2);"> <strong style="color: #ffffff; font-size: 20px;">1️⃣ Start the tool:</strong><br> <div style="background: #1a1a1a; padding: 10px; border-radius: 8px; margin: 10px 0;"> <code style="color: #ffffff;">python LUCIFER_DDOS.py</code> </div>
<strong style="color: #ffffff; font-size: 20px;">2️⃣ Authentication:</strong>

<div style="background: #1a1a1a; padding: 10px; border-radius: 8px; margin: 10px 0;"> Enter the password when prompted </div>
<strong style="color: #ffffff; font-size: 20px;">3️⃣ Main Menu Options:</strong>

<div style="background: #1a1a1a; padding: 10px; border-radius: 8px; margin: 10px 0;"> [1] HTTP Flood Attack<br> [2] TCP Flood Attack<br> [3] UDP Flood Attack<br> [4] Slowloris Attack<br> [5] ICMP Flood Attack<br> [6] Mixed Attack<br> [7] Load Proxies<br> [8] System Statistics<br> [9] About Tool<br> [0] Exit </div>
<strong style="color: #ffffff; font-size: 20px;">4️⃣ Attack Configuration:</strong>

<div style="background: #1a1a1a; padding: 10px; border-radius: 8px; margin: 10px 0;"> • Enter target URL/IP address<br> • Set attack duration (in seconds)<br> • Configure thread count (recommended: 100-500)<br> • Load proxy list (optional, for anonymity) </div>
<strong style="color: #ffffff; font-size: 20px;">5️⃣ Start Attack:</strong>

<div style="background: #1a1a1a; padding: 10px; border-radius: 8px; margin: 10px 0;"> • Confirm target and parameters<br> • Attack will begin with real-time statistics </div> </div>
🔧 Configuration
<div style="background: linear-gradient(135deg, #a8edea 0%, #fed6e3 100%); padding: 20px; border-radius: 10px; margin: 20px 0; box-shadow: 0 10px 20px rgba(0,0,0,0.2);"> <strong style="color: #333; font-size: 20px;">🔧 Proxy Setup</strong><br> Create a <code style="background: #000; color: #fff; padding: 3px 6px; border-radius: 4px;">proxies.txt</code> file in the same directory with your proxies:<br> <div style="background: #1a1a1a; padding: 10px; border-radius: 8px; margin: 10px 0;"> <code style="color: #00ff00;">http://user:pass@ip:port<br> socks5://ip:port<br> http://ip:port</code> </div>
<strong style="color: #333; font-size: 20px;">🌐 User Agents</strong>

<div style="background: #1a1a1a; padding: 10px; border-radius: 8px; margin: 10px 0; color: #fff;"> User agents are automatically rotated from a built-in list. </div>
<strong style="color: #333; font-size: 20px;">🧵 Thread Management</strong>

<div style="background: #1a1a1a; padding: 10px; border-radius: 8px; margin: 10px 0; color: #fff;"> • Default: 100 threads<br> • Maximum recommended: 1000 threads<br> • Adjust based on your system capability </div> </div>
📊 Statistics Display
<div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 20px; border-radius: 10px; margin: 20px 0; box-shadow: 0 10px 20px rgba(0,0,0,0.2);"> <div style="background: #1a1a1a; padding: 15px; border-radius: 8px; margin: 10px 0; color: #fff;"> <strong style="color: #00ff00;">During attack, you'll see:</strong><br><br> ✅ Active threads<br> 📨 Packets sent<br> ⏱️ Time elapsed<br> 🚫 Failed connections<br> 📈 Requests per second </div> </div>
❓ Troubleshooting
<div style="background: linear-gradient(135deg, #ff9a9e 0%, #fad0c4 100%); padding: 20px; border-radius: 10px; margin: 20px 0; box-shadow: 0 10px 20px rgba(0,0,0,0.2);"> <div style="background: #1a1a1a; padding: 15px; border-radius: 8px; margin: 10px 0;"> <strong style="color: #ff9900;">Issue:</strong> Module not found<br> <strong style="color: #00ff00;">Solution:</strong> Run <code>pip install -r requirements.txt</code> </div><div style="background: #1a1a1a; padding: 15px; border-radius: 8px; margin: 10px 0;"> <strong style="color: #ff9900;">Issue:</strong> Permission denied<br> <strong style="color: #00ff00;">Solution:</strong> Use <code>sudo</code> (Linux) or run as admin (Windows) </div><div style="background: #1a1a1a; padding: 15px; border-radius: 8px; margin: 10px 0;"> <strong style="color: #ff9900;">Issue:</strong> Proxy not working<br> <strong style="color: #00ff00;">Solution:</strong> Check proxy format and authentication </div><div style="background: #1a1a1a; padding: 15px; border-radius: 8px; margin: 10px 0;"> <strong style="color: #ff9900;">Issue:</strong> Slow performance<br> <strong style="color: #00ff00;">Solution:</strong> Reduce thread count or use better proxies </div><div style="background: #1a1a1a; padding: 15px; border-radius: 8px; margin: 10px 0;"> <strong style="color: #ff9900;">Issue:</strong> Connection errors<br> <strong style="color: #00ff00;">Solution:</strong> Check target URL and your internet connection </div> </div>
📞 Support & Contact
<div align="center" style="background: linear-gradient(135deg, #43e97b 0%, #38f9d7 100%); padding: 30px; border-radius: 15px; margin: 20px 0; box-shadow: 0 15px 30px rgba(0,0,0,0.3); border: 3px solid #fff;">
🌐 Connect With Developer
<div style="background: rgba(0,0,0,0.8); padding: 20px; border-radius: 10px; display: inline-block; margin: 20px;"> <strong style="color: #00ff00;">Telegram:</strong> <a href="https://t.me/pk_the_lucifer" style="color: #ff9900;">@pk_the_lucifer</a> | ✅ Active<br> <strong style="color: #00ff00;">Facebook:</strong> <a href="https://facebook.com/pk_the_lucifer" style="color: #ff9900;">facebook.com/pk_the_lucifer</a> | ✅ Active </div>
<div style="background: #000; padding: 15px; border-radius: 8px; margin: 20px 0; border: 2px solid #ff0000;"> <strong style="color: #ff0000;">⚠️ Legal Notice:</strong> This tool must only be used for <strong style="color: #00ff00;">authorized security testing</strong> and <strong style="color: #00ff00;">educational purposes</strong>. Unauthorized use is illegal. </div>
<strong style="font-size: 24px; color: #fff; text-shadow: 2px 2px 4px #000;">Made with ❤️ by Foysal</strong>

</div> ```