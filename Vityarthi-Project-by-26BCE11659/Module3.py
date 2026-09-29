#Module 3: Study Goal Tracker

class StudyGoalPlanner:
    def __innit__(self):
        self.goals = {}
    def set_goals(self, subject, hours):
        self.goals[subject] = hours
        def goal_report(self, subject_totals):
            print("[Goal Comparison Report]")
            for subj, goal in self.goal.items():
                studied_hours = subject_totals.get(subj, timedelta()).total_seconds() / 3600
                remaining = max(goal - studied_hours, 0)
                print(f"{subj}: Goal {goal}h, Studied {studied_hours: .2f}h, Remaining ")


class SubjectAnalyzer:
    pass