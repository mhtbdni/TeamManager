from kivymd.uix.screen import MDScreen
from database import register_user


class RegisterScreen(MDScreen):

    def register(self):

        fullname = self.ids.fullname.text.strip()
        username = self.ids.username.text.strip()
        password = self.ids.password.text.strip()

        if fullname == "" or username == "" or password == "":
            self.ids.message.text = "Please fill in all fields."
            return

        if register_user(fullname, username, password):
            self.ids.message.text = ""
            self.manager.current = "login"
        else:
            self.ids.message.text = "This username has already been registered."