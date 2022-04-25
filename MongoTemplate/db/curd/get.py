import json
from db.models.Employees import Employees
from mongoengine import connect
import pandas as pd


def get_employees(db : connect, close_session : bool = True)-> pd.DataFrame:
    employees = Employees.objects
    out = [json.loads(employee.to_json()) for employee in employees]
    result = pd.DataFrame(out)
    if close_session: db.close()
    return result
