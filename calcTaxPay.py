import time
import datetime
import tkinter as tk


def tax():
    try:
        pay_hour = float(entry_pay_hour.get())
        week_hour = float(entry_week_hour.get())

        if week_hour > 40:
            pay = (40 * pay_hour) + ((week_hour - 40) * pay_hour * 1.5)
        else:
            pay = pay_hour * week_hour

        tax_amount = pay * 0.1
        final_pay = pay - tax_amount

        label.config(text=f"Your total pay with tax deduction is ${final_pay:.2f}", fg="green")  # Format output
    except ValueError:
        label.config(text="Invalid input. Please enter numbers.", fg="red")

def clear():
    entry_pay_hour.delete(0, tk.END)
    entry_week_hour.delete(0, tk.END)
    label.config(text="")

root = tk.Tk()

entry_pay_hour = tk.Entry(root, fg="red", bg="yellow")
entry_pay_hour.pack()

entry_week_hour = tk.Entry(root, fg="red", bg="yellow")
entry_week_hour.pack()

button = tk.Button(root, text="Tax",command=tax)
button.pack()

but_clear = tk.Button(root, text="Clear", fg="red", bg="blue", command=clear)
but_clear.pack()


time_label = tk.Label(root, text=datetime.datetime.now())
time_label.pack()

label = tk.Label(root)
label.pack()



root.mainloop()