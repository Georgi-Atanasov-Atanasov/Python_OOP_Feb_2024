class Task:
    def __init__(self, name, due_date):
        self.name = name
        self.due_date = due_date
        self.comments = []
        self.completed = False

    def change_name(self, new_name):
        if new_name != self.name:
           self.name = new_name
           return new_name
        else:
            return "Name cannot be the same."

    def change_due_date(self, new_date):
        if new_date != self.due_date:
            self.due_date = new_date
            return new_date
        else:
            return "Date cannot be the same"

    def add_comment(self, comment):
        self.comments.append(comment)

    def edit_comment(self, comment_number, new_comment):
        if comment_number in range(len(self.comments)):
            self.comments[comment_number] = new_comment
            return f', '.join(self.comments)
        else:
            return "Cannot find comment."

    def details(self):
        return f"Name: {self.name} - Due Date: {self.due_date}"