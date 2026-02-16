from datetime import datetime

class Event:
    def __init__(self, date_str: str, time_str: str, description: str):
        self.date_str = date_str
        self.time_str = time_str
        self.dt = datetime.strptime(f"{date_str} {time_str}", "%d.%m.%Y %H:%M")
        self.description = description

    def __repr__(self):
        return f"[{self.dt.strftime('%d.%m.%Y %H:%M')}] {self.description}"

    def __eq__(self, other):
        return isinstance(other, Event) and self.dt == other.dt and self.description == other.description

    def __hash__(self):
        return hash((self.dt, self.description))