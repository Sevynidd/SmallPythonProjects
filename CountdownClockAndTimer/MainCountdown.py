import pathlib
import pygubu
import tkinter as tk
import tkinter.ttk as ttk

PROJECT_PATH = pathlib.Path(__file__).parent
PROJECT_UI = PROJECT_PATH / "main.ui"


class MainApp:
    def __init__(self, master=None):
        # build ui
        self.mainwindow = tk.Tk() if master is None else tk.Toplevel(master)
        self.Clock = ttk.Label(self.mainwindow)
        self.Clock.configure(anchor='center', font='{Bahnschrift} 20 {}', justify='right', text='00:00:00')
        self.Clock.place(anchor='center', x='200', y='40')
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
        self.buttonStart.configure(text='Start')
        self.buttonStart.place(anchor='center', x='140', y='180')
        self.buttonStop = ttk.Button(self.mainwindow)
        self.buttonStop.configure(text='Stop')
        self.buttonStop.place(anchor='center', x='240', y='180')
        self.entryHours = ttk.Entry(self.mainwindow)
        self.entryHours.configure(font='{bahnschrift} 10 {}', width='4')
        _text_ = '''0'''
        self.entryHours.delete('0', 'end')
        self.entryHours.insert('0', _text_)
        self.entryHours.place(anchor='center', x='230', y='80')
        self.entryMinutes = ttk.Entry(self.mainwindow)
        self.entryMinutes.configure(font='{bahnschrift} 10 {}', width='4')
        _text_ = '''0'''
        self.entryMinutes.delete('0', 'end')
        self.entryMinutes.insert('0', _text_)
        self.entryMinutes.place(anchor='center', x='230', y='110')
        self.entrySeconds = ttk.Entry(self.mainwindow)
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


if __name__ == '__main__':
    app = MainApp()
    app.run()


