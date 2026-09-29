#Module 2: Study-Wise Analyzer
#
from datetime import timedelta

class SubjectAnalyzer:
 def __init__(self, sessions):
        self.sessions = sessions

 def study_time_per_subject(self):
        result = {}
        for s in self.sessions:
            subj = s['subject']
            # assuming duration is in seconds
            result[subj] = result.get(subj, timedelta()) + timedelta(seconds=s["duration"])
        return result
 def subject_report(self):
        print("[Subject-wise Report]")
        for subj, duration in self.study_time_per_subject().items():
            total_seconds = int(duration.total_seconds())
            hours, remainder = divmod(total_seconds, 3600)
            minutes = remainder // 60
            print(f'{subj}: {hours}h {minutes}m')
