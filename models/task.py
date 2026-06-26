class Task:

    STATUS_PENDING = "Pending"
    STATUS_IN_PROGRESS = "In Progress"
    STATUS_COMPLETED = "Completed"

    def __init__(self, id, project_id, title, status):
        self.id = id
        self.project_id = project_id
        self.title = title
        self.status = status

    @property
    def is_completed(self):
        return self.status == self.STATUS_COMPLETED

    def __repr__(self):
        return f"Task(id={self.id}, title={self.title}, status={self.status})"
