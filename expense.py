from datetime import datetime

class Expense:
    def __init__(self, name: str, category: str, amount: float, date: datetime) -> None:
        self.name = name
        self.category = category
        self.amount = amount
        self.date = date
    
    def __repr__(self):
        return f"<{self.name}, {self.category}, ${self.amount:.2f}, {self.date.day}, {self.date.month}, {self.date.year}>"