import time

import MouseKeyboard.keyboard as keyboard
import MouseKeyboard.mouse as mouse


def 登龙(*args):
    time_ms = args[0]
    if time_ms == 0:
        return

    mouse.click('left')
    time.sleep(time_ms / 1000)
    keyboard.keyDown('shift')
    time.sleep(0.02)
    keyboard.keyDown('space')
    time.sleep(0.01)
    keyboard.keyUp('shift')
    keyboard.keyUp('space')
    time.sleep(0.1)
    mouse.click('left')
    time.sleep(0.1)
    mouse.click('left')
    time.sleep(0.1)
    mouse.click('left')


def 重复F(*args):
    keyboard.click('f')
    time.sleep(0.05)


def 胡桃(*args):
    if args[0] == 0:  # 0命
        mouse.click('left', 0.05)  # A
        time.sleep(0.22)
        mouse.click('left', 0.05)  # A
        time.sleep(0.05)
        mouse.click('left', 0.28)  # Z
        time.sleep(0.02)
        keyboard.click('space', 0.02)  # 跳
        time.sleep(0.55)
    else:  # 1命
        mouse.click('left', delay=0.08)  # A
        time.sleep(0.22)
        mouse.click('left', delay=0.05)  # A
        time.sleep(0.05)
        mouse.click('left', delay=0.28)  # Z
        time.sleep(0.02)
        mouse.click('right', delay=0.02)  # 闪避
        keyboard.click('s', delay=0.02)  # S
        time.sleep(0.02)
        keyboard.click('w', delay=0.02)  # W
        time.sleep(0.145)  # 循环间隔


def 那维莱特(*args):
    mouse.mouseMove(500, 0, 0.01)  # 第一个参数越大或第三个参数越小转得越快


def 甘雨(*args):
    mode = args[0]
    if mode == 0:
        mouse.mouseDown('left')
        for i in range(170):
            time.sleep(0.01)
            if mouse.isReleased('x1'):
                mouse.mouseUp('left')
                return
        mouse.mouseUp('left')

        time.sleep(0.05)
        keyboard.click('r')
        time.sleep(0.05)
        keyboard.click('r')
        time.sleep(0.2)
    elif mode == 1:
        mouse.mouseDown('left')
        for i in range(170):
            time.sleep(0.01)
            if mouse.isReleased('x1'):
                mouse.mouseUp('left')
                return
        mouse.mouseUp('left')

        time.sleep(0.05)
        keyboard.click('r')
        time.sleep(0.05)
        keyboard.click('shift')
        time.sleep(0.1)
    elif mode == 2:
        mouse.mouseDown('left')
        for i in range(170):
            time.sleep(0.01)
            if mouse.isReleased('x1'):
                mouse.mouseUp('left')
                return
        mouse.mouseUp('left')

        time.sleep(0.1)
        keyboard.click('r', 0.05)
        time.sleep(0.1)
        mouse.mouseDown('left')
        for i in range(170):
            time.sleep(0.01)
            if mouse.isReleased('x1'):
                mouse.mouseUp('left')
                return
        mouse.mouseUp('left')

        time.sleep(0.01)
        mouse.click('right', 0.02)
        time.sleep(0.2)


def 五郎(*args):
    mouse.click('left', 0.01)
    time.sleep(0.03)
    keyboard.click('r', 0.01)
    time.sleep(0.024)
    keyboard.click('r', 0.01)
    time.sleep(0.01)


def 菲谢尔(*args):
    mouse.click('left', 0.1)
    time.sleep(0.2)
    mouse.click('left', 0.1)
    time.sleep(0.18)
    keyboard.click('r', 0.1)
    time.sleep(0.1)
    keyboard.click('r', 0.05)
    time.sleep(0.05)
