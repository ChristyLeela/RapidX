import traceback
from fastapi import APIRouter, HTTPException
from Business.EmployeesController import fetch_employees
from Schema import Employees

router = APIRouter()

@router.get('/employees',
            response_model = Employees.Employees)
def get_employees():
    try:
        return fetch_employees()
    except:
        print(traceback.format_exc())
        raise HTTPException(status_code=500, detail="Error")