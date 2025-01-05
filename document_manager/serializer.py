from rest_framework import serializers
from .models import Document

class ReactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = ['title', 'file']
        read_only_fields = ['created_at']