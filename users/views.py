from rest_framework import viewsets
from users.models import User
from users.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """Создание, редактирование, просмотр и удаление пользователя"""
    serializer_class = UserSerializer
    queryset = User.objects.all()
