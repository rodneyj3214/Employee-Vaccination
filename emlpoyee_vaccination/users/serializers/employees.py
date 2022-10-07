from rest_framework import serializers

from emlpoyee_vaccination.users.models import Employee
from emlpoyee_vaccination.users.serializers.vaccines import VaccineModelSerializer


class EmployeeModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = (
            "user",
            "birthday",
            "address",
            "phone_number",
            "vaccinated",
        )


class EmployeeInformationSerializer(serializers.Serializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    birthday = serializers.DateField()
    address = serializers.CharField(max_length=500)
    vaccinated = serializers.BooleanField(default=False)
    vaccines = VaccineModelSerializer(many=True, required=False)

    def create(self, data):
        vaccines = data.pop("vaccines")
        employee = Employee.objects.create(**data)
        return vaccines

    class Meta:
        model = Employee
