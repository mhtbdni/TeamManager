from kivymd.uix.screen import MDScreen

from database import (
    add_task,
    get_tasks,
    get_current_project,
    get_project,
    project_progress,
)


class TaskScreen(MDScreen):

    def on_pre_enter(self):
        self.show_tasks()

    def show_tasks(self):

        self.ids.task_list.clear_widgets()

        project_id = get_current_project()

        if project_id is None:
            return

        project = get_project(project_id)
        if project:
            self.ids.project_title.text = f"Project: {project[1]}"

        progress = project_progress(project_id)
        self.ids.progress_bar.value = progress
        self.ids.progress_label.text = f"Progress: {progress}%"

        tasks = get_tasks(project_id)

        from widgets.task_card import TaskCard
        for task in tasks:
            card = TaskCard()

            card.task_id = task[0]
            card.task_title = task[2]
            card.task_status = task[3]
            card.task_priority = task[4]
            card.task_deadline = task[5]
            card.task_member = task[6]
            self.ids.task_list.add_widget(card) 

    def save_task(self):

        title = self.ids.task_title.text.strip()
        priority = self.ids.priority.text
        deadline = self.ids.deadline.text
        member = self.ids.member.text

        add_task(
            get_current_project(),
            title,
            priority,
            deadline,
            member
        )   

        self.ids.task_title.text = ""
        self.ids.message.text = "Task added successfully."

        self.show_tasks()
