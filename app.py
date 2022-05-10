from fileinput import filename
import platform
import os
from pathlib import Path
import subprocess

# Constant Variables
host_os: str = platform.system()

# Control Variables
prepped: bool = False
time_lim: float = 4.0

# Values needed from GUI
program_name: str = "/mnt/c/Users/ragha/Documents/Code/Personal_Projects/TestAutomation/Inputs/simple"
# For UNIX: "/mnt/c/Users/ragha/Documents/Code/Personal_Projects/TestAutomation/Inputs/simple"
# For windows: "C:\\Users\\ragha\\Documents\\Code\\Personal_Projects\\TestAutomation\\Inputs\\simple"

input_folder: str = "C:\\Users\\ragha\\Documents\\Code\\Personal_Projects\\TestAutomation\\Inputs"
# For UNIX: "/mnt/c/Users/ragha/Documents/Code/Personal_Projects/TestAutomation/Inputs"
# For windows: "C:\\Users\\ragha\\Documents\\Code\\Personal_Projects\\TestAutomation\\Inputs"

input_extension: str = ".in"

output_folder: str = "C:\\Users\\ragha\\Documents\\Code\\Personal_Projects\\TestAutomation\\Outputs"
# For UNIX: "/mnt/c/Users/ragha/Documents/Code/Personal_Projects/TestAutomation/Outputs"
# For windows: "C:\\Users\\ragha\\Documents\\Code\\Personal_Projects\\TestAutomation\\Outputs"

output_extension: str = ".out"

# while prepped:

if host_os == "Linux" or host_os == "Darwin":                   # for some reason MacOS is Darwin
    os.chdir(Path.home())                                       # move up to make accessing files & folders easier
    for file in os.listdir(input_folder):
        filename = os.fsdecode(file)
        if filename.endswith(input_extension):
            try:
                result = subprocess.run([program_name + " < " + os.path.join(input_folder, filename) + " > " 
                                        + os.path.join(output_folder, filename.replace(input_extension, output_extension))], 
                                        shell=True,             # indicates we're running a shell command
                                        capture_output=True,    # helps with sending err message to GUI
                                        check=True,             # make sure command didn't cause error
                                        timeout=time_lim)       # kill any test cases taking too long
            except subprocess.CalledProcessError:
                print("test case " + filename + " could not be run.")
            except subprocess.TimeoutExpired:
                print("Test case " + filename + " took too long and was halted.")
            else:
                print("Test case " + filename + " ran successfully.")

elif host_os == "Windows":                                      
    os.chdir(Path.home())                                       # move up to make accessing files & folders easier
    for file in os.listdir(input_folder):
        filename = os.fsdecode(file)
        if filename.endswith(input_extension):
            try:
                result = subprocess.run(["wsl", program_name, "<", os.path.join(input_folder, filename), ">",
                                        os.path.join(output_folder, filename.replace(input_extension, output_extension))], 
                                        shell=True,             # indicates we're running a shell command
                                        capture_output=True,    # helps with sending err message to GUI
                                        check=True,             # make sure command didn't cause error
                                        timeout=time_lim)       # kill any test cases taking too long
            except subprocess.CalledProcessError:
                print("test case " + filename + " could not be run.")
            except subprocess.TimeoutExpired:
                print("Test case " + filename + " took too long and was halted.")
            else:
                print("Test case " + filename + " ran successfully.")

else:
    print("Unsupported OS")

prepped = False


"""
I'm invoking WSL on Windows since most projects tend to be done on Linux and Windows would not be able
to run the executable. Windows's default shell is CMD which can be used to call WSL. In the future I 
might add functioality where you can pick if the executable is for WSL or native Windows if your OS
is detected to be Windows.

The following is some weird behavior that I noticed that I think could be useful for others. When calling 
subprocess.run() on Linux, the entire command needs to be passed as one string. Otherwise subprocess.run()
never returns and times out. On Windows when accessing WSL, the different parts of the argument need to be
passed as separate elements in the arguments array. Otherwise it will not be able to run the executable
for some reason. 

Another explanation for the difference in the Windows code: the executable path is specified in WSL format
since it is being passed as an argument to the wsl command. The redirection is happening in Windows, not
WSL, so the paths for the input and output folders need to be in Windows formatting.
"""