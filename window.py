import win32gui
import win32con

windowHandler = win32gui.dllhandle
windowTitle = ""


class Window:

    def __init__(self, WindowTitle):


        def set_window_pos(targetTitle):
            hWndList = []
            win32gui.EnumWindows((lambda hWnd, param: param.append(hWnd)), hWndList)
            for hwnd in hWndList:
                clsname = win32gui.GetClassName(hwnd)
                title = win32gui.GetWindowText(hwnd)
                if title.find(
                        targetTitle) >= 0:  # Adjust the target window to coordinates (600,300), the size is set to (600,600)
                    win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, 0, 0, 1270, 720,
                                          win32con.SWP_NOSIZE)  # HWND_TOPMOST
                    self.windowHandler = hwnd

    def getWindowHandler(self):
        return self.windowHandler


