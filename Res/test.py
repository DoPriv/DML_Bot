import time
import win32process

handle = win32process.CreateProcess('C:\\Windows\\notepad.exe', '', None, None, 0, win32process
                                    .CREATE_NO_WINDOW, None, None,
                                    win32process.STARTUPINFO())  # Open Notepad and get its handle
print(handle, handle[0])
win32process.SetProcessWorkingSetSize(handle[0], 1, 1)
time.sleep(2)
#win32process.TerminateProcess(handle[0], 0)

import win32gui

hwnd_title = dict()


def get_all_hwnd(hwnd, _):
    if win32gui.IsWindow(hwnd) and win32gui.IsWindowEnabled(hwnd) and win32gui.IsWindowVisible(hwnd):
        hwnd_title.update({hwnd: win32gui.GetWindowText(hwnd)})


win32gui.EnumWindows(get_all_hwnd, 0)

for h, t in hwnd_title.items():
    if t != "":
        print(h, t)

import win32api
import win32gui
import win32con
import win32process
import time

filename = 'Comparison table of company operations in 2020.xlsx'  # file name


def close_process_by_hwnd(hwnd, _):
    if win32gui.IsWindowVisible(hwnd):
        # Can be judged regularly
        if filename in win32gui.GetWindowText(hwnd):
            # PostMessage will pop up a closing prompt, such as when the file has been modified. Method 1
            win32gui.SetForegroundWindow(hwnd)  # Make the current window at the top
            win32gui.PostMessage(hwnd, win32con.WM_CLOSE, 0, 0)

            # # According to the window handle to obtain the process ID the following method two
            # _id = win32process.GetWindowThreadProcessId(hwnd)

            # # Open process based on ID
            # handle = win32api.OpenProcess(1, False, _id[1])
            # # Close the process according to the process handle
            # win32api.TerminateProcess(handle, -1)


if __name__ == '__main__':
    win32gui.EnumWindows(close_process_by_hwnd, None)
    time.sleep(3)
