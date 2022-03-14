import win32gui
import numpy as np

# print(win32gui.GetForegroundWindow())

# win32gui.EnumWindows(callback, None)


def windowEnumerationHandler(hwnd, top_windows):
    if win32gui.IsWindowVisible(hwnd) and win32gui.GetWindowText(hwnd).endswith("| Microsoft Teams") :
         top_windows.append((hwnd, win32gui.GetWindowText(hwnd)))

if __name__ == "__main__":
    top_windows = []
    win32gui.EnumWindows(windowEnumerationHandler, top_windows)
    recent_teams_window = [i for i in  top_windows][-1][0]
    win32gui.ShowWindow(recent_teams_window,5)
    win32gui.SetForegroundWindow(recent_teams_window)