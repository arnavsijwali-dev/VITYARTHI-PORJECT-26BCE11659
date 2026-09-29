# -----------------------------
# Module 6: Daily Planner
# -----------------------------
class DailyPlanner:
    def __init__(self):
        self.tasks = []
    def add_task(self, task):
        self.tasks.append(task)
    def show_tasks(self):
        print("[Daily Planner] Tasks:")
        for idx, task in enumerate(self.tasks, start=1):
            print(f"{idx}. {task}")