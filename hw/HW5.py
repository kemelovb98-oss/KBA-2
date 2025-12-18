
PERMISSIONS = {
    "admin": ["start", "ban", "stop"],
    "user": ["start", "message"]
}



def check_permission(command_name):
    def decorator(func):
        def wrapper(self, user, *args, **kwargs):

            allowed_commands = PERMISSIONS.get(user.role, [])

            if command_name in allowed_commands:

                return func(self, user, *args, **kwargs)
            else:

                print(f"❌ Пользователь {user.username} не может выполнять команду \"{command_name}\"")

        return wrapper

    return decorator


# 1️⃣ Класс User
class User:
    def __init__(self, username, role):
        self.username = username
        self.role = role


    @classmethod
    def create_admin(cls, name):
        """Фабричный метод для быстрого создания админа"""
        return cls(name, "admin")


# 4️⃣ Класс CommandHandler
class CommandHandler:

    @check_permission("start")
    def start(self, user):
        print(f"✅ Команда \"start\" выполнена пользователем {user.username}")

    @check_permission("ban")
    def ban(self, user):
        print(f"✅ Пользователь {user.username} (admin) выполнил команду BAN")

    @check_permission("stop")
    def stop(self, user):
        print(f"✅ Команда \"stop\" выполнена пользователем {user.username}")

    @check_permission("message")
    def message(self, user):
        print(f"✅ Пользователь {user.username} отправил сообщение")


    @staticmethod
    def system_info():
        print("--- Система команд v1.0 (Access Control System) ---")


# 5️⃣ Демонстрация работы
if __name__ == "__main__":

    admin_user = User("Alice", "admin")
    regular_user = User("Bob", "user")

    handler = CommandHandler()


    CommandHandler.system_info()
    print()


    print(f"--- Действия {admin_user.username} ({admin_user.role}) ---")
    handler.start(admin_user)
    handler.ban(admin_user)
    print()


    print(f"--- Действия {regular_user.username} ({regular_user.role}) ---")
    handler.start(regular_user)
    handler.ban(regular_user)  # Должно выдать ошибку
    handler.message(regular_user)


# #Задача 2
# import datetime
#
# def security_audit(func):
#     def wrapper(*args, **kwargs):
#         current_time = datetime.datetime.now().strftime("%H:%M:%S")
#         print(f"--- [AUDIT] Вызов {func.__name__} в {current_time} ---")
#         return func(*args, **kwargs)
#     return wrapper
#
# class GameServer:
#     server_brand = "CyberArena"
#     active_connections = 0
#
#     def __init__(self, player_name, level=1):
#         self.player_name = player_name
#         self.level = level
#         GameServer._register_connection()
#
#     @security_audit
#     def upgrade_level(self, points):
#         self.level += points
#         print(f"🎮 Игрок {self.player_name} повысил уровень до {self.level}")
#
#     @security_audit
#     def reset_progress(self):
#         self.level = 1
#         print(f"⚠️ Прогресс игрока {self.player_name} был сброшен")
#
#     @classmethod
#     def update_brand(cls, new_name):
#         old_name = cls.server_brand
#         cls.server_brand = new_name
#         print(f"🌐 Сервер '{old_name}' переименован в '{new_name}'")
#
#     @classmethod
#     def _register_connection(cls):
#         cls.active_connections += 1
#
#     @staticmethod
#     def get_server_rules():
#         return "Правила: 1. Не читерить. 2. Уважать других игроков."
#
# # Демонстрация
# print(GameServer.get_server_rules())
#
# p1 = GameServer("Maximus", 10)
# p2 = GameServer("SniperElite", 25)
#
# p1.upgrade_level(5)
# p2.reset_progress()
#
# GameServer.update_brand("UltraNet")
#
# print(f"Текущий бренд: {p1.server_brand}")
# print(f"Всего подключений: {GameServer.active_connections}")
