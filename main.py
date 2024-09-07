class User:
    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email

    def __str__(self):
        return f"Username: {self.username}, Email: {self.email}"

class UserManager:
    def __init__(self):
        self.users = {}

    def register(self, username, password, email):
        if username in self.users:
            print("Username already exists.")
            return
        self.users[username] = User(username, password, email)
        print("User registered successfully.")

    def login(self, username, password):
        if username not in self.users:
            print("Username does not exist.")
            return
        if self.users[username].password != password:
            print("Incorrect password.")
            return
        print("Login successful.")

    def delete_user(self, username):
        if username not in self.users:
            print("Username does not exist.")
            return
        del self.users[username]
        print("User deleted successfully.")

    def update_user(self, username, new_username=None, new_password=None, new_email=None):
        if username not in self.users:
            print("Username does not exist.")
            return
        if new_username:
            self.users[new_username] = self.users.pop(username)
            self.users[new_username].username = new_username
        if new_password:
            self.users[username].password = new_password
        if new_email:
            self.users[username].email = new_email
        print("User updated successfully.")

    def display_users(self):
        for user in self.users.values():
            print(user)

def main():
    user_manager = UserManager()
    while True:
        print("\n1. Register")
        print("2. Login")
        print("3. Delete User")
        print("4. Update User")
        print("5. Display Users")
        print("6. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            username = input("Enter username: ")
            password = input("Enter password: ")
            email = input("Enter email: ")
            user_manager.register(username, password, email)
        elif choice == "2":
            username = input("Enter username: ")
            password = input("Enter password: ")
            user_manager.login(username, password)
        elif choice == "3":
            username = input("Enter username: ")
            user_manager.delete_user(username)
        elif choice == "4":
            username = input("Enter username: ")
            new_username = input("Enter new username (optional): ")
            new_password = input("Enter new password (optional): ")
            new_email = input("Enter new email (optional): ")
            user_manager.update_user(username, new_username, new_password, new_email)
        elif choice == "5":
            user_manager.display_users()
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()