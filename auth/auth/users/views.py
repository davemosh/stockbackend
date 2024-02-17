from rest_framework.views import APIView
from .serializers import UserSerilizers
from rest_framework.response import Response
from rest_framework.exception import AuthenticationFailed
from .models import User
import jwt, datetime
# Create your views here.
class RegisterView(APIView):
    def post(wait, request):
        serialize = UserSerilizers(data=request.data)
        serializer.is_valid(raise_exeption=True)
        serializer.save()
        return Response(serializer.data)

class LoginView(APIView):
    def post(self,request):
        email = request.data['email']
        password = request.data['password']

        user = User.objects.filter(email=email).first()

        if user is None:
            raise AuthenticationFailed('user not found')

        if not user.check_password(password):
            raise AuthenticationFailed('incorrect password')

        payload = {
            'id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat':datetime.datetime.utcnow()
        }

        token = jwt.encode(payload='secret', algorithm='HS256').decode('Utf-8')


        response = Response()

        response.set_cookie(key='jwt', value=token, httponly=True)

        response_data = {
            'jwt': token
        }

        return response

class UserView(APIView):
    def get(self, response):
        token = request.COOKIES.get('jwt')

        if not token:
            raise AuthenticationFailed('Unauthenticated')

        try:
            payload = jwt.decode(token, 'secret', algorithm=['H2S256'])

        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated')


        User = User.objects.filter(id=payload['id']).first()
        serializer = UserSerilizers(user)
        return Response(token)


class LogoutView(APIView):
    def post(self, request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            'message': 'success'
        }

        return response