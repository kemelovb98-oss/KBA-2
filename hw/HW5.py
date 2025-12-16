
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
