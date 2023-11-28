import tkinter as tk
import pyperclip
from tkinter import messagebox
from tkinter import filedialog
from tkinter import filedialog
import unicodedata
import re

version = 'YWot Palette 3.0.5'

# Your function to copy characters to clipboard remains unchanged
def copy_to_clipboard(character):
    pyperclip.copy(character)
    print(f"Character '{character}' copied to clipboard.")

def show_characters_frame(root, characters):
    category_frame.pack_forget()  # Hide the category selection frame
    character_frame.pack()  # Show the character display frame

    for widget in character_frame.winfo_children():
        widget.destroy()  # Clear previous character buttons if any

    for i, char in enumerate(characters):
        btn = tk.Button(character_frame, text=char, command=lambda c=char: copy_to_clipboard(c), font=("Arial", 14))
        btn.grid(row=i // 13, column=i % 13, padx=5, pady=6)

    back_btn = tk.Button(character_frame, text="back", command=show_category_frame)
    back_btn.grid(row=(i + 1) // 5 + 1, column=0, columnspan=5, pady=5)  # Positioning the back button at the bottom
def show_category_frame():
    character_frame.pack_forget()  # Hide the character display frame
    category_frame.pack()  # Show the category selection frame

def create_category_buttons(root, categories):
    for category, char_list in categories.items():
        btn = tk.Button(category_frame, text=category, command=lambda cl=char_list: show_characters_frame(root, cl))
        btn.config(font=("Arial", 12))  # Adjusting the font size of category buttons
        btn.pack(pady=5)


def on_closing():
    if messagebox.askokcancel("Quit", f"Are you sure you want to close {version}?"):
        root.destroy()



def process_text_file():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename()

    if not file_path:
        return None

    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Remove spaces and duplicate characters using regular expressions
    content = re.sub(r'\s', '', content)
    unique_chars = sorted(set(content), key=content.index)

    # Get the filename from the file path
    filename = file_path.split('/')[-1]  # Adjust for Windows if needed

    # Create a dictionary with filename as key and unique characters as value
    custom_menu = {filename: unique_chars}

    return custom_menu


# Initialize the main window and frames
root = tk.Tk()
root.protocol("WM_DELETE_WINDOW", on_closing)
root.attributes('-topmost', True)  # Keep the window on top
root.title(version)

category_frame = tk.Frame(root)
character_frame = tk.Frame(root)

create_category_buttons(root, {

# The buttons dynamically load these lists adding a new menu is as simple as adding your own line in.

"Blocks": [ '█', '▓', '▒','░', '▀', '▄', '▌', '▐', '▖', '▘', '▝', '▗', '▙', '▛', '▜', '▟', '▞', '▚'],
    "Pipes": ['─', '│', '═', '║', '╔', '╗', '╚', '╝', '╓', '╕', '╒', '╖', '╙', '╛', '╘', '╜', '╞', '╡', '╠', '╣', '╟', '╢', '╤', '╥', '╦', '╧', '╨', '╩', '╪', '╫', '╬'],
    "Arrows": ['↺', '↻', '⮌', '⮍', '⮎', '⮏', '⇠', '⇡', '⇢', '⇣', '↖', '↗', '↘', '↙', '⯅', '⯆', '⯇', '⯈', '⛛', '⮘', '⮙', '⮚', '⮛', '⮜', '⮝', '⮞', '⮟'],
    "Numbers": ['➀', '➁', '➂', '➃', '➄', '➅', '➆', '➇', '➈', '➉', '➊', '➋', '➌', '➍', '➎', '➏', '➐', '➑', '➒', '➓'],
    "Shapes": ['⚐', '⚑','⛊','❏', '❐', '❑', '❒', '⯊', '⯋', '⬡', '⬢', '⬣', '⬟', '⬖', '⬗', '⬘', '⬙', '⬛', '⬜', '⬤', '❍', '⬬', '⬭', '⬮', '⬯', '⚪', '⚫', '⧉', '⬥', '⬦', '⬧', '⬨', '⬩', '⬪', '⬫','❖','✦', '⯌', '⯍', '⯎', '⯏', '✧', '⟡', '♡',], 
    "Misc": ['｀', 'ゝ','ω', '›', '‹', '»', '«', '⌋', '⌊', '⌉', '⌈', '︾', '︽', '﹀', '︿', '︺', '︹', '︶', '︵', '♫','♪','⚞', '⚟', '⬞', '⬝', '∘', '⯐', '✵', '✶', '✷', '✸', '✹', '✺', '⛯', '⛭', '⛮','✻', '✼', '✽', '✱', '❄', '❅', '❆', '⚝', '⛬', '✕', '⛌', '✖', '➕', '➖', '➗', '⚒', '⚔', '⛓', '⚓', '⚗', '⚠', '⛋', '⩆', '⚍', '⚎', '⚏', '✚', '✛', '✜','⍱', '⍲', '֍', '֎', '⎲', '⎳', '♱', '✮', '˚', '⋆', '｡', '+', '⊹', "❅", "❆", "⎟", "⎞", "⎛", "⎠", "⎝", "⎭", "⎩", "⎫", "⎧", "❈", "❉", "❊", "❋", "⚘", "❦", "❀", "❁", "✿", "❀", "✾", "✼", "❃", "❋",],
     "brail": ['⣿', '⣼', '⣧', '⡟','⢻', '⠛', '⣤', '⡇', '⢸', '⠁', '⠈', '⢀', '⡀']
     })
show_category_frame()  # Show the initial category selection frame


# Function to load custom menu
def load_custom_menu():
    custom_menu = process_text_file()
    if custom_menu:
        truncated_name = list(custom_menu.keys())[0].split('.')[0]  # Extract filename without .txt extension
        truncated_name_button = tk.Button(category_frame, text=truncated_name, command=lambda cl=list(custom_menu.values())[0]: show_characters_frame(root, cl))
        truncated_name_button.config(font=("Arial", 12))
        truncated_name_button.pack(pady=5)

# Adding "Load Custom" button
load_custom_btn = tk.Button(category_frame, text="Load Custom", command=load_custom_menu)
load_custom_btn.config(font=("Arial", 12))
load_custom_btn.pack(pady=5)
load_custom_btn.pack(side='bottom', pady=5)

root.mainloop()
