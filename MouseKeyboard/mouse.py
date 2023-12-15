import time

import win32api
import win32con

from MouseKeyboard import VKeytable


def mouseDown(button):
    if button == 'left':
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    elif button == 'right':
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, 0, 0, 0, 0)
    elif button == 'middle':
        win32api.mouse_event(win32con.MOUSEEVENTF_MIDDLEDOWN, 0, 0, 0, 0)
    elif button == 'x1':
        win32api.mouse_event(win32con.MOUSEEVENTF_XDOWN, 0, 0, VKeytable.VK_XBUTTON1, 0)
    elif button == 'x2':
        win32api.mouse_event(win32con.MOUSEEVENTF_XDOWN, 0, 0, VKeytable.VK_XBUTTON2, 0)
    else:
        raise ValueError('button must be left, right, middle, x1 or x2')


def mouseUp(button):
    if button == 'left':
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
    elif button == 'right':
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, 0, 0, 0, 0)
    elif button == 'middle':
        win32api.mouse_event(win32con.MOUSEEVENTF_MIDDLEUP, 0, 0, 0, 0)
    elif button == 'x1':
        win32api.mouse_event(win32con.MOUSEEVENTF_XUP, 0, 0, VKeytable.VK_XBUTTON1, 0)
    elif button == 'x2':
        win32api.mouse_event(win32con.MOUSEEVENTF_XUP, 0, 0, VKeytable.VK_XBUTTON2, 0)
    else:
        raise ValueError('button must be left, right, middle, x1 or x2')


def click(button, delay=0.05):
    mouseDown(button)
    time.sleep(delay)
    mouseUp(button)


def mouseMove(dx, dy, duration=0.01):
    if duration == 0:
        win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, dx, dy, 0, 0)
    else:
        if duration < 0.01:
            duration = 0.01
        start = time.time()
        ddx = dx * (0.01 / duration)
        ddy = dy * (0.01 / duration)
        while time.time() - start < duration:
            win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, int(ddx), int(ddy), 0, 0)
            time.sleep(0.01)


def mouseMoveTo(x, y, duration=0.01):
    if duration == 0:
        win32api.SetCursorPos((x, y))
    else:
        if duration < 0.01:
            duration = 0.01
        start = time.time()
        x_c, y_c = win32api.GetCursorPos()
        dx = x - x_c
        dy = y - y_c
        ddx = dx * (0.01 / duration)
        ddy = dy * (0.01 / duration)
        while time.time() - start < duration:
            win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, int(ddx), int(ddy), 0, 0)
            time.sleep(0.01)


def mouseDrag(dx, dy, button='left', duration=0.01):
    mouseDown(button)
    mouseMove(dx, dy, duration)
    mouseUp(button)


def mouseDragTo(x, y, button='left', duration=0.01):
    mouseDown(button)
    mouseMoveTo(x, y, duration)
    mouseUp(button)


def isPressed(button):
    if button == 'left':
        return bool(win32api.GetKeyState(VKeytable.VK_LBUTTON) & ~3)
    elif button == 'right':
        return bool(win32api.GetKeyState(VKeytable.VK_RBUTTON) & ~3)
    elif button == 'middle':
        return bool(win32api.GetKeyState(VKeytable.VK_MBUTTON) & ~3)
    elif button == 'x1':
        return bool(win32api.GetKeyState(VKeytable.VK_XBUTTON1) & ~3)
    elif button == 'x2':
        return bool(win32api.GetKeyState(VKeytable.VK_XBUTTON2) & ~3)
    else:
        raise ValueError('button must be left, right, middle, x1 or x2')


def isReleased(button):
    return not isPressed(button)


def isToggled(button):
    if button == 'left':
        return bool(win32api.GetKeyState(VKeytable.VK_LBUTTON))
    elif button == 'right':
        return bool(win32api.GetKeyState(VKeytable.VK_RBUTTON))
    elif button == 'middle':
        return bool(win32api.GetKeyState(VKeytable.VK_MBUTTON))
    elif button == 'x1':
        return bool(win32api.GetKeyState(VKeytable.VK_XBUTTON1))
    elif button == 'x2':
        return bool(win32api.GetKeyState(VKeytable.VK_XBUTTON2))
    else:
        raise ValueError('button must be left, right, middle, x1 or x2')


def isLongPressed(button, delay=0.1, need_release=False):
    if button in ['left', 'right', 'middle', 'x1', 'x2']:
        start = time.time()
        if need_release:
            while isPressed(button):
                time.sleep(0.01)
            if time.time() - start > delay:
                return True
            return False
        else:
            while isPressed(button):
                if time.time() - start > delay:
                    return True
                time.sleep(0.01)
            return False
    else:
        raise ValueError('button must be left, right, middle, x1 or x2')


def buttonPressed():
    for button in ['left', 'right', 'middle', 'x1', 'x2']:
        if isPressed(button):
            return button
    return None
