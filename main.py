from tkinter import *
from tkinter import ttk

import json

root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()

outer_runes = [0,0,0,0,0,0]
inner_runes = [0,0,0,0,0,0,0]

def toggle_line(canvas, line):
    if canvas.itemcget(line, "fill") == "black":
        canvas.itemconfigure(line, fill = "gray75")
        if line < 7:
            outer_runes[line - 1] = 0
        else:
            inner_runes[line - 7] = 0
    else:
        canvas.itemconfigure(line, fill = "black")
        if line < 7:
            outer_runes[line - 1] = 1
        else:
            inner_runes[line - 7] = 1
    print(str(outer_runes))
    print(str(inner_runes))

def create_rune_line(canvas, start_x, start_y, end_x, end_y):
    new_line = canvas.create_line(start_x, start_y, end_x, end_y, width = 8, fill = "grey75")
    canvas.tag_bind(new_line, "<Button-1>", lambda x: toggle_line(canvas, new_line))

def create_outer_rune(canvas):
    # ^
    create_rune_line(canvas, 250, 5, 200, 30)
    create_rune_line(canvas, 250, 5, 300, 30)
    # ||
    create_rune_line(canvas, 200, 30, 200, 135)
    create_rune_line(canvas, 300, 30, 300, 135)
    # v
    create_rune_line(canvas, 200, 135, 250, 160)
    create_rune_line(canvas, 300, 135, 250, 160)

def create_inner_rune(canvas):
    # W
    create_rune_line(canvas, 200, 30, 250, 55)
    create_rune_line(canvas, 250, 5, 250, 55)
    create_rune_line(canvas, 300, 30, 250, 55)
    # |
    create_rune_line(canvas, 250, 55, 250, 110)
    # M
    create_rune_line(canvas, 200, 135, 250, 110)
    create_rune_line(canvas, 250, 160, 250, 110)
    create_rune_line(canvas, 300, 135, 250, 110)

def add_translation(text_widget):
    cur_text = text_widget.cget("text")

    inner_translation = ""

    with open("./data/inner_runes.json", "r") as f:
        data = json.load(f)
        inner_translation = data.get("".join([str(i) for i in inner_runes]))

    if inner_translation is not None:
        cur_text += inner_translation

    outer_translation = ""

    with open("./data/outer_runes.json", "r") as f:
        data = json.load(f)
        outer_translation = data.get("".join([str(i) for i in outer_runes]))

    if outer_translation is not None:
        cur_text += outer_translation

    text_widget.configure(text = cur_text)

def add_space(text_widget):
    text_widget.configure(text = text_widget.cget("text") + " ")


ttk.Label(text="Runes go Here").grid(column=0, row=0)

translation_text = ttk.Label(text="")
translation_text.grid(column=0, row=1)

canvas = Canvas(root, width=500, height=500)
canvas.grid(column=0, row=2)

ttk.Button(root, text="Submit", command = lambda: add_translation(translation_text)).grid(column=0, row = 3)
ttk.Button(root, text="Space", command = lambda: add_space(translation_text)).grid(column=1, row=3)

create_outer_rune(canvas)
create_inner_rune(canvas)

root.mainloop()