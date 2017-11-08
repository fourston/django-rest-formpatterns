from rest_framework import serializers
from rest_framework.validators import UniqueForDateValidator
from .models import FormPattern

class FormSerializer(serializers.ModelSerializer):
    formName = serializers.CharField()
    formFields = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='fieldName'
    )
    class Meta:
        model = FormPattern
        fields = ('formName', 'formFields',)

    validators = [
        UniqueForDateValidator(
            queryset=FormPattern.objects.all(),
            field='slug',
            date_field='field_type'
        )
    ]
    def validate_formFields__fieldName(self, attrs, source):
        value = attrs[source]
        if not self.Meta.model.objects.filter(formFields__fieldName=value).exists():
            raise serializers.ValidationError("Field " + value + " not exist")
        return attrs