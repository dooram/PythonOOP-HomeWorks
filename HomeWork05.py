class Task:
    def __init__(self, name, deadline, description=None):
        self.name = name
        self.description = description
        self.deadline = deadline
        self.status = "NotDone"

class TaskManager:
    def __init__(self) :
        self.tasks = {}

    def addTask(self, Task):
        self.tasks[Task.name] = {"Description": Task.description,
                                 "Deadline": Task.deadline,
                                 "Status": Task.status}

    def delTask(self, Task):
        del self.tasks[Task.name]

    def changeStatus(self, Task):
        if self.tasks[Task.name]["Status"] == "NotDone": self.tasks[Task.name]["Status"] = "Done"
        else: self.tasks[Task.name]["Status"] = "NotDone"

    def listOutput(self):
        for i in self.tasks:
            print(f"\n{i}:", end=" ")
            for j in self.tasks[i]:
                print(f"{j}: {self.tasks[i][j]}\n          ", end="")

buyProducts = Task("Shopping", "Tomorrow", "Buy milk and chocolate")
changePassword = Task("Password", "4p.m.")
doHomeWork = Task("HomeWork", "Sunday", "Do HW from Step Academy")

Nazar = TaskManager()

Nazar.addTask(buyProducts)
Nazar.changeStatus(buyProducts)

Nazar.addTask(changePassword)
Nazar.changeStatus(changePassword)

Nazar.addTask(doHomeWork)

Nazar.listOutput()