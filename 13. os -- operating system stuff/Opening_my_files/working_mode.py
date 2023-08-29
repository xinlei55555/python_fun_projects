import os
import time
import win32gui, win32con
os.startfile(r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\NoteBook FanControl\NoteBook FanControl.lnk")
time.sleep(1)
Minimize = win32gui.GetForegroundWindow()
win32gui.ShowWindow(Minimize, win32con.SW_MINIMIZE)

os.startfile(r"C:\Users\xinle\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\f.lux.lnk")
time.sleep(2)
Minimize = win32gui.GetForegroundWindow()
win32gui.ShowWindow(Minimize, win32con.SW_MINIMIZE)

os.startfile(r"C:\Users\xinle\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\OneDrive.lnk")
time.sleep(2)
Minimize = win32gui.GetForegroundWindow()
win32gui.ShowWindow(Minimize, win32con.SW_MINIMIZE)



os.startfile(r"C:\Users\xinle\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Chrome Apps\Pomodoro timer.lnk")
os.startfile(r"C:\Users\xinle\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Spotify.lnk")
# os.startfile(r"C:\Users\xinle\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\OneDrive.lnk")


# import webbrowser
# url = "https://workona.com/0/"
# #this opens the link i placed in url using the default browser (so if my default browser is edge, it will open it in edge!)
# webbrowser.open_new(url)disc

