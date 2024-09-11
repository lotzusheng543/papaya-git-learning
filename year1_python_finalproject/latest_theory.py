import tkinter as tk
from tkinter import PhotoImage
import os
import subprocess
import sys


main_menu_path = r"C:\Users\user\OneDrive - University of Southampton\Desktop\Year1 python\long project\main_menu.py"
args = '"%s" "%s" "%s"' % (sys.executable, main_menu_path, os.path.basename("main_menu.py"))


def open_main_menu():
    proc = subprocess.run(args)


def back_function():
    theory_window.destroy()
    open_main_menu()  # Corrected to call the function



def setup_theory():
    global theory_window
    theory_window = tk.Tk()
    theory_window.title("Static Friction Theory")
    theory_window.configure(background="black")
    theory_window.geometry("1000x1000")  # Set the fixed
    theory_window.maxsize(1600, 1200)
    theory_window.minsize(1600, 1200)

    theory_label = tk.Label(
        theory_window, text="Static Friction Theory", font=("Arial", 25))
    theory_label.pack(pady=50)
    image_path = r"C:\Users\user\OneDrive - University of Southampton\Desktop\Year1 python\long project\images1.png"
    theory_image = PhotoImage(file=image_path)
    photo1 = theory_image.zoom(2, 2)
    image_label = tk.Label(theory_window, image=photo1)
    image_label.pack(padx=20, pady=20)
    theory_text = tk.Label(theory_window, text="The force on the object has reached the peak of the static friction which then converts to kinetic friction when it starts moving.When the force smaller than maximum static friction, the friction will be equal to outer force apply.", font=("Arial", 18), wraplength=1400, justify="center")
    theory_text.pack(padx=10, pady=5)

    back_button = tk.Button(theory_window, text="Back", command=lambda: [back_function()], width=20, height=3, bg="green")
    back_button.pack(padx=20, pady=20)

    theory_window.attributes('-fullscreen', True)
    theory_window.mainloop()


setup_theory()
