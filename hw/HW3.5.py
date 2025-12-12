from abc import ABC, abstractmethod
import json
class SposobOplaty(ABC):
    """
    Базовый шаблон для всех видов оплаты.
    """
    @abstractmethod
    def oplatit(self, summa):
        """Метод оплаты. Тут пока пусто."""
        pass

    @abstractmethod
    def vernut_dengi(self, summa):
        """Метод возврата. Тут тоже пока пусто."""
        pass


class OplataKartoy(SposobOplaty):
    def oplatit(self, summa):
        print(f"Оплата картой: {summa} KGS")

    def vernut_dengi(self, summa):
        print(f"Возврат на карту: {summa} KGS")

class OplataNalichnymi(SposobOplaty):
    def oplatit(self, summa):
        print(f"Оплата наличными: {summa} KGS")

    def vernut_dengi(self, summa):
        print(f"Возврат наличными: {summa} KGS")

class OplataKriptoy(SposobOplaty):
    def oplatit(self, summa):

        otvet = {"type": "crypto", "amount": summa, "currency": "KGS"}
        print(json.dumps(otvet, indent=4, ensure_ascii=False))

    def vernut_dengi(self, summa):
        otvet = {"type": "crypto", "amount": -summa, "currency": "KGS", "status": "возврат"}
        print(json.dumps(otvet, indent=4, ensure_ascii=False))

class ObrabotkaPlatezhey:
    """
    Класс, который умеет работать с ЛЮБЫМ способом оплаты из нашего шаблона.
    """
    def __init__(self, vibor_sposoba: SposobOplaty):
        self.vib_sposob = vibor_sposoba

    def vipolnit_oplatu(self, summa):
        print(f"\nНачинаем оплату через процессор:")

        self.vib_sposob.oplatit(summa)

karta = OplataKartoy()
nalichka = OplataNalichnymi()
kripta = OplataKriptoy()

protsessor_karta = ObrabotkaPlatezhey(karta)
protsessor_nalichka = ObrabotkaPlatezhey(nalichka)
protsessor_kripta = ObrabotkaPlatezhey(kripta)


protsessor_karta.vipolnit_oplatu(2500)
protsessor_nalichka.vipolnit_oplatu(800)
protsessor_kripta.vipolnit_oplatu(120.50)


print("\nПробуем сделать возврат наличными:")
nalichka.vernut_dengi(100)
