.\pyinstaller --onefile -w 'Csgostatus.py'

For any missing package:
pyinstaller --hidden-import 'package_name' --onefile 'Csgostatus.py'