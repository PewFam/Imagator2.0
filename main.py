import urllib.request
from colorama import Fore
from pathlib import Path
import os

import time

import sys


from quo.dialog import MessageBox

MessageBox(
    title='From PewFam',
    text='Hey, this is the V2 of Imagator',
    ok_text  = "GO !")
    
payload = """     _ __       ,----.          ,-.-.      _,---.   ,---.             ___   
  .-`.' ,`.  ,-.--` , \,-..-.-./  \==\ .-`.' ,  \ .--.'  \     .-._ .'=.'\  
 /==/, -   \|==|-  _.-`|, \=/\=|- |==|/==/_  _.-' \==\-/\ \   /==/ \|==|  | 
|==| _ .=. ||==|   `.-.|- |/ |/ , /==/==/-  '..-. /==/-|_\ |  |==|,|  / - | 
|==| , '=',/==/_ ,    / \, ,     _|==|==|_ ,    / \==\,   - \ |==|  \/  , | 
|==|-  '..'|==|    .-'  | -  -  , |==|==|   .--'  /==/ -   ,| |==|- ,   _ | 
|==|,  |   |==|_  ,`-._  \  ,  - /==/|==|-  |    /==/-  /\ - \|==| _ /\   | 
/==/ - |   /==/ ,     /  |-  /\ /==/ /==/   \    \==\ _.\=\.-'/==/  / / , / 
`--`---'   `--`-----``   `--`  `--`  `--`---'     `--`        `--`./  `--`               """



default = """
.----------.---------------------------.
| Commands |        Utility            |
:----------+---------------------------:
| help     | shows all of the commands |
'----------'---------------------------'\n\n\n"""


help = ("""\n\n...........................................................................
: Commands :                           Utility                            :
:..........:..............................................................:
: download :      Downloads an image in default Windows picture folder    :
:..........:..............................................................:
:   exit   :                      Stops the program                       :
:..........:..............................................................:
\n\n
""")
def clear():
    if os.name == 'nt': os.system('cls')
    else: os.system('clear')
def typingPrint(text):
        for character in text:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.007)
print(Fore.CYAN+ payload)
print(Fore.GREEN + default +Fore.LIGHTRED_EX
 )


while True:
    command= input("")
    if command == "help":
        print(f'{Fore.GREEN}{help}{Fore.LIGHTRED_EX}')
    if command == "download":
        typingPrint(f'\n{Fore.MAGENTA}Enter the image link ( with "https://" ) =>{Fore.LIGHTRED_EX}\n\n')
        link=input('')
        typingPrint(f'\n{Fore.MAGENTA}Save image as ? =>{Fore.LIGHTRED_EX}\n\n')
        name = input('')
        def download(url, fp, fn):
            full = fp + fn + '.jpg'
            urllib.request.urlretrieve(url, full)
            typingPrint(f'\n{Fore.MAGENTA}Image has been correctly downloaded in the default Windows picture folder. Thanks for using <3 {Fore.LIGHTRED_EX}\n\n')
            input('')
            print('\n\n\n\n\n\n\n\n\n\n\n')
            print(Fore.CYAN+ payload)
            print(Fore.GREEN + default +Fore.LIGHTRED_EX)
        try:
            download(link, str(Path.cwd()) + "\Pictures\ ", name)
        except:
            typingPrint(f'\n{Fore.LIGHTYELLOW_EX}/!\ An error has occured : check your link or the name of the file. File has not been downloaded...{Fore.LIGHTRED_EX}\n\n')
    if command == "exit":
        typingPrint(f'\n{Fore.BLUE}Thanks for using <3 Goodbye ! {Fore.LIGHTRED_EX}\n\n')
        sys.exit()
