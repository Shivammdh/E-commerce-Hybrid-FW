import os
import subprocess
import time
import keyboard
def start_grid():
    os.chdir("D:\Selenium")
    hub_process = subprocess.Popen(['java', '-jar', 'selenium-server-4.12.0.jar','hub'],
                                   stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    os.chdir("D:\Selenium")
    node_process = subprocess.Popen(['java', '-jar', 'selenium-server-4.12.0.jar','node','--selenium-manager','true'],
                                    stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    #java -jar selenium-server-4.12.0.jar node --selenium-manager true

    return hub_process, node_process

def close_grid(hub_process,node_process):
# if __name__ == '__main__':
#     hub_process, node_process=start_grid()
    try:
        # Your code that interacts with Selenium Grid here
        time.sleep(5)  # Simulate some interaction
        keyboard.press_and_release('ctrl+c')
        keyboard.press_and_release('ctrl+c')

    except KeyboardInterrupt:
        # Terminate the processes when Ctrl+C is pressed
        print("Terminating processes...")

    finally:
        try:
            keyboard.press_and_release('ctrl+c')
            hub_process.wait()
            node_process.wait()
        except KeyboardInterrupt:
            print('Hub And Node Terminated successfully...')

