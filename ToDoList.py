import tkinter as tk


root = tk.Tk()

root.title("To-Do List")
root.geometry("500x600")
root.resizable(False, False)


title = tk.Label(
    root,
    text="TO-DO LIST",
    font=("Arial", 30, "bold")
)
title.place(x=135, y=30)


add_task_text = tk.Label(
    root,
    text="Добавьте задачу!",
    font=("Arial", 18, "bold")
)
add_task_text.place(x=25, y=120)


entry = tk.Entry(
    root,
    font=("Arial", 14),
    bd=0,
    relief="flat"
)
entry.place(x=25, y=175)


task_y = 230


def add_task():
    global task_y

    task = entry.get()
    entry.delete(0, tk.END)

    task_label = tk.Label(
        root,
        text=task,
        font=("Arial", 14)
    )
    task_label.place(x=25, y=task_y)

    task_y += 35


add_task_button = tk.Button(
    root,
    text="Добавить заметку",
    font=("Arial", 14),
    relief="flat",
    command=add_task
)
add_task_button.place(x=300, y=165)


root.mainloop()

