from enum import Enum
from typing import List
from datetime import datetime
from pydantic import (
    BaseModel,
    Field,
    model_validator,
    ValidationError
)


class Rank(str, Enum):
    """Available military ranks for crew members."""
    cadet = "cadet"
    officer = "officer"
    lieutenant = "lieutenant"
    captain = "captain"
    commander = "commander"


class Crew_member(BaseModel):
    """
    Represents an individual astronaut with age and experience validation.
    """
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = Field(default=True)


class SpaceMission(BaseModel):
    """
    Manages a space mission including budget and nested crew validation.
    """
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: List[Crew_member] = Field(min_length=1, max_length=12)
    mission_status: str = Field(default="Planned")
    budget_millions: float = Field(ge=1, le=1000000)

    @model_validator(mode='after')
    def val_rules(self):
        """
        Verify leadership and experience requirements.
        """
        if not self.mission_id.startswith('M'):
            raise ValueError("Mission ID must start with 'M'")

        have_leader = any(
            p.rank in [Rank.commander, Rank.captain] for p in self.crew
        )
        if not have_leader:
            raise ValueError(
                "Mission must have at least one Commander or Captain"
            )

        if self.duration_days > 365:
            p_expe = sum(1 for p in self.crew if p.years_experience >= 5)
            porcent = (p_expe / len(self.crew)) * 100
            if porcent < 50:
                raise ValueError(
                    "Long missions need 50% experienced crew"
                )

        if not all(p.is_active for p in self.crew):
            raise ValueError("All crew members must be active")

        return self


def main():
    """
    Execute tests for valid mission setup and rejection.
    """
    try:
        mission1 = SpaceMission(
            mission_id="M2024_MARS",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            launch_date=datetime(2024, 6, 15, 10, 0, 0),
            duration_days=90,
            budget_millions=2500.0,
            crew=[
                Crew_member(
                    member_id="CM001",
                    name="Sarah Connor",
                    rank="commander",
                    age=45,
                    specialization="Mission Command",
                    years_experience=20,
                    is_active=True
                ),
                Crew_member(
                    member_id="CM002",
                    name="John Smith",
                    rank="lieutenant",
                    age=35,
                    specialization="Navigation",
                    years_experience=10,
                    is_active=True
                ),
                Crew_member(
                    member_id="CM003",
                    name="Alice Johnson",
                    rank="officer",
                    age=30,
                    specialization="Engineering",
                    years_experience=8,
                    is_active=True
                )
            ]
        )

        print("Space Mission Crew Validation")
        print("=" * 40)
        print(f"Mission: {mission1.mission_name}")
        print(f"ID: {mission1.mission_id}")
        print(f"Crew size: {len(mission1.crew)}")
        print("Crew members:")
        for member in mission1.crew:
            print(f"   - {member.name} ({member.rank.value})")
        print("=" * 40 + "\n")
    except ValidationError as e:
        print(f"Error: {e}")

    try:
        print("Expected validation error:")
        SpaceMission(
            mission_id="M2024_MARS",
            mission_name="Mars Colony",
            destination="Mars",
            launch_date=datetime(2024, 6, 15, 10, 0, 0),
            duration_days=90,
            budget_millions=2500.0,
            crew=[
                Crew_member(
                    member_id="CM003",
                    name="Sara Johnson",
                    rank="officer",
                    age=30,
                    specialization="Engineering",
                    years_experience=8,
                    is_active=True
                )
            ]
        )
    except ValidationError as e:
        for error in e.errors():
            print(f"{error['msg'][13:]}")


if __name__ == "__main__":
    main()
