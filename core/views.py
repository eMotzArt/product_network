from django.contrib.auth import get_user_model, login, logout
from rest_framework.generics import CreateAPIView, GenericAPIView, ListAPIView
from rest_framework.response import Response

from core.serializers import AgentCreateSerializer, UserLoginSerializer
from goods.models import Product

USER_MODEL = get_user_model()

class RegisterAgentView(CreateAPIView):
    queryset = USER_MODEL.objects.all()
    serializer_class = AgentCreateSerializer

class LoginLogoutView(GenericAPIView):
    serializer_class = UserLoginSerializer
    queryset = USER_MODEL.objects.all()

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = self.get_object()
        login(request, user, backend='django.contrib.auth.backends.ModelBackend')
        return Response({'status': 'Successfully logged in'}, status=204)

    def get_object(self):
        return USER_MODEL.objects.get(email=self.request.data['email'])

    def delete(self, request):
        logout(request)
        return Response({'status': 'Successfully logged out'}, status=204)
