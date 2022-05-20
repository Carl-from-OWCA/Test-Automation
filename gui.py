from concurrent.futures import process
from ctypes import alignment
from mimetypes import common_types
import config
from app import runTests
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from functools import partial


# Helper Functions =======================================================================

def queryFile(entry: Entry) -> None:
    selected = filedialog.askopenfilename(initialdir="/", title="Select a file")
    entry.delete(0, END)
    entry.insert(0, selected)

def queryFolder(entry: Entry) -> None:
    selected = filedialog.askdirectory(initialdir="/", title="Select a folder")
    entry.delete(0, END)
    entry.insert(0, selected)

def processAndRun() -> None:
    config.program_name = entry_exec.get()
    config.input_folder = entry_indir.get()
    config.input_extension = entry_inext.get()
    config.output_folder = entry_outdir.get()
    config.output_extension = entry_outext.get()
    try:
        float(entry_time.get())
    except:
        config.time_lim = 4.0   # probably don't need to since it's already set
    else:
        config.time_lim = float(entry_time.get())
    runTests()
    instr.config(state=NORMAL)
    instr.delete('1.0', END)
    instr.insert('0.0', config.log)
    instr.config(state=DISABLED)

# End of functions ========================================================================


# Start of GUI specification ==============================================================
root = Tk()
root.title("Test Automator")
root.geometry("545x720") # 1920x1080 is full screen
root.resizable(False, False)

frm = ttk.Frame(root)
frm.grid()

# Specifications for instructions
instr = Text(frm, width=62, height=8, relief=GROOVE, bg="light grey", wrap=WORD)
instr.insert('0.0', config.instructions)
instr.config(state=DISABLED)
instr.grid(column=0, row=0, pady=(config.default_pad, 0))

# End of Specifications for instructions

# Specifications for interactive area
actions = ttk.Frame(frm, padding=10)
actions.grid(column=0, row=1)

# Labels
label_exec = ttk.Label(actions, text=config.label_exec, padding=config.default_pad)
label_exec.grid(column=0, row=1, sticky='w')

ttk.Label(actions, text="").grid(column=0, row=2)   # spacer

label_indir = ttk.Label(actions, text=config.label_indir, padding=config.default_pad)
label_indir.grid(column=0, row=3, sticky='w')

label_inext = ttk.Label(actions, text=config.label_inext, padding=config.default_pad)
label_inext.grid(column=0, row=4, sticky='w')

ttk.Label(actions, text="").grid(column=0, row=5)   # spacer

label_outdir = ttk.Label(actions, text=config.label_outdir, padding=config.default_pad)
label_outdir.grid(column=0, row=6, sticky='w')

label_outext = ttk.Label(actions, text=config.label_outext, padding=config.default_pad)
label_outext.grid(column=0, row=7, sticky='w')

ttk.Label(actions, text="").grid(column=0, row=8)   # spacer

label_time = ttk.Label(actions, text=config.label_time, padding=config.default_pad)
label_time.grid(column=0, row=9, sticky="w")

ttk.Label(actions, text="").grid(column=0, row=10)   # spacer
ttk.Label(actions, text="").grid(column=0, row=12)   # spacer

# Entries
entry_exec = ttk.Entry(actions, textvariable=StringVar(), width=config.entry_width1)
entry_exec.grid(column=1, row=1, sticky='w')

entry_indir = ttk.Entry(actions, textvariable=StringVar(), width=config.entry_width1)
entry_indir.grid(column=1, row=3, sticky='w')

entry_inext = ttk.Entry(actions, textvariable=StringVar(), width=config.entry_width2)
entry_inext.grid(column=1, row=4, sticky='w')
entry_inext.insert(0, ".in")

entry_outdir = ttk.Entry(actions, textvariable=StringVar(), width=config.entry_width1)
entry_outdir.grid(column=1, row=6, sticky='w')

entry_outext = ttk.Entry(actions, textvariable=StringVar(), width=config.entry_width2)
entry_outext.grid(column=1, row=7, sticky='w')
entry_outext.insert(0, ".out")

entry_time = ttk.Entry(actions, textvariable=StringVar(), width=config.entry_width2)
entry_time.grid(column=1, row=9, sticky="w")
entry_time.insert(0, "4.0")

# Buttons
but_exec = ttk.Button(actions, text="Browse", command=partial(queryFile, entry_exec))
but_exec.grid(column=2, row=1, padx=(config.default_pad, config.default_pad))

but_indir = ttk.Button(actions, text="Browse", command=partial(queryFolder, entry_indir))
but_indir.grid(column=2, row=3, padx=(config.default_pad, config.default_pad))

but_outdir = ttk.Button(actions, text="Browse", command=partial(queryFolder, entry_outdir))
but_outdir.grid(column=2, row=6, padx=(config.default_pad, config.default_pad))

but_run = ttk.Button(actions, text="Run Tests", command=processAndRun)
but_run.grid(column=1, row=11)
# End of Interactive Area

# Specifications for Log
logArea = ttk.Frame(frm)
logArea.grid(column=0, row=2)

label_log = ttk.Label(logArea, text=config.label_log)
label_log.grid(column=0, row=0, sticky="w")

scrollbar = Scrollbar(logArea)
scrollbar.grid(column=1, row=1, sticky=NSEW)

instr = Text(logArea, width=60, height=10, wrap=WORD, yscrollcommand=scrollbar.set)
instr.grid(column=0, row=1)

scrollbar.config(command=instr.yview) # is this necessary?

# End of specification for Log

# End of GUI specification =======================================================================

root.mainloop()

