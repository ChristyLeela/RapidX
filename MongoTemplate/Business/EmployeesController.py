from Business.utils import convert_dict_to_model
from Schema import Employees
from db.connection import get_db
from db.curd import get


def fetch_employees():
    emp_rows =  get.get_employees(get_db())
    emp_rows = emp_rows[['emp_id', 'Name', 'Address']]
    list_of_dicts = emp_rows.to_dict(orient = 'records')
    emps = convert_dict_to_model(list_of_dicts,
                                    Employees.EmployeesRow)
    employees_out = Employees.Employees(out = emps)
    return employees_out