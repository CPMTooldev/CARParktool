#!/usr/bin/python

import os
import random
import requests
import time
import signal
import sys
from threading import Thread
from PIL import ImageGrab
from rich.console import Console
from rich.prompt import Prompt, IntPrompt
from rich.text import Text
from rich.style import Style
import pystyle
from pystyle import Colors, Colorate

from cpmtooldev import CPMTooldev

__CHANNEL_USERNAME__ = "TelmunnDev"
__GROUP_USERNAME__   = "BaldanShopChat"

# Screenshot detection flag
screenshot_detected = False

def detect_screenshot(interval=1):
    """Detects screenshots and masks sensitive data when a screenshot is taken."""
    global screenshot_detected
    prev_screenshot = None
    while True:
        try:
            screenshot = ImageGrab.grab()
            if prev_screenshot is not None and screenshot != prev_screenshot:
                print("\n[SYSTEM] Screenshot detected! Masking sensitive data.")
                screenshot_detected = True
                time.sleep(5)  # Mask data for 5 seconds
                screenshot_detected = False
            prev_screenshot = screenshot
        except Exception as e:
            pass  # Handle headless systems where screenshots may fail
        time.sleep(interval)

def signal_handler(sig, frame):
    print("\n Bye Bye...")
    sys.exit(0)

def gradient_text(text, colors):
    """Applies a gradient color effect to text."""
    lines = text.splitlines()
    height = len(lines)
    width = max(len(line) for line in lines)
    colorful_text = Text()
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char != ' ':
                color_index = int(((x / (width - 1 if width > 1 else 1)) + (y / (height - 1 if height > 1 else 1))) * 0.5 * (len(colors) - 1))
                color_index = min(max(color_index, 0), len(colors) - 1)  
                style = Style(color=colors[color_index])
                colorful_text.append(char, style=style)
            else:
                colorful_text.append(char)
        colorful_text.append("\n")
    return colorful_text

def banner(console):
    """Displays a colorful banner."""
    os.system('cls' if os.name == 'nt' else 'clear')
    brand_name =  "Car Parking Multiplayer 1 Tool - t.me/Kayzen1P"
    colors = [
        "rgb(255,0,0)", "rgb(255,69,0)", "rgb(255,140,0)", "rgb(255,215,0)", "rgb(173,255,47)", 
        "rgb(0,255,0)", "rgb(0,255,255)", "rgb(0,191,255)", "rgb(0,0,255)", "rgb(139,0,255)",
        "rgb(255,0,255)"
    ]
    colorful_text = gradient_text(brand_name, colors)
    console.print(colorful_text)
    print(Colorate.Horizontal(Colors.rainbow, '=================================================================='))
    print(Colorate.Horizontal(Colors.rainbow, '\t         𝐏𝐋𝐄𝐀𝐒𝐄 𝐋𝐎𝐆𝐎𝐔𝐓 𝐅𝐑𝐎𝐌 𝐂𝐏𝐌 𝐁𝐄𝐅𝐎𝐑𝐄 𝐔𝐒𝐈𝐍𝐆 𝐓𝐇𝐈𝐒 𝐓𝐎𝐎𝐋'))
    print(Colorate.Horizontal(Colors.rainbow, '=================================================================='))

def load_key_data(cpm):
    """Loads access key details and masks them if a screenshot is detected."""
    data = cpm.get_key_data()
    masked_key = "************" if screenshot_detected else data.get("access_key")

    print(Colorate.Horizontal(Colors.rainbow, '========[ ACCESS KEY DETAILS ]========'))
    print(Colorate.Horizontal(Colors.rainbow, f'Access Key : {masked_key}.'))
    print(Colorate.Horizontal(Colors.rainbow, f'Telegram ID: {data.get("telegram_id")}.'))
    print(Colorate.Horizontal(Colors.rainbow, f'Balance $  : {(data.get("coins") if not data.get("is_unlimited") else "Unlimited")}.'))

def load_client_details():
    """Loads client IP and location details, masking them if a screenshot is detected."""
    response = requests.get("http://ip-api.com/json")
    data = response.json()
    
    masked_ip = "XXX.XXX.XXX.XXX" if screenshot_detected else data.get("query")
    masked_location = "Hidden" if screenshot_detected else f'{data.get("city")} {data.get("regionName")} {data.get("countryCode")}'

    print(Colorate.Horizontal(Colors.rainbow, '=============[ 𝐋𝐎𝐂𝐀𝐓𝐈𝐎𝐍 ]============='))
    print(Colorate.Horizontal(Colors.rainbow, f'Ip Address : {masked_ip}.'))
    print(Colorate.Horizontal(Colors.rainbow, f'Location   : {masked_location}.'))
    print(Colorate.Horizontal(Colors.rainbow, f'Country    : {masked_location}.'))
    print(Colorate.Horizontal(Colors.rainbow, '===============[ 𝐌𝐄𝐍𝐔 ]==============='))

if __name__ == "__main__":
    console = Console()
    signal.signal(signal.SIGINT, signal_handler)

    # Start screenshot detection in a separate thread
    Thread(target=detect_screenshot, daemon=True).start()

    while True:
        banner(console)
        acc_email = Prompt.ask("[bold][?] Account Email[/bold]")
        acc_password = Prompt.ask("[bold][?] Account Password[/bold]", password=True)
        acc_access_key = Prompt.ask("[bold][?] Access Key[/bold]", password=True)

        console.print("[bold cyan][%] Trying to Login[/bold cyan]: ", end=None)
        cpm = CPMTooldev(acc_access_key)
        login_response = cpm.login(acc_email, acc_password)

        if login_response == 0:
            print(Colorate.Horizontal(Colors.rainbow, 'SUCCESSFUL.'))
            time.sleep(2)
        else:
            print(Colorate.Horizontal(Colors.rainbow, 'LOGIN FAILED. TRY AGAIN.'))
            time.sleep(2)
            continue

        while True:
            banner(console)
            load_key_data(cpm)
            load_client_details()
            exit_choice = Prompt.ask("[?] Exit? (y/n)", choices=["y", "n"], default="n")
            if exit_choice == "y":
                print(Colorate.Horizontal(Colors.rainbow, f'Thank you for using our tool! Join our Telegram: @{__CHANNEL_USERNAME__}.'))
                break
