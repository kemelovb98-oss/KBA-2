from abc import ABC, abstractmethod

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
        return password == self.__password
    @property
    def full_info(self):
        return (f"Банк {self.bank_name} | Владелец: {self.hero.name} | Баланс: {self._balance}")
    def get_bank_name(self):
        return self.bank_name
    def bonus_for_level(self):
        return self.hero.lvl * 10
    def __str__(self):
        return f"{self.hero.name} | Баланс: {self._balance} SOM"
    def __add__(self, other):
        if type(self.hero) == type(other.hero):
            new_balance = self._balance + other._balance
            return BankAccount(self.hero, self.bank_name, new_balance, self.__password)
        else:
            raise TypeError("Нельзя сложить счета героев разных классов!")
    def __eq__(self, other):
        return self.hero.name == other.hero.name and self.hero.lvl == other.hero.lvl


class SmsService(ABC):
    @abstractmethod
    def send_otp(self, phone):
        pass

class KGSms(SmsService):
    def send_otp(self, phone):
        return f"<text>Код: 1234</text><phone>{phone}</phone>"

class RUSms(SmsService):
    def send_otp(self, phone):
        return {"text": "Код: 1234", "phone": phone}





satoru_hero = MageHero(name="Satoru", lvl=50, hp=100, mp=150)
sukuna_hero = WarriorHero(name="Sukuna", lvl=50, hp=200)


satoru_hero.action()
sukuna_hero.action()


acc_satoru_1 = BankAccount(hero_obj=satoru_hero, bank_name="Simba", initial_balance=5000, password="p1")
acc_satoru_2 = BankAccount(hero_obj=satoru_hero, bank_name="Simba", initial_balance=3000, password="p2")
acc_sukuna = BankAccount(hero_obj=sukuna_hero, bank_name="Simba", initial_balance=1000, password="p3")


print(acc_satoru_1)
print(acc_satoru_2)


print(f"Банк: {acc_satoru_1.get_bank_name()}")
print(f"Бонус за уровень: {acc_satoru_1.bonus_for_level()} SOM")


try:
    combined_account = acc_satoru_1 + acc_satoru_2
    print(f"\nСумма счетов двух магов: {combined_account._balance}")
except TypeError as e:
    print(f"\nОшибка: {e}")

try:
    acc_satoru_1 + acc_sukuna
except TypeError as e:
    print(f"Ошибка: {e}")


print(f"\nMage1 == Mage2 ? {acc_satoru_1 == acc_satoru_2}")
print(f"Mage1 == Warrior ? {acc_satoru_1 == acc_sukuna}")


kg_service = KGSms()
print(kg_service.send_otp('+996777123456'))
