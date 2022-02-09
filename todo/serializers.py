from rest_framework import ModalSerializer
from .models import Todo

class TodoSerializer(ModalSerializer):

  class Meta:
    model = Todo
    fields = ('__all__')
