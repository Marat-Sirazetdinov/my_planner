from datetime import datetime

class Planner:
    def __init__(self):
        self.events = []
        self.reminders = {}

    def add_event(self, event):
        if self.check_duplicates(event):
            return False, "Дубликат события уже существует!"
        self.events.append(event)
        self.reminders[event] = []
        return True, "Событие успешно добавлено."

    def add_reminder(self, event_idx, reminder):
        if 0 <= event_idx < len(self.events):
            event = self.events[event_idx]
            self.reminders[event].append(reminder)
            return True
        return False

    def remove_event(self, index):
        if 0 <= index < len(self.events):
            event = self.events.pop(index)
            del self.reminders[event]
            return True
        return False

    def check_duplicates(self, event):
        return any(e == event for e in self.events)

    def get_upcoming(self):
        return sorted([e for e in self.events if e.dt > datetime.now()], key=lambda x: x.dt)