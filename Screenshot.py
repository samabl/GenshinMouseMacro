import winreg

import pyautogui


class Screenshot:
    @staticmethod
    def is_application_fullscreen(window):
        screen_width, screen_height = pyautogui.size()
        return (window.width, window.height) == (screen_width, screen_height)

    @staticmethod
    def get_window_region(window, title='原神'):
        # 去除边框
        if title in ['原神', 'Genshin Impact']:
            key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Software\\miHoYo\\{}".format(title))
        else:
            raise Exception('不支持的游戏')
        width, _ = winreg.QueryValueEx(key, "Screenmanager Resolution Width_h182942802")
        height, _ = winreg.QueryValueEx(key, "Screenmanager Resolution Height_h2627697771")
        other_border = (window.width - width) // 2
        up_border = window.height - height - other_border

        if Screenshot.is_application_fullscreen(window):
            return (window.left, window.top, window.width, window.height)
        else:
            return (window.left + other_border, window.top + up_border, window.width -
                    other_border - other_border, window.height - up_border - other_border)

    @staticmethod
    def get_window(title):
        windows = pyautogui.getWindowsWithTitle(title)
        if windows:
            window = windows[0]
            return window
        return False

    @staticmethod
    def take_screenshot(title, crop=(0, 0, 0, 0)):
        window = Screenshot.get_window(title)
        if window:
            if crop == (0, 0, 0, 0):
                screenshot_pos = Screenshot.get_window_region(window, title)
            else:
                left, top, width, height = Screenshot.get_window_region(window, title)
                screenshot_pos = int(left + width * crop[0]), int(top + height * crop[1]), int(width * crop[2]), int(
                    height * crop[3])
            screenshot = pyautogui.screenshot(region=screenshot_pos)
            return screenshot, screenshot_pos

        return False

    @staticmethod
    def get_aspect_ratio(title='原神'):
        if title in ['原神', 'Genshin Impact']:
            key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Software\\miHoYo\\{}".format(title))
        else:
            raise Exception('不支持的游戏')
        height, _ = winreg.QueryValueEx(key, "Screenmanager Resolution Height_h2627697771")
        width, _ = winreg.QueryValueEx(key, "Screenmanager Resolution Width_h182942802")
        if width / height == 16 / 10:
            return '16:10'
        elif width / height == 16 / 9:
            return '16:9'
        else:
            return 'other'

    @staticmethod
    def screenshot(crop, title='原神'):
        img, _ = Screenshot.take_screenshot(title)
        width, height = img.size
        aspect_ratio = Screenshot.get_aspect_ratio(title)
        if aspect_ratio == '16:10':
            img = img.crop((width * crop[0] / 2560, height * crop[1] / 1600, width * crop[2] / 2560,
                            height * crop[3] / 1600))
        elif aspect_ratio == '16:9':
            img = img.crop((width * crop[0] / 2560, height * crop[1] / 1440, width * crop[2] / 2560,
                            height * crop[3] / 1440))
        else:
            raise Exception('不支持的长宽比，请设置为16:10或16:9')

        return img
