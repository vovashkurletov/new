from tkinter import *
import sqlite3 as sql
n=[]
def run():
    root=Tk()
    root.geometry('300x200')
    def getreg():
        xc='vk'
        con = sql.connect(xc+'.db')
        with con:
            cur = con.cursor()
            cur.execute("CREATE TABLE IF NOT EXISTS vk (id text, name text, sur text)")
            name = en.get()
            cur.execute("SELECT id FROM `vk`")
            rows = cur.fetchall()       
            if len(rows)==0: k='0'
            else:
                k=int(''.join(rows[-1]))+1
            cur.execute("SELECT name FROM `vk`")
            rows = cur.fetchall() 
            for i in rows:
                if ''.join(i)==name:
                    lb.configure(text='Это имя уже занято')
                    break
            else:
                passw = en1.get()
                cur.execute(f"INSERT INTO vk(id,name,sur) VALUES ('{k}','{name}', '{passw}')")
                lb.configure(text='Успешно!')
            con.commit()
            cur.close()
    lb = Label(root)
    en = Entry(root)
    en1 = Entry(root)
    btn = Button(root,text='Зарегистрироваться',command=getreg,padx=30,pady=10)
    lb.pack()
    en.pack()
    en1.pack()
    btn.pack()
def run2():
    root=Tk()
    root.geometry('300x200')
    def getprov():
        con = sql.connect('vk.db')
        
        with con:
            cur = con.cursor()
            o=0
            cur.execute("SELECT name FROM `vk`")
            rows = cur.fetchall()
            name = en.get()
            s=0
            n.append(name)
            print(n)
            for i in rows:
                if ''.join(i)==name:
                    s=5
            for row in rows:
                o+=1
                if name == ''.join(row):   
                    cur.execute("SELECT sur FROM `vk`")
                    rows = cur.fetchall()
                    passw = en1.get() 
                    if passw == ''.join(rows[o-1]):
                        lb.configure(text='Хорошо. Пароль верный!')
                        chats(name)
                        break
                    else: 
                        lb.configure(text='Ошибка. Пароль неверный!')
                        break
            if s==0:
                lb.configure(text='Нет такого пользователя!')
            
            
            con.commit()
            cur.close()

    lb = Label(root)
    en = Entry(root)
    en1 = Entry(root)
    btn = Button(root,text='Войти',command=getprov,padx=30,pady=10)
    lb.pack()
    en.pack()
    en1.pack()
    btn.pack()
    root.mainloop()
def run3():
    root=Tk()
    root.geometry('300x200')
    con = sql.connect('vk.db')
    def go():    
        with con:
            cur = con.cursor()
            cur.execute("SELECT id FROM `vk`")
            ig = cur.fetchall()
            cur.execute("SELECT name FROM `vk`")
            rows = cur.fetchall()
            s=''
            h=0
            l=0
            for i in rows:
                    lb = Label(root,text=''.join(i))
                    lb.grid(column=0,row=l)
                    l+=1
            for i in ig:
                    lb = Label(root,text=''.join(i))
                    lb.grid(column=1,row=h)
                    h+=1
            con.commit()
            cur.close()
    go()
    root.mainloop()
def chats(name):
    root=Tk()
    root.geometry('300x200')          
    scrollbar = Scrollbar(root)
    scrollbar.pack(side=RIGHT, fill=Y)
    mylist = Listbox(root, yscrollcommand=scrollbar.set)
    mylist.pack(side=TOP, fill=BOTH)
    scrollbar.config(command=mylist.yview)
    en = Entry(root)
    en.place(relx=.05,rely=.88)

    con = sql.connect('mesi.db')
    with con:
        cur = con.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS mesi (mes text)")
        cur.execute("SELECT mes FROM `mesi`")
        rows = cur.fetchall()
        print(rows)
        if len(rows)==0: mylist.insert(END,'WELCOME TO vk!')
        else:
            cur.execute("SELECT mes FROM `mesi`")
            rows = cur.fetchall()
            for i in rows:
                mylist.insert(END,''.join(i))
        con.commit()
        cur.close()
              
    def otpr():
        con = sql.connect('mesi.db')
        with con:
            cur = con.cursor()
            a = en.get()
            #b=mylist.get(ACTIVE)
            mylist.insert(END,n[-1]+'   '+a) 
            a=n[0]+'   '+a
            print(a)
            cur.execute(f"INSERT INTO mesi VALUES ('{a}')")
            con.commit()
            cur.close()
        en.delete(0,END)
            
        
    bt=Button(root,text='ОТПРАВИТЬ',command=otpr)
    bt.place(relx=.5,rely=.86)
    
     
    root.mainloop()

root=Tk()
root.geometry('300x200')
lab=Label(root,text='chatroom',font="Arial 14" )
lab.pack()
btn = Button(root,text='Войти',command=run2,padx=30,pady=10)
btn.place(relx=.05,rely=.3)
btn1 = Button(root,text='Зарегистрироваться',command=run,pady=10,padx=30)
btn1.place(relx=.4,rely=.3)
btn1 = Button(root,text='Пользователи',command=run3,pady=10,padx=30)
btn1.place(relx=.05,rely=.55)
root.mainloop()