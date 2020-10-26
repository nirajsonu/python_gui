from tkinter import *
from tkinter.messagebox import *
window=Tk()
window.title('my calculator')
window.geometry('450x600')
font=('Verdana',22,'italic')

#picture label
pic=PhotoImage(file='calc.png')
h=Label(window,image=pic)
h.pack(side=TOP,pady=15)

#text label
te=Label(window,text='My Calcuator',font=font)
te.pack(side=TOP)

#textbox
textfiled=Entry(window,font=font,justify=CENTER,relief='ridge')
textfiled.pack(side=TOP,pady=10,fill=X,padx=10)

#frame
buttonfram=Frame(window)
buttonfram.pack(side=TOP)

#adding button
#bt1=Button(buttonfram,text="1",font=font)
#bt1.grid(row=0,column=0)


#All clear function
def all_clear():
	ex=textfiled.get()
	ex=ex[0:len(ex)-1]
	textfiled.delete(0,END)
	textfiled.insert(0,ex)
	

#clear one by one
def clear():
	textfiled.delete(0,END)


#important function
def click_btn_function(event):
	b=event.widget
	text=b['text']
	print(text)
	if text == '=':
		try:
			ex=textfiled.get()
			answer=eval(ex)
			textfiled.delete(0,END)
			textfiled.insert(0,answer)
		except Exception as e:
			print("error",e)
			showerror("error",e)
		return
	textfiled.insert(END,text)

temp=1
for i in range(0,3):
	for j in range(0,3):
			bt1=Button(buttonfram,text=str(temp),font=font,width=5,relief='ridge',activebackground='orange',activeforeground='white')
			bt1.grid(row=i,column=j,padx=5,pady=5)
			temp=temp+1
			bt1.bind('<Button-1>',click_btn_function)
#zerobtn
zerobtn=Button(buttonfram,text='0',font=font,width=5,relief='ridge',activebackground='orange',activeforeground='white')
zerobtn.grid(row=3,column=0,padx=3,pady=3)

#dotbutton
dotbtn=Button(buttonfram,text='.',font=font,width=5,relief='ridge',activebackground='orange',activeforeground='white')
dotbtn.grid(row=3,column=1,padx=3,pady=3)

#equal buuton
equalbtn=Button(buttonfram,text='=',font=font,width=5,relief='ridge',activebackground='orange',activeforeground='white')
equalbtn.grid(row=3,column=2,padx=3,pady=3)

#plus button
plusbtn=Button(buttonfram,text='+',font=font,width=5,relief='ridge',activebackground='orange',activeforeground='white')
plusbtn.grid(row=0,column=4,padx=3,pady=3)

#minus button
minusbtn=Button(buttonfram,text='-',font=font,width=5,relief='ridge',activebackground='orange',activeforeground='white')
minusbtn.grid(row=1,column=4,padx=3,pady=3)

#multiply button
mulbtn=Button(buttonfram,text='*',font=font,width=5,relief='ridge',activebackground='orange',activeforeground='white')
mulbtn.grid(row=2,column=4,padx=3,pady=3)

#divide button
divdbtn=Button(buttonfram,text='/',font=font,width=5,relief='ridge',activebackground='orange',activeforeground='white')
divdbtn.grid(row=3,column=4,padx=3,pady=3)

#clear button
cleardbtn=Button(buttonfram,text='<--',font=font,width=11,relief='ridge',activebackground='orange',activeforeground='white',command=all_clear)
cleardbtn.grid(row=4,column=0,columnspan=2)

#clearAll button
cleardbtn=Button(buttonfram,text='AC',font=font,width=5,relief='ridge',activebackground='orange',activeforeground='white',command=clear)
cleardbtn.grid(row=4,column=2,columnspan=2)

#bindallbutton
plusbtn.bind('<Button-1>',click_btn_function)
minusbtn.bind('<Button-1>',click_btn_function)
divdbtn.bind('<Button-1>',click_btn_function)
mulbtn.bind('<Button-1>',click_btn_function)
zerobtn.bind('<Button-1>',click_btn_function)
equalbtn.bind('<Button-1>',click_btn_function)
dotbtn.bind('<Button-1>',click_btn_function)


window.mainloop()
