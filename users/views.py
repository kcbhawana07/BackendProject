from rest_framework.decorators import api_view#function based 
from rest_framework.response import Response
from .serializers import RegisterSerializer
from rest_framework_simplejwt.views import TokenObtainPairView #for login
from rest_framework_simplejwt.tokens import RefreshToken #for logouts
from rest_framework.views import APIView#class based 


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
    




# ✅ Register API (Class-Based)
class RegisterView(APIView):

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({
                "success": True,
                "message": "User registered successfully"
            }, status=status.HTTP_201_CREATED)

        return Response({
            "success": False,
            "errors": serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)


# ✅ Logout API (Class-Based)
class LogoutView(APIView):

    def post(self, request):
        try:
            refresh_token = request.data.get("refresh")
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
            }, status=status.HTTP_400_BAD_REQUEST)