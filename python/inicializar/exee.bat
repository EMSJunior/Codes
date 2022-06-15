import os
import ctypes
ctypes.windll.kernel32.FreeConsole()

info=os.STARTUPINFO()

os.popen("C:\\Program Files (x86)\\VB\\Voicemeeter\\voicemeeterpro.exe",startupinfo=info)
os.popen("C:\\Program Files (x86)\\Steam\\steam.exe",startupinfo=info)
os.popen("C:\\Users\\jumen\\AppData\\Local\\Discord\\Update.exe --processStart Discord.exe",m)
os.popen("C:\\Program Files\\BakkesMod\\BakkesMod.exe",m)