from time import sleep
from infi.systray import SysTrayIcon
import threading
import os
import requests
import sys
import ctypes

_sys_state = True
_exit_app = False
_ip = "20.80.233.86"

mensagem_popup = 'Você está fora de postura. Fique de postura reta em sua cadeira!'
titulo_popup = "Health Chair 🪑"
distance_person_from_chair = 15 #CM

def turn_on(systray):
    global _sys_state
    _sys_state = True
    print("Ligado!")

def turn_off(systray):
    global _sys_state
    _sys_state = False

    print("Desligado!")

def request_server():
    while True:
        if _exit_app == True:
            break
        sleep(3)
        print(f"sys_state: {_sys_state}")
        if _sys_state:
            try:
                data:float = requests.get(f"http://{_ip}:1026/v2/entities/urn:ngsi-ld:Pstr:001/attrs/distance", headers={
                    "fiware-service": "smart",
                    "fiware-servicepath": "/",
                    "accept": "application/json"
                }).json()["value"]
                print(data)
                if data > distance_person_from_chair:
                    ctypes.windll.user32.MessageBoxW(0, mensagem_popup, titulo_popup, 0)
            except:
                print("Houve um erro na conexão...")

menu_options = (("Ativar Sistema", None, turn_on), ("Desativar Sistema", None, turn_off))

def quit_callback(systray):
    global _exit_app
    _exit_app = True

tray_app = SysTrayIcon("icon.ico", "HealthChair", menu_options, on_quit=quit_callback)

exec_t = threading.Thread(target=request_server, name="t1")
exec_t.start()

tray_app.start()
tray_app.shutdown()