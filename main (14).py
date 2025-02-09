##############################################################################
# Copyright (C) trese xeno <me@trese_xeno> - All Rights Reserved             #
# Unauthorized copying of this file, via any medium is strictly prohibited   #
# Proprietary and confidential                                               #
##############################################################################
# Written by trese xeno <me@trese_xeno>, 16, Jan, 2025.                      #
##############################################################################

import random
import cpmnuker
import base64
from time import sleep
import os, signal, sys
from rich.console import Console
from rich.prompt import Prompt, IntPrompt
from rich.text import Text
from rich.style import Style


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
                color_index = int(((x / (width - 1 if width > 1 else 1)) + (y / (height - 1 if height > 1 else 1))) * 0.5 * (len(colors) - 1))
                color_index = min(max(color_index, 0), len(colors) - 1)  # Ensure the index is within bounds
                style = Style(color=colors[color_index])
                colorful_text.append(char, style=style)
            else:
                colorful_text.append(char)
        colorful_text.append("\n")
    return colorful_text

def banner(console):
    try:
        os.system('cls' if os.name=='nt' else 'clear')
    except:
        console.clear()
    console.print("[bold red][*] " + base64.b64decode('V2VsY29tZSB0byBDUE1OdWtlciwgdGhlIGhhY2tlcnMgdG9vbGtpdA==').decode('utf-8') + "[/bold red].", "\n")
    console.print("[bold green][*] Description[/bold green]: Car Parking Multiplayer Hacking Tool.")
    console.print("[bold green][*] Telegram[/bold green]: [bold blue]@" + base64.b64decode('Q1BNTnVrZXJPZmZpY2lhbA==').decode('utf-8') + "[/bold blue].")
    console.print("[bold red]==================================================[/bold red]")
    console.print("[bold yellow][!] Note[/bold yellow]: Logout from CPM before using this tool !.", end="\n\n")

def load_player_data(cpm):
    response = cpm.get_player_data()
    if response.get('ok'):
        data = response.get('data')
        if 'floats' in data and 'localID' in data and 'money' in data and 'coin' in data:
            console.print("[bold][red]========[/red][ PLAYER DETAILS ][red]========[/red][/bold]")
            console.print("[bold green]Name   [/bold green]: " + (data.get('Name') if 'Name' in data else 'UNDEFINED') + ".")
            console.print("[bold green]ID[/bold green]     : " + (data.get('localID') if 'localID' in data else 'UNDEFINED') + ".")
            console.print("[bold green]Money  [/bold green]: " + (str(data.get('money')) if 'money' in data else 'UNDEFINED') + ".")
            console.print("[bold green]Coins  [/bold green]: " + (str(data.get('coin')) if 'coin' in data else 'UNDEFINED') + ".", end="\n\n")
        else:
            console.print("[bold red]! ERROR[/bold red]: new accounts most be signed-in to the game at least once !.")
            exit(1)
    else:
        console.print("[bold red]! ERROR[/bold red]: seems like your login is not properly set !.")
        exit(1)

def load_key_data(cpm):
    data = cpm.get_key_data()
    console.print("[bold][red]========[/red][ ACCESS KEY DETAILS ][red]========[/red][/bold]")
    console.print("[bold green]Access Key [/bold green]: " + data.get('access_key') + ".")
    console.print("[bold green]Telegram ID[/bold green]: " + str(data.get('telegram_id')) + ".")
    console.print("[bold green]Credits    [/bold green]: " + (str(data.get('coins')) if not data.get('is_unlimited') else 'Unlimited') + ".", end="\n\n")

def prompt_valid_value(content, tag, password=False):
    while True:
        value = Prompt.ask(content, password=password)
        if not value or value.isspace():
            print(tag + " cannot be empty or just spaces. Please try again.")
        else:
            return value

def interpolate_color(start_color, end_color, fraction):
    start_rgb = tuple(int(start_color[i:i+2], 16) for i in (1, 3, 5))
    end_rgb = tuple(int(end_color[i:i+2], 16) for i in (1, 3, 5))
    interpolated_rgb = tuple(int(start + fraction * (end - start)) for start, end in zip(start_rgb, end_rgb))
    return "{:02x}{:02x}{:02x}".format(*interpolated_rgb)

