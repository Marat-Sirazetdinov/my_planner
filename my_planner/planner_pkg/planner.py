from datetime import datetime

class Planner:
    """
    Класс для управления списком событий и напоминаний.
    """
    def __init__(self):
        """Инициализация пустого планировщика."""
        self.events = []
        self.reminders = {}

    def add_event(self, event):
        """
         Добавляет новое событие в систему.

        :param event: Объект класса Event
        :return: Кортеж (статус успеха, информационное сообщение)
        """
        if self.check_duplicates(event):
            return False, "Дубликат события уже существует!"
        self.events.append(event)
        self.reminders[event] = []
        return True, "Событие успешно добавлено."

    def add_reminder(self, event_idx, reminder):
        """
        Устанавливает напоминание для конкретного события.

        :param event_idx: Индекс события в списке
        :param reminder: Объект класса Reminder
        :return: True, если индекс верен и напоминание добавлено
        """
        if 0 <= event_idx < len(self.events):
            event = self.events[event_idx]
            self.reminders[event].append(reminder)
            return True
        return False

    def remove_event(self, index):
        """
        Удаляет событие и все его напоминания.

         :param index: Индекс удаляемого события
         :return: True, если удаление прошло успешно
        """
        if 0 <= index < len(self.events):
            event = self.events.pop(index)
            del self.reminders[event]
            return True
        return False

    def check_duplicates(self, event):
        """
        Проверяет наличие дубликатов события.

        :param event: Объект Event для проверки
        :return: True, если событие уже существует в списке
        """
        return any(e == event for e in self.events)

    def get_upcoming(self):
        """
        Возвращает текущий список событий.

        :return: Список объектов Event
         """
        return sorted([e for e in self.events if e.dt > datetime.now()], key=lambda x: x.dt)