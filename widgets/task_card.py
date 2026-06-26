from kivymd.uix.card import MDCard
from kivy.properties import NumericProperty, StringProperty
from kivy.app import App
from database import delete_task, complete_task, update_task_status


class TaskCard(MDCard):
    task_priority = StringProperty()
    task_deadline = StringProperty()
    task_id = NumericProperty()
    task_title = StringProperty()
    task_status = StringProperty()
    task_member = StringProperty()

    def delete(self):
        delete_task(self.task_id)
        app = App.get_running_app()
        screen = app.root.get_screen("tasks")
        screen.show_tasks()

    def mark_done(self):
        complete_task(self.task_id)
        app = App.get_running_app()
        screen = app.root.get_screen("tasks")
        screen.show_tasks()

    def mark_in_progress(self):
        update_task_status(self.task_id, "In Progress")
        app = App.get_running_app()
        screen = app.root.get_screen("tasks")
        screen.show_tasks()
