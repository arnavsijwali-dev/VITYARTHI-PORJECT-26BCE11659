# -----------------------------
# Module 4: Break Tracker
# -----------------------------
class BreakTracker:
    def __init__(self):
        self.breaks = []
    def add_break(self, start, end):
        start_dt = parse_time(start)
        end_dt = parse_time(end)
        self.breaks.append(calculate_duration(start_dt, end_dt))
    def total_break_time(self):
        return sum(self.breaks, timedelta())
    def break_report(self):
        total = self.total_break_time()
        hours, remainder = divmod(total.seconds, 3600)
        minutes = remainder // 60
        print(f"[Break Tracker] Total break time: {hours}h {minutes}m")