from rest_framework import serializers
from .models import Competition, Category


class CompetitionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Competition
        fields = ['id', 'name', 'category', 'description', 'start_date', 'end_date',
                  'min_age', 'max_age', 'min_point', 'max_point', 'image', ]


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', ]
