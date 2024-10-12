from rest_framework import serializers
from hadr_exemple.exemples import hadr_zero_zero_exemple


class HadrZeroZeroSerializer(serializers.Serializer):
    target_material = serializers.CharField()
    target_radius = serializers.IntegerField()
    target_length = serializers.IntegerField()

    def create(self, validated_data):
        output = hadr_zero_zero_exemple(**validated_data)
        return {'output': output}

