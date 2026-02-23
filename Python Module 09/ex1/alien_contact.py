from enum import Enum
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, model_validator, ValidationError


class ContactType(str, Enum):
    """Enumeration of allowed alien contact methods."""
    radio = "radio"
    visual = "visual"
    physical = "physical"
    telepathic = "telepathic"


class AlienContact(BaseModel):
    """
    Model for alien contact reports with business logic validation.
    """
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime = Field(...)
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType = Field(...)
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: Optional[str] = Field(
        default=None, max_length=500
    )
    is_verified: bool = Field(default=False)

    @model_validator(mode='after')
    def validation_rules(self) -> 'AlienContact':
        """
        Apply rules based on contact type and signal strength.
        """
        if not self.contact_id.startswith("AC"):
            raise ValueError("Contact ID must start with 'AC'")

        if self.contact_type == ContactType.physical and not self.is_verified:
            raise ValueError("Physical contact reports must be verified")

        if (self.contact_type == ContactType.telepathic and
                self.witness_count < 3):
            raise ValueError(
                "Telepathic contact requires at least 3 witnesses"
            )

        if self.signal_strength > 7.0 and not self.message_received:
            raise ValueError(
                "Strong signals (> 7.0) must include a message"
            )

        return self


def main():
    """
    Demonstrate valid AlienContact logging and catch validation errors.
    """
    try:
        alien = AlienContact(
            contact_id="AC_2024_001",
            timestamp="2024-02-04 12:00:00",
            location="Area 51, Nevada",
            contact_type=ContactType.radio,
            signal_strength=8.5,
            duration_minutes=45,
            witness_count=5,
            message_received="Greetings from Zeta Reticuli",
            is_verified=True
        )

        print("Alien Contact Log Validation")
        print("======================================")
        print(f"ID: {alien.contact_id}")
        print(f"Type: {alien.contact_type.value}")
        print(f"Location: {alien.location}")
        print(f"Signal: {alien.signal_strength}/10")
        print(f"Duration: {alien.duration_minutes} minutes")
        print(f"Witnesses: {alien.witness_count}")
        print(f"Message: '{alien.message_received}'")
        print("======================================\n")
    except ValidationError as e:
        print(f"Error inesperado: {e}")

    print("Expected validation error:")
    try:
        AlienContact(
            contact_id="AC_2024_002",
            timestamp="2024-02-04 12:05:00",
            location="Mars Base Alpha",
            contact_type=ContactType.telepathic,
            signal_strength=5.0,
            duration_minutes=30,
            witness_count=2,
            is_verified=False
        )
    except ValidationError as e:
        for error in e.errors():
            print(f"{error['msg'][13:]}")


if __name__ == "__main__":
    main()
