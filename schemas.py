from pydantic import BaseModel
from typing import Optional
from datetime import date

class ReportCreate(BaseModel):
    client: str
    num_receipt: Optional[str] = None
    date: date
    description: Optional[str] = None
    amount : float

    class Config:
        orm_mode = True