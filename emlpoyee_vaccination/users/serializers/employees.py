from rest_framework import serializers

from emlpoyee_vaccination.users.models import Employee
from emlpoyee_vaccination.users.serializers.vaccines import VaccineModelSerializer
from emlpoyee_vaccination.utils.validators import phone_regex


class EmployeeModelSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    birthday = serializers.DateField()
    address = serializers.CharField(max_length=500)
    phone_number = serializers.CharField(max_length=17, validators=[phone_regex])
    vaccinated = serializers.BooleanField(default=False)
    vaccine_set = VaccineModelSerializer(many=True, required=False)

    def update(self, instance, validated_data):
        vaccines = validated_data.pop("vaccine_set")
        instance = super().update(instance, validated_data)
        for vaccine in vaccines:
            employee = vaccine.pop("employee")
            employee_id = employee.id
            vaccine.update({"employee": employee_id})
            vaccines_serializer = VaccineModelSerializer(data=vaccine)
            vaccines_serializer.is_valid(raise_exception=True)
            vaccines_serializer.save()
        return instance

    class Meta:
        model = Employee
        fields = (
            "user",
            "birthday",
            "address",
            "phone_number",
            "vaccinated",
            "vaccine_set",
        )
