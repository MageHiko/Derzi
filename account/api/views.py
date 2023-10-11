from rest_framework.generics import (
    ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView, RetrieveUpdateAPIView,
    RetrieveDestroyAPIView, RetrieveUpdateDestroyAPIView
)
from account.models import Account
from account.api.serializers import(
    AccountCreateSerizlizer, AccountListSerializer, AccountUpdateSerializer
)
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from account.api.permission import IsOwner

class AccountListAPIView(ListAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountListSerializer
    permission_classes = (IsAdminUser,)

class AccountCreateAPIView(CreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountCreateSerizlizer
class AccountRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountUpdateSerializer
    permission_classes = (IsOwner,)

class AccountDestroyAPIView(DestroyAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountCreateSerizlizer
    permission_classes = (IsAdminUser, IsAdminUser,)