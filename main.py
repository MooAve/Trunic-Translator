from tkinter import *
from tkinter import ttk
from tkinter import filedialog

import json
import pyttsx3

from input_rune import Rune
from rune_output import OutputRunes

engine = pyttsx3.init()

root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()

root.option_add("*tearOff", FALSE)

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
    # |
    rune.create_rune_line(200, 30, 200, 135)
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
    
    
def toggle_circle(circle):
    """
    Toggles the rune circle

    :param circle: the oval widget on the provided canvas
    """
    if canvas.itemcget(circle, "outline") == "black":
        canvas.itemconfigure(circle, outline="gray75")
    else:
        canvas.itemconfigure(circle, outline="black")


def is_circle_on(circle):
    """
    Returns the current state of the circle rune

    :param circle: the oval widget on the provided canvas
    :return: Bool
    """
    if canvas.itemcget(circle, "outline") == "black":
        return True
    else:
        return False


def add_translation(text_widget, circle):
    """
    Takes the current state of the input rune and outputs its translation onto a text widget

    :param text_widget: ID of a label widget
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

    circle_on = is_circle_on(circle)

    # Don't add output if inner + outer runes are blank
    if outer_translation != "" or inner_translation != "":
        runes_out.add_rune(outer_rune.get_rune_string(), inner_rune.get_rune_string(), circle_on)
    else:
        return

    if circle_on:
        cur_text += "-" + outer_translation + inner_translation
    else:
        cur_text += "-" + inner_translation + outer_translation

    text_widget.configure(text = cur_text)


def add_space(text_widget):
    """
    Outputs a space to the provided text widget

    :param text_widget: a label widget
    """
    text_widget.configure(text = text_widget.cget("text") + " ")
    runes_out.add_space()


def delete_word(text_widget):
    """
    Deletes the last word added to a text widget

    :param text_widget: a label widget
    """
    cur_text = text_widget.cget("text")

    text_widget.configure(text = cur_text.rsplit("-", 1)[0])
    runes_out.delete_rune()


def clear_input_rune(inner, outer, circle):
    """
    Resets both the inner and outer runes to their default state
    :param inner: inner rune widget
    :param outer: outer rune widget
    :param circle: cirlce rune widget
    """

    inner_rune.clear_rune()
    outer_rune.clear_rune()
    canvas.itemconfigure(circle, outline="gray75")


def clear_all(text_widget):
    """
    Deletes all text and output runes
    :param text_widget: a label widget
    """

    text_widget.configure(text = "")
    runes_out.clear_all_runes()


def save_text(text_widget):
    """
    Saves the translated text to a user-specified file
    :param text_widget: a label widget containing translated text
    """

    text = text_widget.cget("text")

    text_file = filedialog.asksaveasfile(mode="w", title="Save Translated Text", defaultextension=".txt")

    if text_file is not None:

        text_file.write(text)

        text_file.close()


def save_runes(rune_out):
    """
    Saves the current output runes to a text file
    :param rune_out: Output rune object
    """

    text_file = filedialog.asksaveasfile(mode="w", title="Save Translated Text", defaultextension=".txt")

    if text_file is not None:

        for rune in rune_out.get_output_runes():
            text_file.write(rune + " ")

        text_file.close()


def load_runes(rune_out):
    """
    Loads a file containing strings of output runes
    :param rune_out: Output rune object
    """

    text_file = filedialog.askopenfile(mode="r", defaultextension=".txt")

    if text_file is not None:

        rune_out.set_output_runes(text_file.read().split())

        text_file.close()


# Create widget used to hold previously input runes
output_canvas = Canvas(root, width=500, height=100)
output_canvas.grid(column=0, row=0)

runes_out = OutputRunes(output_canvas)

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

canvas.tag_bind(rune_circle, "<Button-1>", lambda x: toggle_circle(rune_circle))

# Add menu bar
menu = Menu(root)
root["menu"] = menu

file_menu = Menu(menu)
menu.add_cascade(menu=file_menu, label="File")
file_menu.add_command(label="Save Text As", command=lambda: save_text(translation_text))
file_menu.add_command(label="Save Runes As", command=lambda: save_runes(runes_out))
file_menu.add_command(label="Load Runes From File", command=lambda: load_runes(runes_out))

edit_menu = Menu(menu)
menu.add_cascade(menu=edit_menu, label="Edit")
edit_menu.add_command(label="Clear Rune", command = lambda:(clear_input_rune(inner_rune, outer_rune, rune_circle)))
edit_menu.add_command(label="Delete All Text", command = lambda: clear_all(translation_text))

# Create misc. functional buttons
submit_button = ttk.Button(root, text="Submit", command = lambda: add_translation(translation_text, rune_circle))
submit_button.grid(column=0, row = 3)

ttk.Button(root, text="Space", command = lambda: add_space(translation_text)).grid(column=1, row=3)
ttk.Button(root, text="Delete", command = lambda: delete_word(translation_text)).grid(column=2, row=3)
ttk.Button(root, text="Clear", command = lambda: clear_all(translation_text)).grid(column=3, row=3)

# Add keybinds for some misc. functions
root.bind("<Return>", lambda x: add_translation(translation_text, rune_circle))
root.bind("<space>", lambda x: add_space(translation_text))
root.bind("<BackSpace>", lambda x: delete_word(translation_text))

root.mainloop()