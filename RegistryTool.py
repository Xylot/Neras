import winreg


def connect(computer_name=None, base_key=winreg.HKEY_CURRENT_USER):
    return winreg.ConnectRegistry(computer_name, base_key)


def open_key(registy, key_directory):
    return winreg.OpenKey(registy, key_directory, 0, winreg.KEY_ALL_ACCESS)


def get_value(key, key_index):
    return winreg.EnumValue(key, key_index)


def get_key_values(key, count) -> list:
    return [get_value(key, i) for i in range(count)]


def query_key_info(key):
    return winreg.QueryInfoKey(key)


def get_key_info(key) -> dict:
    key_info = query_key_info(key)
    return {
        'sub_key_count': key_info[0],
        'value_count': key_info[1],
        'last_modified': key_info[2]
    }


def set_key_value(key, value_name, value_type, value):
    winreg.SetValueEx(key, value_name, 0, value_type, value)
