''' Намалюйте UML діаграми класів для вашої останньої домашньої роботи "Персональний помічник" з минулого курсу.
 Для роботи можете скористатися безкоштовним draw.io або будь-яким іншим зручним для вас додатком.
Ваш домашня робота зараз працює в консольному режимі та взаємодіє з користувачем у вигляді команд в консолі.
 Модифікуйте код вашого застосунку, щоб подання інформації користувачу (виведення карток з контактами користувача, сторінка з інформацією про доступні команди) було легко змінити.
   Для цього треба описати абстрактний базовий клас для користувальницьких уявлень та конкретні реалізації, які успадковують базовий клас та реалізують консольний інтерфейс.  
'''
from abc import ABC, abstractmethod

class UserView(ABC):
    """Abstract base class for user views."""
    
    @abstractmethod
    def show_info(self):
        """Display information to the user."""
        pass

    @abstractmethod
    def show_commands(self):
        """Display available commands to the user."""
        pass

class ConsoleView(UserView):
    """Console-based user view implementation."""
    
    def show_info(self):
        print("Welcome to the assistant bot!")

    def show_commands(self):
        print("Available commands:")
        print("add - Add a contact")
        print("change - Change contact information")
        print("phone - Show phone information")
        print("delete - Delete a contact")
        print("all - Show all contacts")
        print("add-birthday - Add or change a contact's birthday")
        print("show-birthday - Show a contact's birthday")
        print("birthdays - Show upcoming birthdays")
        print("exit - Close the program")
def main():
    """Main function"""
    view = ConsoleView()
    view.show_info()

    print("How can I help you?")
    view.show_commands()

    # Продовження з рештою логіки програми

if __name__ == "__main__":
    main()

''' Тепер у програмі є абстрактний базовий клас UserView, який визначає два абстрактних методи: show_info та show_commands.
 Клас ConsoleView успадковує цей базовий клас і реалізує ці методи для взаємодії з користувачем через консольний інтерфейс.
  Це дозволяє легко змінювати представлення інформації користувачу та доступних команд, додавши нові реалізації для інших інтерфейсів, наприклад, графічного.
'''
   
