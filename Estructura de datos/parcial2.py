import requests

class Users:
    def __init__(self, n:int) -> None:
        self.__users = self.fetch_users(n)

    def fetch_users(self, n):
        url_api = f"https://randomuser.me/api/?results={n}&inc=gender,name,dob,picture,nat"
        try:
            response = requests.get(url_api)
            response.raise_for_status()
            data = response.json()
            users = data.get("results", [])
            return [{"name": user["name"]["first"],
                     "surname": user["name"]["last"],
                     "nationality": user.get("nat", "Nationality not available"),
                     "age": user["dob"]["age"],
                     "gender": user["gender"],
                     "photo": user["picture"]["medium"]} for user in users]
        except requests.exceptions.RequestException as e:
            print("Request error:", e)
            return []

    def get_users(self):
        return self.__users

    def get_user(self, user_id):
        if 0 <= user_id < len(self.__users):
            return self.__users[user_id]
        return "Invalid ID, that ID is not registered."

    def get_gender(self, gender):
        return [user for user in self.__users if user['gender'] == gender]
    
    def get_nationality(self, nationality):
        return [user for user in self.__users if user['nationality'] == nationality]

    def menu(self):
        options = {
            '1': self.get_users,
            '2': lambda: self.get_user(int(input("Please enter an ID: "))),
            '3': lambda: self.get_gender(input("Enter a gender (can only be male or female): ")),
            '4': lambda: self.get_nationality(input("Enter the nationality you want to display: ").upper()),
            '5': "Exit"
        }

        while True:
            print("\n1. Print all users")
            print("2. Get a single user (requires their ID)")
            print("3. Get users depending on gender")
            print("4. Get user by nationality")
            print("5. End operation")

            choice = input("\nChoose an option: ")

            if choice in options:
                if choice == '5':
                    print("Closing program.")
                    break
                else:
                    print(options[choice]())
            else:
                print("Invalid option. Choose one of the displayed options")


num = int(input("Enter the number of users you want in the list: "))
users = Users(n=num)
users.menu()