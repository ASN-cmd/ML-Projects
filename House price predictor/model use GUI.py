# model use GUI

from tkinter import *
from tkinter.messagebox import * 
from pickle import *

root = Tk()
root.title("House Price Predictor")
root.geometry("700x600+50+50")
f = ("Centruy", 35, "bold")



def find():
	try:
		area = float(ent_area.get())
		bedrooms = float(ent_bedroom.get())
		f1 = open("hpp.pkl", "rb")
		model = load(f1)
		f1.close()
		price = model.predict([[area, bedrooms]])
		msg = "price " + str(round(price[0], 2)) + "crs"
		showinfo("Msg", msg)
	except ValueError:
		showerror("Issue", "u shud enter numbers only")
		ent_area.delete(0,END)
		ent_bedroom.delete(0,END)
		ent_area.focus()	


lab_area = Label(root, font=f, text="Enter Area ")
ent_area = Entry(root, font=f)
lab_bedroom = Label(root, font=f, text="Enter Bedrooms ")
ent_bedroom = Entry(root, font=f)
btn_predict = Button(root, font=f, text="Submit", command=find)

lab_area.pack(pady=5)
ent_area.pack(pady=5)
lab_bedroom.pack(pady=5)
ent_bedroom.pack(pady=5)
btn_predict.pack(pady=5)
root.mainloop()