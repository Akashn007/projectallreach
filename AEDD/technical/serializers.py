from rest_framework import serializers
from .models import TechnicalForm

class TechnicalFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = TechnicalForm
        fields = '__all__'
