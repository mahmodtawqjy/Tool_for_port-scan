import socket
from _pydatetime import datetime

print(
    """ __  __ _____   ____
|  \/  |_   _| |  _ \ _ __ ___   __ _ _ __ __ _ _ __ ___   ___  ___ _ __
| |\/| | | |   | |_) | '__/ _ \ / _` | '__/ _` | '_ ` _ \ / _ \/ _ \ '__|
| |  | | | |   |  __/| | | (_) | (_| | | | (_| | | | | | |  __/  __/ |
|_|  |_| |_|   |_|   |_|  \___/ \__, |_|  \__,_|_| |_| |_|\___|\___|_|
                                |___/"""
)

confirmation = input("Do you want to start the scan? (y/n): ")

if confirmation.lower() == "y":
    target = input("Please Enter the Target IP address: ")

    def port_scan(target):
        try:
            ip = socket.gethostbyname(target)
            print(f"Scanning the Target: {ip}")
            print("Time started: ", datetime.now())
            for port in range(1, 4000):
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(1)
                result = sock.connect_ex((ip, port))
                if result == 0:
                    print("Port {}: Open".format(port))
                sock.close()
        except socket.gaierror:
            print("Hostname could not be resolved")
        except socket.error:
            print("Could not connect to the server")

    port_scan(target)

else:
    print("Error: Invalid input. The scan will not be performed.")
