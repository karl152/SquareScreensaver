# SquareScreensaver
# Copyright (c) 2024-2026 Isso123, Karl "karl152"
# This software is licensed under the BSD 3-Clause License.
# See the LICENSE file for details.
# SPDX-License-Identifier: BSD-3-Clause

import ctypes
try:
    ctypes.windll.shcore.SetProcessDpiAwareness(1)
except:
    pass
from turtle import *
import random
import sys
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkinter import filedialog
from tkinter import colorchooser
import winreg
import subprocess

ver = "1.3"
failcounter = 0

def loadRegistry():
    global failcounter, BackgroundImagePath, CloseOnMouseMovement, Thickness, Speed, UseBackgroundImage, Squares, R, G, B
    if failcounter >= 2:
        messagebox.showerror("Error", "Loop while trying to create registry")
        sys.exit(1)
    try:
        with winreg.OpenKeyEx(winreg.HKEY_CURRENT_USER, r"Software\SquareScreensaver") as SQSKey:
            ConfigVersion = winreg.QueryValueEx(SQSKey, "ConfigVersion")[0]
            BackgroundImagePath = winreg.QueryValueEx(SQSKey, "BackgroundImagePath")[0]
            CloseOnMouseMovement = winreg.QueryValueEx(SQSKey, "CloseOnMouseMovement")[0]
            Thickness = winreg.QueryValueEx(SQSKey, "Thickness")[0]
            Speed = winreg.QueryValueEx(SQSKey, "Speed")[0]
            UseBackgroundImage = winreg.QueryValueEx(SQSKey, "UseBackgroundImage")[0]
            Squares = winreg.QueryValueEx(SQSKey, "Squares")[0]
            R = winreg.QueryValueEx(SQSKey, "BackgroundR")[0]
            G = winreg.QueryValueEx(SQSKey, "BackgroundG")[0]
            B = winreg.QueryValueEx(SQSKey, "BackgroundB")[0]
        # print(f"ConfigVersion: {ConfigVersion}\nBackgroundImagePath: {BackgroundImagePath}\nCloseOnMouseMovement: {CloseOnMouseMovement}\nThickness: {Thickness}\nSpeed: {Speed}\nUseBackgroundImage: {UseBackgroundImage}\nSquares: {Squares}\nbackground colors: {R} {G} {B}")
    except:
        failcounter += 1
        createRegistry()

def rgb_to_hex(r, g, b):
    return f"#{r:02x}{g:02x}{b:02x}"

def clearRegistry(exitafter):
    try:
        whatever = subprocess.getoutput(r'reg delete "HKEY_CURRENT_USER\Software\SquareScreensaver" /f') # sorry, but I'm not figuring out how to do that with winreg right now
        print(whatever)
    except:
        pass
    if exitafter == True:
        sys.exit(0)
def createRegistry():
    clearRegistry(False)
    with winreg.OpenKeyEx(winreg.HKEY_CURRENT_USER, r"Software") as SoftwareKey:
        with winreg.CreateKey(SoftwareKey, "SquareScreensaver") as SQSKey:
            # default settings
            winreg.SetValueEx(SQSKey, "ConfigVersion", 0, winreg.REG_DWORD, 1)
            winreg.SetValueEx(SQSKey, "BackgroundImagePath", 0, winreg.REG_SZ, "")
            winreg.SetValueEx(SQSKey, "CloseOnMouseMovement", 0, winreg.REG_DWORD, 1)
            winreg.SetValueEx(SQSKey, "Thickness", 0, winreg.REG_DWORD, 1)
            winreg.SetValueEx(SQSKey, "Speed", 0, winreg.REG_DWORD, 0)
            winreg.SetValueEx(SQSKey, "UseBackgroundImage", 0, winreg.REG_DWORD, 0)
            winreg.SetValueEx(SQSKey, "Squares", 0, winreg.REG_DWORD, 1000)
            winreg.SetValueEx(SQSKey, "BackgroundR", 0, winreg.REG_DWORD, 0)
            winreg.SetValueEx(SQSKey, "BackgroundG", 0, winreg.REG_DWORD, 0)
            winreg.SetValueEx(SQSKey, "BackgroundB", 0, winreg.REG_DWORD, 0)
    loadRegistry()

