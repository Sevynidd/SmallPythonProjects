import datetime
import time as t


def countdown(MainApp):
    totalSeconds = int(datetime.timedelta(hours=int(MainApp.ClockHours["text"]),
                                          minutes=int(MainApp.ClockMinutes["text"]),
                                          seconds=int(MainApp.ClockSeconds["text"])).total_seconds())
    while not totalSeconds == 0:
        totalSeconds -= 1

        time = str(datetime.timedelta(seconds=totalSeconds))
        h, m, s = time.split(":")
        if len(h) == 1:
            MainApp.ClockHours["text"] = "0" + h
        else:
            MainApp.ClockHours["text"] = h
        MainApp.ClockMinutes["text"] = m
        MainApp.ClockSeconds["text"] = s

        t.sleep(1)

    MainApp.buttonStart["state"] = "normal"
    MainApp.entryHours["state"] = "normal"
    MainApp.entryMinutes["state"] = "normal"
    MainApp.entrySeconds["state"] = "normal"

    MainApp.sv_hours = MainApp.entryHours["text"] if (len(MainApp.entryHours["text"]) > 1) else ("0" + MainApp.entryHours["text"])
    MainApp.sv_minutes = MainApp.entryMinutes["text"] if (len(MainApp.entryMinutes["text"]) > 1) else ("0" + MainApp.entryMinutes["text"])
    MainApp.sv_seconds = MainApp.entrySeconds["text"] if (len(MainApp.entrySeconds["text"]) > 1) else ("0" + MainApp.entrySeconds["text"])
