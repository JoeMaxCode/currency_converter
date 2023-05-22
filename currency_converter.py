import tkinter as tk

# Initializing Tkinter screen
win = tk.Tk()
win.geometry("800x500")
win.title("Currency Converter")
title = tk.Label(win, text="Currency Converter", font=("Ariel", 25))
title.place(anchor="center", relx=.5, rely=.2)

def check_valid(curr):
	s_entry.delete(first=0, last=20)
	
	if curr1.get() == '' or curr2.get() == '':
		label.config(text='A CURRENCY HAS YET TO BE SELECTED')
	elif curr1.get() == curr2.get():
		label.config(text='BOTH CURRENCIES ARE THE SAME')
	else:
		try:
			int(f_entry.get())
			label.config(text="TRANSFER COMPLETE")
			currency_exchange(curr)
		except ValueError:
			label.config(text="NOT A VALID ENTRY")

def currency_exchange(rates):
	usrInput = int(f_entry.get())
	base_curr = curr1.get()
	to_curr = curr2.get()
	output = 0.0 
	if base_curr != "US Dollar" or to_curr != "US Dollar":
		output = usrInput/rates[base_curr]
		output = output * rates[to_curr]
	else:
		if base_curr == "US Dollar":
			output = usrInput * rates[to_curr]
		else:
			output = usrInput / rates[to_curr]

	output = float(f"{output:.2f}")
	s_entry.insert(0, f"{output:,}")

currencies = [
"US Dollar",
"Japanese Yen",
"Canadian Dollar",
"Australian Dollar",
"Cuban Peso"
]

# This program treat US Dollar as the base/standard currency
rates_dict = {
	"US Dollar": 1,
	"Japanese Yen": 137.97,
	"Canadian Dollar": 1.35,
	"Australian Dollar": 1.50,
	"Cuban Peso": 23.94
}

""" FIRST CURRENCY SLOT """
curr1 = tk.StringVar()
first_curr = tk.OptionMenu(win, curr1, *currencies)
first_curr.place(anchor='center', relx=.3, rely=.5)

f_entry = tk.Entry(win, font=('Ariel', 17))
f_entry.place(anchor='center', relx=.3, rely=.65)

""" SECOND CURRENCY SLOT """
curr2 = tk.StringVar()
second_curr = tk.OptionMenu(win, curr2, *currencies)
second_curr.place(anchor='center', relx=.7, rely=.5)

s_entry = tk.Entry(win, font=('Ariel', 17))
s_entry.place(anchor='center', relx=.7, rely=.65)

# Convert Button
button = tk.Button(win, text="Convert", command=lambda:check_valid(rates_dict))
button.place(anchor='center', relx=.5, rely=.85)

label = tk.Label(win, text='')
label.place(anchor='center', relx=.5, rely=.77)

win.mainloop()