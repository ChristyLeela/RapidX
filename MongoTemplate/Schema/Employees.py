from typing import List
from pydantic import BaseModel


class EmployeesRow(BaseModel):
    emp_id : str
    Name : str
    Address : str

class Employees(BaseModel):
    out : List[EmployeesRow]