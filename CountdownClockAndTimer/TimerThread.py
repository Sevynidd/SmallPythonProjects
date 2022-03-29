import datetime


def countdown(MainApp):
    totalSeconds = int(datetime.timedelta(hours=int(MainApp.ClockHours.get()),
                                          minutes=int(MainApp.ClockMinutes.get()),
                                          seconds=int(MainApp.ClockSeconds.get())).total_seconds())
    while not totalSeconds == 0:
        totalSeconds -= 1

        time = str(datetime.timedelta(seconds=totalSeconds))
        h, m, s = time.split(":")
        MainApp.ClockHours.set(h)
        MainApp.ClockMinutes.set(m)
        MainApp.ClockSeconds.set(s)
