import os, colorama, subprocess, time
from multiprocessing import Process
from colorama import init, Fore, Back
def clear():
     os.system('clear')
clear()
print(f"""
{Back.WHITE}
{Fore.BLACK}
 ____  ____  _____    _    ____     ____ ____  __  __ 
|  _ \|  _ \| ____|  / \  |  _ \   / ___/ ___||  \/  |
| | | | |_) |  _|   / _ \ | | | | | |  _\___ \| |\/| |
| |_| |  _ <| |___ / ___ \| |_| | | |_| |___) | |  | |
|____/|_| \_\_____/_/   \_\____/   \____|____/|_|  |_|
                                                      
{Fore.RESET}
{Back.RESET}
""")
print(f"{Fore.GREEN}Attack menu")

def livemon(arg1, arg2):
    os.system(f'grgsm_livemon -f {arg2} --args={arg1} >/dev/null 2>&1')

def listen(arg1, arg2):
    clear()
    print(f"{Fore.BLUE} Starting listen with {arg1} on frequency {arg2}... {Fore.GREEN}")
    p = Process(target=livemon, args=(arg1, arg2,))
    p.start()
    os.chdir('IMSI-catcher')
    time.sleep(2)
    os.system('clear')
    print(f"{Fore.BLUE}Listening with {arg1} on frequency {arg2}... {Fore.GREEN}")
    os.system('python3 simple_IMSI-catcher.py -s')

def main(ss):
    global sdr
    if ss == '0':
        sdr = 'rtl'
    elif ss == '1':
        sdr = 'bladerf'
    elif ss == '2':
        sdr = 'hackrf'
    elif ss == '3':
        sdr = 'airspy'
    elif ss == '4':
        sdr = 'airspyf'
    elif ss == '5':
        sdr = 'soapy'
    elif ss == '6':
        sdr = 'rtl_tcp'
    else:
        select()
    clear()
    print(f"{Fore.GREEN} Your sdr is: {sdr}, right? Y/N {Fore.WHITE}")
    sr = input(f"Dre@d{Fore.GREEN}~/attack/sdr{Fore.BLUE}: ")
    if sr == 'Y' or sr == 'y':
        scan(sdr)
    if sr == 'N':
        clear()
        select()

def select():
    print(f"""
    {Fore.BLUE}
=============================
    Select your SDR:

    rtl-sdr - 0

    bladerf - 1

    hackrf - 2

    airspy - 3

    airspyf - 4

    soapysdr - 5
    
    rtl-tcp - 6
=============================

{Fore.WHITE}
    """)
    ss = input(f"Dre@d{Fore.GREEN}~/attack/sdr{Fore.BLUE}: ")
    main(ss)

def scan(arg):
    print(f"{Fore.BLUE} Scanning with {arg}... {Fore.GREEN}")
    os.system(f'grgsm_scanner -v -b GSM900 --args={arg}')
    print(f"{Fore.BLUE}Done!{Fore.WHITE}")
    starter()


def starter():
    print(f"{Fore.GREEN}Type in your preferred frequency:{Fore.WHITE}")
    sr = input(f"Dre@d{Fore.GREEN}~/attack/sdr/freq{Fore.BLUE}: ")
    print(f"{Fore.GREEN} Your frequency is: {sr}, right? Y/N or redoscan {Fore.WHITE}")
    sd = input(f"Dre@d{Fore.GREEN}~/attack/sdr/freq{Fore.BLUE}: ")
    if sd == 'Y' or sd == 'y':
        clear()
        listen(sdr, sr)
    elif sd == 'redoscan':
        clear()
        scan(sdr)
    else:
        starter()
        

select()

