# The python file must be imported as rtplotter, just rename rt-plotter into the corresponding one.

import rtplotter
import tkinter as tk

window = tk.Tk()
window.geometry("400x180")
window.configure(bg="#F8CFFF")
window.title("Reference Triangle Plotter")

# image = tk.PhotoImage(file="jiggly.gif")

# canvas = tk.Canvas(window, width=image.width(), height=image.height())
# canvas.pack(fill="both", expand=True)
# canvas.create_image(0, 0, anchor="nw", image=image)

# gradient_frame = tk.Frame(window, bg="#D3D3D3")
# gradient_frame.pack(fill="both", expand=True)

# canvas = tk.Canvas(gradient_frame, width=500, height=300)
# canvas.pack(fill="both", expand=True)

# gradient = canvas.create_rectangle(0, 0, 500, 300, fill="#0000FF")
# canvas.create_rectangle(0, 300, 500, 600, fill="#FF0000")
# canvas.lower(gradient)

# gradient = canvas.create_rectangle(0, 0, 500, 300, fill="#00FF00")
# canvas.create_rectangle(500, 0, 1000, 300, fill="#FFFF00")
# canvas.lower(gradient)

# frame = tk.Frame(window)
# frame.pack(fill="both", expand=True)
# frame.place(x=0, y=0, width=500, height=300)

def run_function():
    dms = (deg_entry.get(), min_entry.get(), sec_entry.get())
    val = dmsdeg(*dms)
    rtplotter(trig_func.get(), val)

deg_label = tk.Label(text="Degrees:", bg="#F8CFFF")
deg_label.pack()
deg_entry = tk.Entry(bg="#D3D3D3")
deg_entry.pack()

def deg_entry_change(event):
    if deg_entry.get().isnumeric():
        deg_entry.configure(bg="#22FFC3")
    else:
        deg_entry.configure(bg="#FF225E")
deg_entry.bind("<KeyRelease>", deg_entry_change)

min_label = tk.Label(text="Minutes:", bg="#F8CFFF")
min_label.pack()
min_entry = tk.Entry(bg="#D3D3D3")
min_entry.pack()

def min_entry_change(event):
    if min_entry.get().isnumeric():
        min_entry.configure(bg="#22FFC3")
    else:
        min_entry.configure(bg="#FF225E")
min_entry.bind("<KeyRelease>", min_entry_change)

sec_label = tk.Label(text="Seconds:", bg="#F8CFFF")
sec_label.pack()
sec_entry = tk.Entry(bg="#D3D3D3")
sec_entry.pack()

def sec_entry_change(event):
    if sec_entry.get().isnumeric():
        sec_entry.configure(bg="#22FFC3")
    else:
        sec_entry.configure(bg="#FF225E")
sec_entry.bind("<KeyRelease>", sec_entry_change)

trig_func = tk.StringVar(window)
trig_func.set("Function Select")
func_menu = tk.OptionMenu(window, trig_func, "sin", "cos", "tan", "sec", "csc", "cot")
func_menu["menu"].configure(bg="#CFF8FF")
func_menu.pack()

button = tk.Button(text="Run Function", command=run_function, bg="#CFF8FF")
button.pack()

window.mainloop()

if __name__=="__main__":
    main()

