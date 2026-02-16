class Reminder:
    def __init__(self, minutes: int):
        self.minutes = minutes

    def __repr__(self):
        return f"Напомнить за {self.minutes} мин."