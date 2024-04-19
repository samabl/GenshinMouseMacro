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
launch_game = 1
launch_korepi = 0
korepi_version = 'v'  # v or f
OS = 0
game_path = 'D:/Games/Genshin Impact/Genshin Impact Game/YuanShen.exe' if not OS else 'D:/Games/Genshin Impact OS/Genshin Impact/Genshin Impact Game/GenshinImpact.exe'
korepi_path = 'D:/Applications/tool/colorpicker_' + korepi_version + '.exe'
if OS:
    Callback.Character.title = 'Genshin Impact'
pynput.keyboard.Listener(on_press=Callback.on_press, daemon=True).start()
threading.Thread(target=Callback.x1_thread, daemon=True).start()
threading.Thread(target=Callback.x2_thread, daemon=True).start()

if debug:
    threading.Thread(target=Callback.tcp_thread, daemon=True, args=(port,)).start()
    ip = [a for a in os.popen('route print').readlines() if ' 0.0.0.0 ' in a][0].split()[-2]
    print('请使用调试工具连接到{}:{}'.format(ip, port))

print('ready')


def getpid(name) -> int:
    for proc in psutil.process_iter():
        if proc.name() == name:
            return proc.pid
    return 0


lanuch_path = os.path.abspath(os.path.dirname(game_path) + '/../launcher.exe')
EditReg.create_runasinvoker(lanuch_path)
EditReg.create_runasinvoker(game_path)
exec_name = os.path.basename(game_path)
pid = getpid(exec_name)
if pid == 0:
    if launch_game:
        if launch_korepi:
            win32api.ShellExecute(0, 'runas', korepi_path, '', '', 1)
        else:
            win32api.ShellExecute(0, 'open', game_path, '', '', 1)
    while pid == 0:
        pid = getpid(exec_name)
        time.sleep(0.5)
    print(pid)
    # print('game start')


while True:
    if not psutil.pid_exists(pid):
        print('game end')
        break
    time.sleep(1)
