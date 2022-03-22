from tkinter import *


def slider_changed(event):
    print(hours_slider.get())


if __name__ == '__main__':
    root = Tk()
    root.geometry("300x100")
    root.title("Counter")
    root.resizable(False, False)
    hour_label = Label(root,
                       text="00:",
                       font=("Courier", 10))
    hour_label.grid(column=0, row=0)

    minute_label = Label(root,
                         text="00:",
                         font=("Courier", 10))
    minute_label.grid(column=1, row=0)

    second_label = Label(root,
                         text="00",
                         font=("Courier", 10))
    second_label.grid(column=2, row=0)

    hours_slider = Scale(root,
                         from_=0,
                         to=60,
                         orient=HORIZONTAL,
                         command=slider_changed)
    hours_slider.grid(column=3, row=0)

    root.mainloop()
