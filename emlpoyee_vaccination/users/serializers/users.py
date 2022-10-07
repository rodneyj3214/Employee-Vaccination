from django.core.mail import EmailMultiAlternatives
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from emlpoyee_vaccination.users.models import Employee, User
from emlpoyee_vaccination.users.serializers.employees import EmployeeModelSerializer
from emlpoyee_vaccination.utils.validators import (
    alphanumeric_blank_validator,
    numeric_validator,
)


class UserModelSerializer(serializers.ModelSerializer):
    employee = EmployeeModelSerializer(read_only=True)

    class Meta:
        model = User
        fields = [
            "username",
            "first_name",
            "employee",
            "last_name",
            "identifier",
            "email",
            "url",
        ]
        extra_kwargs = {
            "url": {"view_name": "api:user-detail", "lookup_field": "username"}
        }


class UserRegisterSerializer(serializers.Serializer):
    identifier = serializers.CharField(
        min_length=10,
        max_length=10,
        validators=[UniqueValidator(queryset=User.objects.all()), numeric_validator],
    )
    first_name = serializers.CharField(
        validators=[alphanumeric_blank_validator], min_length=2, max_length=30
    )
    last_name = serializers.CharField(
        validators=[alphanumeric_blank_validator], min_length=2, max_length=30
    )
    email = serializers.EmailField(
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    class Meta:
        fields = ("identifier", "first_name", "last_name", "email")

    def create(self, data):
        temporary_password = "1234"
        username = self.create_username(data.get("first_name"), data.get("last_name"))
        data.update({"password": temporary_password, "username": username})
        user = User.objects.create_user(**data)
        Employee.objects.create(user=user)
        self.send_confirmation_email(user, temporary_password)
        return user

    def create_username(self, first_name, last_name):
        name = first_name.split(" ")[0]
        lastname = last_name.split(" ")[0]
        username = (
            f"{name} {lastname}".lower()
            .replace(" ", "_")
            .replace("á", "a")
            .replace("é", "e")
            .replace("í", "i")
            .replace("ó", "o")
            .replace("ú", "u")
            .replace("ñ", "n")
        )
        return username

    def send_confirmation_email(self, user, temporary_password):
        subject = (
            f"Welcome @{user.username}! ,You have a new user to update you vaccine info"
        )
        from_email = user.email
        text_content = f"Welcome you can access with you email {user.email}! ,and you password is: {temporary_password}"
        html_content = "Hola"
        msg = EmailMultiAlternatives(subject, text_content, from_email, [user.email])
        msg.attach_alternative(html_content, "text/html")
        msg.send()
