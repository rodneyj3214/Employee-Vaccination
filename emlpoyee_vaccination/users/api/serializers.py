from django.contrib.auth import get_user_model
from rest_framework import serializers

from emlpoyee_vaccination.users.serializers.employees import EmployeeModelSerializer

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    employee = EmployeeModelSerializer(read_only=True)

    class Meta:
        model = User
        fields = [
            "username",
            "first_name",
            "employee",
            "last_name",
            "identifier",
            "url",
        ]
        extra_kwargs = {
            "url": {"view_name": "api:user-detail", "lookup_field": "username"}
        }
