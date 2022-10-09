"""from cx_Freeze import setup, Executable
import sys

base = None

if sys.platform == "win32":
    base = "Win32GUI"

bdist_msi_options = {
    "upgrade_code": "{48B079F4-B598-438D-A62A-8A233A3F8901}",
    "add_to_path": False,
    "initial_target_dir": r"[ProgramFilesFolder]\%s\%s" % ("DiscordScraping - Shytix", "DiscordScraping")
}

executables = [Executable("main_GUI.py",
                          base=base,
                          target_name="DiscordScraping",
                          )]

packages = ["tkinter", "discum.gateway.session", "discord", "discord.ext.commands"]

options = {
    "build_exe": {
        "packages": packages,
        "include_files": ["dm.py", "users.txt", "main.py"],
        "include_msvcr": True,
    }}"""
"""
setup(
    name="DiscordScraping",
    # options=options,
    version="1.0",
    description="Discord Scraping by Shytix",
    author="Shytix",
    executables=executables,
)
"""
import sys
from cx_Freeze import setup, Executable

base = None
"""if sys.platform == "win32":
    base = "Win32GUI"""

packages = ["tkinter", "discum.gateway.session", "discord", "discord.ext.commands", "discum.start.superproperties", "ua_parser"]

setup(
	name="DiscordScrap",
	version="0.1",
	description="Discord Scraping",
	options={"build_exe": {"include_files": ["dm.py", "users.txt", "main.py"], "include_msvcr": True}},
	executables=[Executable("discord_scrap.py", base=base)]
)
