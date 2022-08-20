from tkinter import *
from tkinter import ttk

r = Tk()
r.title("Calculator")



dis_cal = Entry(r,borderwidth=7,bg="lightgrey",font=("Arial",25))
dis_cal.grid(row=0,column=0,columnspan=4,padx=20,pady=40)

def button_click(num):
	dis_cal.insert(END, num)

def button_all_clear():
	dis_cal.delete(0, END)

def btn_cls():
	dis_cal.delete(len(dis_cal.get())-1, END)

def btn_add():
	global math
	global f_num
	number = dis_cal.get()
	f_num = int(number)
	math = 1
	dis_cal.delete(0,END)

def btn_sub():
	global math
	global f_num
	number = dis_cal.get()
	f_num = int(number)
	math = 2
	dis_cal.delete(0,END)

def btn_multiply():
	global math
	global f_num
	number = dis_cal.get()
	f_num = int(number)
	math = 3
	dis_cal.delete(0,END)

def btn_divide():
	global math
	global f_num
	number = dis_cal.get()
	f_num = int(number)
	math = 4
	dis_cal.delete(0,END)



def btn_eq():
	global math
	global f_num
	number = dis_cal.get()
	dis_cal.delete(0, END)
	if math == 1:
		dis_cal.insert(0,f_num + int(number))
	elif math == 2:
		dis_cal.insert(0,f_num - int(number))
	elif math == 3:
		dis_cal.insert(0,f_num * int(number))
	elif math == 4:
		dis_cal.insert(0,f_num / int(number))
	else:
		dis_cal.insert(number)





btn_CE = Button(r,text="CE",padx=87,pady=20,borderwidth=3,command=button_all_clear)

btn_ba = Button(r,text="C",padx=40,pady=20,borderwidth=3,command=btn_cls)
btn_di = Button(r,text="%",padx=38,pady=20,borderwidth=3,command=btn_divide)

btn_7 = Button(r,text="7",padx=40,pady=20,borderwidth=3,command=lambda:button_click(7))
btn_8 = Button(r,text="8",padx=40,pady=20,borderwidth=3,command=lambda:button_click(8))
btn_9 = Button(r,text="9",padx=40,pady=20,borderwidth=3,command=lambda:button_click(9))
btn_x = Button(r,text="x",padx=40,pady=20,borderwidth=3,command=btn_multiply)

btn_4 = Button(r,text="4",padx=40,pady=20,borderwidth=3,command=lambda:button_click(4))
btn_5 = Button(r,text="5",padx=40,pady=20,borderwidth=3,command=lambda:button_click(5))
btn_6 = Button(r,text="6",padx=40,pady=20,borderwidth=3,command=lambda:button_click(6))
btn_s = Button(r,text="-",padx=40,pady=20,borderwidth=3,command=btn_sub)

btn_1 = Button(r,text="1",padx=40,pady=20,borderwidth=3,command=lambda:button_click(1))
btn_2 = Button(r,text="2",padx=40,pady=20,borderwidth=3,command=lambda:button_click(2))
btn_3 = Button(r,text="3",padx=40,pady=20,borderwidth=3,command=lambda:button_click(3))
btn_a = Button(r,text="+",padx=40,pady=20,borderwidth=3,command=btn_add)

btn_0 = Button(r,text="0",padx=90,pady=20,borderwidth=3,command=lambda:button_click(0))
btn_do = Button(r,text=".",padx=40,pady=20,borderwidth=3,command=lambda:button_click("."))
btn_eq = Button(r,text="=",padx=40,pady=20,borderwidth=3,command=btn_eq)

btn_CE.grid(row=1 ,column=0, columnspan=2)
btn_ba.grid(row=1 ,column=2)
btn_di.grid(row=1 ,column=3)

btn_7.grid(row=2 ,column=0)
btn_8.grid(row=2 ,column=1)
btn_9.grid(row=2 ,column=2)
btn_x.grid(row=2 ,column=3)

btn_4.grid(row=3 ,column=0)
btn_5.grid(row=3 ,column=1)
btn_6.grid(row=3 ,column=2)
btn_s.grid(row=3 ,column=3)

btn_1.grid(row=4 ,column=0)
btn_2.grid(row=4 ,column=1)
btn_3.grid(row=4 ,column=2)
btn_a.grid(row=4 ,column=3)

btn_0.grid(row=5 ,column=0,columnspan=2)
btn_do.grid(row=5 ,column=2)
btn_eq.grid(row=5 ,column=3)

r.mainloop()