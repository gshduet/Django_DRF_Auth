from audioop import reverse
from django.contrib.auth import login, logout
from django.shortcuts import redirect
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.request import Request
from rest_framework.response import Response

from users.serializers import SignUpSerializer, SignInSerializer


class SignUpView(APIView):

    permissions_classes = [AllowAny]
    serializer_class = SignUpSerializer

    def post(self, request: Request) -> Response:
        """
        회원가입 API
        """
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()

            return Response({'MESSAGE': 'SIGN_UP_SUCCESS'}, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DjangoSignInView(APIView):

    permissions_classes = [AllowAny]
    serializer_class = SignInSerializer

    def post(self, request: Request) -> Response:
        serializer = self.serializer_class(data=request.data)
        
        if serializer.is_valid(raise_exception=True):
            user = serializer.validated_data
            response = Response(
                {
                    'MESSAGE': 'SIGN_IN_SUCCESS',
                }, status=status.HTTP_200_OK)

            login(request, user)

            return response

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LogoutView(APIView):

    def delete(self, request: Request) -> Response:

        response = Response(
                {
                    'MESSAGE': 'SIGN_OUT_SUCCESS',
                }, status=status.HTTP_202_ACCEPTED)
                
        logout(request)

        # return response
        return redirect('/users/auth/django')