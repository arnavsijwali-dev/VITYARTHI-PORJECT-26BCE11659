#StudysessionTracker
from ast import parse


def __init__(self):
    self.sessions = []
def add_session(self,start,end, subject="General"):
    start_dt = parse_time(start)
    end_dt = parse_time(end)
    if end_dt< start_dt:
        print("End time cannot be earlier then our start time!")
        return
    duration = calculate_duration(start_dt, end_dt)
    self.sessions.append({"subject": subject,"duration": duration})
def total_study_time(self):
    return sum((session["duration"] for session in self.sessions))
def daily_report(self):
    total = self.total_study_time()
    hours, remainder = divmod(total.seconds, 3600)
    minutes = remainder // 60
    print(f'[Study Session Tracker] Total Study Time: {hours}h {minutes}m')


class StudySessionTracker:
    pass