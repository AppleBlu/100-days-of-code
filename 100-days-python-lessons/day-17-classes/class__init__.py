class User:
    def __init__(self, user_id='000', username='None'):
        self.id = user_id
        self.username = username
        self.followers = 0


user_1 = User('001', 'Tom')
print(user_1.id)
print(user_1.username)
print(user_1.followers)

user_2 = User()
print(user_2.id)
print(user_2.username)
print(user_1.followers)

