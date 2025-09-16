from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.exceptions import InvalidToken
class JwtUser:
    def __init__(self,user_id,email,username):
        self.id=user_id
        self.email=email
        self.username=username
        self.is_authenticated=True
    def __str__(self):
        return self.email
    

class CustomJwtAuthentication(JWTAuthentication):
    def get_user(self, validated_token):
        try:
            user_id=validated_token['user_id']
            email=validated_token['email']
            username=validated_token['username']
        except KeyError:
            raise InvalidToken('token missing,required claims.')
        return JwtUser(user_id,email,username)