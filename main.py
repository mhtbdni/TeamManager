from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
from kivymd.app import MDApp

from database import create_tables

from screens.login import LoginScreen
from screens.register import RegisterScreen
from screens.dashboard import DashboardScreen
from screens.project import ProjectScreen
from screens.task import TaskScreen


class TeamManager(MDApp):

    def build(self):

        create_tables()

        Builder.load_file("kv/login.kv")
        Builder.load_file("kv/register.kv")
        Builder.load_file("kv/dashboard.kv")
        Builder.load_file("kv/project.kv")
        Builder.load_file("kv/project_card.kv")
        Builder.load_file("kv/task_card.kv")
        Builder.load_file("kv/task.kv")

        sm = ScreenManager()

        sm.add_widget(LoginScreen(name="login"))
        sm.add_widget(RegisterScreen(name="register"))
        sm.add_widget(DashboardScreen(name="dashboard"))
        sm.add_widget(ProjectScreen(name="projects"))
        sm.add_widget(TaskScreen(name="tasks"))

        return sm


TeamManager().run()
