import os, colorama
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
def select():
    print(f"""
    {Fore.GREEN}
    By GLUTEN
    Inspired by fuckwbored
    {Fore.BLUE}
=============================
    Select:

    Info - 0

    Setup DRE@AD - 1

    Run DRE@AD attack menu - 2
=============================

{Fore.WHITE}
    """)
    global ss
    ss = input(f"Dre@d{Fore.GREEN}~{Fore.BLUE}: ")


def main():
    select()
    if ss == '0':
        clear()
        print(f"""
              {Fore.RED}
Made by GLUTEN,
a 12 y/o boy 

Inspired by fuckwbored
admin of TG:termuxqew

DRE@D AUTOGSM V. 1.2

Script made for automation
of using IMSI-catcher and searching
base stations.
              """)
        print(f"{Fore.BLUE} Back? Y/N {Fore.WHITE}")

        sw = input(f"Dre@d{Fore.GREEN}~/info{Fore.BLUE}:")
        if sw == 'Y' or sw == 'y':
            clear()
            main()
        else:
            clear()
            print(f"{Fore.RED} Thanks for using!")
            os.system('exit')
    elif ss == '1':
        setup()
    elif ss == '2':
        os.system('python main.py')

def setup():
    print(f"{Fore.GREEN} Installing...{Fore.WHITE}")
    os.system('apt update')
    os.system('apt -y install git && apt -y install python3 && git clone https://github.com/Oros42/IMSI-catcher.git')
    os.system('apt -y install gnuradio gr-gsm gnuradio-dev git cmake autoconf libtool pkg-config g++ gcc make libc6 libc6-dev libcppunit-dev swig doxygen liblog4cpp5v5 liblog4cpp5-dev gr-osmosdr osmo-sdr libosmosdr-dev libboost-all-dev libgmp-dev liborc-dev libboost-regex-dev build-essential automake librtlsdr-dev libfftw3-dev tshark')
    os.system('apt -y install gqrx-sdr:i386 gqrx-sdr libcppunit-dev libcppunit-doc')
    os.system('apt -y install libc6 libgcc1')
    os.system('apt -y install libcppunit-1.13-0v5 libcunit1 libcunit1-doc libcunit1-dev libjs-qunit libjs-sink-test node-sink-test')
    os.system('apt -y install osinfo-db-tools iraf-dev libgnuradio-osmosdr0.2.0:i386')
    print(f"{Fore.GREEN} Done! Now you can run main.py or run in menu{Fore.WHITE}")
    print(f"{Fore.BLUE} Exit to menu? Y/N {Fore.WHITE}")
    sw = input(f"Dre@d{Fore.GREEN}~{Fore.BLUE}/setup:")
    if sw == 'Y' or sw == 'y':
        clear()
        main()
    else:
        clear()
        print(f"{Fore.RED} Thanks for using!")
        os.system('exit')

main()
