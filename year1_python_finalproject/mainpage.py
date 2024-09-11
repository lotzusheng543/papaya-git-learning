import tkinter as tk
import os
import subprocess
import sys

root = tk.Tk()
root.title("Static Friction Simulation")
root.configure(background="black")
root.geometry("1000x1000")
root.minsize(500, 500)

# Provide the full path to the Python script files you want to execute
graph_path = r'C:\Users\user\OneDrive - University of Southampton\Desktop\Year1 python\long project\graph.py'
theory_path = r"C:\Users\user\OneDrive - University of Southampton\Desktop\Year1 python\long project\theory_pg.py"
graph2_path = r'C:\Users\user\OneDrive - University of Southampton\Desktop\Year1 python\long project\graph2.py'
graph3_path = r'C:\Users\user\OneDrive - University of Southampton\Desktop\Year1 python\long project\graph3.py'
graph4_path = r'C:\Users\user\OneDrive - University of Southampton\Desktop\Year1 python\long project\new_testing_without_wallfriction.py'
graph5_path = r"C:\Users\user\OneDrive - University of Southampton\Desktop\Year1 python\long project\latest_withwall.py"

args_graph = [sys.executable, graph_path]
args_theory = [sys.executable, theory_path]
args_graph2 = [sys.executable, graph2_path]
args_graph3 = [sys.executable, graph3_path]
args_graph4 = [sys.executable, graph4_path]
args_graph5 = [sys.executable, graph5_path]


def open_graph():
    subprocess.run(args_graph)


def open_graph2():
    subprocess.run(args_graph2)


def open_graph3():
    subprocess.run(args_graph3)


def open_graph4():
    subprocess.run(args_graph4)


def open_graph5():
    subprocess.run(args_graph5)


def open_theory():
    subprocess.run(args_theory)


def end_function():
    root.destroy()


def start_function():
    root.destroy()
    open_graph()


def start_function2():
    root.destroy()
    open_graph2()


def start_function3():
    root.destroy()
    open_graph3()


def theory_show():
    root.destroy()
    open_theory()






width= root.winfo_screenwidth() 
height= root.winfo_screenheight()

widthL = width*3/8
widthR = width*5/8
widthM = width/2
height1 = height*3/8
height2 = height/2
height2_5 = height*5/8
height3 = height*3/4
height4 = height*5/6
height_title = height/8

static_friction_label = tk.Label(root, text="Static Friction", font=("Arial", 50))
static_friction_label.pack(pady=20)
static_friction_label.place(x=width/2, y=height_title, anchor='n')

start_button = tk.Button(root, text="Experimental result", command=start_function, width=20, height=1, bg="green", font=("Arial", 20))
start_button.pack(pady=30)
start_button.place(x=widthL, y=height1, anchor='n')

start_button2 = tk.Button(root, text='Theoretical result', command=start_function2, width=20, height= 1, bg="green", font=("Arial", 20))
start_button2.pack(pady=30)
start_button2.place(x=widthR, y=height1, anchor='n')

start_button3 = tk.Button(root, text='Original result', command=start_function3, width=20, height= 1, bg="aqua", font=("Arial", 20))
start_button3.pack(pady=30)
start_button3.place(x=widthM, y=height2_5, anchor='n')

start_button4 = tk.Button(root, text='Finals result(without wall)', command=open_graph4, width=20, height= 1, bg="orange", font=("Arial", 20))
start_button4.pack(pady=30)
start_button4.place(x=widthR, y=height2, anchor='n')

start_button5 = tk.Button(root, text='Final result(with wall)', command=open_graph5, width=20, height= 1, bg="orange", font=("Arial", 20))
start_button5.pack(pady=30)
start_button5.place(x=widthL, y=height2, anchor='n')

theory_button = tk.Button(root, text='Theory', command=theory_show, width=30, height=1, bg='yellow', font=("Arial", 20))
theory_button.pack(pady=30)
theory_button.place(x=widthM, y=height3, anchor='n')

end_button = tk.Button(root, text="End", command=end_function, width=30, height=1, bg="red", font=("Arial", 20))
end_button.pack(pady=30)
end_button.place(x=widthM, y=height4, anchor='n')

root.attributes('-fullscreen', True)
root.mainloop()
