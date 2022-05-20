import os
from pathlib import Path
import subprocess
import config

def runTests() -> None:

    if config.host_os == "Linux" or config.host_os == "Darwin":             # for some reason MacOS is Darwin
        os.chdir(Path.home())                                               # move up to make accessing files & folders easier
        for file in os.listdir(config.input_folder):
            filename = os.fsdecode(file)
            if filename.endswith(config.input_extension):
                try:
                    result = subprocess.run([config.program_name + " < " + os.path.join(config.input_folder, filename) 
                                            + " > " + os.path.join(config.output_folder, 
                                            filename.replace(config.input_extension, config.output_extension))], 
                                            shell=True,                     # indicates we're running a shell command
                                            capture_output=True,            # helps with sending err message to GUI
                                            check=True,                     # make sure command didn't cause error
                                            timeout=config.time_lim)        # kill any test cases taking too long
                except subprocess.CalledProcessError:
                    print("test case " + filename + " could not be run.")
                except subprocess.TimeoutExpired:
                    print("Test case " + filename + " took too long and was halted.")
                else:
                    print("Test case " + filename + " ran successfully.")

    elif config.host_os == "Windows":                                      
        os.chdir(Path.home())                                               # move up to make accessing files & folders easier
        for file in os.listdir(config.input_folder):
            filename = os.fsdecode(file)
            if filename.endswith(config.input_extension):
                try:
                    result = subprocess.run(["wsl", dosToUNIX(config.program_name), "<", os.path.join(config.input_folder, filename), 
                                            ">", os.path.join(config.output_folder, 
                                            filename.replace(config.input_extension, config.output_extension))], 
                                            shell=True,                     # indicates we're running a shell command
                                            capture_output=True,            # helps with sending err message to GUI
                                            check=True,                     # make sure command didn't cause error
                                            timeout=config.time_lim)        # kill any test cases taking too long
                except subprocess.CalledProcessError:
                    print("test case " + filename + " could not be run.")
                except subprocess.TimeoutExpired:
                    print("Test case " + filename + " took too long and was halted.")
                else:
                    print("Test case " + filename + " ran successfully.")

    else:
        print("Unsupported OS")

    return                                                                  # Useless, but I like knowing the end of a function


def dosToUNIX(filepath: str) -> str:
    """
    Takes a filpath in DOS format as a string and returns the equivalent filepath
    in UNIX formatting. Pretty crappy implementation as of now.
    """
    filepath = filepath.replace("\\", "/")
    filepath = filepath.replace("C:", "/mnt/c", 1)
    return filepath


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