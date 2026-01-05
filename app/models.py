from dataclasses import dataclass
from datetime import date
from typing import List


@dataclass
class ExpenseItem:
    date: date
    category: str
    description: str
    note: str
    amount: float


@dataclass
class Invoice:
    company: str
    prepared_by: str
    employee_id: str
    department: str
    start_date: date
    end_date: date
    expenses: List[ExpenseItem]

    @property
    def total_amount(self) -> float:
        return round(sum(item.amount for item in self.expenses), 2)
