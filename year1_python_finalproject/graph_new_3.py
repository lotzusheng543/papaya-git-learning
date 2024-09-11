import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg # type:ignore
from matplotlib.figure import Figure # type:ignore
import os
import subprocess
import sys
from tkinter import ttk, PhotoImage

main_menu_path = r"C:\Users\user\OneDrive - University of Southampton\Desktop\Year1 python\long project\main_menu.py"
args = [sys.executable, main_menu_path]

def open_main_menu():
    proc = subprocess.run(args)

def back_function():
    result.destroy()
    open_main_menu()

# Define coefficients
mu_kinetic = 0.47  # coefficient of kinetic friction
mu_static = 0.6    # coefficient of static friction
g = 9.81
masses_g = range(500, 950, 1)  # 500 g to 900 g in steps of 50 g
forces_N = [mass / 1000 * g for mass in masses_g]  # kg to N
load_anchor = 4.905
static_friction = [mu_static * force for force in forces_N]
kinetic_friction = [mu_kinetic * force for force in forces_N]
load_anchor_list = [load_anchor] * len(masses_g)  # Create a list of anchor

def simulate():
    simulated_friction = []
    for load, static, kinetic in zip(load_anchor_list, static_friction, kinetic_friction):
        if load > static:
            simulated_friction.append(kinetic)
        else:
            simulated_friction.append(load)
    return simulated_friction

result = tk.Tk()
result.title("Frictional Force vs. Mass")

# Create a Matplotlib figure, label and data
fig = Figure(figsize=(2, 1), dpi=140)
plot = fig.add_subplot(1, 1, 1)
plot.plot(masses_g, static_friction, label='Maximum static friction force between both surface')
plot.plot(masses_g, kinetic_friction, label='Kinetic friction between both surface')
plot.plot(masses_g, simulate(), label='The friction between both surface')
plot.axhline(y=4.905, color='gray', linestyle=':', label = 'Applied force (500 grams anchor)')
plot.set_xlabel('Mass of ship (g)')
plot.set_ylabel('Frictional Force (N)')
plot.set_title('Frictional Force vs. Mass')
plot.legend()
plot.grid(True)

# Embed the plot in the Tkinter window
canvas = FigureCanvasTkAgg(fig, master=result)
canvas.draw()
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)


table_frame = tk.Frame(result)
table_frame.pack(pady=20)
style = ttk.Style()
style.configure("Treeview.Heading", foreground="brown")
table = ttk.Treeview(table_frame, columns=('weight', "Kinetic Friction", "Static Friction", 'friction by loading', 'real friction'), show="headings")
table.heading('weight', text='Weight (g)')
table.heading("Kinetic Friction", text="Kinetic Friction (N)")
table.heading("Static Friction", text=" Maximum Static Friction (N)")
table.heading('friction by loading', text='Friction by load (N) (fixed)')
table.heading('real friction', text='Real (Mock) friction')
table.pack()

data = [('500', "2.305", "2.943", '4.905', '> max static friction'),
        ('550', "2.536", "3.237", '4.905', '> max static friction'),
        ('600', "2.766", "3.532", '4.905', '> max static friction'),
        ('650', "2.997", "3.826", '4.905', '> max static friction'),
        ('850', "3.919", "5.003", '4.905', '< max static friction')]
for row in data:
    table.insert("", "end", values=row)

back_button = tk.Button(result, text="Back", command=back_function, width=20, height=3, bg="green")
back_button.pack(padx=10, pady=10)

result.attributes('-fullscreen', True)
result.mainloop()  # run tkinter
