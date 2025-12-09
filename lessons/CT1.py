
class Hero:
    def __init__(self, name, lvl, hp):
        self.name = name
        self.lvl = lvl
        self.hp = hp

    def action(self):

        print(f"{self.name} готов к бою!")

    def __str__(self):

        return f"{self.name} (Уровень: {self.lvl}, HP: {self.hp})"

class MageHero(Hero):
    def __init__(self, name, lvl, hp, mp):

        super().__init__(name, lvl, hp)
        self.mp = mp

    def action(self):

        print(f"Маг {self.name} кастует заклинание! MP: {self.mp}")


class WarriorHero(MageHero):
    def __init__(self, name, lvl, hp):

        super().__init__(name, lvl, hp, mp=0)

    def action(self):

        print(f"Воин {self.name} рубит мечом! Уровень: {self.lvl}")


class BankAccount:
    def __init__(self, hero_obj, bank_name, initial_balance, password):
        self.hero = hero_obj
        self.bank_name = bank_name
        self._balance = initial_balance
        self.__password = password

    def login(self, password):

        if password == self.__password:
            print(f"Вход в аккаунт {self.bank_name} выполнен успешно.")
            return True
        else:
            print("Неверный пароль.")
            return False

    @property
    def full_info(self):

        return (f"Банк {self.bank_name} | Владелец: {self.hero.name} | Баланс: {self._balance}")

    def get_bank_name(self):
        return self.bank_name

    def bonus_for_level(self):
        return self.hero.lvl * 10


print("--- Демонстрация 3 условий ООП ---")


satoru = MageHero(name="Сатору", lvl=20, hp=150, mp=500)
sukuna = WarriorHero(name="Сукуна", lvl=25, hp=400)

print("\n--- 1 & 2: Герои и Наследование/Полиморфизм ---")
satoru.action()
sukuna.action()


acc_sukuna = BankAccount(hero_obj=sukuna, bank_name="Curse Bank", initial_balance=5000, password="ryomen")

print("\n--- 3: Инкапсуляция и Свойства ---")
print(acc_sukuna.full_info)
acc_sukuna.login("wrong_password")
acc_sukuna.login("ryomen")
print(f"Бонус за уровень для {acc_sukuna.hero.name}: {acc_sukuna.bonus_for_level()} монет")
