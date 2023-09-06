from battery import battery
from datetime import date

class SplinderBattery(battery):
    def __init__(self, current_date: date, last_service_date: date):
        self.current_date = current_date
        self.last_service_date = last_service_date

    def needs_service(self):
        return (self.current_date - self.last_service_date).days >= 1460 