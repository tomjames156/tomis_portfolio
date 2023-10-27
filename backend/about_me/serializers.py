from rest_framework import serializers
from .models import *

class UserPortfolioSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserPortfolio
        fields = ['user', 'email', 'bio']