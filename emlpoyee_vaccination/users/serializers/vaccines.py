from rest_framework import serializers

from emlpoyee_vaccination.users.models import Vaccine


class VaccineModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vaccine
        fields = ("employee", "vaccine_type", "vaccine_date", "number_doses")
