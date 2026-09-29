# Language: Python
from datetime import datetime, timedelta

# -------------------------------
# Helper Functions
# -------------------------------
def parse_time(time_str):
    """Convert HH:MM to datetime object."""
    return datetime.strptime(time_str, "%H:%M")

def calculate_time(start_str, end_str):
    """Return timedelta between start and end times."""
    start_time = parse_time(start_str)
    end_time = parse_time(end_str)
    return end_time - start_time

# -------------------------------
# Module 1: Study Session Tracker
# -------------------------------
class StudySessionTracker:
    def __init__(self):
        self.sessions = []

    def add_session(self, subject, start, end):
        """Add a study session with subject and start/end times (HH:MM)."""
        duration = calculate_time(start, end)
        self.sessions.append({
            "subject": subject,
            "duration": int(duration.total_seconds())
        })

    def get_sessions(self):
        return self.sessions

# -------------------------------
# Module 2: Subject Analyzer
# -------------------------------
class SubjectAnalyzer:
    def __init__(self, sessions):
        self.sessions = sessions

    def study_time_per_subject(self):
        result = {}
        for s in self.sessions:
            subj = s['subject']
            result[subj] = result.get(subj, timedelta()) + timedelta(seconds=s["duration"])
        return result

    def subject_report(self):
        print("[Subject-wise Report]")
        for subj, duration in self.study_time_per_subject().items():
            total_seconds = int(duration.total_seconds())
            hours, remainder = divmod(total_seconds, 3600)
            minutes = remainder // 60
            print(f"{subj}: {hours}h {minutes}m")

# -------------------------------
# Module 3: Study Goal Planner
# -------------------------------
class StudyGoalPlanner:
    def __init__(self):
        self.goals = {}

    def set_goals(self, subject, hours):
        self.goals[subject] = hours

    def goal_report(self, subject_totals):
        print("[Goal Comparison Report]")
        for subj, goal in self.goals.items():
            studied_hours = subject_totals.get(subj, timedelta()).total_seconds() / 3600
            remaining = max(goal - studied_hours, 0)
            print(f"{subj}: Goal {goal}h, Studied {studied_hours:.2f}h, Remaining {remaining:.2f}h")

# -------------------------------
# Module 4: Break Tracker
# -------------------------------
class BreakTracker:
    def __init__(self):
        self.breaks = []

    def add_break(self, start, end):
        """Add a break with start and end times (HH:MM)."""
        duration = calculate_time(start, end)
        self.breaks.append(duration)

    def total_break_time(self):
        return sum(self.breaks, timedelta())

    def break_report(self):
        total = self.total_break_time()
        total_seconds = int(total.total_seconds())
        hours, remainder = divmod(total_seconds, 3600)
        minutes = remainder // 60
        print(f"[Break Tracker] Total break time: {hours}h {minutes}m")

# -------------------------------
# Module 5: Efficiency Analyzer
# -------------------------------
class EfficiencyAnalyzer:
    def __init__(self, study_time, break_time):
        self.study_time = study_time
        self.break_time = break_time

    def efficiency_report(self):
        total_minutes = (self.study_time.total_seconds() + self.break_time.total_seconds()) / 60
        if total_minutes == 0:
            print("[Efficiency Analyzer] No sessions recorded.")
            return
        efficiency = (self.study_time.total_seconds() / 60) / total_minutes * 100
        print(f"[Efficiency Analyzer] Study Efficiency: {efficiency:.2f}%")

# -------------------------------
# Module 6: Daily Planner
# -------------------------------
class DailyPlanner:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def show_tasks(self):
        print("[Daily Planner] Tasks:")
        for idx, task in enumerate(self.tasks, start=1):
            print(f"{idx}. {task}")

# -------------------------------
# Main Runner
# -------------------------------
def main():
    # Track study sessions
    tracker = StudySessionTracker()
    tracker.add_session("Math", "09:00", "10:30")
    tracker.add_session("Science", "11:00", "12:00")
    tracker.add_session("Math", "14:00", "14:30")
    sessions = tracker.get_sessions()

    # Analyze study sessions
    analyzer = SubjectAnalyzer(sessions)
    analyzer.subject_report()
    subject_totals = analyzer.study_time_per_subject()

    # Set goals and compare
    planner = StudyGoalPlanner()
    planner.set_goals("Math", 5)
    planner.set_goals("Science", 3)
    planner.goal_report(subject_totals)

    # Track breaks
    break_tracker = BreakTracker()
    break_tracker.add_break("10:30", "10:45")
    break_tracker.add_break("13:00", "13:20")
    break_tracker.break_report()

    # Efficiency analysis
    total_study_time = sum(subject_totals.values(), timedelta())
    total_break_time = break_tracker.total_break_time()
    efficiency = EfficiencyAnalyzer(total_study_time, total_break_time)
    efficiency.efficiency_report()

    # Daily planner
    daily_planner = DailyPlanner()
    daily_planner.add_task("Revise Math chapters 1-3")
    daily_planner.add_task("Complete Science assignment")
    daily_planner.add_task("Take a 20-minute walk")
    daily_planner.show_tasks()

if __name__ == "__main__":
    main()