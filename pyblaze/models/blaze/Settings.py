from pydantic import BaseModel


class Settings(BaseModel):
    crash_enabled: bool
    roulette_enabled: bool
    switch_card_vaulting_disabled: bool
    autobetting_disabled: bool
    casino_enabled: bool
    mines_enabled: bool
    plinko_enabled: bool