if "/p" in sys.argv:
    sys.exit(0)
elif "/?" in sys.argv:
    print(f"""SquareScreensaver {ver} by Isso123 and karl152
********************************************
/c open options menu
/? show this""")
    sys.exit(0)
elif "/s" in sys.argv:
    loadRegistry()
    def exit_input(event=None):
        screen.bye()
        sys.exit(0)

    try:
        colormode(255)
        speed(Speed)
        screen = Screen()
        screen.cv._rootwindow.attributes("-fullscreen", True)
        if CloseOnMouseMovement == 1:
            screen.cv._rootwindow.bind("<Motion>", exit_input)
        screen.cv._rootwindow.bind("<Key>", exit_input)
        screen.cv._rootwindow.config(cursor="none")
        canvas = screen.getcanvas()
        canvas.config(highlightthickness=0, borderwidth=0)
        canvas.config(bg=rgb_to_hex(R, G, B))
        height = screen.cv._rootwindow.winfo_screenheight()
        width = screen.cv._rootwindow.winfo_screenwidth()
        halfwidth = int(width/2)
        halfheight = int(height/2)
        screen.bgcolor(R, G, B)
        if UseBackgroundImage == 1:
            try:
                screen.bgpic(BackgroundImagePath)
            except:
                pass
        pensize(Thickness)
        for i in range (Squares):
            x=random.randint(int(f"-{halfwidth}"), halfwidth)
            y=random.randint(int(f"-{halfheight}"), halfheight)
            penup()
            setpos(x,y)
            pendown()

            r=random.randint(0,255)
            g=random.randint(0, 255)
            b=random.randint(0, 255)
            pencolor (r,g,b)

            d=random.randint(5, 50)

            for x in range (4):
                forward(d)
                right(90)
        screen.mainloop()
    except:
        sys.exit(0)
