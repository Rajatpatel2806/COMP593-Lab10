
"""
name: Rajat Patel - (10327381)
group: Rajat Patel, Ayush Navadiya, Amirash Thakkar, Yash Patel


Description:
  Graphical user interface that displays the official artwork for a
  user-specified Pokemon, which can be set as the desktop background image.

Usage:
  python poke_image_viewer.py
"""
from tkinter import *
from tkinter import ttk
import os
import poke_api
import image_lib
import ctypes
import inspect

# Get the script and images directory
script_name= inspect.getfile(inspect.currentframe()) ## TODO please please finish this
script_dir = os.path.dirname(os.path.abspath(__file__))
images_dir = os.path.join(script_dir, 'images')

# TODO: Create the images directory if it does not exist

# Create the main window
root = Tk()
root.title("Pokemon Viewer")
root.geometry('600x600')
root.minsize(500, 600)
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# TODO: Set the icon
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID('COMP593.PokeImageViewer')
root.iconbitmap(os.path.join(script_dir, 'poke_ball.ico'))
# TODO: Create frames
frm = ttk.Frame(root)
frm.columnconfigure(0, weight=1)
frm.rowconfigure(0, weight=1)
frm.grid(sticky = NSEW)

# TODO: Populate frames with widgets and define event handler functions
image_path = os.path.join(script_dir, 'poke_ball.png')
photo = PhotoImage(file=image_path)

lbl_image = ttk.Label(frm, image=photo)
lbl_image.grid(row=0, column=0, padx=10, pady=10)

pokemon_list = poke_api.get_pokemon_names()
pokemon_list_viewer = ttk.Combobox(root, values=pokemon_list, state='readonly')
pokemon_list_viewer.set('Select a Pokemon')
pokemon_list_viewer.grid(row=1,column=0,padx=10,pady=10)


#Create button to set desktop background
def handle_set_desktop():
  image_lib.set_desktop_background_image(image_path)
  return

# Button to set the desktop wallpaper of the selected pokemon.
Set_desktop_button = ttk.Button(root, text='Set as Desktop Image' , command=handle_set_desktop)
Set_desktop_button.grid(row=2,column=0,padx=20,pady=10)
Set_desktop_button.state(['disabled'])

def handle_poke_sel(event):
  name = cbox_poke_sel.get()
  global image_path
  image_path = poke_api.download_pokemon_artwork(pokemon_name=name, folder_path=images_dir)
  if image_path is not None:
      photo['file'] = image_path
  Set_desktop_button.state(['!disabled'])
  return

pokemon_list = poke_api.get_pokemon_names()
print(pokemon_list)
cbox_poke_sel = ttk.Combobox(root, values=pokemon_list, state='readonly')
cbox_poke_sel.set('Select a Pokemon')
cbox_poke_sel.grid(row=1,column=0,padx=10,pady=10)
cbox_poke_sel.bind('<<ComboboxSelected>>', handle_poke_sel)

root.mainloop()