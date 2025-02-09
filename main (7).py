#!/usr/bin/python

import random
import requests
from time import sleep
import os, signal, sys
from rich.console import Console
from rich.prompt import Prompt, IntPrompt
from rich.text import Text
from rich.style import Style
import pystyle
from pystyle import Colors, Colorate

from cpmtooldev import CPMTooldev

__CHANNEL_USERNAME__ = "BaldanShopChannel"
__GROUP_USERNAME__ = "BaldanShopChat"


def signal_handler(sig, frame):
    print("\n Bye Bye...")
    sys.exit(0)


def gradient_text(text, colors):
    lines = text.splitlines()
    height = len(lines)
    width = max(len(line) for line in lines)
    colorful_text = Text()
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char != ' ':
                color_index = int(
                    ((x / (width - 1 if width > 1 else 1)) + (y / (height - 1 if height > 1 else 1))) * 0.5 * (
                            len(colors) - 1))
                color_index = min(max(color_index, 0), len(colors) - 1)
                style = Style(color=colors[color_index])
                colorful_text.append(char, style=style)
            else:
                colorful_text.append(char)
        colorful_text.append("\n")
    return colorful_text


def banner(console):
    os.system('cls' if os.name == 'nt' else 'clear')
    brand_name = "Car Parking Multiplayer 1 Tool - t.me/Kayzen1P"
    colors = [
        "rgb(255,0,0)", "rgb(255,69,0)", "rgb(255,140,0)", "rgb(255,215,0)", "rgb(173,255,47)",
        "rgb(0,255,0)", "rgb(0,255,255)", "rgb(0,191,255)", "rgb(0,0,255)", "rgb(139,0,255)",
        "rgb(255,0,255)"
    ]
    colorful_text = gradient_text(brand_name, colors)
    console.print(colorful_text)
    print(Colorate.Horizontal(Colors.rainbow, '================================================'))
    print(Colorate.Horizontal(Colors.rainbow, '𝐏𝐋𝐄𝐀𝐒𝐄 𝐋𝐎𝐆𝐎𝐔𝐓 𝐅𝐑𝐎𝐌 𝐂𝐏𝐌 𝐁𝐄𝐅𝐎𝐑𝐄 𝐔𝐒𝐈𝐍𝐆 𝐓𝐇𝐈𝐒 𝐓𝐎𝐎𝐋'))
    print(Colorate.Horizontal(Colors.rainbow, '================================================'))


def prompt_valid_value(content, tag, password=False):
    while True:
        value = Prompt.ask(content, password=password)
        if not value or value.isspace():
            print(Colorate.Horizontal(Colors.rainbow, f'{tag} cannot be empty or just spaces. Please try again.'))
        else:
            return value


def load_client_details():
    try:
        response = requests.get("http://ip-api.com/json", timeout=5)
        response.raise_for_status()
        data = response.json()
    except requests.exceptions.RequestException:
        print(Colorate.Horizontal(Colors.red, 'ERROR: Unable to fetch location details.'))
        return

    print(Colorate.Horizontal(Colors.rainbow, '=============[ 𝐋𝐎𝐂𝐀𝐓𝐈𝐎𝐍 ]============='))
    print(Colorate.Horizontal(Colors.rainbow, f'Ip Address : {data.get("query", "N/A")}.'))


if __name__ == "__main__":
    console = Console()
    signal.signal(signal.SIGINT, signal_handler)

    while True:
        banner(console)
        acc_email = prompt_valid_value("[bold][?] Account Email[/bold]", "Email", password=False)
        acc_password = prompt_valid_value("[bold][?] Account Password[/bold]", "Password", password=False)
        acc_access_key = prompt_valid_value("[bold][?] Access Key[/bold]", "Access Key", password=False)

        cpm = CPMTooldev(acc_access_key)
        login_response = cpm.login(acc_email, acc_password)

        if login_response != 0:
            print(Colorate.Horizontal(Colors.rainbow, 'LOGIN FAILED. TRY AGAIN.'))
            sleep(2)
            continue

        print(Colorate.Horizontal(Colors.rainbow, 'LOGIN SUCCESSFUL.'))
        sleep(2)

        while True:
            banner(console)
            load_client_details()

            service = IntPrompt.ask("[bold][?] Select a Service [red][1-2 or 0 to Exit][/red][/bold]", choices=["0", "1", "2"], show_choices=False)

            if service == 0:
                print(Colorate.Horizontal(Colors.rainbow, f'Thank You for using our tool, join Telegram: @{__CHANNEL_USERNAME__}.'))
                break
            elif service == 1:
                print(Colorate.Horizontal(Colors.rainbow, '[?] Enter how much money you want.'))
                amount = IntPrompt.ask("[?] Amount")
                if 0 < amount <= 999999999:
                    if cpm.set_player_money(amount):
                        print(Colorate.Horizontal(Colors.rainbow, 'SUCCESSFUL'))
                    else:
                        print(Colorate.Horizontal(Colors.red, 'FAILED. TRY AGAIN.'))
                else:
                    print(Colorate.Horizontal(Colors.red, 'INVALID AMOUNT.'))
                sleep(2)
            elif service == 2:
                print(Colorate.Horizontal(Colors.rainbow, '[?] Enter the steering intensity (1-900).'))
                intensity = IntPrompt.ask("[?] Intensity")
                if 1 <= intensity <= 900:
                    if cpm.car_steering(intensity):
                        print(Colorate.Horizontal(Colors.rainbow, 'SUCCESSFUL'))
                    else:
                        print(Colorate.Horizontal(Colors.red, 'FAILED. TRY AGAIN.'))
                else:
                    print(Colorate.Horizontal(Colors.red, 'INVALID INTENSITY. MUST BE 1-900.'))
                sleep(2)
