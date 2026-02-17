"""
Главный модуль запуска планировщика.
Тег: #PersonalPlanner
Описание: Реализует консольный интерфейс для управления событиями и напоминаниями.
"""

from my_planner import Planner, Reminder, Event

def main():
    """
    Основная функция (главное тело) программы.
    Инициализирует объекты и запускает цикл взаимодействия с пользователем.
    """
    my_planner = Planner()

    while True:
        print("\n--- ПЕРСОНАЛЬНЫЙ ПЛАНИРОВЩИК ---")
        print("1. Добавить событие")
        print("2. Показать ближайшие события")
        print("3. Добавить напоминание")
        print("4. Удалить событие")
        print("0. Выход")

        choice = input("\nВыберите действие: ")

        if choice == "1":
            d = input("Введите дату (ДД.ММ.ГГГГ): ")
            t = input("Введите время (ЧЧ:ММ): ")
            desc = input("Описание: ")
            try:
                new_ev = Event(d, t, desc)
                success, msg = my_planner.add_event(new_ev)
                print(msg)
            except Exception as e:
                print(f"Ошибка формата: {e}")

        elif choice == "2":
            upcoming = my_planner.get_upcoming()
            if not upcoming:
                print("Событий пока нет.")
            for i, ev in enumerate(upcoming):
                rems = my_planner.reminders.get(ev, [])
                print(f"{i}. {ev} | {rems}")

        elif choice == "3":
            if not my_planner.events:
                print("Сначала добавьте событие!")
                continue
            for i, ev in enumerate(my_planner.events):
                print(f"{i}. {ev}")

            try:
                idx = int(input("Введите номер события: "))
                mins = int(input("За сколько минут напомнить?: "))
                if my_planner.add_reminder(idx, Reminder(mins)):
                    print("Напоминание установлено.")
                else:
                    print("Неверный номер.")
            except ValueError:
                print("Ошибка: введите числовое значение.")

        elif choice == "4":
            if not my_planner.events:
                print("Список пуст.")
                continue
            for i, ev in enumerate(my_planner.events):
                print(f"{i}. {ev}")

            try:
                idx = int(input("Введите номер для удаления: "))
                if my_planner.remove_event(idx):
                    print("Удалено.")
                else:
                    print("Ошибка индекса.")
            except ValueError:
                print("Ошибка: введите число.")

        elif choice == "0":
            print("Завершение работы...")
            break

if __name__ == "__main__":
    main()