from tkinter import Tk, Canvas
from datetime import date, datetime
from dotenv import load_dotenv
import os

load_dotenv()
EVENTS_FILE = os.getenv("EVENTS_FILE")

def get_events():
    events = []
    with open(EVENTS_FILE) as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            name, date_str = line.split(",")
            date = datetime.strptime(date_str, "%d/%m/%y").date()
            events.append((name, date))
    return events

def days_between_dates(date1, date2):
    return (date1 - date2).days

root = Tk()
root.title("Countdown Calendar")

canvas = Canvas(root, width=800, height=800, bg="black")
canvas.pack()

canvas.create_text(
    250, 40,
    text="Countdown calendar",
    fill="blue",
    font=("Arial", 24, "bold")
)

events = get_events()
today = date.today()

y_position = 100

for days, events in events:
    days_left = days_between_dates(events, today)

    if days_left > 0:
        display_text = f"{days}: {days_left} days left"
    elif days_left == 0:
        display_text = f"{days}: Today"
    else:
        display_text = f"{days}: Passed"

    canvas.create_text(
        50, y_position,
        anchor="w",
        text=display_text,
        fill="orange",
        font=("Arial", 16)
    )

    y_position += 30

root.mainloop()
