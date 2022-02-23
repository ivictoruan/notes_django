from rest_framework.serializers import ModelSerializer
from .models import Note

"""
    Classe responsável por serializar os dados de uma nota.
"""
class NoteSerializer(ModelSerializer):
    class Meta:
        model = Note
        fields = '__all__'