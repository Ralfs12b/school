import tkinter as tk
from tkinter import ttk 

# Tiek veidots tkinker sākuma logs

root = tk.Tk()
root.title("Ātruma kalkulātors")
root.geometry('680x400')
root.resizable(False, False) # nevar mainīt window lielumu

# Programmas nosaukums
tk.Label(root, text="Ātruma kalkulātors", font=(
    "Helvetica", 18, "bold"), fg="black").pack()

message = tk.Label(root, text="Sveicināts, šeit būs fizikas formula: S = d/t") # raksts lai sasveicinātos ar lietotāju
message.pack()


ievadteksts = tk.Label(root, text="Ievadiet laiku")
ievadteksts.pack(pady=10)
ievade = tk.Entry(root)
ievade.pack(pady=10)

ievadteksts2 = tk.Label(root, text="Ievadiet distanci")
ievadteksts2.pack(pady=10)
ievade2 = tk.Entry(root)
ievade2.pack(pady=10)




def error():
   messagebox.showerror('Python Error', 'Error: This is an Error Message!')

def m():
    d = ievadteksts2
    t = ievadteksts
    d/t



  
poga = tk.Button(root, text="Ātrums ir",command= m)
poga.pack(pady=10)




# Iziešanas poga 
exit_button = ttk.Button(
    root,
    text='Iziet',
    command=lambda: root.quit()
)

exit_button.pack(
    ipadx=5,
    ipady=5,
    expand=True
)

root.mainloop()  # saka lai python ieslēdz tkinter 