from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, ValidationError


class SpaceStation(BaseModel):
    """
    Represents a space station with validated technical specifications.
    """
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0, le=100)
    oxygen_level: float = Field(ge=0, le=100)
    last_maintenance: datetime = Field(...)
    is_operational: bool = Field(default=True)
    notes: Optional[str] = Field(default=None, max_length=200)


def main():
    """
    Execute validation tests for valid and invalid SpaceStation data.
    """
    try:
        station = SpaceStation(
            station_id="ISS001",
            name="International Space Station",
            crew_size=6,
            power_level=85.5,
            oxygen_level=92.3,
            last_maintenance="2024-01-01 10:00:00",
            notes="Operational"
        )

        print("Space Station Data Validation")
        print("========================================")
        print("Valid station created:")
        print(f"ID: {station.station_id}")
        print(f"Name: {station.name}")
        print(f"Crew: {station.crew_size} people")
        print(f"Power: {station.power_level}%")
        print(f"Oxygen: {station.oxygen_level}")
        print(f"Status: {station.notes}")
        print("========================================")
        print()
    except ValidationError as e:
        print(f"Unexpected error: {e}")

    try:
        print("Expected validation error:")
        SpaceStation(
            station_id="ISS002",
            name="Mini Station",
            crew_size=21,
            power_level=85.5,
            oxygen_level=92.0,
            last_maintenance="2024-01-01 10:00:00",
            notes="Testing invalid"
        )
    except ValidationError as e:
        for error in e.errors():
            print(f"{error['msg']}")


if __name__ == "__main__":
    main()
