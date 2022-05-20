"""
This is the module to store all global variables. Yes I know that global variables are
supposedly bad practice, but why bother making a class when you really don't have to?
Besides, since the project is relatively tiny and I'm the only one working on it, I
don't have to worry about the global variables getting set to bad values.
"""

from email.policy import default
import platform

# Constant Variables
host_os: str = platform.system()

# Control Variables
time_lim: float = 4.0

# Values needed from GUI
program_name: str = "/mnt/c/Users/ragha/Documents/Code/Personal_Projects/TestAutomation/Inputs/simple"

input_folder: str = "C:\\Users\\ragha\\Documents\\Code\\Personal_Projects\\TestAutomation\\Inputs"
input_extension: str = ".in"

output_folder: str = "C:\\Users\\ragha\\Documents\\Code\\Personal_Projects\\TestAutomation\\Outputs"
output_extension: str = ".out"

# Values used in GUI
label_exec: str = "Executable: "
label_indir: str = "Input Folder: "
label_inext: str = "Input Extension: "
label_outdir: str = "Output Folder: "
label_outext: str = "Output Extension: "
default_pad: int = 10
entry_width: int = 100
