class Task:
    def __init__(self, id, description, done, completed_on, created) -> None:
        self.id = id
        self.description = description
        self.done = done
        self.completed_on = completed_on
        self.created = created
