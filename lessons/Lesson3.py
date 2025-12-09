from abc import ABC, abstractmethod

# ----------------------------------------------------
# 1. Базовый класс Hero
# ----------------------------------------------------
class Hero:
    def __init__(self, name, lvl, hp):
        self.name = name
        self.lvl = lvl
        self.hp = hp
    def action(self):
        print(f"{self.name} готов к бою!")
    def __str__(self):
        return f"{self.name} (Уровень: {self.lvl}, HP: {self.hp})"

# ----------------------------------------------------
# 2. Дочерние классы (MageHero и WarriorHero)
# ----------------------------------------------------
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

# ----------------------------------------------------
# 3. Класс BankAccount (Инкапсуляция и свойства)
# ----------------------------------------------------
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

# ----------------------------------------------------
# 5. Абстрактный класс SmsService (Абстракция)
# ----------------------------------------------------
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


# ====================================================
# ИТОГОВЫЙ ВЫВОД ПРОГРАММЫ (По вашему примеру, с новыми именами)
# ====================================================

# 1. Создаем героев с нужными именами/уровнями (Сатору - маг, Сукуна - воин)
satoru_hero = MageHero(name="Satoru", lvl=50, hp=100, mp=150)
sukuna_hero = WarriorHero(name="Sukuna", lvl=50, hp=200)

# 2. Выводим их действия
satoru_hero.action()
sukuna_hero.action()

# 3. Создаем счета с нужными балансами и названием банка
# Для демонстрации равенства, создадим два счета для Сатору
acc_satoru_1 = BankAccount(hero_obj=satoru_hero, bank_name="Simba", initial_balance=5000, password="p1")
acc_satoru_2 = BankAccount(hero_obj=satoru_hero, bank_name="Simba", initial_balance=3000, password="p2")
acc_sukuna = BankAccount(hero_obj=sukuna_hero, bank_name="Simba", initial_balance=1000, password="p3")

# 4. Выводим информацию о счетах через __str__
print(acc_satoru_1)
print(acc_satoru_2)

# 5. Выводим название банка и бонус
print(f"Банк: {acc_satoru_1.get_bank_name()}")
print(f"Бонус за уровень: {acc_satoru_1.bonus_for_level()} SOM")

# 6. Демонстрация __add__
try:
    combined_account = acc_satoru_1 + acc_satoru_2
    print(f"\nСумма счетов двух магов: {combined_account._balance}")
except TypeError as e:
    print(f"\nОшибка: {e}")

try:
    acc_satoru_1 + acc_sukuna # Эта строка вызовет ошибку, как в вашем примере
except TypeError as e:
    print(f"Ошибка: {e}")

# 7. Демонстрация __eq__
print(f"\nMage1 == Mage2 ? {acc_satoru_1 == acc_satoru_2}") # True, т.к. герой один и тот же
print(f"Mage1 == Warrior ? {acc_satoru_1 == acc_sukuna}")   # False, разные герои

# 8. Демонстрация SmsService
kg_service = KGSms()
print(kg_service.send_otp('+996777123456'))
