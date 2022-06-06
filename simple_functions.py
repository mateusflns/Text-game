import ctypes


def maximize():
    kernel32 = ctypes.WinDLL('kernel32')
    user32 = ctypes.WinDLL('user32')

    SW_MAXIMIZE = 3

    hWnd = kernel32.GetConsoleWindow()
    user32.ShowWindow(hWnd, SW_MAXIMIZE)