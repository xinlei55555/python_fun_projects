import os
import time
#because  i am importing another module, I have to specify it in the auto-ex-to-py thingy, under --hidden-imports
#you have to add pywin32 to the --hidden-import
#the name of the api is actually win32api (not pywin32, although try both in case)
import win32gui, win32con
# os.startfile(r"C:\Users\xinle\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Chrome Apps\Outlook -- Xin Lei.lnk")
# os.startfile(r"C:\Users\xinle\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Chrome Apps\Coba.Net.lnk")
# os.startfile(r"C:\Users\xinle\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Microsoft Teams.lnk")

os.startfile(r"C:\Users\xinle\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Chrome Apps\Omnivox - Marianopolis College.lnk")
#Here, I am waiting a second (for the program to open the files and then minimizing the open window)
time.sleep(1)
Minimize = win32gui.GetForegroundWindow()
win32gui.ShowWindow(Minimize, win32con.SW_MINIMIZE)

os.startfile(r"C:\Users\xinle\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Chrome Apps\Gmail -- Xin Lei.lnk")
time.sleep(1)
Minimize = win32gui.GetForegroundWindow()
win32gui.ShowWindow(Minimize, win32con.SW_MINIMIZE)

os.startfile(r"D:\Programs\Todoist\Todoist-1.0.8.exe")

os.startfile(r"C:\Users\xinle\Desktop\Google Calendar -- Xin Lei.lnk")
