from rest_framework import serializers

from emlpoyee_vaccination.users.models import Vaccine


class ChoiceField(serializers.ChoiceField):
    def to_representation(self, obj):
        if obj == "" and self.allow_blank:
            return obj
        return self._choices[obj]

    def to_internal_value(self, data):
        # To support inserts with the value
        if data == "" and self.allow_blank:
            return ""

        for key, val in self._choices.items():
            if val == data:
                return key
        self.fail("invalid_choice", input=data)


class VaccineModelSerializer(serializers.ModelSerializer):
    vaccine_type = ChoiceField(
        choices=Vaccine.VACCINE_TYPE,
    )

    class Meta:
        model = Vaccine
        fields = ("employee", "vaccine_type", "vaccine_date", "number_doses")
