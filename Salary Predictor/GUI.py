# model use ----> GUI
from tkinter import *
from tkinter.messagebox import *
from pickle import *

root = Tk()
root.title("Salary Predictor By Aryan")
root.geometry("500x400+50+50")
f = ("Century", 30, "bold")

def predict():
	try:
		exp = float(ent_exp.get())
		f = open("sal.pkl", "rb")
		model = load(f)
		f.close()
		sal = model.predict([[exp]])
		msg = "salary = " + str(round(sal[0], 2)) + "K"
		showinfo("Msg", msg)	
	except ValueError:
		showerror("Issue", "u shud enter numbers only")
		ent_exp.delete(0,END)
		ent_exp.focus()	

lab_title = Label(root, font=f, text="Salary Predictor")
lab_exp = Label(root, text = "Enter exp", font=f)
ent_exp = Entry(root, font=f)
btn_predict = Button(root, text="Predict Salary", font=f, command=predict)

lab_title.pack(pady=5)
lab_exp.pack(pady=5)
ent_exp.pack(pady=5)
btn_predict.pack(pady=5)

root.mainloop()