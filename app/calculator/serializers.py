from rest_framework.serializers import ModelSerializer

from calculator.models import Problem


class ProblemSerializer(ModelSerializer):
    class Meta:
        model = Problem
        fields = "id",
