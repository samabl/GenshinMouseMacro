import winreg


def value_exist(key, value):
    try:
        winreg.QueryValueEx(key, value)
        return True
    except FileNotFoundError:
        return False


def create_value(key, value, type, data):
    try:
        winreg.SetValueEx(key, value, 0, type, data)
        return True
    except PermissionError:
        return False


def get_value(key, value):
    try:
        return winreg.QueryValueEx(key, value)
    except FileNotFoundError:
        return False


def create_runasinvoker(path):
    if '/' in path:
        path = path.replace('/', '\\')
    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,
                         'Software\\Microsoft\\Windows NT\\CurrentVersion\\AppCompatFlags\\Layers', 0,
                         winreg.KEY_ALL_ACCESS)

    if value_exist(key, path):
        if get_value(key, path)[0] != 'RUNASINVOKER':
            create_value(key, path, winreg.REG_SZ, 'RUNASINVOKER')
    else:
        create_value(key, path, winreg.REG_SZ, 'RUNASINVOKER')


