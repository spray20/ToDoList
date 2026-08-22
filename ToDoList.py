import tkinter as tk


root = tk.Tk()         #Создание окна
root.title("To-Do List")
root.geometry("500x600")
root.resizable(False, False)
root.title("To-Do List")


title = tk.Label(      #Создание заголовка
    root,
    text="TO-DO LIST",
    font=("Arial", 30, "bold", )
)
title.place(x=135,y=30)


add_task_text = tk.Label(    #Создание надписи, которая говорит пользователю, что делать
    root,
    text="Добавьте задачу!",
    font=("Arial", 18, "bold", )
)
add_task_text.place(x=25,y=120)


entry = tk.Entry(    #Создание Entry поля
    root,
    font=("Arial", 14),
     #insertbackground="white",
    bd=0,
    relief="flat"
)
entry.place(x=25,y=175)


def add_task():  #Функция для удалиния написанного после нажатия кнопки
    task = entry.get()       
    entry.delete(0, tk.END)


add_task_button = tk.Button(        #Создание кнопки "Добавить заметку"
    root,
    text="Добавить заметку",
    font=("Arial", 14),
    relief="flat",
    command=add_task
)
add_task_button.place(x=300,y=165)


def add_task():
    task = entry.get()       
    entry.delete(0, tk.END)

    label = tk.Label(root, text=task)
    label.pack()


    









root.mainloop()



