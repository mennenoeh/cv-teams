import win32gui
import numpy as np

# print(win32gui.GetForegroundWindow())
# win32gui.EnumWindows(callback, None)



def teamsWindowEnumerationHandler(hwnd, teams_windows):
    if win32gui.IsWindowVisible(hwnd) and win32gui.GetWindowText(hwnd).endswith("| Microsoft Teams") :
         teams_windows.append((hwnd, win32gui.GetWindowText(hwnd)))

def windowEnumerationHandler(hwnd, windows):
    if win32gui.IsWindowVisible(hwnd) and (win32gui.GetWindowText(hwnd).endswith("Visual Studio Code") or win32gui.GetWindowText(hwnd).endswith("Gesture Control")):
         windows.append((hwnd, win32gui.GetWindowText(hwnd)))

def set_recent_teams_window_active():
    teams_windows = []
    win32gui.EnumWindows(teamsWindowEnumerationHandler, teams_windows)
    # print(teams_windows)
    recent_teams_window = max([i[0] for i in  teams_windows])
    win32gui.ShowWindow(recent_teams_window,5)
    win32gui.SetForegroundWindow(recent_teams_window)
    # print(recent_teams_window)

def set_code_and_monitor_active():
    windows = []
    win32gui.EnumWindows(windowEnumerationHandler, windows)
    # print(windows)
    for window in windows:
        print(window)
        win32gui.ShowWindow(window[0],5)
        win32gui.SetForegroundWindow(window[0])


if __name__ == "__main__":
    set_code_and_monitor_active()