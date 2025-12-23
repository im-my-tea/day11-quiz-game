class User:
    def __init__(self,uid,uname):
        self.uid = uid
        self.uname = uname
        self.followers = 0
        self.following = 0
        pass
    def follow(self, user):
        self.following += 1
        user.followers += 1


user_1 = User("001", "Ayush")
user_2 = User("002", "Jack")

user_1.follow(user_2)

print(user_1.following) # Should be 1
print(user_2.followers) # Should be 1