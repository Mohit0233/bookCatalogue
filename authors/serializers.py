from rest_framework import serializers

from authors.validators import validate_author_id, validate_name


class AddAuthorSerializers(serializers.Serializer):
    authorId = serializers.CharField(max_length=15, validators=[validate_author_id])
    name = serializers.CharField(max_length=50, validators=[validate_name])
    phoneNumber = serializers.IntegerField(default=None, allow_null=True)
    birthDate = serializers.DateField(input_formats=['%d-%m-%Y', '%d-%b-%Y'])
    deathDate = serializers.DateField(input_formats=['%d-%m-%Y', '%d-%b-%Y'], default=None, allow_null=True)
