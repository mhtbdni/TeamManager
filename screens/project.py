from database import project_progress
from database import get_project, update_project
from kivymd.uix.screen import MDScreen
from widgets.project_card import ProjectCard
from database import add_project, get_projects


class ProjectScreen(MDScreen):

    def on_pre_enter(self):
        self.show_projects()

    def save_project(self):

        title = self.ids.title.text.strip()
        description = self.ids.description.text.strip()
        deadline = self.ids.deadline.text.strip()

        if title == "":
            self.ids.message.text = "Project title is required."
            return

        add_project(title, description, deadline)

        self.ids.title.text = ""
        self.ids.description.text = ""
        self.ids.deadline.text = ""

        self.ids.message.text = "Project saved successfully."

        self.show_projects()

    def show_projects(self):

        self.ids.project_list.clear_widgets()

        projects = get_projects()

        for project in projects:

           card = ProjectCard()

           card.project_id = project[0]
           card.title = project[1]
           card.description = project[2]
           card.deadline = f"{project[3]}   |   {project_progress(project[0])}%"

           self.ids.project_list.add_widget(card)
           selected_project = None


    def load_project(self, project_id):

        project = get_project(project_id)

        self.selected_project = project_id

        self.ids.title.text = project[1]
        self.ids.description.text = project[2]
        self.ids.deadline.text = project[3]

        self.ids.message.text = "Editing project..."
    def update_selected(self):

        if self.selected_project is None:
            return

        update_project(

            self.selected_project,

            self.ids.title.text,

            self.ids.description.text,

            self.ids.deadline.text

        )

        self.selected_project = None

        self.ids.title.text = ""
        self.ids.description.text = ""
        self.ids.deadline.text = ""

        self.ids.message.text = "Project updated."

        self.show_projects()