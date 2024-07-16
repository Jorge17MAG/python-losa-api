from fastapi import FastAPI, HTTPException
from typing import List
from schemas import *
from crud import *

app = FastAPI()

from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/reports")
def api_get_reports():
    return get_all_reports()

@app.get("/reports/{id}")
def api_get_report(id : int):
    return get_report(id)

@app.post("/reports")
def api_create_report(report : ReportCreate):
    return create_report(report)

@app.put("/reports/{id}")
def api_update_report(id: int, report : ReportCreate):
    return update_report(id, report)

@app.get("/reports_month_year")
def api_get_reports_month_year(month: Optional[str] = None, year: Optional[str] = None):
    if month is not None or year is not None:
        return get_report_month_year(month, year)
    else:
        return get_all_reports()

@app.delete("/reports/{id}")
def api_delete_report(id : int):
    return delete_report(id)