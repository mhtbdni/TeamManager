from kivymd.uix.screen import MDScreen
from database import login_user


class LoginScreen(MDScreen):

    def login(self):

        username = self.ids.username.text.strip()
        password = self.ids.password.text.strip()

        if username == "" or password == "":
            self.ids.message.text = "Please fill in all fields."
            return

        user = login_user(username, password)

        if user:
            self.ids.message.text = ""
            self.manager.current = "dashboard"
        else:
            self.ids.message.text = "Invalid username or password."

    def open_register(self):
        self.manager.current = "register"