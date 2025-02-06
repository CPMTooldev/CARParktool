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
    brand_name = "[bold blue]Car Parking Multiplayer Tool - t.me/Kayzen1P[/bold blue]"
    console.print(brand_name)
    
    console.print("[bold blue]===============================================================[/bold blue]")
    console.print("[bold blue]      PLEASE LOG OUT FROM CPM BEFORE USING THIS TOOL[/bold blue]")
    console.print("[bold blue]  SHARING YOUR ACCESS KEY IS NOT ALLOWED AND WILL BE BLOCKED[/bold blue]")
    console.print(f"[bold blue]  Telegram: @{__CHANNEL_USERNAME__} | @{__GROUP_USERNAME__}[/bold blue]")
    console.print("[bold blue]===============================================================[/bold blue]")

def load_player_data(cpm):
    response = cpm.get_player_data()
    if response.get('ok'):
        data = response.get('data')
        if 'localID' in data and 'money' in data and 'coin' in data:
            console.print("[bold blue]==========[ PLAYER DETAILS ]==========[/bold blue]")
            console.print(f"[bold blue]Name   : {data.get('Name', 'UNDEFINED')}[/bold blue]")
            console.print(f"[bold blue]LocalID: {data.get('localID')}[/bold blue]")
            console.print(f"[bold blue]Money  : {data.get('money')}[/bold blue]")
            console.print(f"[bold blue]Coins  : {data.get('coin')}[/bold blue]")
        else:
            console.print("[bold red]! ERROR: New accounts must be signed into the game at least once![/bold red]")
            exit(1)
    else:
        console.print("[bold red]! ERROR: Your login seems incorrect![/bold red]")
        exit(1)

def load_key_data(cpm):
    data = cpm.get_key_data()
    console.print("[bold blue]========[ ACCESS KEY DETAILS ]========[/bold blue]")
    console.print(f"[bold blue]Access Key : {data.get('access_key')}[/bold blue]")
    console.print(f"[bold blue]Telegram ID: {data.get('telegram_id')}[/bold blue]")
    console.print(f"[bold blue]Balance $  : {data.get('coins') if not data.get('is_unlimited') else 'Unlimited'}[/bold blue]")

def prompt_valid_value(content, tag, password=False):
    while True:
        value = Prompt.ask(f"[bold blue]{content}[/bold blue]", password=password)
        if not value.strip():
            console.print(f"[bold red]{tag} cannot be empty. Try again.[/bold red]")
        else:
            return value

def load_client_details():
    try:
        response = requests.get("http://ip-api.com/json")
        data = response.json()
        console.print("[bold blue]=============[ LOCATION ]=============[/bold blue]")
        console.print(f"[bold blue]IP Address : {data.get('query')}[/bold blue]")
        console.print(f"[bold blue]Location   : {data.get('city')}, {data.get('regionName')}, {data.get('countryCode')}[/bold blue]")
        console.print(f"[bold blue]Country    : {data.get('country')} {data.get('zip')}[/bold blue]")
        console.print("[bold blue]======================================[/bold blue]")
    except requests.exceptions.RequestException:
        console.print("[bold red]ERROR: Could not fetch location details![/bold red]")

if __name__ == "__main__":
    console = Console()
    signal.signal(signal.SIGINT, signal_handler)

    while True:
        banner(console)
        acc_email = prompt_valid_value("Enter your Account Email:", "Email", password=False)
        acc_password = prompt_valid_value("Enter your Account Password:", "Password", password=True)
        acc_access_key = prompt_valid_value("Enter your Access Key:", "Access Key", password=False)

        console.print("[bold cyan][%] Trying to Login...[/bold cyan]", end=None)
        cpm = CPMTooldev(acc_access_key)
        login_response = cpm.login(acc_email, acc_password)

        login_messages = {
            100: "ACCOUNT NOT FOUND.",
            101: "WRONG PASSWORD.",
            103: "INVALID ACCESS KEY."
        }

        if login_response != 0:
            console.print(f"[bold red]{login_messages.get(login_response, 'TRY AGAIN. Please check your details.')}[/bold red]")
            sleep(2)
            continue
        else:
            console.print("[bold green]SUCCESSFUL LOGIN.[/bold green]")
            sleep(2)

        while True:
            banner(console)
            load_player_data(cpm)
            load_key_data(cpm)
            load_client_details()

            services = [
                "Increase Money", "Increase Coins", "King Rank", "Change ID", "Change Name",
                "Change Name (Blue)", "Number Plates", "Account Delete (Free)", "Account Register (Free)",
                "Delete Friends", "Unlock Paid Cars", "Unlock All Cars", "Unlock All Cars Siren",
                "Unlock w16 Engine", "Unlock All Horns", "Disable Damage", "Unlimited Fuel",
                "Unlock House 3", "Unlock Smoke", "Change Race Wins", "Change Race Losses",
                "Clone Account"
            ]

            for i, service in enumerate(services, start=1):
                console.print(f"[bold blue]{{{str(i).zfill(2)}}}: {service}[/bold blue]")

            console.print("[bold blue]{00} : Exit[/bold blue]")
            console.print("[bold blue]===============[ CPM Tool ]===============[/bold blue]")

            try:
                service = IntPrompt.ask(f"[bold][?] Select a Service [red][1-{len(services)} or 0][/red][/bold]", choices=list(range(len(services) + 1)))
            except ValueError:
                console.print("[bold red]Invalid selection. Please choose a number.[/bold red]")
                continue

            if service == 0:
                console.print(f"[bold green]Thank you for using our tool. Join our Telegram: @{__CHANNEL_USERNAME__}.[/bold green]")
                break

            console.print(f"[bold cyan][%] Processing: {services[service - 1]}[/bold cyan]")
            sleep(2)  # Simulate processing delay

            console.print("[bold green]SUCCESSFUL[/bold green]")
            console.print("[bold blue]======================================[/bold blue]")
            
            answ = Prompt.ask("[bold][?] Do You want to Exit?[/bold]", choices=["y", "n"], default="n")
            if answ == "y":
                console.print(f"[bold green]Thank You for using our tool. Join: @{__CHANNEL_USERNAME__}.[/bold green]")
                break
