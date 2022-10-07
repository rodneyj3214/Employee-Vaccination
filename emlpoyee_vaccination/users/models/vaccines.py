from django.db.models import (
    CASCADE,
    CharField,
    DateField,
    ForeignKey,
    PositiveIntegerField,
)
from django.utils.translation import gettext_lazy as _

from emlpoyee_vaccination.utils.models import GenericModel


class Vaccine(GenericModel):
    employee = ForeignKey("users.Employee", on_delete=CASCADE)
    VACCINE_TYPE = (
        ("1", "Sputnik"),
        ("2", "AstraZeneca"),
        ("3", "Pfizer"),
        ("4", "Jhonson&Jhonson"),
    )
    vaccine_type = CharField(_("Vaccine type"), max_length=3, choices=VACCINE_TYPE)
    vaccine_date = DateField(_("Vaccine date"))
    number_doses = PositiveIntegerField(_("Number of doses"), default=1)

    def __str__(self):
        """Return User's str representation"""
        return f"{self.employee.user.first_name} at #{self.employee.user.last_name}"
