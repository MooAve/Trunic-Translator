from tkinter import *
from tkinter import ttk

import json
import pyttsx3
from rune import Rune

engine = pyttsx3.init()

root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()

def read_translation(text, tts):
    tts.say(text)
    tts.runAndWait()

def create_outer_rune(rune):
    # ^
    rune.create_rune_line(250, 5, 200, 30)
    rune.create_rune_line(250, 5, 300, 30)
    # ||
    rune.create_rune_line(200, 30, 200, 135)
    rune.create_rune_line(300, 30, 300, 135)
    # v
    rune.create_rune_line(200, 135, 250, 160)
    rune.create_rune_line(300, 135, 250, 160)

def create_inner_rune(rune):
    # W
    rune.create_rune_line(200, 30, 250, 55)
    rune.create_rune_line(250, 5, 250, 55)
    rune.create_rune_line(300, 30, 250, 55)
    # |
    rune.create_rune_line(250, 55, 250, 110)
    # M
    rune.create_rune_line(200, 135, 250, 110)
    rune.create_rune_line(250, 160, 250, 110)
    rune.create_rune_line(300, 135, 250, 110)

def add_translation(text_widget):
    cur_text = text_widget.cget("text")

    inner_translation = ""

    with open("./data/inner_runes.json", "r") as f:
        data = json.load(f)
        inner_translation = data.get(inner_rune.get_rune_string())

    if inner_translation is not None:
        cur_text += inner_translation

    outer_translation = ""

    with open("./data/outer_runes.json", "r") as f:
        data = json.load(f)
        outer_translation = data.get(outer_rune.get_rune_string())

    if outer_translation is not None:
        cur_text += outer_translation

    text_widget.configure(text = cur_text)

def add_space(text_widget):
    text_widget.configure(text = text_widget.cget("text") + " ")

ttk.Label(text="Runes go Here").grid(column=0, row=0)

translation_text = ttk.Label(text="")
translation_text.grid(column=0, row=1)

ttk.Button(root, text="Read", command=lambda: read_translation(translation_text.cget("text"), engine)).grid(column=1, row=1)

canvas = Canvas(root, width=500, height=500)
canvas.grid(column=0, row=2)

inner_rune = Rune(canvas)
create_inner_rune(inner_rune)

outer_rune = Rune(canvas)
create_outer_rune(outer_rune)

ttk.Button(root, text="Submit", command = lambda: add_translation(translation_text)).grid(column=0, row = 3)
ttk.Button(root, text="Space", command = lambda: add_space(translation_text)).grid(column=1, row=3)

root.mainloop()