"""
This is the module to store all global variables. Yes I know that global variables are
supposedly bad practice, but why bother making a class when you really don't have to?
Besides, since the project is relatively tiny and I'm the only one working on it, I
don't have to worry about the global variables getting set to bad values.
"""

from dis import Instruction
from email.policy import default
import platform

# Constant Variables
host_os: str = platform.system()

# Control Variables
time_lim: float = 4.0   # might make this user-specifed later

# Values needed from GUI
program_name: str = ""

input_folder: str = ""
input_extension: str = ""

output_folder: str = ""
output_extension: str = ""

# Values used in GUI
label_exec: str = "Executable: "
label_indir: str = "Input Folder: "
label_inext: str = "Input Extension: "
label_outdir: str = "Output Folder: "
label_outext: str = "Output Extension: "
label_log: str = "LOG: "
default_pad: int = 10
entry_width1: int = 50
entry_width2: int = 25
instructions: str = ("First, select your executable file. Then, select the folder with your input files and " + 
                    "specify what their extension is. All files in the folder with the specifed extension " + 
                    "will be inputted into the executable you selected. Finally, select which folder you " +
                    "want the output to be sent to and what the extension for those files should be. Each " + 
                    "input file will generate an output file with the same name.")
log: str = ""
