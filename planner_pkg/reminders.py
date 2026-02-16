class Reminder:
    """
    Класс для представления настроек напоминания.
    """
    def __init__(self, minutes: int):
        """
        Конструктор настройки времени напоминания.

        :param minutes: Количество минут до начала события
        """
        self.minutes = minutes

    def __repr__(self):
        """Возвращает строковое описание настройки."""
        return f"Напомнить за {self.minutes} мин."