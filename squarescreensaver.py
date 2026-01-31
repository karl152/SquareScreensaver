# SquareScreensaver
# Copyright (c) 2024-2026 Isso123, Karl "karl152"
# This software is licensed under the BSD 3-Clause License.
# See the LICENSE file for details.
# SPDX-License-Identifier: BSD-3-Clause

from turtle import *
import random
import sys
from tkinter import messagebox

ver = "1.0"
if "/p" in sys.argv:
    sys.exit(0)
elif "/?" in sys.argv:
    print(f"""SquareScreensaver {ver} by Isso123 and karl152
********************************************
/c open options menu
/? show this""")
    sys.exit(0)
elif "/s" in sys.argv: 
    def exit_input(event=None):
        screen.bye()
        sys.exit(0)

    try:
        colormode(255)
        speed(0)
        screen = Screen()
        screen.cv._rootwindow.attributes("-fullscreen", True)
        screen.cv._rootwindow.bind("<Motion>", exit_input)
        screen.cv._rootwindow.bind("<Key>", exit_input)
        height = screen.cv._rootwindow.winfo_screenheight()
        width = screen.cv._rootwindow.winfo_screenwidth()
        halfwidth = int(width/2)
        halfheight = int(height/2)
        screen.bgcolor(0, 0, 0)
        for i in range (1000):
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
    except:
        sys.exit(0)
else:
    messagebox.showinfo(f"SquareScreensaver {ver}", "no options available")
    sys.exit(0)
