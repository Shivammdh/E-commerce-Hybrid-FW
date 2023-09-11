import os
import subprocess
import time
import keyboard


def start_grid():
    hpath = os.getcwd()
    print("Current Directory:", hpath)

    # Add try-except block to capture and print exceptions
    try:
        hub_process = subprocess.Popen(['java', '-jar', 'selenium-server-4.12.0.jar', 'hub'],
                                       stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        time.sleep(2)

        npath = os.getcwd()
        print("New Directory:", npath)
        os.chdir(os.getcwd())

        node_process = subprocess.Popen(['java', '-jar', 'selenium-server-4.8.0.jar', 'node'],
                                        stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        return hub_process, node_process
    except Exception as e:
        print("Error:", str(e))
        return None


if __name__ == "__main__":
    processes = start_grid()
    if processes:
        print("Selenium Grid Hub and Node started successfully.")
    else:
        print("Failed to start Selenium Grid Hub and Node.")
