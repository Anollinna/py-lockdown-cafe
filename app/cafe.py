import datetime
from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError,
                        NotWearingMaskError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if visitor.get("vaccine", 0) == 0:
            raise NotVaccinatedError(f"{visitor["name"]} is not vaccinated.")
        elif visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError(f"{visitor["name"]}'s "
                                       f"vaccine is outdated.")
        elif not visitor.get("wearing_a_mask", False):
            raise NotWearingMaskError(f"{visitor["name"]} "
                                      f"is not wearing a mask.")
        else:
            return f"Welcome to {self.name}"
