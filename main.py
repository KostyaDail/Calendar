from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import locale
import calendar
from datetime import datetime as dt

root = Tk()
root.geometry("980x600+500+200")
root.title("Calendar")
root.iconbitmap("img/calendar_icon.ico")
root.resizable(False, False)
root.config(bg="#B0C4DE")
frame = Frame(root, background="#B0C4DE")
frame.grid()


# функция закрыть программу
def pad_quit():
    answer = messagebox.askyesno(title="Выход", message="Закрыть программу?")
    if answer:
        root.destroy()


# функция окно о программе
def about_program():
    messagebox.showinfo(title="Программа", message="Календарь")


# Local
def change_local(local):
    locale.setlocale(locale.LC_ALL, t_local[local])
    for day in range(7):
        lb_d = Label(frame, text=calendar.day_abbr[day], width=2, height=2, font="Verdana 16 bold", fg="darkblue",
                     background="#B0C4DE")
        lb_d.grid(row=2, column=day + 1, sticky=NSEW)
    text = "Вернуть" if local == 'Ru' else "Return"
    f_ret = Button(frame, text=text, font="Verdana 9 bold", fg="black", background="black", command=return_fill)
    f_ret["border"] = 1
    f_ret["bg"] = "#ceb8db"
    f_ret.grid(row=0, column=1, ipadx=0, ipady=0, padx=0, pady=20, sticky=NSEW)
    fill()


def press_back():
    global month, year
    month -= 1
    if month == 0:
        month = 12
        year -= 1
    fill()


def press_forward():
    global month, year
    month += 1
    if month == 13:
        month = 1
        year += 1
    fill()


def return_fill():
    global month, year
    current_datetime = dt.now()
    month = current_datetime.month
    year = current_datetime.year
    fill()


def fill():
    data_label['text'] = f"{calendar.month_name[month]}, {str(year)}"
    month_days = calendar.monthrange(year, month)[1]
    if month == 1:
        back_month_days = calendar.monthrange(year - 1, 12)[1]
    else:
        back_month_days = calendar.monthrange(year, month - 1)[1]
    week_day = calendar.monthrange(year, month)[0]

    for d in range(month_days + 1):
        days[d + week_day]["text"] = d + 1
        days[d + week_day]["fg"] = "black"

        if year == now.year and month == now.month and d == now.day:
            days[d + week_day - 1]["bg"] = "#00FF00"
            days[d + week_day]["bg"] = "#4682B4"
            if d + week_day in (5, 6, 12, 13, 19, 20, 26, 27, 33, 34):
                days[d + week_day]["bg"] = "#FF0000"

        else:
            days[d + week_day]["bg"] = "#4682B4"
            if d + week_day in (5, 6, 12, 13, 19, 20, 26, 27, 33, 34):
                days[d + week_day]["bg"] = "#FF0000"

    for d in range(week_day):
        days[week_day - d - 1]["text"] = back_month_days - d
        days[week_day - d - 1]["fg"] = "#C0C0C0"
        days[week_day - d - 1]["bg"] = "#E0FFFF"

    for d in range(6 * 7 - month_days - week_day):
        days[week_day + month_days + d]["text"] = d + 1
        days[week_day + month_days + d]["fg"] = "#C0C0C0"
        days[week_day + month_days + d]["bg"] = "#E0FFFF"


# Menu
main_menu = Menu(root)
root.config(menu=main_menu)

file_menu = Menu(main_menu, tearoff=0)
file_menu.add_command(label="О программе", command=about_program)
file_menu.add_separator()
file_menu.add_command(label="Выход", command=pad_quit)
main_menu.add_cascade(label="Файл", menu=file_menu)

# Menu local
theme_menu = Menu(main_menu, tearoff=0)
theme_menu_sub = Menu(theme_menu, tearoff=0)
theme_menu_sub.add_command(label="Rus", command=lambda: change_local("Ru"))
theme_menu_sub.add_command(label="Eng", command=lambda: change_local("Eng"))
theme_menu.add_cascade(label="Оформление", menu=theme_menu_sub)
main_menu.add_cascade(label="Local (Локаль)", menu=theme_menu)

t_local = {
    "Ru": "ru_RU.UTF-8",
    "Eng": "en_US"
}
# Button back
left_frame = Frame(frame, border=5, background="#B0C4DE")
left_frame.grid(row=0, column=0, padx=80)
img_but = "img/back.png"
img_but_back = Image.open(img_but)
img_photo = ImageTk.PhotoImage(img_but_back)
back_but = Button(left_frame, image=img_photo, command=press_back)
back_but["border"] = "0"
back_but["bg"] = "#B0C4DE"
back_but.grid(row=0, column=4, sticky=NSEW)

# Button forward
right_frame = Frame(frame, border=5, background="#B0C4DE")
right_frame.grid(row=0, column=8, padx=80)
img_but_f = "img/up.png"
img_but_fr = Image.open(img_but_f)
img_photo_fr = ImageTk.PhotoImage(img_but_fr)
f_but = Button(right_frame, image=img_photo_fr, command=press_forward)
f_but["border"] = 0
f_but["bg"] = "#B0C4DE"
f_but.grid(row=0, column=8, ipadx=0, ipady=0, padx=0, pady=0, sticky=NSEW)

# Button return
f_ret = Button(frame, text="Вернуть", font="Verdana 9 bold", fg="black", background="black", command=return_fill)
f_ret["border"] = 1
f_ret["bg"] = "#ceb8db"
f_ret.grid(row=0, column=1, ipadx=0, ipady=0, padx=0, pady=20, sticky=NSEW)

# Calendar
locale.setlocale(locale.LC_ALL, 'Russian_Russia')
now = dt.now()
days = []
month = now.month
year = now.year
data_label = Label(frame, text="0", width=1, font="Verdana 30 bold", fg="#3725a4", background="#B0C4DE")
data_label.grid(row=0, column=2, columnspan=6, sticky=NSEW)

# days of the week
for day in range(7):
    lb_d = Label(frame, text=calendar.day_abbr[day], width=2, height=2, font="Verdana 16 bold", fg="darkblue",
                 background="#B0C4DE")
    lb_d.grid(row=2, column=day + 1, sticky=NSEW)

# days
for row in range(6):
    for col in range(7):
        lb_d = Label(frame, text="0", width=4, height=2, font="Verdana 16 bold", background="#B0C4DE")
        lb_d.grid(row=row + 3, column=col + 1, sticky=NSEW)
        days.append(lb_d)
fill()

if __name__ == '__main__':
    root.mainloop()
