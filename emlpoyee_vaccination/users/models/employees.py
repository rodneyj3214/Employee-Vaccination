from django.db.models import (
    CASCADE,
    BooleanField,
    CharField,
    DateField,
    OneToOneField,
    TextField,
)
from django.utils.translation import gettext_lazy as _

from emlpoyee_vaccination.utils.models import GenericModel
from emlpoyee_vaccination.utils.validators import phone_regex


class Employee(GenericModel):
    user = OneToOneField("users.User", on_delete=CASCADE)
    birthday = DateField(_("Birthday"), blank=True, null=True)
    address = TextField(max_length=500, blank=True, null=True)
    phone_number = CharField(
        max_length=17, validators=[phone_regex], blank=True, null=True
    )
    vaccinated = BooleanField(default=0)

    def __str__(self):
        """Return User's str representation"""
        return str(self.user)
