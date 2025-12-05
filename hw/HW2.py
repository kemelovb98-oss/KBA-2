class MythicalAnimal:
    def __init__(self, name, age, health):
        self.name = name
        self.age = age
        self.health = health


    def display_info(self):
        print(f"Имя: {self.name}, Возраст: {self.age}, Здоровье: {self.health}")

    def special_ability(self):
        return f"{self.name} не имеет уникальной способности."


class Fenrir(MythicalAnimal):

    def __init__(self, name, age, health):
        super().__init__(name, age, health)
        self.is_bound = True 

    def special_ability(self):
        if self.is_bound:
            self.is_bound = False
            return f"{self.name} Он разрывает свои оковы!"
        else:
            return f"{self.name} уже свободен."


class Jormungandr(MythicalAnimal):

    def __init__(self, name, age, health):
        super().__init__(name, age, health)
        self.coiled_around_world = True

    def special_ability(self):
        if self.coiled_around_world:
            return f"{self.name} выпускает яд в мировые воды! Нанес урон всему живому."
        else:
            return f"{self.name} идет битва с Тором."


class Huginn(MythicalAnimal):

    def __init__(self, name, age, health):
        super().__init__(name, age, health)
        self.has_knowledge = False

    def special_ability(self):
        if not self.has_knowledge:
            self.has_knowledge = True
            return f"{self.name} собирает тайные знания для Всеотца Одина."
        else:
            return f"{self.name} уже возвращается."


print("--- Скандинавский Пантеон Животных ---")

fenrir_wolf = Fenrir("Фенрир", 4500, 8000)
jormungandr_serpent = Jormungandr("Ёрмунганд", 5000, 10000)
huginn_raven = Huginn("Хугин", 3000, 100)

animals = [fenrir_wolf, jormungandr_serpent, huginn_raven]

for animal in animals:
    animal.display_info()
    print(f"-> {animal.special_ability()}")
    print("-" * 40)
