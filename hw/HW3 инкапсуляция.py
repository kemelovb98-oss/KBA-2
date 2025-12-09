class Product:
    def __init__(self, name, price):
        self.name = name                # Публичный атрибут: название продукта
        self._base_price = price       # Защищенный атрибут: базовая цена без скидок
        self.__discount = 0             # Приватный атрибут: текущий размер скидки в процентах (от 0 до 50)
        self.__secret_code = "VIP123"   # Приватный атрибут: секретный код для доп. скидки

    def get_price(self):
        """Возвращает финальную цену с учетом скидки."""
        final_amount = self._base_price * (1 - self.__discount / 100)
        return round(final_amount, 2)

    def set_discount(self, percent):
        """Устанавливает скидку, если процент не превышает 50%."""
        if 0 <= percent <= 50:
            self.__discount = percent
            print(f"Скидка установлена на {percent}%.")
        else:
            print("Ошибка: Скидка должна быть в диапазоне от 0% до 50%.")

    def apply_extra_discount(self, code_input):
        """Применяет дополнительную скидку 5%, если введен верный код."""
        if code_input == self.__secret_code:
            # Проверяем, не превысим ли лимит в 50%
            if self.__discount + 5 <= 50:
                 self.__discount += 5
                 print("Секретный код верен. Применена доп. скидка 5%.")
            else:
                 self.__discount = 50
                 print("Секретный код верен. Достигнут максимальный лимит скидки (50%).")
        else:
            print("Неверный код")



item = Product("T-Shirt", 50.00)

print(f"Название: {item.name}")
print(f"Базовая цена: ${item._base_price}")
print(f"Текущая цена: ${item.get_price()}")

item.set_discount(15)
print(f"Цена после установки скидки 15%: ${item.get_price()}")

item.apply_extra_discount("GUEST") # Неверный код
item.apply_extra_discount("VIP123") # Верный код
print(f"Финальная цена после доп. скидки: ${item.get_price()}")
