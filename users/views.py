from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import RegisterSerializer
from rest_framework_simplejwt.views import TokenObtainPairView #for login
from rest_framework_simplejwt.tokens import RefreshToken #for logouts

@api_view(['POST'])
def register(request):
    serializer = RegisterSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response({
            "success": True,
            "message": "User registered successfully"
        })

    return Response({
        "success": False,
        "errors": serializer.errors
    })




@api_view(['POST'])
def logout(request):
    try:
        refresh_token = request.data["refresh"]
        token = RefreshToken(refresh_token)
        token.blacklist()

        return Response({
            "success": True,
            "message": "Logged out successfully"
        })
    except Exception:
        return Response({
            "success": False,
            "message": "Invalid token"
        })