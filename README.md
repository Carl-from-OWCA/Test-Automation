## GUI App to automate testing
#### By: Raghav Varshney

This is a GUI based app to help automate the process of running testcases for executable programs. Instead of having to write a Python script for each project separately, you can just select the folder with the test cases, the folder where you want to print the output, and the executable that is being tested.

The app will work on Windows (WSL only as of now), Linux, and MacOS. I will eventually upload executable versions of this into the repo so that minimal tinkering is required from the user, but I do recommend looking throgh the code to make sure it's not doing anything you don't like. (It's esentially just sending commands to the terminal.) 

Since this program relies heavily on the terminal, it is susceptible to a variety of issues stemming from the user's environment. However, the most common issue is that the executable file may not have the permissions to be run. This can usually be fixed by issuing the following command on UNIX-based systems: `chmod +rwx filename`.

How to use:
* Just run the driver.py file

Requirements:
* Python 3
* WSL (Windows only)
