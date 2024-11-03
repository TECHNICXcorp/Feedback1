from tkinter import *
import pickle 

root1 = Tk()
root1.title("Feedback")
root1.geometry("300x400")
root1.resizable(width=False,height=False)
root1['bg']="#3C3C3C"

Lab1=Label(text="Оберіть свій варіант",font="Vernada 15",bg="#3C3C3C",fg="white")
Lab1.place(x=50,y=30)

Butt2=Button(width=20,text="я клієнт",font="Vernada 15",bg="#282828",fg="white",relief=FLAT,overrelief=GROOVE)
Butt2.place(x=35,y=200)

Butt1=Button(width=20,text="я надаю послуги",font="Vernada 15",bg="#282828",fg="white",relief=FLAT,overrelief=GROOVE)
Butt1.place(x=35,y=250)

def c():
    Butt1= root2 = Tk()
    root2.title("Registration feedback")
    root2.geometry("500x500") 
    root2.resizable(width=False,height=False)
    root2['bg'] = "#3C3C3C"

    l1=Label(root2,text="Вітаємо в додатку!", font="Vernada 17" , fg="white")
    l1.place(x=145,y=7)
    l1['bg']="#3C3C3C"

    l2=Label(root2,text="Для того щоб продовжити необхідно зареєструватись.", font="Vernada 13" , fg="white")
    l2.place(x=35,y=40)
    l2['bg']="#3C3C3C"

    l3=Label(root2,text="Ключ доступу" , font="Vernada 15" , fg="white")
    l3.place(x=175,y=70)
    l3['bg']="#3C3C3C"
    
    
    e1=Entry(root2,width=53,font="Vernada 13",justify=CENTER,foreground="#3C3C3C")
    e1.place(x=8,y=105)
    e1.insert(0,"")
    e1['bg']= "white"
    e1.get()

    l4=Label(root2,text="Ваш email" , font="Vernada 15" , fg="white")
    l4.place(x=190,y=135)
    l4['bg']="#3C3C3C"

    e2=Entry(root2,width=53 , font="Vernada 13",justify=RIGHT,foreground="#3C3C3C")
    e2.place(x=8,y=170)
    e2.insert(0,"@gmail  ")
    e2['bg']= "white"
    e2.get()

    l4=Label(root2,text="Ваше П.І.Б." , font="Vernada 15" , fg="white")
    l4.place(x=187,y=200)
    l4['bg']="#3C3C3C"

    e3=Entry(root2,width=53 , font="Vernada 13",justify=CENTER,foreground="#3C3C3C")
    e3.place(x=8,y=235)
    e3.insert(0,"")
    e3['bg']= "white"
    e3.get()
    
    l5=Label(root2,text="Назва компанії" , font="Vernada 15" , fg="white")
    l5.place(x=173,y=270)
    l5['bg']="#3C3C3C"

    e4=Entry(root2,width=53 , font="Vernada 13",justify=CENTER,foreground="#3C3C3C")
    e4.place(x=8,y=305)
    e4.insert(0,"")
    e4['bg']= "white"
    e4.get()

    b1 = Button(root2,text="готово", font="Vernada 15" ,foreground="white",relief=FLAT,overrelief=GROOVE)
    b1['bg']="#282828"
    b1.place(x=205,y=355)

    #main window
    
    
    def reg():
        b1=root3 = Tk()
        root3.title("feedback host")
        root3.geometry("940x750")
        root3.resizable(width=False , height=False)
        root3['bg'] = "#3C3C3C"

        hd1=Button(root3,text="Кабінет",font="Vernada 19",bg="#282828",fg="white", relief=FLAT,overrelief=GROOVE)
        hd1.place(x=0,y=0)

        hd2=Button(root3,text="Наряди",font="Vernada 19",bg="#282828",fg="white", relief=FLAT,overrelief=GROOVE)
        hd2.place(x=111,y=0)

        hd3=Button(root3,text="Рахунки",font="Vernada 19",bg="#282828",fg="white", relief=FLAT,overrelief=GROOVE)
        hd3.place(x=223,y=0)

        hd4=Button(root3,text="Клієнти",font="Vernada 19",bg="#282828",fg="white", relief=FLAT,overrelief=GROOVE)
        hd4.place(x=339,y=0)

        hd5=Button(root3,text="Робітники",font="Vernada 19",bg="#282828",fg="white", relief=FLAT,overrelief=GROOVE)
        hd5.place(x=450,y=0)

        hd6=Button(root3,text="Історія СТО",font="Vernada 19",bg="#282828",fg="white", relief=FLAT,overrelief=GROOVE)
        hd6.place(x=588,y=0)

        hd7=Button(root3,text="Налаштування",font="Vernada 19",bg="#282828",fg="white", relief=FLAT,overrelief=GROOVE)
        hd7.place(x=747,y=0)

        c1=Label(root3,text="")

        #Cabinet

        def f():
            c1=Label(root3,text=" Ім'я користувача :",font="Vernada 19",bg="#3C3C3C",fg="white")
            c1.place(x=0,y=80)
            c1=Label(root3,text="1",font="Vernada 19",bg="#3C3C3C",fg="white")
            c1.place(x=210,y=80)
            c1=Label(root3,text=" Назва Компанії :",font="Vernada 19",bg="#3C3C3C",fg="white")
            c1.place(x=0,y=120)
            c1=Label(root3,text="1",font="Vernada 19",bg="#3C3C3C",fg="white")
            c1.place(x=195,y=120)
            c1=Label(root3,text=" Працівників компанії :",font="Vernada 19",bg="#3C3C3C",fg="white")
            c1.place(x=0,y=160)
            c1=Label(root3,text="1",font="Vernada 19",bg="#3C3C3C",fg="white")
            c1.place(x=269,y=160)
            
            bt1=Button(width=30,text="Назначити працівника",font="Vernada 19",bg="#282828",fg="white", relief=FLAT,overrelief=GROOVE)
            bt1.place(x=8,y=220)
            
            bt2=Button(width=30,text="Відкрити наряд",font="Vernada 19",bg="#282828",fg="white", relief=FLAT,overrelief=GROOVE)
            bt2.place(x=8,y=285)
            
            bt3=Button(width=30,text="Відкрити рахунок",font="Vernada 19",bg="#282828",fg="white", relief=FLAT,overrelief=GROOVE)
            bt3.place(x=8,y=350)

        hd1.config(command=f)
        
        root2.destroy()
                   
        root3.mainloop()  
    
    b1.config(command=reg)     

    root1.destroy()
    
    root2.mainloop()

Butt1.config(command=c)

root1.mainloop()

