#!/usr/bin/env python3
import os
import sys
import subprocess
import platform

def print_banner():
    print(f"""
    ╔══════════════════════════════════════════════╗
    ║           LUCIFER DDOS INSTALLER             ║
    ║           Professional Edition v2.0          ║
    ║                                              ║
    ║         Created by Foysal                    ║
    ╚══════════════════════════════════════════════╝
    """)

def check_python():
    """Check if Python is installed"""
    try:
        version = sys.version_info
        print(f"✅ Python {version.major}.{version.minor}.{version.micro} detected")
        return True
    except:
        print("❌ Python not found!")
        return False

def check_pip():
    """Check if pip is available"""
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "--version"], 
                            stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print("✅ pip is available")
        return True
    except:
        print("❌ pip not found!")
        return False

def install_requirements():
    """Install required packages"""
    print("\n📦 Installing requirements...")
    try:
        subprocess.check_call([
            sys.executable, "-m", "pip", "install", "-r", "requirements.txt"
        ])
        print("✅ Requirements installed successfully!")
        return True
    except subprocess.CalledProcessError:
        print("❌ Failed to install requirements using pip")
        return False

def main():
    print_banner()
    
    print("🔍 Checking system requirements...")
    
    if not check_python():
        sys.exit(1)
    
    if not check_pip():
        sys.exit(1)
    
    if install_requirements():
        print("\n🎉 Installation completed successfully!")
        print("\n🚀 Starting LUCIFER DDOS...")
        print("🔐 Default password: lucifer123")
        print("\n" + "="*50)
        
        # Start the main application
        try:
            from main import main as start_app
            start_app()
        except ImportError:
            print("✅ Installation complete! Run: python main.py")
    else:
        print("\n❌ Installation failed!")
        print("💡 Try installing manually: pip install -r requirements.txt")
        sys.exit(1)

if __name__ == "__main__":
    main()