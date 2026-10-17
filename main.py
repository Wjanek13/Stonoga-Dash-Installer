import os, shutil
from pathlib import Path
path = os.path.expanduser("~") + "/.local/share/Steam/steamapps/common/Geometry Dash/Resources"
print("1: Install Stonoga Dash")
print("2: Backup Icon")
match input("What would you like to do (enter number):"):
    case "1":
        player_png_name = "player_01-uhd.png"
        shutil.copy2(f"files/icons/{player_png_name}", Path(path) / "icons" / player_png_name)
        for file_path in Path("files/Resources").iterdir():
            if file_path.is_file():
                shutil.copy2(file_path, Path(path) / file_path.name)
                print(f"added: {file_path.name}")
    case "2":
        player_png_name = "player_01-uhd.png"
        shutil.copy2(f"files/backup/{player_png_name}", Path(path) / "icons" / player_png_name)
    case _:
        print("Action not found")
