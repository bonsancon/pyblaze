from pydantic import BaseModel


class Country(BaseModel):
    country: str
    blocked: bool
    blocked_withdraw_enabled: bool
    currency_type: str
