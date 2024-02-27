from pydantic import BaseModel


class ConvertedAmount(BaseModel):
    amount: float
    currency: str