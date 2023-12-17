import os
import threading
import time

import psutil
import pynput.keyboard
import win32api

os.chdir(os.path.dirname(os.path.abspath(__file__)))

import Callback
import EditReg

debug = False
port = 8080
launch_game = True
game_path = 'D:/Games/Genshin Impact/Genshin Impact Game/YuanShen.exe'

pynput.keyboard.Listener(on_press=Callback.on_press, daemon=True).start()
threading.Thread(target=Callback.x1_thread, daemon=True).start()
threading.Thread(target=Callback.x2_thread, daemon=True).start()

if debug:
    threading.Thread(target=Callback.tcp_thread, daemon=True, args=(port,)).start()

print('ready')


def getpid(name) -> int:
    for proc in psutil.process_iter():
        if proc.name() == name:
            return proc.pid
    return 0


lanuch_path = os.path.abspath(os.path.dirname(game_path) + '/../launcher.exe')
EditReg.create_runasinvoker(lanuch_path)
EditReg.create_runasinvoker(game_path)

pid = getpid('YuanShen.exe')
if pid == 0:
    if launch_game:
        win32api.ShellExecute(0, 'open', game_path, '', '', 1)
        time.sleep(2)
        pid = getpid('YuanShen.exe')
        print(pid)
    else:
        while pid == 0:
            pid = getpid('YuanShen.exe')
            time.sleep(0.5)
        print('game start')

while True:
    if not psutil.pid_exists(pid):
        print('game end')
        break
    time.sleep(2)
