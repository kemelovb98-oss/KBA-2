class Hero:

 def __init__(self, name, lvl, hp):
    # атрибуты класса
    self.name = name
    self.lvl = lvl
    self.hp = hp
 def base_action(self):
     return f"base action {self.name}"
# объект/экземпляр на основе класса
kirito = Hero("kirito", 100,1000)
Asuno = Hero("asuno",101,1001)
# print(kirito.lvl
#       )
# print(Asuno.name)

print(Asuno.base_action())
