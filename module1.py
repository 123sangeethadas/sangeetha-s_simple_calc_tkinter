from tkinter import *

window=Tk()
window.geometry("400x400")
window.title("CALCULATOR")
window.configure(bg="grey")



def click(num):
    equation.set(equation.get() + str(num))

def equals():
  try:
    result=(eval(equation.get()))
    equation.set(result)

  except:
    equation.set('ERROR')

def clr():
   value =" "
   equation.set(value)





#add images of buttons
btn_7=PhotoImage(file=r"C:\Users\CHITHRA\Desktop\btn_7.png")
btn_8=PhotoImage(file=r"C:\Users\CHITHRA\Desktop\btn_8.png")
btn_9=PhotoImage(file=r"C:\Users\CHITHRA\Desktop\btn_9.png")
btn_division=PhotoImage(file=r"C:\Users\CHITHRA\Desktop\btn_division.png")
btn_4=PhotoImage(file=r"C:\Users\CHITHRA\Desktop\btn_4.png")
btn_5=PhotoImage(file=r"C:\Users\CHITHRA\Desktop\btn_5.png")
btn_6=PhotoImage(file=r"C:\Users\CHITHRA\Desktop\btn_6.png")
btn_multiplication=PhotoImage(file=r"C:\Users\CHITHRA\Desktop\btn_multiplication.png")
btn_1=PhotoImage(file=r"C:\Users\CHITHRA\Desktop\btn_1.png")
btn_2=PhotoImage(file=r"C:\Users\CHITHRA\Desktop\btn_2.png")
btn_3=PhotoImage(file=r"C:\Users\CHITHRA\Desktop\btn_3.png")
btn_minus=PhotoImage(file=r"C:\Users\CHITHRA\Desktop\btn_minus.png")
btn_0=PhotoImage(file=r"C:\Users\CHITHRA\Desktop\btn_0.png")
btn_decimal=PhotoImage(file=r"C:\Users\CHITHRA\Desktop\btn_decimal.png")
btn_add=PhotoImage(file=r"C:\Users\CHITHRA\Desktop\btn_add.png")
btn_equal=PhotoImage(file=r"C:\Users\CHITHRA\Desktop\btn_equal.png")






equation=StringVar()
#create input area
input_area=Entry(window,
                 width=20, textvariable=equation,font=("arial 24"),justify='right').place(x=20,y=20)




#create buttons
button7=Button(window,
               image=btn_7,border=0,command=lambda :click(7)).place(x=40,y=100)
button8=Button(window,
               image=btn_8,border=0,command=lambda :click(8)).place(x=120,y=100)
button9=Button(window,
               image=btn_9,border=0,command=lambda :click(9)).place(x=200,y=100)
button_division=Button(window,
                      image=btn_division,border=0,command=lambda :click('/')).place(x=280,y=100)
button4=Button(window,
               image=btn_4,border=0,command=lambda :click(4)).place(x=40,y=170)
button5=Button(window,
               image=btn_5,border=0,command=lambda :click(5)).place(x=120,y=170)
button6=Button(window,
               image=btn_6,border=0,command=lambda :click(6)).place(x=200,y=170)
button_multiplication=Button(window,
                             image=btn_multiplication,border=0,command=lambda :click('*')).place(x=280,y=170)
button1=Button(window,
               image=btn_1,border=0,command=lambda :click(1)).place(x=40,y=240)
button2=Button(window,
               image=btn_2,border=0,command=lambda :click(2)).place(x=120,y=240)
button3=Button(window,
               image=btn_3,border=0,command=lambda :click(3)).place(x=200,y=240)
button_minus=Button(window,
               image=btn_minus,border=0,command=lambda :click('-')).place(x=280,y=240)
button_0=Button(window,
               image=btn_0,border=0,command=lambda :click(0)).place(x=40,y=310)
button_decimal=Button(window,
               image=btn_decimal,border=0,command=lambda :click('.')).place(x=120,y=310)
button_add=Button(window,
               image=btn_add,border=0,command=lambda :click('+')).place(x=200,y=310)
button_equal=Button(window,
               image=btn_equal,border=0,command=equals).place(x=280,y=310)
button_clr=Button(window,
                  width=7,height=0,text='clear',font=("arial 9 bold"),command=clr).place(x=280,y=70)







window.mainloop()