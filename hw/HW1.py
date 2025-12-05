class GameCharacter:
    """
    Класс, представляющий игрового персонажа .
    """
    def __init__(self, name, character_class, element, level=1):
        """
        Инициализация атрибутов имени, класса, стихии и уровня персонажа.
        """
        self.name = name
        self.character_class = character_class
        self.element = element
        self.level = level
        self.health = level * 100  # Здоровье зависит от уровня

    def level_up(self, levels_gained=1):
        """
        Метод для повышения уровня персонажа.
        """
        self.level += levels_gained
        self.health = self.level * 100
        print(f"{self.name} повысил уровень до {self.level}! Здоровье обновлено до {self.health}.")

    def perform_attack(self, target_name):
        """
        Метод для выполнения атаки с учетом стихии.
        """
        print(f"{self.name} ({self.character_class}) атакует {target_name} с помощью магии {self.element}!")

    def display_stats(self):
        """
        Метод для вывода полной статистики персонажа.
        """
        print(f"--- Статистика Персонажа ---")
        print(f"Имя: {self.name}")
        print(f"Класс: {self.character_class}")
        print(f"Стихия: {self.element}")
        print(f"Уровень: {self.level}")
        print(f"Здоровье: {self.health}")
        print(f"----------------------------\n")



# 1. Первый персонаж (Воин Огня)
hero_warrior = GameCharacter(name="Арагорн", character_class="Воин", element="Огонь")

# 2. второй персонаж (Маг Льда)
hero_mage = GameCharacter(name="Гендальф", character_class="Маг", element="Лед", level=10)

# 3. третий персонаж (Разбойник Земли)
hero_rogue = GameCharacter(name="Леголас", character_class="Разбойник", element="Земля")

print("--- Работа с Воином (Арагорн) ---")
hero_warrior.display_stats()
hero_warrior.perform_attack("Орк")
hero_warrior.level_up()
hero_warrior.display_stats()

print("\n--- Работа с Магом (Гендальф) ---")
hero_mage.display_stats()
hero_mage.perform_attack("Дракон")
hero_mage.level_up(levels_gained=2)

print("\n--- Работа с Разбойником (Леголас) ---")
hero_rogue.display_stats()
hero_rogue.perform_attack("Гоблин")
hero_rogue.level_up()
