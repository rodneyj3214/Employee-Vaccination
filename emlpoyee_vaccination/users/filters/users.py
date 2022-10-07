from django_filters import ChoiceFilter, DateFromToRangeFilter
from django_filters.rest_framework import BooleanFilter, FilterSet

from emlpoyee_vaccination.users.models import User, Vaccine


class EmployeesFilter(FilterSet):
    vaccine_date = DateFromToRangeFilter(
        label="Vaccine Date",
        field_name="employee__vaccine__vaccine_date",
        distinct=True,
    )
    vaccine_type = ChoiceFilter(
        choices=Vaccine.VACCINE_TYPE,
        label="Vaccine Type",
        field_name="employee__vaccine__vaccine_type",
        distinct=True,
    )
    vaccinated = BooleanFilter(label="Vaccinated", field_name="employee__vaccinated")

    class Meta:
        model = User
        fields = ["vaccinated", "vaccine_type", "vaccine_date"]
