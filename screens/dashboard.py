from kivymd.uix.screen import MDScreen
from database import get_projects, get_tasks, project_progress


class DashboardScreen(MDScreen):

    def on_pre_enter(self):
        self.refresh()

    def refresh(self):

        projects = get_projects()
        project_count = len(projects)

        total_tasks = 0
        completed_tasks = 0
        total_progress = 0

        for project in projects:
            tasks = get_tasks(project[0])
            total_tasks += len(tasks)
            completed_tasks += sum(1 for t in tasks if t[3] == "Completed")
            total_progress += project_progress(project[0])

        avg_progress = int(total_progress / project_count) if project_count > 0 else 0

        self.ids.project_count.text = f"Projects: {project_count}"
        self.ids.task_count.text = f"Total Tasks: {total_tasks}"
        self.ids.completed_count.text = f"Completed Tasks: {completed_tasks}"
        self.ids.avg_progress.text = f"Average Progress: {avg_progress}%"
        self.ids.overall_progress.value = avg_progress

    def open_projects(self):
        self.manager.current = "projects"

    def logout(self):
        self.manager.current = "login"
