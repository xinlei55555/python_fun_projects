import time
import os
import win32gui, win32con

#opening google chrome, which is an application that ends with .exe
#subprocess.call("C:\Program Files (x86)\Google\Chrome\Application\chrome.exe")
#or directly open the shorcut:
# os.startfile(r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Edge.lnk")

os.startfile(r"D:\Personnel\Other learning\Langues et matières scolaires\English\Words_\English vocabulary.docx")
#minimizing the app
time.sleep(2)
Minimize = win32gui.GetForegroundWindow()
win32gui.ShowWindow(Minimize, win32con.SW_MINIMIZE)

os.startfile(r"C:\Users\xinle\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Chrome Apps\Goodreads.lnk")
time.sleep(1)
Minimize = win32gui.GetForegroundWindow()
win32gui.ShowWindow(Minimize, win32con.SW_MINIMIZE)

#opening a folder
os.startfile(r"D:\Personnel\Other learning\Livres lus_Constituent la connaissance universelle!")
time.sleep(1.5)
Minimize = win32gui.GetForegroundWindow()
win32gui.ShowWindow(Minimize, win32con.SW_MINIMIZE)

os.startfile(r"C:\Users\xinle\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Chrome Apps\Library Genesis.lnk")
time.sleep(1)
Minimize = win32gui.GetForegroundWindow()
win32gui.ShowWindow(Minimize, win32con.SW_MINIMIZE)

#opening an app shortcut, which ends with .lnk -- the r"" tells it that is is a string
os.startfile(r"C:\Users\xinle\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Chrome Apps\Libby.lnk")



#opening a file

##################################################### 
# import webbrowser
# #https://www.pythonforbeginners.com/code-snippets-source-code/python-webbrowser#:~:text=Using%20the%20web%20browser%20in%20Python.%20The%20webbrowser,from%20this%20module%20will%20do%20the%20right%20thing.


# #i am finding the url of a dictionary
# url = "https://workona.com/0/kmbkv7/reading-time-"
# #this opens the link i placed in url using the default browser (so if my default browser is edge, it will open it in edge!)
# webbrowser.open_new(url)
