import os
import socket
import time

import pygetwindow as gw

import Character
import Macro
from MouseKeyboard import mouse, keyboard

_x1_pressed = False
_x2_pressed = False
Character = Character.Character()


def tcp_server(port=8080):
    def cut(s):
        num = ''
        string = ''
        for i in s:
            if '0' <= i <= '9':
                num += i
            else:
                string += i
        if num:
            return int(num), string
        return 999, string

    ip = [a for a in os.popen('route print').readlines() if ' 0.0.0.0 ' in a][0].split()[-2]
    server = socket.socket()
    server.bind((ip, port))
    server.listen(5)
    print('{}:{} tcp ready'.format(ip, port))
    while True:
        try:
            client, addr = server.accept()
            print('connected')
            while True:
                data = client.recv(1024)
                if not data:
                    break
                delay_time, is_save = cut(data.decode('utf-8'))
                if is_save in ['s', 'save']:
                    if Character.bianshen['flag']:
                        Character.config['special'][Character.current_character]['delay'] = delay_time
                    else:
                        Character.config['common'][Character.current_character] = delay_time

                    Character.save_config()
                    print('save {} delay: {}'.format(Character.current_character, delay_time))

        except Exception:
            server.close()
            break
        time.sleep(0)
    server.close()


def on_press(key):
    global _mode, _last_index
    try:
        title = gw.getActiveWindow().title
    except AttributeError:
        return
    if title == Character.title:

        key = str(key)
        if len(key) == 3:
            key = key[1]

        if '1' <= key <= '4':
            if mouse.isPressed('x2'):
                Character.mode = ['single', 'double', 'three', 'four'][int(key) - 1]
                print('模式: {}'.format(Character.mode))
            else:
                if Character.mode == 'single':
                    Character.index = int(key)
                    Character.get_current_character()
                    _last_index = key
                elif Character.mode == 'double':
                    if key in '12':
                        Character.index = int(key)
                        Character.get_current_character()
                        _last_index = key
                else:
                    if key == '1':
                        Character.index = 1
                        Character.get_current_character()
                if Character.current_character not in Character.all_characters:
                    time.sleep(0.1)
                    Character.get_current_character()
                if Character.current_character != Character.bianshen['character']:
                    Character.bianshen = {'character': '',
                                          'flag': False,
                                          'duration': 0,
                                          'start': 0.0}
                print(Character.current_character)

        if key == 'q':
            if Character.current_character in Character.special_characters:
                if Character.is_burst() and not Character.bianshen['flag']:
                    Character.bianshen = {
                        'character': Character.current_character,
                        'flag': True,
                        'duration': Character.config['special'][Character.current_character]['duration'],
                        'start': time.time()
                    }


def do_while_pressed(device, key, func, delay=0, *args):
    if type(func) is str:
        func = getattr(Macro, func)
    if device == 'mouse':
        while mouse.isPressed(key):
            func(*args)
            time.sleep(delay)
        return
    elif device == 'keyboard':
        while keyboard.isPressed(key):
            func(*args)
            time.sleep(delay)
        return
    else:
        raise ValueError('device must be mouse or keyboard')


def x1_callback():
    if Character.current_character not in Character.all_characters:
        Character.get_current_character()
    # print(Character.current_character)
    if Character.current_character not in Character.all_characters:
        return

    if Character.current_character in Character.special_mode.keys():
        do_while_pressed('mouse', 'x1', Character.current_character, 0,
                         Character.special_mode[
                             Character.current_character])
        print(Character.current_character)

    else:
        if mouse.isLongPressed('x1', 0.2, True):
            return
        if Character.bianshen['flag'] and time.time() - Character.bianshen['start'] > Character.bianshen['duration']:
            Character.bianshen = {'character': '',
                                  'flag': False,
                                  'duration': 0,
                                  'start': 0.0}
        Character.update_config()
        if Character.bianshen['flag']:
            Macro.登龙(Character.config['special'][Character.current_character]['delay'])
            print('{}  {}'.format(Character.current_character,
                                  Character.config['special'][Character.current_character]['delay']))
        else:
            Macro.登龙(Character.config['common'][Character.current_character])
            print('{}  {}'.format(Character.current_character,
                                  Character.config['common'][Character.current_character]))


def x2_callback():
    if Character.current_character == '甘雨' and not mouse.isLongPressed('x2', 0.2):
        Character.special_mode['甘雨'] += 1
        Character.special_mode['甘雨'] %= 3
        print('甘雨模式: {}'.format(Character.special_mode['甘雨']))
        return

    if Character.current_character == '胡桃' and not mouse.isLongPressed('x2', 0.2):
        Character.special_mode['胡桃'] += 1
        Character.special_mode['胡桃'] %= 2
        print('胡桃模式: {}'.format(Character.special_mode['胡桃']))
        return

    do_while_pressed('mouse', 'x2', Macro.重复F)


def x1_thread():
    global _x1_pressed
    while True:
        try:
            if gw.getActiveWindow().title == Character.title:
                do_while_pressed('mouse', 'x1', x1_callback)
        except AttributeError:
            pass
            time.sleep(0)


def x2_thread():
    global _x2_pressed
    while True:
        try:
            if gw.getActiveWindow().title == Character.title:
                do_while_pressed('mouse', 'x2', x2_callback)
        except AttributeError:
            pass
            time.sleep(0)


def tcp_thread(port=8080):
    tcp_server(port)
