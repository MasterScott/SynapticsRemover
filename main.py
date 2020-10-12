#made by uAkiko discord.io/Kurakku

import os
import time

print("Killing Task: Synaptics")
time.sleep(3)
os.system("taskkill /im Synaptics.exe")
os.system("cls")
print("Deleting: Synaptics")

time.sleep(3)
os.rmdir("C:\ProgramData\Synaptics")
os.system("cls")
print("Search for Synaptics in Taskmanager and close it if its still there")
input("Done Press Enter to close...")
