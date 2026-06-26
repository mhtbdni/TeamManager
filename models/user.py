class User:

    def __init__(self, id, fullname, username):
        self.id = id
        self.fullname = fullname
        self.username = username

    def __repr__(self):
        return f"User(id={self.id}, username={self.username})"
