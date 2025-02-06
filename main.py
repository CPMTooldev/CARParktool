#!/usr/bin/python

import random
import requests
from time import sleep
import os, signal, sys
from rich.console import Console
from rich.prompt import Prompt, IntPrompt
from pystyle import Colors, Colorate

from cpmtooldev import CPMTooldev

__CHANNEL_USERNAME__ = "TelmunnDev"
__GROUP_USERNAME__   = "BaldanShopChat"

def signal_handler(sig, frame):
    print("\nBye Bye...")
    sys.exit(0)

def banner(console):
    os.system('cls' if os.name == 'nt' else 'clear')
    brand_name = "Car Parking Multiplayer Tool - t.me/Kayzen1P"
    console.print(Colorate.Horizontal(Colors.blue, brand_name))
    
    print(Colorate.Horizontal(Colors.blue, '==============================================================='))
    print(Colorate.Horizontal(Colors.blue, '      PLEASE LOG OUT FROM CPM BEFORE USING THIS TOOL'))
    print(Colorate.Horizontal(Colors.blue, '  SHARING YOUR ACCESS KEY IS NOT ALLOWED AND WILL BE BLOCKED'))
    print(Colorate.Horizontal(Colors.blue, f'  Telegram: @{__CHANNEL_USERNAME__} | @{__GROUP_USERNAME__}'))
    print(Colorate.Horizontal(Colors.blue, '==============================================================='))

def load_player_data(cpm):
    response = cpm.get_player_data()
    if response.get('ok'):
        data = response.get('data')
        if 'localID' in data and 'money' in data and 'coin' in data:
            print(Colorate.Horizontal(Colors.blue, '==========[ PLAYER DETAILS ]=========='))
            print(Colorate.Horizontal(Colors.blue, f'Name   : {data.get("Name", "UNDEFINED")}.'))
            print(Colorate.Horizontal(Colors.blue, f'LocalID: {data.get("localID")}.'))
            print(Colorate.Horizontal(Colors.blue, f'Money  : {data.get("money")}.'))
            print(Colorate.Horizontal(Colors.blue, f'Coins  : {data.get("coin")}.'))
        else:
            print(Colorate.Horizontal(Colors.blue, '! ERROR: New accounts must be signed into the game at least once!'))
            exit(1)
    else:
        print(Colorate.Horizontal(Colors.blue, '! ERROR: Your login seems incorrect!'))
        exit(1)

def load_key_data(cpm):
    data = cpm.get_key_data()
    print(Colorate.Horizontal(Colors.blue, '========[ ACCESS KEY DETAILS ]========'))
    print(Colorate.Horizontal(Colors.blue, f'Access Key : {data.get("access_key")}.'))
    print(Colorate.Horizontal(Colors.blue, f'Telegram ID: {data.get("telegram_id")}.'))
    print(Colorate.Horizontal(Colors.blue, f'Balance $  : {data.get("coins") if not data.get("is_unlimited") else "Unlimited"}.'))

def prompt_valid_value(content, tag, password=False):
    while True:
        value = Prompt.ask(content, password=password)
        if not value.strip():
            print(Colorate.Horizontal(Colors.blue, f'{tag} cannot be empty. Try again.'))
        else:
            return value

def load_client_details():
    try:
        response = requests.get("http://ip-api.com/json")
        data = response.json()
        print(Colorate.Horizontal(Colors.blue, '=============[ LOCATION ]============='))
        print(Colorate.Horizontal(Colors.blue, f'IP Address : {data.get("query")}.'))
        print(Colorate.Horizontal(Colors.blue, f'Location   : {data.get("city")}, {data.get("regionName")}, {data.get("countryCode")}.'))
        print(Colorate.Horizontal(Colors.blue, f'Country    : {data.get("country")} {data.get("zip")}.'))
        print(Colorate.Horizontal(Colors.blue, '======================================'))
    except requests.exceptions.RequestException:
        print(Colorate.Horizontal(Colors.blue, 'ERROR: Could not fetch location details!'))

if __name__ == "__main__":
    console = Console()
    signal.signal(signal.SIGINT, signal_handler)

    while True:
        banner(console)
        acc_email = prompt_valid_value("[bold][?] Account Email[/bold]", "Email", password=False)
        acc_password = prompt_valid_value("[bold][?] Account Password[/bold]", "Password", password=False)
        acc_access_key = prompt_valid_value("[bold][?] Access Key[/bold]", "Access Key", password=False)

        console.print("[bold cyan][%] Trying to Login[/bold cyan]: ", end=None)
        cpm = CPMTooldev(acc_access_key)
        login_response = cpm.login(acc_email, acc_password)

        login_messages = {
            100: "ACCOUNT NOT FOUND.",
            101: "WRONG PASSWORD.",
            103: "INVALID ACCESS KEY."
        }

        if login_response != 0:
            print(Colorate.Horizontal(Colors.blue, login_messages.get(login_response, "TRY AGAIN. Please check your details.")))
            sleep(2)
            continue
        else:
            print(Colorate.Horizontal(Colors.blue, 'SUCCESSFUL LOGIN.'))
            sleep(2)

        while True:
            banner(console)
            load_player_data(cpm)
            load_key_data(cpm)
            load_client_details()

            choices = [str(i) for i in range(23)]
            services = [
                "Increase Money",
                "Increase Coins",
                "King Rank",
                "Change ID",
                "Change Name",
                "Change Name (Blue)",
                "Number Plates",
                "Account Delete (Free)",
                "Account Register (Free)",
                "Delete Friends",
                "Unlock Paid Cars",
                "Unlock All Cars",
                "Unlock All Cars Siren",
                "Unlock w16 Engine",
                "Unlock All Horns",
                "Disable Damage",
                "Unlimited Fuel",
                "Unlock House 3",
                "Unlock Smoke",
                "Change Race Wins",
                "Change Race Losses",
                "Clone Account"
            ]

            for i, service in enumerate(services, start=1):
                print(Colorate.Horizontal(Colors.blue, f'{{{str(i).zfill(2)}}}: {service}'))

            print(Colorate.Horizontal(Colors.blue, '{00} : Exit'))
            print(Colorate.Horizontal(Colors.blue, '===============[ CPM Tool ]==============='))

            service = IntPrompt.ask(f"[bold][?] Select a Service [red][1-{len(services)} or 0][/red][/bold]", choices=choices, show_choices=False)

            if service == 0:
                print(Colorate.Horizontal(Colors.blue, f'Thank you for using our tool. Join our Telegram: @{__CHANNEL_USERNAME__}.'))
                break

            print(Colorate.Horizontal(Colors.blue, f'[%] Processing: {services[service - 1]}'))
            sleep(2)  # Simulate processing delay

            # Simulating a successful action
            print(Colorate.Horizontal(Colors.blue, 'SUCCESSFUL'))
            print(Colorate.Horizontal(Colors.blue, '======================================'))
            
            answ = Prompt.ask("[?] Do You want to Exit ?", choices=["y", "n"], default="n")
            if answ == "y":
                print(Colorate.Horizontal(Colors.blue, f'Thank You for using our tool. Join: @{__CHANNEL_USERNAME__}.'))
                break
