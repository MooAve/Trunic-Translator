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
    """
    Reads the provided text using text-to-speech
    :param text: the text to read
    :param tts: a pyttsx engine
    """

    tts.say(text)
    tts.runAndWait()


def create_outer_rune(rune):
    """
    Draws all the lines to form the outer input rune

    :param rune: a rune object that will hold all the created lines
    :return:
    """
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
    """
    Draws all the lines that form the inner input rune

    :param rune: a rune object that will hold all the created lines
    """
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
    
    
def toggle_circle(canvas, circle):
    """
    Toggles the rune circle

    :param canvas: the canvas widget that holds the circle
    :param circle: the oval widget on the provided canvas
    """
    if canvas.itemcget(circle, "outline") == "black":
        canvas.itemconfigure(circle, outline="gray75")
    else:
        canvas.itemconfigure(circle, outline="black")


def is_circle_on(canvas, circle):
    """
    Returns the current state of the circle rune

    :param canvas: the canvas widget that holds the circle
    :param circle: the oval widget on the provided canvas
    :return: Bool
    """
    if canvas.itemcget(circle, "outline") == "black":
        return True
    else:
        return False


def add_translation(text_widget, canvas, circle):
    """
    Takes the current state of the input rune and outputs its translation onto a text widget

    :param text_widget: ID of a label widget
    :param canvas: a canvas object
    :param circle: an oval widget
    """
    cur_text = text_widget.cget("text")

    inner_translation = ""

    with open("./data/inner_runes.json", "r") as f:
        data = json.load(f)
        inner_translation = data.get(inner_rune.get_rune_string(), "")

    outer_translation = ""

    with open("./data/outer_runes.json", "r") as f:
        data = json.load(f)
        outer_translation = data.get(outer_rune.get_rune_string(), "")

    if is_circle_on(canvas, circle):
        cur_text += outer_translation + inner_translation
    else:
        cur_text += inner_translation + outer_translation

    text_widget.configure(text = cur_text)


def add_space(text_widget):
    """
    Outputs a space to the provided text widget

    :param text_widget: a label widget
    """
    text_widget.configure(text = text_widget.cget("text") + " ")


def delete_word(text_widget):
    """
    Deletes the last word added to a text widget

    :param text_widget: a label widget
    """
    cur_text = text_widget.cget("text")

    text_widget.configure(text = cur_text.rsplit(" ", 1)[0])


# TODO: display previously inputted runes
ttk.Label(text="Runes go Here").grid(column=0, row=0)

# Create widget used to hold translated text
translation_text = ttk.Label(text="")
translation_text.grid(column=0, row=1)

# Create read-aloud button
ttk.Button(root, text="Read", command=lambda: read_translation(translation_text.cget("text"), engine)).grid(column=1, row=1)

# Create the input runes
canvas = Canvas(root, width=500, height=500)
canvas.grid(column=0, row=2)

inner_rune = Rune(canvas)
create_inner_rune(inner_rune)

outer_rune = Rune(canvas)
create_outer_rune(outer_rune)

rune_circle = canvas.create_oval(225, 160, 275, 210, width=8, outline = "grey75")

canvas.tag_bind(rune_circle, "<Button-1>", lambda x: toggle_circle(canvas, rune_circle))

# Create misc. functional buttons
submit_button = ttk.Button(root, text="Submit", command = lambda: add_translation(translation_text, canvas, rune_circle))
submit_button.grid(column=0, row = 3)

ttk.Button(root, text="Space", command = lambda: add_space(translation_text)).grid(column=1, row=3)
ttk.Button(root, text="Delete", command = lambda: delete_word(translation_text)).grid(column=2, row=3)
ttk.Button(root, text="Clear", command = lambda: translation_text.configure(text = "")).grid(column=3, row=3)

# Add keybinds for some misc. functions
root.bind("<Return>", lambda x: add_translation(translation_text, canvas, rune_circle))
root.bind("<space>", lambda x: add_space(translation_text))
root.bind("<BackSpace>", lambda x: delete_word(translation_text))

root.mainloop()