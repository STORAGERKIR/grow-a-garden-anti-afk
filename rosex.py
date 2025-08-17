import subprocess
import sys

# Automatically install missing packages
required = ['pygetwindow', 'pynput', 'colorama']
for package in required:
    try:
        __import__(package)
    except ImportError:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# Now import the installed modules
import time
import datetime
import pygetwindow as gw
from pynput.keyboard import Controller, Listener
from colorama import init, Fore

# Initialize colorama
init()

keyboard = Controller()
skip_next = False  # Flag to skip next jump

def bring_roblox_to_front():
    for window in gw.getAllWindows():
        if "Roblox" in window.title:
            try:
                window.activate()
                return True
            except:
                return False
    return False

def perform_action():  # Renamed from jump()
    keyboard.press(' ')  # Space
    keyboard.press('d')  # D key
    time.sleep(0.05)
    keyboard.release('d')
    keyboard.release(' ')
    # Mouse wheel simulation (if needed)
    # Note: pynput doesn't support mouse wheel directly - would need mouse controller

def format_time(seconds):
    m, s = divmod(seconds, 60)
    return f"{m:02}:{s:02}"

def on_press(key):
    global skip_next
    skip_next = True  

def main():
    global skip_next
    interval = 2 * 20  # 5 seconds
    next_action = 0

    print("\nAuto action started. Perform action every 5 minutes.")  # Changed text
    print("Press any key to skip the next action.")  # Changed text
    print("Press Ctrl+C to stop.\n")

    listener = Listener(on_press=on_press)
    listener.start()

    try:
        while True:
            if next_action <= 0:
                now = datetime.datetime.now().strftime("%H:%M:%S")

                if skip_next:
                    print(f"\n[{now}] {Fore.RED}Action skipped due to key press.{Fore.RESET}\n")  # Changed text
                    skip_next = False
                else:
                    print(f"\n[{now}] Performing action...\n")  # Changed text
                    if bring_roblox_to_front():
                        time.sleep(0.5)
                        perform_action()  # Changed function call
                        print(f"{Fore.GREEN}Action performed.{Fore.RESET}\n")  # Changed text
                    else:
                        print("Roblox not found.\n")

                next_action = interval

            sys.stdout.write(f"\rNext action in: {format_time(next_action)}   ")  # Changed text
            sys.stdout.flush()
            time.sleep(1)
            next_action -= 1

    except KeyboardInterrupt:
        print("\n\nScript stopped by user.\n")
        listener.stop()

if __name__ == "__main__":
    main()