def rainbow_gradient_string(customer_name):
    modified_string = ""
    num_chars = len(customer_name)
    start_color = "{:06x}".format(random.randint(0, 0xFFFFFF))
    end_color = "{:06x}".format(random.randint(0, 0xFFFFFF))
    for i, char in enumerate(customer_name):
        fraction = i / max(num_chars - 1, 1)
        interpolated_color = interpolate_color(start_color, end_color, fraction)
        modified_string += f'[{interpolated_color}]{char}'
    return modified_string

if __name__ == "__main__":
    console = Console()
    signal.signal(signal.SIGINT, signal_handler)
    while True:
        banner(console)
        acc_email = prompt_valid_value("[bold][?] Account Email[/bold]", "Email", password=False)
        acc_password = prompt_valid_value("[bold][?] Account Password[/bold]", "Password", password=False)
        acc_access_key = prompt_valid_value("[bold][?] Access Key[/bold]", "Access Key", password=False)
        console.print("[bold cyan][%] Trying to Login[/bold cyan]: ", end=None)
        cpm = cpmnuker.CPMNuker(acc_access_key)
        login_response = cpm.login(acc_email, acc_password)
        if login_response != 0:
            if login_response == 100:
                console.print("[bold red]ACCOUNT NOT FOUND (✘)[/bold red].")
                sleep(2)
                continue
            elif login_response == 101:
                console.print("[bold red]WRONG PASSWORD (✘)[/bold red].")
                sleep(2)
                continue
            elif login_response == 103:
                console.print("[bold red]INVALID ACCESS KEY (✘)[/bold red].")
                sleep(2)
                continue
            else:
                console.print("[bold red]TRY AGAIN (✘)[/bold red].")
                console.print("[bold yellow]! Note:[/bold yellow]: make sure you filled out the fields !.")
                sleep(2)
                continue
        else:
            console.print("[bold green]SUCCESSFUL (✔)[/bold green].")
            sleep(2)
        while True:
            banner(console)
            load_player_data(cpm)
            load_key_data(cpm)
            choices = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25"]
            console.print("[bold cyan](01): Increase Money ~ 1K[/bold cyan]")
            console.print("[bold cyan](02): Increase Coins ~ 3.5K[/bold cyan]")
            console.print("[bold cyan](03): King Rank ~ 4K[/bold cyan]")
            console.print("[bold cyan](04): Change ID ~ 3.5K[/bold cyan]")
            console.print("[bold cyan](05): Change Name ~ 100[/bold cyan]")
            console.print("[bold cyan](06): Change Name (Rainbow) ~ 100[/bold cyan]")
            console.print("[bold cyan](07): Account Delete ~ FREE[/bold cyan]")
            console.print("[bold cyan](08): Account Register ~ FREE[/bold cyan]")
            console.print("[bold cyan](09): Delete Friends ~ 500[/bold cyan]")
            console.print("[bold cyan](10): Unlock Paid Cars + Siren ~ 5K[/bold cyan]")
            console.print("[bold cyan](11): Unlock w16 Engine ~ 3K[/bold cyan]")
            console.print("[bold cyan](12): Unlock All Horns ~ 3K[/bold cyan]")
            console.print("[bold cyan](13): Unlock Disable Damage ~ 2K[/bold cyan]")
            console.print("[bold cyan](14): Unlock Unlimited Fuel ~ 2K[/bold cyan]")
            console.print("[bold cyan](15): Unlock House 3 ~ 3.5K[/bold cyan]")
            console.print("[bold cyan](16): Unlock Smoke ~ 2K[/bold cyan]")
            console.print("[bold cyan](17): Change Race Wins ~ 1K[/bold cyan]")
            console.print("[bold cyan](18): Change Race Loses ~ 1K[/bold cyan]")
            console.print("[bold cyan](19): Clone Account ~ 5K[/bold cyan]")
            console.print("[bold cyan](20): Unlock all Cars ~ 3K[/bold cyan]")
            console.print("[bold cyan](21): Unlock Siren all Cars ~ 3.5K[/bold cyan]")
            console.print("[bold cyan](22): Unlock Lamborghinis 299hp (IOS Only) ~ 7K[/bold cyan]")
            console.print("[bold cyan](23): Hack Car Speed (299hp) ~ 5K[/bold cyan]")
            console.print("[bold cyan](24): Remove Front Bumper ~ 2.5K[/bold cyan]")
            console.print("[bold cyan](25): Remove Rear Bumper ~ 2.5K[/bold cyan]")
            console.print("[bold cyan](0) : Exit[/bold cyan]", end="\n\n")
            service = IntPrompt.ask("[bold][?] Select a Service [red][1-" + choices[-1] + " or 0][/red][/bold]", choices=choices, show_choices=False)
            if service == 0: # Exit
                console.print("[bold yellow][!] Thank You for using our tool.[/bold yellow].")
            elif service == 1: # Increase Money
                console.print("[bold cyan][!] Insert how much money do you want.[/bold cyan]")
                amount = IntPrompt.ask("[bold][?] Amount[/bold]")
                console.print("[bold cyan][%] Saving your data[/bold cyan]: ", end=None)
                if amount > 0 and amount <= 50000000:
                    if cpm.set_player_money(amount):
                        console.print("[bold green]SUCCESSFUL (✔)[/bold green]")
                        console.print("==================================")
                        answ = Prompt.ask("[bold cyan][?] Do You want to Exit ?[/bold cyan]", choices=["y", "n"], default="n")
                        if answ == "y": console.print("[bold yellow][!] Thank You for using our tool.[/bold yellow].")
                        else: continue
                    else:
                        console.print("[bold red]FAILED (✘)[/bold red]")
                        console.print("[bold yellow][!] Please try again.[/bold yellow]")
                        sleep(2)
                        continue
                else:
                    console.print("[bold red]FAILED (✘)[/bold red]")
                    console.print("[bold yellow][!] Please use valid values.[/bold yellow]")
                    sleep(2)
                    continue
            elif service == 2: # Increase Coins
                console.print("[bold cyan][!] Insert how much coins do you want.[/bold cyan]")
                amount = IntPrompt.ask("[bold][?] Amount[/bold]")
                console.print("[bold cyan][%] Saving your data[/bold cyan]: ", end=None)
                if amount > 0 and amount <= 90000:
                    if cpm.set_player_coins(amount):
                        console.print("[bold green]SUCCESSFUL (✔)[/bold green]")
                        console.print("==================================")
                        answ = Prompt.ask("[bold cyan][?] Do You want to Exit ?[/bold cyan]", choices=["y", "n"], default="n")
                        if answ == "y": console.print("[bold yellow][!] Thank You for using our tool.[/bold yellow].")
                        else: continue
                    else:
                        console.print("[bold red]FAILED (✘)[/bold red]")
                        console.print("[bold yellow][!] Please try again.[/bold yellow]")
                        sleep(2)
                        continue
                else:
                    console.print("[bold red]FAILED (✘)[/bold red]")
                    console.print("[bold yellow][!] Please use valid values.[/bold yellow]")
                    sleep(2)
                    continue
            elif service == 3: # King Rank
                console.print("[bold red][!] Note:[/bold red]: if the king rank doesn't appear in game, close it and open few times.", end=None)
                console.print("[bold red][!] Note:[/bold red]: please don't do King Rank on same account twice.", end=None)
                sleep(2)
                console.print("[bold cyan][%] Giving you a King Rank[/bold cyan]: ", end=None)
                if cpm.set_player_rank():
                    console.print("[bold green]SUCCESSFUL (✔)[/bold green]")
                    console.print("==================================")
                    answ = Prompt.ask("[bold cyan][?] Do You want to Exit ?[/bold cyan]", choices=["y", "n"], default="n")
                    if answ == "y": console.print("[bold yellow][!] Thank You for using our tool.[/bold yellow].")
                    else: continue
                else:
                    console.print("[bold red]FAILED (✘)[/bold red]")
                    console.print("[bold yellow][!] Please try again.[/bold yellow]")
                    sleep(2)
                    continue
            elif service == 4: # Change ID
                console.print("[bold cyan][!] Enter your new ID.[/bold cyan]")
                new_id = Prompt.ask("[bold][?] ID[/bold]")
                console.print("[bold cyan][%] Saving your data[/bold cyan]: ", end=None)
                if len(new_id) >= 9 and len(new_id) <= 14 and (' ' in new_id) == False:
                    if cpm.set_player_localid(new_id.upper()):
                        console.print("[bold green]SUCCESSFUL (✔)[/bold green]")
                        console.print("==================================")
                        answ = Prompt.ask("[bold cyan][?] Do You want to Exit ?[/bold cyan]", choices=["y", "n"], default="n")
                        if answ == "y": console.print("[bold yellow][!] Thank You for using our tool.[/bold yellow].")
                        else: continue
                    else:
                        console.print("[bold red]FAILED (✘)[/bold red]")
                        console.print("[bold yellow][!] Please try again.[/bold yellow]")
                        sleep(2)
                        continue
                else:
                    console.print("[bold red]FAILED (✘)[/bold red]")
                    console.print("[bold yellow][!] Please use valid ID.[/bold yellow]")
                    sleep(2)
                    continue
            elif service == 5: # Change Name
                console.print("[bold cyan][!] Enter your new Name.[/bold cyan]")
                new_name = Prompt.ask("[bold][?] Name[/bold]")
                console.print("[bold cyan][%] Saving your data[/bold cyan]: ", end=None)
                if len(new_name) >= 0 and len(new_name) <= 30:
                    if cpm.set_player_name(new_name):
                        console.print("[bold green]SUCCESSFUL (✔)[/bold green]")
                        console.print("==================================")
                        answ = Prompt.ask("[bold cyan][?] Do You want to Exit ?[/bold cyan]", choices=["y", "n"], default="n")
                        if answ == "y": console.print("[bold yellow][!] Thank You for using our tool.[/bold yellow].")
                        else: continue
                    else:
                        console.print("[bold red]FAILED (✘)[/bold red]")
                        console.print("[bold yellow][!] Please try again.[/bold yellow]")
                        sleep(2)
                        continue
                else:
                    console.print("[bold red]FAILED (✘)[/bold red]")
                    console.print("[bold yellow][!] Please use valid values.[/bold yellow]")
                    sleep(2)
                    continue
            elif service == 6: # Change Name Rainbow
                console.print("[bold cyan][!] Enter your new Rainbow Name.[/bold cyan]")
                new_name = Prompt.ask("[bold][?] Name[/bold]")
                console.print("[bold cyan][%] Saving your data[/bold cyan]: ", end=None)
                if len(new_name) >= 0 and len(new_name) <= 30:
                    if cpm.set_player_name(rainbow_gradient_string(new_name)):
                        console.print("[bold green]SUCCESSFUL (✔)[/bold green]")
                        console.print("==================================")
                        answ = Prompt.ask("[bold cyan][?] Do You want to Exit ?[/bold cyan]", choices=["y", "n"], default="n")
                        if answ == "y": console.print("[bold yellow][!] Thank You for using our tool.[/bold yellow].")
                        else: continue
                    else:
                        console.print("[bold red]FAILED (✘)[/bold red]")
                        console.print("[bold yellow][!] Please try again.[/bold yellow]")
                        sleep(2)
                        continue
                else:
                    console.print("[bold red]FAILED (✘)[/bold red]")
                    console.print("[bold yellow][!] Please use valid values.[/bold yellow]")
                    sleep(2)
                    continue
            elif service == 7: # Account Delete
                console.print("[bold cyan][!] After deleting your account there is no going back !!.[/bold cyan]")
                answ = Prompt.ask("[bold cyan][?] Do You want to Delete this Account ?![/bold cyan]", choices=["y", "n"], default="n")
                if answ == "y":
                    cpm.delete()
                    console.print("[bold cyan][%] Deleting Your Account[/bold cyan]: [bold green]SUCCESSFUL (✔)[/bold green].")
                    console.print("==================================")
                    console.print("[bold yellow][!] Thank You for using our tool.[/bold yellow].")
                else: continue
            elif service == 8: # Account Register
                console.print("[bold cyan][!] Registring new Account.[/bold cyan]")
                acc2_email = prompt_valid_value("[bold][?] Account Email[/bold]", "Email", password=False)
                acc2_password = prompt_valid_value("[bold][?] Account Password[/bold]", "Password", password=False)
                console.print("[bold cyan][%] Creating new Account[/bold cyan]: ", end=None)
                status = cpm.register(acc2_email, acc2_password)
                if status == 0:
                    console.print("[bold green]SUCCESSFUL (✔)[/bold green]")
                    console.print("==================================")
                    console.print("[bold red][!] INFO[/bold red]: In order to tune this account with CPMNuker")
                    console.print("you most sign-in to the game using this account.")
                    sleep(2)
                    continue
                elif status == 105:
                    console.print("[bold red]FAILED (✘)[/bold red]")
                    console.print("[bold yellow][!] This email is already exists !.[/bold yellow]")
                    sleep(2)
                    continue
                else:
                    console.print("[bold red]FAILED (✘)[/bold red]")
                    console.print("[bold yellow][!] Please try again.[/bold yellow]")
                    sleep(2)
                    continue
            elif service == 9: # Delete Friends
                console.print("[bold cyan][%] Deleting your Friends[/bold cyan]: ", end=None)
                if cpm.delete_player_friends():
                    console.print("[bold green]SUCCESSFUL (✔)[/bold green]")
                    console.print("==================================")
                    answ = Prompt.ask("[bold cyan][?] Do You want to Exit ?[/bold cyan]", choices=["y", "n"], default="n")
                    if answ == "y": console.print("[bold yellow][!] Thank You for using our tool.[/bold yellow].")
                    else: continue
                else:
                    console.print("[bold red]FAILED (✘)[/bold red]")
                    console.print("[bold yellow][!] Please try again.[/bold yellow]")
                    sleep(2)
                    continue
            elif service == 10: # Unlock All Paid Cars + Siren
                console.print("[bold yellow]! Note[/bold yellow]: this function takes a while to complete, please don't cancel.")
                console.print("[bold cyan][%] Unlocking All Paid Cars[/bold cyan]: ", end=None)
                if cpm.unlock_paid_cars():
                    console.print("[bold green]SUCCESSFUL (✔)[/bold green]")
                    console.print("==================================")
                    answ = Prompt.ask("[bold cyan][?] Do You want to Exit ?[/bold cyan]", choices=["y", "n"], default="n")
                    if answ == "y": console.print("[bold yellow][!] Thank You for using our tool.[/bold yellow].")
                    else: continue
                else:
                    console.print("[bold red]FAILED (✘)[/bold red]")
                    console.print("[bold yellow][!] Please try again.[/bold yellow]")
                    sleep(2)
                    continue
            elif service == 11: # Unlock w16 Engine
                console.print("[bold cyan][%] Unlocking w16 Engine[/bold cyan]: ", end=None)
                if cpm.unlock_w16():
                    console.print("[bold green]SUCCESSFUL (✔)[/bold green]")
                    console.print("==================================")
                    answ = Prompt.ask("[bold cyan][?] Do You want to Exit ?[/bold cyan]", choices=["y", "n"], default="n")
                    if answ == "y": console.print("[bold yellow][!] Thank You for using our tool.[/bold yellow].")
                    else: continue
                else:
                    console.print("[bold red]FAILED (✘)[/bold red]")
                    console.print("[bold yellow][!] Please try again.[/bold yellow]")
                    sleep(2)
                    continue
            elif service == 12: # Unlock All Horns
                console.print("[bold cyan][%] Unlocking All Horns[/bold cyan]: ", end=None)
                if cpm.unlock_horns():
                    console.print("[bold green]SUCCESSFUL (✔)[/bold green]")
                    console.print("==================================")
                    answ = Prompt.ask("[bold cyan][?] Do You want to Exit ?[/bold cyan]", choices=["y", "n"], default="n")
                    if answ == "y": console.print("[bold yellow][!] Thank You for using our tool.[/bold yellow].")
                    else: continue
                else:
                    console.print("[bold red]FAILED (✘)[/bold red]")
                    console.print("[bold yellow][!] Please try again.[/bold yellow]")
                    sleep(2)
                    continue
            elif service == 13: # Disable Engine Damage
                console.print("[bold cyan][%] Unlocking Disable Damage[/bold cyan]: ", end=None)
                if cpm.disable_engine_damage():
                    console.print("[bold green]SUCCESSFUL (✔)[/bold green]")
                    console.print("==================================")
                    answ = Prompt.ask("[bold cyan][?] Do You want to Exit ?[/bold cyan]", choices=["y", "n"], default="n")
                    if answ == "y": console.print("[bold yellow][!] Thank You for using our tool.[/bold yellow].")
                    else: continue
                else:
                    console.print("[bold red]FAILED (✘)[/bold red]")
                    console.print("[bold yellow][!] Please try again.[/bold yellow]")
                    sleep(2)
                    continue
            elif service == 14: # Unlimited Fuel
                console.print("[bold cyan][%] Unlocking Unlimited Fuel[/bold cyan]: ", end=None)
                if cpm.unlimited_fuel():
                    console.print("[bold green]SUCCESSFUL (✔)[/bold green]")
                    console.print("==================================")
                    answ = Prompt.ask("[bold cyan][?] Do You want to Exit ?[/bold cyan]", choices=["y", "n"], default="n")
                    if answ == "y": console.print("[bold yellow][!] Thank You for using our tool.[/bold yellow].")
                    else: continue
                else:
                    console.print("[bold red]FAILED (✘)[/bold red]")
                    console.print("[bold yellow][!] Please try again.[/bold yellow]")
                    sleep(2)
                    continue
            elif service == 15: # Unlock House 3
                console.print("[bold cyan][%] Unlocking House 3[/bold cyan]: ", end=None)
                if cpm.unlock_houses():
                    console.print("[bold green]SUCCESSFUL (✔)[/bold green]")
                    console.print("==================================")
                    answ = Prompt.ask("[bold cyan][?] Do You want to Exit ?[/bold cyan]", choices=["y", "n"], default="n")
                    if answ == "y": console.print("[bold yellow][!] Thank You for using our tool.[/bold yellow].")
                    else: continue
                else:
                    console.print("[bold red]FAILED (✘)[/bold red]")
                    console.print("[bold yellow][!] Please try again.[/bold yellow]")
                    sleep(2)
                    continue
            elif service == 16: # Unlock Smoke
                console.print("[bold cyan][%] Unlocking Smoke[/bold cyan]: ", end=None)
                if cpm.unlock_smoke():
                    console.print("[bold green]SUCCESSFUL (✔)[/bold green]")
                    console.print("==================================")
                    answ = Prompt.ask("[bold cyan][?] Do You want to Exit ?[/bold cyan]", choices=["y", "n"], default="n")
                    if answ == "y": console.print("[bold yellow][!] Thank You for using our tool.[/bold yellow].")
                    else: continue
                else:
                    console.print("[bold red]FAILED (✘)[/bold red]")
                    console.print("[bold yellow][!] Please try again.[/bold yellow]")
                    sleep(2)
                    continue
            elif service == 17: # Change Races Wins
                console.print("[bold cyan][!] Insert how much races you win.[/bold cyan]")
                amount = IntPrompt.ask("[bold][?] Amount[/bold]")
                console.print("[bold cyan][%] Changing your data[/bold cyan]: ", end=None)
                if amount > 0 and amount <= 999:
                    if cpm.set_player_wins(amount):
                        console.print("[bold green]SUCCESSFUL (✔)[/bold green]")
                        console.print("==================================")
                        answ = Prompt.ask("[bold cyan][?] Do You want to Exit ?[/bold cyan]", choices=["y", "n"], default="n")
                        if answ == "y": console.print("[bold yellow][!] Thank You for using our tool.[/bold yellow].")
                        else: continue
                    else:
                        console.print("[bold red]FAILED (✘)[/bold red]")
                        console.print("[bold yellow][!] Please try again.[/bold yellow]")
                        sleep(2)
                        continue
                else:
                    console.print("[bold red]FAILED (✘)[/bold red]")
                    console.print("[bold yellow][!] Please use valid values.[/bold yellow]")
                    sleep(2)
                    continue
            elif service == 18: # Change Races Loses
                console.print("[bold cyan][!] Insert how much races you lose.[/bold cyan]")
                amount = IntPrompt.ask("[bold][?] Amount[/bold]")
                console.print("[bold cyan][%] Changing your data[/bold cyan]: ", end=None)
                if amount > 0 and amount <= 999:
                    if cpm.set_player_loses(amount):
                        console.print("[bold green]SUCCESSFUL (✔)[/bold green]")
                        console.print("==================================")
                        answ = Prompt.ask("[bold cyan][?] Do You want to Exit ?[/bold cyan]", choices=["y", "n"], default="n")
                        if answ == "y": console.print("[bold yellow][!] Thank You for using our tool.[/bold yellow].")
                        else: continue
                    else:
                        console.print("[bold red]FAILED (✘)[/bold red]")
                        console.print("[bold yellow][!] Please try again.[/bold yellow]")
                        sleep(2)
                        continue
                else:
                    console.print("[bold red]FAILED (✘)[/bold red]")
                    console.print("[bold yellow][!] Please use valid values.[/bold yellow]")
                    sleep(2)
                    continue
            elif service == 19: # Clone Account
                console.print("[bold cyan]Please Enter Account Detalis[/bold cyan]:")
                to_email = prompt_valid_value("[bold][?] Email[/bold]", "Email", password=False)
                to_password = prompt_valid_value("[bold][?] Password[/bold]", "Password", password=False)
                console.print("[bold cyan][%] Cloning your account[/bold cyan]: ", end=None)
                if cpm.account_clone(to_email, to_password):
                    console.print("[bold green]SUCCESSFUL.[/bold green]")
                    console.print("==================================")
                    answ = Prompt.ask("[bold cyan][?] Do You want to Exit ?[/bold cyan]", choices=["y", "n"], default="n")
                    if answ == "y": console.print("[bold yellow][!] Thank You for using our tool.[/bold yellow].")
                    else: continue
                else:
                    console.print("[bold red]FAILED.[/bold red]")
                    console.print("[bold yellow][!] Please try again.[/bold yellow]")
                    sleep(2)
                    continue
            elif service == 20: # Unlock all cars
                console.print("[bold yellow][!] Note[/bold yellow]: this function takes a while to complete, please don't cancel.")
                console.print("[bold cyan][%] Unlocking All Cars[/bold cyan]: ", end=None)
                if cpm.unlock_all_cars():
                    console.print("[bold green]SUCCESSFUL (✔)[/bold green]")
                    console.print("==================================")
                    answ = Prompt.ask("[bold cyan][?] Do You want to Exit ?[/bold cyan]", choices=["y", "n"], default="n")
                    if answ == "y": console.print("[bold yellow][!] Thank You for using our tool.[/bold yellow].")
                    else: continue
                else:
                    console.print("[bold red]FAILED (✘)[/bold red]")
                    console.print("[bold yellow][!] Please try again.[/bold yellow]")
                    sleep(2)
                    continue
            elif service == 21: # Unlock Siren all cars
                console.print("[bold cyan][%] Unlocking All Cars Siren[/bold cyan]: ", end=None)
                if cpm.unlock_all_cars_siren():
                    console.print("[bold green]SUCCESSFUL.[/bold green]")
                    console.print("==================================")
                    answ = Prompt.ask("[bold cyan][?] Do You want to Exit ?[/bold cyan]", choices=["y", "n"], default="n")
                    if answ == "y": console.print("[bold yellow][!] Thank You for using our tool.[/bold yellow].")
                    else: continue
                else:
                    console.print("[bold red]FAILED.[/bold red]")
                    console.print("[bold yellow][!] Please try again.[/bold yellow]")
                    sleep(2)
                    continue
            elif service == 22: # Unlocking lamborghinis 299hp (IOS Only)
                console.print("[bold cyan][%] Unlocking lamborghinis 299hp (IOS Only)[/bold cyan]: ", end=None)
                if cpm.unlock_lambo_ios_hs():
                    console.print("[bold green]SUCCESSFUL.[/bold green]")
                    console.print("==================================")
                    answ = Prompt.ask("[bold cyan][?] Do You want to Exit ?[/bold cyan]", choices=["y", "n"], default="n")
                    if answ == "y": console.print("[bold yellow][!] Thank You for using our tool.[/bold yellow].")
                    else: continue
                else:
                    console.print("[bold red]FAILED.[/bold red]")
                    console.print("[bold yellow][!] Please try again.[/bold yellow]")
                    sleep(2)
                    continue
            elif service == 23: # Hack Car Speed (299hp)
                console.print("[bold yellow][!] Note[/bold yellow]: original speed can not be restored !.")
                console.print("[bold cyan][!] Enter Car Details.[/bold cyan]")
                car_id = IntPrompt.ask("[bold][?] Car ID[/bold]")
                console.print("[bold cyan][%] Hacking Car Speed[/bold cyan]: ", end=None)
                if cpm.hack_car_speed(car_id):
                    console.print("[bold green]SUCCESSFUL (✔)[/bold green]")
                    console.print("==================================")
                    answ = Prompt.ask("[bold cyan][?] Do You want to Exit ?[/bold cyan]", choices=["y", "n"], default="n")
                    if answ == "y": console.print("[bold yellow][!] Thank You for using our tool.[/bold yellow].")
                    else: continue
                else:
                    console.print("[bold red]FAILED (✘)[/bold red]")
                    console.print("[bold yellow][!] Please try again.[/bold yellow]")
                    sleep(2)
                    continue
            elif service == 24: # Remove Front Bumper
                console.print("[bold cyan][!] Enter Car Details.[/bold cyan]")
                car_id = IntPrompt.ask("[bold][?] Car ID[/bold]")
                console.print("[bold cyan][%] Removing Bumber[/bold cyan]: ", end=None)
                if cpm.remove_front_bumper(car_id):
                    console.print("[bold green]SUCCESSFUL (✔)[/bold green]")
                    console.print("==================================")
                    answ = Prompt.ask("[bold cyan][?] Do You want to Exit ?[/bold cyan]", choices=["y", "n"], default="n")
                    if answ == "y": console.print("[bold yellow][!] Thank You for using our tool.[/bold yellow].")
                    else: continue
                else:
                    console.print("[bold red]FAILED (✘)[/bold red]")
                    console.print("[bold yellow][!] Please try again.[/bold yellow]")
                    sleep(2)
                    continue
            elif service == 25: # Remove Rear Bumper
                console.print("[bold cyan][!] Enter Car Details.[/bold cyan]")
                car_id = IntPrompt.ask("[bold][?] Car ID[/bold]")
                console.print("[bold cyan][%] Removing Bumber[/bold cyan]: ", end=None)
                if cpm.remove_rear_bumper(car_id):
                    console.print("[bold green]SUCCESSFUL (✔)[/bold green]")
                    console.print("==================================")
                    answ = Prompt.ask("[bold cyan][?] Do You want to Exit ?[/bold cyan]", choices=["y", "n"], default="n")
                    if answ == "y": console.print("[bold yellow][!] Thank You for using our tool.[/bold yellow].")
                    else: continue
                else:
                    console.print("[bold red]FAILED (✘)[/bold red]")
                    console.print("[bold yellow][!] Please try again.[/bold yellow]")
                    sleep(2)
                    continue
            else:
                continue
            break
        break
