import tkinter as tk

# Initializing Tkinter screen
win = tk.Tk()
win.geometry("800x500")
win.title("Currency Converter")
title = tk.Label(win, text="Currency Converter", font=("Ariel", 25))
title.place(anchor="center", relx=.5, rely=.2)


def check_valid():
	s_entry.delete(first=0, last=20)
	if curr1.get() == curr2.get():
		label.config(text='BOTH CURRENCIES ARE THE SAME')
	else:
		try:
			int(f_entry.get())
			label.config(text="TRANSFER COMPLETE")
			currency()
		except ValueError:
			label.config(text="NOT A VALID ENTRY")

def currency():
	"""US DOLLAR COMBINATIONS"""
	if curr1.get() == "US Dollar" or curr2.get() == "US Dollar":
		# Canadian Dollar
		if (curr1.get() == "US Dollar" and curr2.get() == "Canadian Dollar" or 
			curr1.get() == "Canadian Dollar" and curr2.get() == "US Dollar") :
			rate = 1.34725
		# Japanese Yen
		elif (curr1.get() == "US Dollar" and curr2.get() == "Japanese Yen" or 
			curr1.get() == "Japanese Yen" and curr2.get() == "US Dollar") :
			rate = 137.083
		# Australian Dollar
		elif (curr1.get() == "US Dollar" and curr2.get() == "Australian Dollar" or 
			curr1.get() == "Australian Dollar" and curr2.get() == "US Dollar") :
			rate = 1.50238
		# Cuban Peso
		elif (curr1.get() == "US Dollar" and curr2.get() == "Cuban Peso" or 
			curr1.get() == "Cuban Peso" and curr2.get() == "US Dollar") :
			rate = 25	

		user_input = int(f_entry.get())
		if curr1.get() == "US Dollar":
			user_input = user_input*rate
			user_input = float(f"{user_input:.2f}")
			s_entry.insert(0, f"{user_input:,}")
		else:
			user_input = user_input/rate
			user_input = float(f"{user_input:.2f}")
			s_entry.insert(0, f"{user_input:,}")

	"""CUBAN PESO COMBINATIONS"""
	if curr1.get() == "Cuban Peso" or curr2.get() == "Cuban Peso":
		# Canadian Dollar
		if (curr1.get() == "Cuban Peso" and curr2.get() == "Canadian Dollar" or 
			curr1.get() == "Canadian Dollar" and curr2.get() == "Cuban Peso") :
			rate = 0.05389
		# Australian Dollar
		if (curr1.get() == "Cuban Peso" and curr2.get() == "Australian Dollar" or 
			curr1.get() == "Australian Dollar" and curr2.get() == "Cuban Peso") :
			rate = 0.0601
		# Japanese Yen
		if (curr1.get() == "Cuban Peso" and curr2.get() == "Japanese Yen" or 
			curr1.get() == "Japanese Yen" and curr2.get() == "Cuban Peso") :
			rate = 5.48334

		user_input = int(f_entry.get())
		if curr1.get() == "Cuban Peso":
			user_input = user_input*rate
			user_input = float(f"{user_input:.2f}")
			s_entry.insert(0, f"{user_input:,}")
		else:
			user_input = user_input/rate
			user_input = float(f"{user_input:.2f}")
			s_entry.insert(0, f"{user_input:,}")

	"""JAPANESE YEN COMBINATIONS"""
	if curr1.get() == "Japanese Yen" or curr2.get() == "Japanese Yen":
		# Canadian Dollar
		if (curr1.get() == "Japanese Yen" and curr2.get() == "Canadian Dollar" or 
			curr1.get() == "Canadian Dollar" and curr2.get() == "Japanese Yen") :
			rate = 0.00983
		# Australian Dollar
		if (curr1.get() == "Japanese Yen" and curr2.get() == "Australian Dollar" or 
			curr1.get() == "Australian Dollar" and curr2.get() == "Japanese Yen") :
			rate = 0.01096

		user_input = int(f_entry.get())
		if curr1.get() == "Japanese Yen":
			user_input = user_input*rate
			user_input = float(f"{user_input:.2f}")
			s_entry.insert(0, f"{user_input:,}")
		else:
			user_input = user_input/rate
			user_input = float(f"{user_input:.2f}")
			s_entry.insert(0, f"{user_input:,}")

	""" AUSTRALIAN COMBINATIONS """
	if curr1.get() == "Australian Dollar" or curr2.get() == "Australian Dollar":
		# Canadian Dollar
		if (curr1.get() == "Australian Dollar" and curr2.get() == "Canadian Dollar" or 
			curr1.get() == "Canadian Dollar" and curr2.get() == "Australian Dollar") :
			rate = 0.89655

		user_input = int(f_entry.get())
		if curr1.get() == "Australian Dollar":
			user_input = user_input*rate
			user_input = float(f"{user_input:.2f}")
			s_entry.insert(0, f"{user_input:,}")
		else:
			user_input = user_input/rate
			user_input = float(f"{user_input:.2f}")
			s_entry.insert(0, f"{user_input:,}")

	




	

currencies = [
"US Dollar",
"Japanese Yen",
"Canadian Dollar",
"Australian Dollar",
"Cuban Peso"
]

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
button = tk.Button(win, text="Convert", command=check_valid)
button.place(anchor='center', relx=.5, rely=.85)

label = tk.Label(win, text='')
label.place(anchor='center', relx=.5, rely=.77)





win.mainloop()
