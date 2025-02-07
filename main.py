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

__CHANNEL_USERNAME__ = "https://t.me/TelmunnDev"
__GROUP_USERNAME__   = "BaldanShopChat"

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
    os.system('cls' if os.name == 'nt' else 'clear')
    brand_name =  "Car Parking Multiplayer 1 Tool - t.me/Kayzenn1P"
    colors = [
        "rgb(255,0,0)", "rgb(255,69,0)", "rgb(255,140,0)", "rgb(255,215,0)", "rgb(173,255,47)", 
        "rgb(0,255,0)", "rgb(0,255,255)", "rgb(0,191,255)", "rgb(0,0,255)", "rgb(139,0,255)",
        "rgb(255,0,255)"
    ]
    colorful_text = gradient_text(brand_name, colors)
    console.print(colorful_text)
    print(Colorate.Horizontal(Colors.rainbow, '=================================================================='))
    print(Colorate.Horizontal(Colors.rainbow, '\t         ЭНЭ ХЭРЭГСЛИЙГ АШИГЛАХЫН ӨМНӨ CPM-ээс ГАРНА УУ
                                                          PLEASE LOG OUT OF CPM BEFORE USING THIS TOOL!
'))
    print(Colorate.Horizontal(Colors.rainbow, '    𝐒𝐇𝐀𝐑𝐈𝐍𝐆 𝐓𝐇𝐄 𝐀𝐂𝐂𝐄𝐒𝐒 𝐊𝐄𝐘 𝐈𝐒 𝐍𝐎𝐓 𝐀𝐋𝐋𝐎𝐖𝐄𝐃 𝐀𝐍𝐃 𝐖𝐈𝐋𝐋 𝐁𝐄 𝐁𝐋𝐎𝐂𝐊𝐄𝐃'))
    print(Colorate.Horizontal(Colors.rainbow, f' ‌  𝐓𝐞𝐥𝐞𝐠𝐫𝐚𝐦: @{__CHANNEL_USERNAME__} 𝐎𝐫 @{__GROUP_USERNAME__}'))
    print(Colorate.Horizontal(Colors.rainbow, '=================================================================='))

def load_player_data(cpm):
    response = cpm.get_player_data()
    if response.get('ok'):
        data = response.get('data')
        if 'floats' in data and 'localID' in data and 'money' in data and 'coin' in data:
        
            print(Colorate.Horizontal(Colors.rainbow, '==========[ PLAYER DETAILS ]=========='))
            
            print(Colorate.Horizontal(Colors.rainbow, f'Name   : {(data.get("Name") if "Name" in data else "UNDEFINED")}.'))
                
            print(Colorate.Horizontal(Colors.rainbow, f'LocalID: {data.get("localID")}.'))
            
            print(Colorate.Horizontal(Colors.rainbow, f'Money  : {data.get("money")}.'))
            
            print(Colorate.Horizontal(Colors.rainbow, f'Coins  : {data.get("coin")}.'))
            
        else:
            print(Colorate.Horizontal(Colors.rainbow, '! ERROR: new accounts most be signed-in to the game at least once !.'))
            exit(1)
    else:
        print(Colorate.Horizontal(Colors.rainbow, '! ERROR: seems like your login is not properly set !.'))
        exit(1)


def load_key_data(cpm):

    data = cpm.get_key_data()
    
    print(Colorate.Horizontal(Colors.rainbow, '========[ ACCESS KEY DETAILS ]========'))
    
    print(Colorate.Horizontal(Colors.rainbow, f'Access Key : {data.get("access_key")}.'))
    
    print(Colorate.Horizontal(Colors.rainbow, f'Telegram ID: {data.get("telegram_id")}.'))
    
    print(Colorate.Horizontal(Colors.rainbow, f'Balance $  : {(data.get("coins") if not data.get("is_unlimited") else "Unlimited")}.'))
        
    

def prompt_valid_value(content, tag, password=False):
    while True:
        value = Prompt.ask(content, password=password)
        if not value or value.isspace():
            print(Colorate.Horizontal(Colors.rainbow, f'{tag} cannot be empty or just spaces. Please try again.'))
        else:
            return value
            
def load_client_details():
    response = requests.get("http://ip-api.com/json")
    data = response.json()
    print(Colorate.Horizontal(Colors.rainbow, '=============[ 𝐋𝐎𝐂𝐀𝐓𝐈𝐎𝐍 ]============='))
    print(Colorate.Horizontal(Colors.rainbow, f'Ip Address : {data.get("hidden")}.'))
    print(Colorate.Horizontal(Colors.rainbow, f'Location   : {data.get("city")} {data.get("regionName")} {data.get("countryCode")}.'))
    print(Colorate.Horizontal(Colors.rainbow, f'Country    : {data.get("country")} {data.get("zip")}.'))
    print(Colorate.Horizontal(Colors.rainbow, '===============[ 𝐌𝐄𝐍𝐔 ]==============='))

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
        cpm = CPMTooldevz(acc_access_key)
        login_response = cpm.login(acc_email, acc_password)
        if login_response != 0:
            if login_response == 100:
                print(Colorate.Horizontal(Colors.rainbow, 'ACCOUNT NOT FOUND.'))
                sleep(2)
                continue
            elif login_response == 101:
                print(Colorate.Horizontal(Colors.rainbow, 'WRONG PASSWORD.'))
                sleep(2)
                continue
            elif login_response == 103:
                print(Colorate.Horizontal(Colors.rainbow, 'INVALID ACCESS KEY.'))
                sleep(2)
                continue
            else:
                print(Colorate.Horizontal(Colors.rainbow, 'TRY AGAIN.'))
                print(Colorate.Horizontal(Colors.rainbow, '! Note: make sure you filled out the fields !.'))
                sleep(2)
                continue
        else:
            print(Colorate.Horizontal(Colors.rainbow, 'SUCCESSFUL.'))
            sleep(2)
        while True:
            banner(console)
            load_player_data(cpm)
            load_key_data(cpm)
            load_client_details()
            choices = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26"]
            print(Colorate.Horizontal(Colors.rainbow, '{01}: Increase Money           1,000₮'))
            print(Colorate.Horizontal(Colors.rainbow, '{02}: Increase Coins           3,500₮'))
            print(Colorate.Horizontal(Colors.rainbow, '{03}: King Rank                4,000₮'))
            print(Colorate.Horizontal(Colors.rainbow, '{04}: Change ID                3,500₮'))
            print(Colorate.Horizontal(Colors.rainbow, '{05}: Change Name              100₮'))
            print(Colorate.Horizontal(Colors.rainbow, '{06}: Change Name (Rainbow)    100₮'))
            print(Colorate.Horizontal(Colors.rainbow, '{07}: Number Plates            2,000₮'))
            print(Colorate.Horizontal(Colors.rainbow, '{08}: Account Delete           Үнэгүй'))
            print(Colorate.Horizontal(Colors.rainbow, '{09}: Account Register         Үнэгүй'))
            print(Colorate.Horizontal(Colors.rainbow, '{10}: Delete Friends           500₮'))
            print(Colorate.Horizontal(Colors.rainbow, '{11}: Unlock Paid Cars         4,000₮'))
            print(Colorate.Horizontal(Colors.rainbow, '{12}: Unlock all Cars          3,000₮'))
            print(Colorate.Horizontal(Colors.rainbow, '{13}: Unlock all Cars Siren    2,000₮'))
            print(Colorate.Horizontal(Colors.rainbow, '{14}: Unlock w16 Engine        3,000₮'))
            print(Colorate.Horizontal(Colors.rainbow, '{15}: Unlock All Horns         3,000₮'))
            print(Colorate.Horizontal(Colors.rainbow, '{16}: Unlock Disable Damage    2,000₮'))
            print(Colorate.Horizontal(Colors.rainbow, '{17}: Unlock Unlimited Fuel    2,000₮'))
            print(Colorate.Horizontal(Colors.rainbow, '{18}: Unlock House 3           3,500₮'))
            print(Colorate.Horizontal(Colors.rainbow, '{19}: Unlock Smoke             2,000₮'))
            print(Colorate.Horizontal(Colors.rainbow, '{20}: Unlock Wheels            4,000₮'))
            print(Colorate.Horizontal(Colors.rainbow, '{21}: Unlock Animations        2,000₮'))
            print(Colorate.Horizontal(Colors.rainbow, '{22}: Unlock Equipaments M     3,000₮'))
            print(Colorate.Horizontal(Colors.rainbow, '{23}: Unlock Equipaments F     3,000₮'))
            print(Colorate.Horizontal(Colors.rainbow, '{24}: Change Race Wins         1,000₮'))
            print(Colorate.Horizontal(Colors.rainbow, '{25}: Change Race Loses        1,000₮'))
            print(Colorate.Horizontal(Colors.rainbow, '{26}: Clone Account            5,000₮'))
            print(Colorate.Horizontal(Colors.rainbow, '{0} : Exit'))
            
            print(Colorate.Horizontal(Colors.rainbow, '===============[ Baldan☆ ]==============='))
            
            service = IntPrompt.ask(f"[bold][?] Select a Service [red][1-{choices[-1]} or 0][/red][/bold]", choices=choices, show_choices=False)
            
            print(Colorate.Horizontal(Colors.rainbow, '===============[ Baldan☆ ]==============='))
            
            if service == 0: # Exit
                print(Colorate.Horizontal(Colors.rainbow, f'Thank You for using our tool, please join our telegram channel: @{__CHANNEL_USERNAME__}.'))
            elif service == 1: # Increase Money
                print(Colorate.Horizontal(Colors.rainbow, '[?] Insert how much money do you want.'))
                amount = IntPrompt.ask("[?] Amount")
                console.print("[%] Saving your data: ", end=None)
                if amount > 0 and amount <= 999999999:
                    if cpm.set_player_money(amount):
                        print(Colorate.Horizontal(Colors.rainbow, 'SUCCESSFUL'))
                        print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                        answ = Prompt.ask("[?] Do You want to Exit ?", choices=["y", "n"], default="n")
                        if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'Thank You for using our tool, please join our telegram channe: @{__CHANNEL_USERNAME__}.'))
                        else: continue
                    else:
                        print(Colorate.Horizontal(Colors.rainbow, 'FAILED.'))
                        print(Colorate.Horizontal(Colors.rainbow, 'Please try again.'))
                        sleep(2)
                        continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'FAILED.'))
                    print(Colorate.Horizontal(Colors.rainbow, 'Please use valid values.'))
                    sleep(2)
                    continue
            elif service == 2: # Increase Coins
                print(Colorate.Horizontal(Colors.rainbow, '[?] Insert how much coins do you want.'))
                amount = IntPrompt.ask("[?] Amount")
                console.print("[%] Saving your data: ", end=None)
                if amount > 0 and amount <= 999999999:
                    if cpm.set_player_coins(amount):
                        print(Colorate.Horizontal(Colors.rainbow, 'SUCCESSFUL'))
                        print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                        answ = Prompt.ask("[?] Do You want to Exit ?", choices=["y", "n"], default="n")
                        if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'Thank You for using our tool, please join our telegram channe: @{__CHANNEL_USERNAME__}.'))
                        else: continue
                    else:
                        print(Colorate.Horizontal(Colors.rainbow, 'FAILED.'))
                        print(Colorate.Horizontal(Colors.rainbow, 'Please try again.'))
                        sleep(2)
                        continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'FAILED.'))
                    print(Colorate.Horizontal(Colors.rainbow, 'Please use valid values.'))
                    sleep(2)
                    continue
            elif service == 3: # King Rank
                console.print("[bold red][!] Note:[/bold red]: if the king rank doesn't appear in game, close it and open few times.", end=None)
                console.print("[bold red][!] Note:[/bold red]: please don't do King Rank on same account twice.", end=None)
                sleep(2)
                console.print("[%] Giving you a King Rank: ", end=None)
                if cpm.set_player_rank():
                    print(Colorate.Horizontal(Colors.rainbow, 'SUCCESSFUL'))
                    print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                    answ = Prompt.ask("[?] Do You want to Exit ?", choices=["y", "n"], default="n")
                    if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'Thank You for using our tool, please join our telegram channe: @{__CHANNEL_USERNAME__}.'))
                    else: continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'FAILED.'))
                    print(Colorate.Horizontal(Colors.rainbow, 'Please try again.'))
                    sleep(2)
                    continue
            elif service == 4: # Change ID
                print(Colorate.Horizontal(Colors.rainbow, '[?] Enter your new ID.'))
                new_id = Prompt.ask("[?] ID")
                console.print("[%] Saving your data: ", end=None)
                if len(new_id) >= 0 and len(new_id) <= 999999999 and (' ' in new_id) == False:
                    if cpm.set_player_localid(new_id.upper()):
                        print(Colorate.Horizontal(Colors.rainbow, 'SUCCESSFUL'))
                        print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                        answ = Prompt.ask("[?] Do You want to Exit ?", choices=["y", "n"], default="n")
                        if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'Thank You for using our tool, please join our telegram channe: @{__CHANNEL_USERNAME__}.'))
                        else: continue
                    else:
                        print(Colorate.Horizontal(Colors.rainbow, 'FAILED.'))
                        print(Colorate.Horizontal(Colors.rainbow, 'Please try again.'))
                        sleep(2)
                        continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'FAILED.'))
                    print(Colorate.Horizontal(Colors.rainbow, 'Please use valid ID.'))
                    sleep(2)
                    continue
            elif service == 5: # Change Name
                print(Colorate.Horizontal(Colors.rainbow, '[?] Enter your new Name.'))
                new_name = Prompt.ask("[?] Name")
                console.print("[%] Saving your data: ", end=None)
                if len(new_name) >= 0 and len(new_name) <= 999999999:
                    if cpm.set_player_name(new_name):
                        print(Colorate.Horizontal(Colors.rainbow, 'SUCCESSFUL'))
                        print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                        answ = Prompt.ask("[?] Do You want to Exit ?", choices=["y", "n"], default="n")
                        if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'Thank You for using our tool, please join our telegram channe: @{__CHANNEL_USERNAME__}.'))
                        else: continue
                    else:
                        print(Colorate.Horizontal(Colors.rainbow, 'FAILED.'))
                        print(Colorate.Horizontal(Colors.rainbow, 'Please try again.'))
                        sleep(2)
                        continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'FAILED.'))
                    print(Colorate.Horizontal(Colors.rainbow, 'Please use valid values.'))
                    sleep(2)
                    continue
            elif service == 6: # Change Name Rainbow
                print(Colorate.Horizontal(Colors.rainbow, '[?] Enter your new Rainbow Name.'))
                new_name = Prompt.ask("[?] Name")
                console.print("[%] Saving your data: ", end=None)
                if len(new_name) >= 0 and len(new_name) <= 999999999:
                    if cpm.set_player_name(rainbow_gradient_string(new_name)):
                        print(Colorate.Horizontal(Colors.rainbow, 'SUCCESSFUL'))
                        print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                        answ = Prompt.ask("[?] Do You want to Exit ?", choices=["y", "n"], default="n")
                        if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'Thank You for using our tool, please join our telegram channe: @{__CHANNEL_USERNAME__}.'))
                        else: continue
                    else:
                        print(Colorate.Horizontal(Colors.rainbow, 'FAILED.'))
                        print(Colorate.Horizontal(Colors.rainbow, 'Please try again.'))
                        sleep(2)
                        continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'FAILED.'))
                    print(Colorate.Horizontal(Colors.rainbow, 'Please use valid values.'))
                    sleep(2)
                    continue
            elif service == 7: # Number Plates
                console.print("[%] Giving you a Number Plates: ", end=None)
                if cpm.set_player_plates():
                    print(Colorate.Horizontal(Colors.rainbow, 'SUCCESSFUL'))
                    print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                    answ = Prompt.ask("[?] Do You want to Exit ?", choices=["y", "n"], default="n")
                    if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'Thank You for using our tool, please join our telegram channe: @{__CHANNEL_USERNAME__}.'))
                    else: continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'FAILED.'))
                    print(Colorate.Horizontal(Colors.rainbow, 'Please try again.'))
                    sleep(2)
                    continue
            elif service == 8: # Account Delete
                print(Colorate.Horizontal(Colors.rainbow, '[!] After deleting your account there is no going back !!.'))
                answ = Prompt.ask("[?] Do 
