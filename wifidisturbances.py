import pywifi
import time
import keyboard
import os
import subprocess

def get_wifi_signal_info():
    wifi = pywifi.PyWiFi()
    iface = wifi.interfaces()[0]

    iface.scan()
    time.sleep(0.3)  # Reduce the delay to 0.3 seconds

    results = iface.scan_results()
    if results:
        ssid = results[0].ssid
        signal_strength = results[0].signal
        return f"Wi-Fi Signal Information:\nSSID: {ssid}\nSignal Strength: {signal_strength} dBm"
    else:
        return "No available networks found."

def print_banner():
    print('''
@@@@@@@    @@@@@@   @@@   @@@@@@    @@@@@@   @@@  @@@      @@@@@@@   @@@@@@   @@@@@@@   @@@@@@@
@@@@@@@@  @@@@@@@@  @@@  @@@@@@@   @@@@@@@@  @@@@ @@@     @@@@@@@@  @@@@@@@@  @@@@@@@@  @@@@@@@@
@@!  @@@  @@!  @@@  @@!  !@@       @@!  @@@  @@!@!@@@     !@@       @@!  @@@  @@!  @@@  @@!  @@@
!@!  @!@  !@!  @!@  !@!  !@!       !@!  @!@  !@!!@!@!     !@!       !@!  @!@  !@!  @!@  !@!  @!@
@!@@!@!   @!@  !@!  !!@  !!@@!!    @!@  !@!  @!@ !!@!     !@!       @!@  !@!  @!@!!@!   @!@@!@!
!!@!!!    !@!  !!!  !!!   !!@!!!   !@!  !!!  !@!  !!!     !!!       !@!  !!!  !!@!@!    !!@!!!
!!:       !!:  !!!  !!:       !:!  !!:  !!!  !!:  !!!     :!!       !!:  !!!  !!: :!!   !!:
:!:       :!:  !:!  :!:      !:!   :!:  !:!  :!:  !:!     :!:       :!:  !:!  :!:  !:!  :!:
::       ::::: ::   ::  :::: ::   ::::: ::   ::   ::      ::: :::  ::::: ::  ::   :::   ::
 :         : :  :   :    :: : :     : :  :   ::    :       :: :: :   : :  :    :   : :   :

''')
    print('''
   _____                               ______            __    
  / ___/___  ____  _________  _____   /_  __/___  ____  / /____
  \__ \/ _ \/ __ \/ ___/ __ \/ ___/    / / / __ \/ __ \/ / ___/
 ___/ /  __/ / / (__  ) /_/ / /       / / / /_/ / /_/ / (__  ) 
/____/\___/_/ /_/____/\____/_/       /_/  \____/\____/_/____/  
                                                               
''')

def run_python_script(script):
    process = subprocess.Popen(['python', script], stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output, error = process.communicate()
    return output.decode('utf-8'), error.decode('utf-8')

# Set the variable to stop the process with the "Escape" key
stop_process = False

# Get and display the Wi-Fi signal strength
while not stop_process:
    # Clear console screen
    os.system('cls' if os.name == 'nt' else 'clear')

    # Print banner and instructions
    print_banner()
    print("Stop the process by pressing the 'ESC' key on the keyboard REPEATEDLY\n")

    # Get and print the Wi-Fi signal information
    wifi_info = get_wifi_signal_info()
    print(wifi_info)

    # Check if the "Escape" key has been pressed to stop the process
    if keyboard.is_pressed('esc'):
        stop_process = True
        print("\nProcess stopped by the user.")

    # Wait for 0.3 seconds before the next update
    time.sleep(0.3)
