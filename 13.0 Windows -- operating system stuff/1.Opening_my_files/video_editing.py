import time
import os
import win32gui, win32con
import webbrowser

url = "https://workona.com/0/"
#this opens the link i placed in url using the default browser (so if my default browser is edge, it will open it in edge!)
webbrowser.open_new(url)
time.sleep(1.5)
Minimize = win32gui.GetForegroundWindow()
win32gui.ShowWindow(Minimize, win32con.SW_MINIMIZE)

os.startfile(r"D:\Personnel\Other learning\Personal\Video editing with resolve")
os.startfile(r"C:\Users\xinle\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Blackmagic Design\DaVinci Resolve\DaVinci Resolve.lnk")
