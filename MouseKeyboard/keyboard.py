import time

import win32api
import win32con

from MouseKeyboard import VKeytable

keytable = {'backspace': win32con.VK_BACK,
            'tab': win32con.VK_TAB,
            'clear': win32con.VK_CLEAR,
            'enter': win32con.VK_RETURN,
            'shift': win32con.VK_SHIFT,
            'ctrl': win32con.VK_CONTROL,
            'alt': win32con.VK_MENU,
            'pause': win32con.VK_PAUSE,
            'capslock': win32con.VK_CAPITAL,
            'esc': win32con.VK_ESCAPE,
            'space': win32con.VK_SPACE,
            'pageup': win32con.VK_PRIOR,
            'pagedown': win32con.VK_NEXT,
            'end': win32con.VK_END,
            'home': win32con.VK_HOME,
            'left': win32con.VK_LEFT,
            'up': win32con.VK_UP,
            'right': win32con.VK_RIGHT,
            'down': win32con.VK_DOWN,
            'print': win32con.VK_PRINT,
            'insert': win32con.VK_INSERT,
            'delete': win32con.VK_DELETE,
            'help': win32con.VK_HELP,
            '0': VKeytable.VK_0,
            '1': VKeytable.VK_1,
            '2': VKeytable.VK_2,
            '3': VKeytable.VK_3,
            '4': VKeytable.VK_4,
            '5': VKeytable.VK_5,
            '6': VKeytable.VK_6,
            '7': VKeytable.VK_7,
            '8': VKeytable.VK_8,
            '9': VKeytable.VK_9,
            'a': VKeytable.VK_A,
            'b': VKeytable.VK_B,
            'c': VKeytable.VK_C,
            'd': VKeytable.VK_D,
            'e': VKeytable.VK_E,
            'f': VKeytable.VK_F,
            'g': VKeytable.VK_G,
            'h': VKeytable.VK_H,
            'i': VKeytable.VK_I,
            'j': VKeytable.VK_J,
            'k': VKeytable.VK_K,
            'l': VKeytable.VK_L,
            'm': VKeytable.VK_M,
            'n': VKeytable.VK_N,
            'o': VKeytable.VK_O,
            'p': VKeytable.VK_P,
            'q': VKeytable.VK_Q,
            'r': VKeytable.VK_R,
            's': VKeytable.VK_S,
            't': VKeytable.VK_T,
            'u': VKeytable.VK_U,
            'v': VKeytable.VK_V,
            'w': VKeytable.VK_W,
            'x': VKeytable.VK_X,
            'y': VKeytable.VK_Y,
            'z': VKeytable.VK_Z,
            'numpad0': win32con.VK_NUMPAD0,
            'numpad1': win32con.VK_NUMPAD1,
            'numpad2': win32con.VK_NUMPAD2,
            'numpad3': win32con.VK_NUMPAD3,
            'numpad4': win32con.VK_NUMPAD4,
            'numpad5': win32con.VK_NUMPAD5,
            'numpad6': win32con.VK_NUMPAD6,
            'numpad7': win32con.VK_NUMPAD7,
            'numpad8': win32con.VK_NUMPAD8,
            'numpad9': win32con.VK_NUMPAD9,
            'numpad*': win32con.VK_MULTIPLY,
            'numpad+': win32con.VK_ADD,
            'numpad-': win32con.VK_SUBTRACT,
            'numpad.': win32con.VK_DECIMAL,
            'numpad/': win32con.VK_DIVIDE,
            'f1': win32con.VK_F1,
            'f2': win32con.VK_F2,
            'f3': win32con.VK_F3,
            'f4': win32con.VK_F4,
            'f5': win32con.VK_F5,
            'f6': win32con.VK_F6,
            'f7': win32con.VK_F7,
            'f8': win32con.VK_F8,
            'f9': win32con.VK_F9,
            'f10': win32con.VK_F10,
            'f11': win32con.VK_F11,
            'f12': win32con.VK_F12,
            'lshift': win32con.VK_LSHIFT,
            'rshift': win32con.VK_RSHIFT,
            'lctrl': win32con.VK_LCONTROL,
            'rctrl': win32con.VK_RCONTROL,
            'lalt': win32con.VK_LMENU,
            'ralt': win32con.VK_RMENU,
            'lwin': win32con.VK_LWIN,
            'rwin': win32con.VK_RWIN,
            'apps': win32con.VK_APPS,
            'numlock': win32con.VK_NUMLOCK,
            'scrolllock': win32con.VK_SCROLL,
            ';': 186,
            '=': 187,
            ',': 188,
            '-': 189,
            '.': 190,
            '/': 191,
            '`': 192,
            '[': 219,
            '\\': 220,
            ']': 221,
            "'": 222
            }


def keyDown(key):
    if key in keytable:
        win32api.keybd_event(keytable[key], 0, 0, 0)
    else:
        raise ValueError('key is not in keytable')


def keyUp(key):
    if key in keytable:
        win32api.keybd_event(keytable[key], 0, 2, 0)
    else:
        raise ValueError('key is not in keytable')


def click(key, delay=0.05):
    if key in keytable:
        win32api.keybd_event(keytable[key], 0, 0, 0)
        time.sleep(delay)
        win32api.keybd_event(keytable[key], 0, 2, 0)


def inputString(string, delay=0.05):
    for char in string:
        if char == ' ':
            click('space', delay)
        elif char == '\n':
            click('enter', delay)
        elif char == '\t':
            click('tab', delay)
        else:
            click(char, delay)


def isPressed(key):
    if key in keytable:
        return win32api.GetKeyState(keytable[key]) in [-127, -128]
    else:
        raise ValueError('key is not in keytable')


def isReleased(key):
    return not isPressed(key)


def isToggled(key):
    if key in keytable:
        return bool(win32api.GetKeyState(keytable[key]) & 1)
    else:
        raise ValueError('key is not in keytable')


def isLongPressed(key, delay=0.1, need_release=False):
    if key in keytable:
        start = time.time()
        if need_release:
            while isPressed(key):
                time.sleep(0.01)
            if time.time() - start > delay:
                return True
            return False
        else:
            while isPressed(key):
                if time.time() - start > delay:
                    return True
                time.sleep(0.01)
            return False
    else:
        raise ValueError('key is not in keytable')


def keyPressed():
    for key in keytable:
        if isPressed(key):
            return key
    return None
