class User:

    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username

        print("new user created...")

user_1 = User("001", "Jules")
user_2 = User("002", "Ablam")

user_1.id = "001"
user_1.username = "Jules"

print(user_1.username)