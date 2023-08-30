import tkinter as tk

def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(number))

def button_clear():
    entry.delete(0, tk.END)

def button_equal():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

root = tk.Tk()
root.title("G")

entry = tk.Entry(root, width=20, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4)

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('+', 4, 3),
]

for button_text, row, col in buttons:
    tk.Button(root, text=button_text, padx=15, pady=10,
              command=lambda text=button_text: handle_button_click(text)).grid(row=row, column=col)

def handle_button_click(text):
    if text == '=':
        button_equal()
    elif text == 'C':
        button_clear()
    else:
        button_click(text)

root.mainloop()
