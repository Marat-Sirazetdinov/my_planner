from datetime import datetime
class Event:
    """
    Класс для хранения деталей события.
    """
    def __init__(self, date_str: str, time_str: str, description: str):
        """
        Базовый конструктор класса.

        :param date_str: Дата события в формате строки
        :param time_str: Время события в формате строки
        :param description: Описание события
        """
        self.date_str = date_str
        self.time_str = time_str
        self.dt = datetime.strptime(f"{date_str} {time_str}", "%d.%m.%Y %H:%M")
        self.description = description

    def __repr__(self):
        """Возвращает строковое представление события."""
        return f"[{self.dt.strftime('%d.%m.%Y %H:%M')}] {self.description}"

    def __eq__(self, other):
        """
        Проверяет равенство текущего события с другим объектом.

        :param other: Объект для сравнения
        :return: True, если события идентичны, иначе False
        """
        return isinstance(other, Event) and self.dt == other.dt and self.description == other.description

    def __hash__(self):
        """Возвращает хеш-значение события."""
        return hash((self.dt, self.description))