else:
    loadRegistry()
    def ChangeColor():
        global R, G, B
        ChosenColor = tk.colorchooser.askcolor()
        R = ChosenColor[0][0]
        G = ChosenColor[0][1]
        B = ChosenColor[0][2]
        BackgroundColorThing.config(bg=ChosenColor[1], fg=ChosenColor[1])
    def openBackgroundImage():
        BackgroundPicturePath = filedialog.askopenfilename(title="Choose Background Picture", filetypes=[("Pictures", "*.png *.gif *.pgm *.ppm")])
        BackgroundPathEntry.delete(0, tk.END)
        BackgroundPathEntry.insert(0, BackgroundPicturePath)
    def clearConfig():
        clearRegistry(False)
        Window.destroy()
        sys.exit(0)
    def saveandclose():
        global BackgroundImagePath, CloseOnMouseMovement, Thickness, Speed, UseBackgroundImage, Squares, R, G, B
        try:
            SQSKey = winreg.OpenKeyEx(winreg.HKEY_CURRENT_USER, r"Software\\SquareScreensaver\\", 0, winreg.KEY_SET_VALUE)
            winreg.SetValueEx(SQSKey, "BackgroundImagePath", 0, winreg.REG_SZ, BackgroundPathEntryTk.get())
            winreg.SetValueEx(SQSKey, "CloseOnMouseMovement", 0, winreg.REG_DWORD, CloseScreensaverOnMouseMovementBooleanTk.get())
            winreg.SetValueEx(SQSKey, "Thickness", 0, winreg.REG_DWORD, ThicknessTk.get())
            winreg.SetValueEx(SQSKey, "Speed", 0, winreg.REG_DWORD, SpeedTk.get())
            winreg.SetValueEx(SQSKey, "UseBackgroundImage", 0, winreg.REG_DWORD, UseBackgroundImageTk.get())
            winreg.SetValueEx(SQSKey, "Squares", 0, winreg.REG_DWORD, SquaresTk.get())
            winreg.SetValueEx(SQSKey, "BackgroundR", 0, winreg.REG_DWORD, R)
            winreg.SetValueEx(SQSKey, "BackgroundG", 0, winreg.REG_DWORD, G)
            winreg.SetValueEx(SQSKey, "BackgroundB", 0, winreg.REG_DWORD, B)
            winreg.CloseKey(SQSKey)
        except:
            messagebox.showerror("Error", "Error while trying to save settings")
        Window.destroy()
    Window = tk.Tk()
    Window.resizable(False, False)
    SpeedTk = tk.IntVar(value=Speed)
    ThicknessTk = tk.IntVar(value=Thickness)
    UseBackgroundImageTk = tk.IntVar(value=UseBackgroundImage)
    SquaresTk = tk.IntVar(value=Squares)
    BackgroundPathEntryTk = tk.StringVar(value=BackgroundImagePath)
    CloseScreensaverOnMouseMovementBooleanTk = tk.IntVar(value=CloseOnMouseMovement) # this was a boolean, but it's now an integer because that works easier with the registry
    Window.title("Settings")
    BigText = tk.Label(Window, text="SquareScreensaver", font=("Lucida Console", 15))
    SmallText = ttk.Label(Window, text=f"Version {ver}")
    SpeedBox = ttk.LabelFrame(Window, text="Speed")
    SpeedSlider = tk.Scale(SpeedBox, from_=0, to=5, orient="horizontal", variable=SpeedTk)
    ThicknessBox = ttk.LabelFrame(Window, text="Thickness") # or should I call it pen size?
    ThicknessSlider = tk.Scale(ThicknessBox, from_=0, to=5, orient="horizontal", variable=ThicknessTk)
    BackgroundBox = ttk.LabelFrame(Window, text="Background")
    BackgroundColorThing = tk.Label(BackgroundBox, text="####", bg=rgb_to_hex(R, G, B), fg=rgb_to_hex(R, G, B))
    BackgroundColorButton = ttk.Button(BackgroundBox, text="Change Color", command=ChangeColor)
    BackgroundImageCheckbox = ttk.Checkbutton(BackgroundBox, text="use background image", variable=UseBackgroundImageTk)
    BackgroundOpenButton = tk.Button(BackgroundBox, text="1", font=("Wingdings", 10), command=openBackgroundImage)
    BackgroundPathEntry = ttk.Entry(BackgroundBox, textvariable=BackgroundPathEntryTk)
    OtherThingsBox = ttk.LabelFrame(Window, text="Other things")
    SquaresLabel = ttk.Label(OtherThingsBox, text="Squares: ")
    SquaresSpinbox = ttk.Spinbox(OtherThingsBox, width=5, from_=0, to=99999, textvariable=SquaresTk)
    CloseOnMouseMovementCheckbox = ttk.Checkbutton(OtherThingsBox, text="stop on mouse movement", variable=CloseScreensaverOnMouseMovementBooleanTk)
    ClearConfigButton = ttk.Button(OtherThingsBox, text="Clear Configuration", command=clearConfig)
    BigText.grid(row=0, column=0, columnspan=2)
    SmallText.grid(row=1, column=0, columnspan=2)
    ttk.Separator(Window, orient="horizontal").grid(row=2, column=0, columnspan=2, sticky="news")
    SpeedBox.grid(row=3, column=0, pady=5)
    SpeedSlider.grid(row=0, column=0)
    ThicknessBox.grid(row=3, column=1, pady=5)
    ThicknessSlider.grid(row=0, column=0)
    BackgroundBox.grid(row=4, column=0, columnspan=2, padx=10, pady=5)
    BackgroundColorThing.grid(row=0, column=0)
    BackgroundColorButton.grid(row=0, column=1)
    BackgroundImageCheckbox.grid(row=0, column=2)
    BackgroundOpenButton.grid(row=1, column=0)
    BackgroundPathEntry.grid(row=1, column=1, columnspan=2, sticky="news")
    OtherThingsBox.grid(row=5, column=0, columnspan=2, pady=5)
    SquaresLabel.grid(row=0, column=0)
    SquaresSpinbox.grid(row=0, column=1)
    CloseOnMouseMovementCheckbox.grid(row=0, column=2)
    ClearConfigButton.grid(row=1, columnspan=3, pady=5)
    ttk.Separator(Window, orient="horizontal").grid(row=6, column=0, columnspan=2, sticky="news")
    ttk.Button(Window, text="OK", command=saveandclose).grid(row=7, column=0)
    ttk.Button(Window, text="Cancel", command=lambda: Window.destroy()).grid(row=7, column=1)
    Window.mainloop()
