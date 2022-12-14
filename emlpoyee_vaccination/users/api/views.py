from django.contrib.auth import get_user_model
from django_filters import rest_framework as filters
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from ..filters.users import EmployeesFilter
from ..permissions import IsAdmin
from ..serializers.employees import EmployeeModelSerializer
from ..serializers.users import UserLoginSerializer, UserModelSerializer

User = get_user_model()


class UserViewSet(ModelViewSet):
    serializer_class = UserModelSerializer
    queryset = User.objects.all()
    lookup_field = "username"
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = EmployeesFilter

    def get_queryset(self, *args, **kwargs):
        assert isinstance(self.request.user.id, int)
        if not self.request.user.is_superuser:
            return self.queryset.filter(id=self.request.user.id)
        return self.queryset

    def get_permissions(self):
        if self.action in ["login"]:
            permissions = [AllowAny]
        else:
            permissions = [IsAuthenticated]
        if self.action not in ["employee", "list", "retrieve"]:
            permissions.append(IsAdmin)
        return [permission() for permission in permissions]

    @action(detail=False, methods=["post"])
    def login(self, request):
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user, token = serializer.save()
        data = {
            "user": UserModelSerializer(user, context={"request": request}).data,
            "token": token,
        }
        return Response(data, status=status.HTTP_201_CREATED)

    @action(
        detail=True, methods=["put", "patch"], serializer_class=EmployeeModelSerializer
    )
    def employee(self, request, *args, **kwargs):
        user = self.get_object()
        employee = user.employee
        partial = request.method == "PATCH"
        serializer = EmployeeModelSerializer(
            employee, data=request.data, partial=partial, context={"request": request}
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        # data = UserModelSerializer(user, context={"request": request}).data
        data = serializer.data
        return Response(status=status.HTTP_200_OK, data=data)
