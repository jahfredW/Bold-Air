from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def get_company_name():
    return {"compagny_name": "Example company, LLC"}

@router.get("/employees")
async def number_of_employees():
    return 132