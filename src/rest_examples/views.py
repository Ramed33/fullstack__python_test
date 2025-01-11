from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import TestSerializer

class TestAPIView(APIView):
    """API View de Prueba"""

    serializer_class = TestSerializer

    def get(self, request, format=None):
        """Regresa una lista de características de un APIView"""
        apiview_info = [
            "Usa métodos HTTP como funciones (get, post, patch, put, delete)",
            "Es similar a un django view tradicional",
            "Te da el mayor control de la lógica de la app",
            "Es mapeado manualmente a los urls"
        ]

        return Response({"message":"Hola", "api_view_info":apiview_info})
    
    def post(self, request):
        """Crea un mensaje con el nombre ingresado"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get("name")
            message = f"Hola {name}!"
            return Response({"message" : message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def put(self, request, pk=None):
        """Manejar la actualización de un objeto"""
        return Response({"method":"PUT"})

    def patch(self, request, pk=None):
        """Manejar la actualización parcial de un objeto"""
        return Response({"method":"PATCH"})

    def delete(self, request, pk=None):
        """Manejar la eliminación de un objeto"""
        return Response({"method":"DELETE"})