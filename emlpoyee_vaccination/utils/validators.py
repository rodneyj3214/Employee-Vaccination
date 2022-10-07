from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _

phone_regex = RegexValidator(
    regex=r"\+?1?\d{9,15}$",
    message=_("Phone number must be in the format: +9999999. Up 15 digits allowed."),
)

alphanumeric_blank_validator = RegexValidator(
    regex=r"^[a-zA-Z\sÀ-ÿ\u00f1\u00d1\s]*$",
    message=_("Only letters and blank spaces are required"),
)
numeric_validator = RegexValidator(
    regex=r"^\d*$",
    message=_("Only letters and blank spaces are required"),
)
