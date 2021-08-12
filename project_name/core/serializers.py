from rest_framework import serializers

# import your model
from .models import ExampleModel

# name your serializer {MODEL_NAME}Serializer
class ExampleModelSerializer(serializers.ModelSerializer):
    class Meta:
        # name of model the serializer is for
        model = ExampleModel
        # all the fields you want returned (comes from model fields defined in models.py)
        # doesn't have to be all the fields
        fields = (
            "id",
            "ex_int_field",
            "ex_char_field",
            "ex_text_field",
            "ex_date_field",
            "ex_bool_field",
        )