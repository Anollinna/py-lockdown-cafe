import datetime
from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError,
                        NotWearingMaskError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if visitor.get("vaccine", 0) == 0:
            raise NotVaccinatedError("You are not vaccinated.")
        elif visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError("Your vaccine is outdated.")
        elif not visitor.get("wearing_a_mask", False):
            raise NotWearingMaskError("You are not wearing a mask.")
        return f"Welcome to {self.name}"
