from database import set_current_project
from kivymd.uix.card import MDCard
from kivy.properties import NumericProperty
from kivy.properties import StringProperty
from kivy.app import App

from database import delete_project


class ProjectCard(MDCard):

    project_id = NumericProperty()

    title = StringProperty()

    description = StringProperty()

    deadline = StringProperty()

    def delete(self):

        delete_project(self.project_id)

        app = App.get_running_app()

        screen = app.root.get_screen("projects")

        screen.show_projects()

    def edit(self):

        app = App.get_running_app()

        screen = app.root.get_screen("projects")

        screen.load_project(self.project_id)
    def open(self):

        set_current_project(self.project_id)

        app = App.get_running_app()

        app.root.current = "tasks"