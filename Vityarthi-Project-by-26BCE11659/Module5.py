# Module 5: Efficiency Analyzer
# -----------------------------
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