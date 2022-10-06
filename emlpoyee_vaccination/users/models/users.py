from django.contrib.auth.models import AbstractUser
from django.db.models import CharField, EmailField
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from emlpoyee_vaccination.utils.models import GenericModel
from emlpoyee_vaccination.utils.validators import (
    alphanumeric_blank_validator,
    numeric_validator,
)


class User(GenericModel, AbstractUser):
    """
    Default custom user model for Emlpoyee Vaccination.
    If adding fields that need to be filled at user signup,
    check forms.SignupForm and forms.SocialSignupForms accordingly.
    """

    email = EmailField(
        _("Email address"),
        unique=True,
        error_messages={"unique": _("A user with that email already exists.")},
    )

    #: First and last name do not cover name patterns around the globe
    first_name = CharField(
        _("first name"),
        validators=[alphanumeric_blank_validator],
        max_length=150,
        blank=True,
    )
    last_name = CharField(
        _("last name"),
        validators=[alphanumeric_blank_validator],
        max_length=150,
        blank=True,
    )
    identifier = CharField(
        _("Identifier"), validators=[numeric_validator], max_length=15
    )

    def get_absolute_url(self):
        """Get url for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"username": self.username})
