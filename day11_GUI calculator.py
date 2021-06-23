# Making a calculator using GUI Development using Tkinter
import tkinter as t

app = t.Tk()
app.title('Calculator')
app.geometry('500x600')

result = t.Variable(app)
result.set('Result')
t.Label(app,textvariable = result).place(x=230,y=50)


p=''

def string(h):
    global p
    p+=h
    
    result.set(p)

def ans():
    global p
    result.set(eval(p))
    
def clear():
    global p
    p=''
    result.set(p)

def back():
    global p
    p=p[:-1]
    result.set(p)


t.Button(app,text='1',width='10',command= lambda:string('1')).place(x=30,y=150)
t.Button(app,text='2',width='10',command= lambda:string('2')).place(x=150,y=150)
t.Button(app,text='3',width='10',command= lambda:string('3')).place(x=270,y=150)
t.Button(app,text='+',width='10',command= lambda:string('+')).place(x=390,y=150)   

t.Button(app,text='4',width='10',command= lambda:string('4')).place(x=30,y=250)
t.Button(app,text='5',width='10',command= lambda:string('5')).place(x=150,y=250)
t.Button(app,text='6',width='10',command= lambda:string('6')).place(x=270,y=250)
t.Button(app,text='-',width='10',command= lambda:string('-')).place(x=390,y=250)

t.Button(app,text='7',width='10',command= lambda:string('7')).place(x=30,y=350)
t.Button(app,text='8',width='10',command= lambda:string('8')).place(x=150,y=350)
t.Button(app,text='9',width='10',command= lambda:string('9')).place(x=270,y=350)
t.Button(app,text='*',width='10',command= lambda:string('*')).place(x=390,y=350)

t.Button(app,text='.',width='10',command= lambda:string('.')).place(x=30,y=450)
t.Button(app,text='0',width='10',command= lambda:string('0')).place(x=150,y=450)
t.Button(app,text='/',width='10',command= lambda:string('/')).place(x=270,y=450)
t.Button(app,text='=',width='10',command= lambda:ans()).place(x=390,y=450)

t.Button(app,text='Clear',width='10',command= lambda:clear()).place(x=0,y=0)
t.Button(app,text='Back',width='10',command= lambda:back()).place(x=410,y=0)

app.mainloop()
