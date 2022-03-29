import pathlib
import pygubu
import tkinter as tk
import tkinter.ttk as ttk


PROJECT_PATH = pathlib.Path(__file__).parent
PROJECT_UI = PROJECT_PATH / "main.ui"


def start_button():
    print("startbutton")


def stop_button():
    print("stopButton")


class MainApp:
    def __init__(self, master=None):
        # build ui
        self.mainwindow = tk.Tk() if master is None else tk.Toplevel(master)
        self.ClockHours = ttk.Label(self.mainwindow)
        self.ClockHours.configure(anchor='center', cursor='arrow', font='{Bahnschrift} 20 {}', justify='right')
        self.ClockHours.configure(text='00')
        self.ClockHours.place(anchor='e', x='170', y='40')
        self.ClockMinutes = ttk.Label(self.mainwindow)
        self.ClockMinutes.configure(anchor='center', cursor='arrow', font='{Bahnschrift} 20 {}', justify='right')
        self.ClockMinutes.configure(text='00')
        self.ClockMinutes.place(anchor='center', x='200', y='40')
        self.ClockSeconds = ttk.Label(self.mainwindow)
        self.ClockSeconds.configure(anchor='center', cursor='arrow', font='{Bahnschrift} 20 {}', justify='right')
        self.ClockSeconds.configure(text='00')
        self.ClockSeconds.place(anchor='center', x='240', y='40')
        self.Doppelpunkt1 = ttk.Label(self.mainwindow)
        self.Doppelpunkt1.configure(anchor='center', cursor='arrow', font='{Bahnschrift} 20 {}', justify='right')
        self.Doppelpunkt1.configure(text=':')
        self.Doppelpunkt1.place(anchor='center', x='180', y='38')
        self.Doppelpunkt2 = ttk.Label(self.mainwindow)
        self.Doppelpunkt2.configure(anchor='center', cursor='arrow', font='{Bahnschrift} 20 {}', justify='right')
        self.Doppelpunkt2.configure(text=':')
        self.Doppelpunkt2.place(anchor='center', x='220', y='38')

        self.labelHours = ttk.Label(self.mainwindow)
        self.labelHours.configure(font='{bahnschrift} 10 {}', text='Hours:')
        self.labelHours.place(anchor='center', x='150', y='80')
        self.labelMinutes = ttk.Label(self.mainwindow)
        self.labelMinutes.configure(font='{bahnschrift} 10 {}', text='Minutes:')
        self.labelMinutes.place(anchor='center', x='150', y='110')
        self.labelSeconds = ttk.Label(self.mainwindow)
        self.labelSeconds.configure(font='{bahnschrift} 10 {}', text='Seconds:')
        self.labelSeconds.place(anchor='center', x='150', y='140')

        self.buttonStart = ttk.Button(self.mainwindow)
        self.buttonStart.configure(compound='top', text='Start')
        self.buttonStart.place(anchor='center', x='140', y='180')
        self.buttonStart.configure(command=start_button)
        self.buttonStart.bind('<1>', self.callback, add='')
        self.buttonStop = ttk.Button(self.mainwindow)
        self.buttonStop.configure(text='Stop')
        self.buttonStop.place(anchor='center', x='240', y='180')
        self.buttonStop.configure(command=stop_button)
        self.buttonStop.bind('<1>', self.callback, add='')

        self.sv_hours = tk.StringVar()
        self.sv_hours.trace_add("write", self.entry_callback_hours)
        self.sv_minutes = tk.StringVar()
        self.sv_minutes.trace_add("write", self.entry_callback_minutes)
        self.sv_seconds = tk.StringVar()
        self.sv_seconds.trace_add("write", self.entry_callback_seconds)

        self.entryHours = ttk.Entry(self.mainwindow, textvariable=self.sv_hours)
        self.entryHours.configure(font='{bahnschrift} 10 {}', width='4')
        _text_ = '''0'''
        self.entryHours.delete('0', 'end')
        self.entryHours.insert('0', _text_)
        self.entryHours.place(anchor='center', x='230', y='80')

        self.entryMinutes = ttk.Entry(self.mainwindow,
                                      textvariable=self.sv_minutes)
        self.entryMinutes.configure(font='{bahnschrift} 10 {}', width='4')
        _text_ = '''0'''
        self.entryMinutes.delete('0', 'end')
        self.entryMinutes.insert('0', _text_)
        self.entryMinutes.place(anchor='center', x='230', y='110')

        self.entrySeconds = ttk.Entry(self.mainwindow,
                                      textvariable=self.sv_seconds)
        self.entrySeconds.configure(font='{bahnschrift} 10 {}', width='4')
        _text_ = '''0'''
        self.entrySeconds.delete('0', 'end')
        self.entrySeconds.insert('0', _text_)
        self.entrySeconds.place(anchor='center', x='230', y='140')

        self.mainwindow.configure(height='250', width='400')
        self.mainwindow.resizable(True, True)
        self.mainwindow.title('Hello World App')

        # Main widget
        self.mainwindow = self.mainwindow

    def run(self):
        self.mainwindow.mainloop()

    def callback(self, event=None):
        pass

    def entry_callback_hours(self, var, index, mode):
        if not self.sv_hours.get() == '':
            if not self.sv_hours.get().isnumeric():
                self.sv_hours.set(self.sv_hours.get()[:len(self.sv_hours.get()) - 1])
            else:
                self.ClockHours["text"] = self.sv_hours.get()
        else:
            self.ClockHours["text"] = "0"

    def entry_callback_minutes(self, var, index, mode):
        if not self.sv_minutes.get() == '':
            if not self.sv_minutes.get().isnumeric():
                self.sv_minutes.set(self.sv_minutes.get()[:len(self.sv_minutes.get()) - 1])
            else:
                if int(self.sv_minutes.get()) > 60:
                    self.sv_minutes.set(str(60))
                self.ClockMinutes["text"] = self.sv_minutes.get()
        else:
            self.ClockMinutes["text"] = "0"

    def entry_callback_seconds(self, var, index, mode):
        if not self.sv_seconds.get() == '':
            if not self.sv_seconds.get().isnumeric():
                self.sv_seconds.set(self.sv_seconds.get()[:len(self.sv_seconds.get()) - 1])
            else:
                if int(self.sv_seconds.get()) > 60:
                    self.sv_seconds.set(str(60))
                self.ClockSeconds["text"] = self.sv_seconds.get()
        else:
            self.ClockSeconds["text"] = "0"
