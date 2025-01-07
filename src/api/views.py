from rest_framework import views
from rest_framework.response import Response

class ProductAPIView(views.APIView):

    def get(self, request):
        content = {
            "Estás llamando el método GET"
        }
        return Response(content)
    
    def post(self, request):
        content = {
            "Estás llamando el método POST"
        }
        return Response(content)
    
    def put(self, request):
        content = {
            "Estás llamando el método PUT"
        }
        return Response(content)
    
    def patch(self, request):
        content = {
            "Estás llamando el método PATCH"
        }
        return Response(content)
    
    def delete(self, request):
        content = {
            "Estás llamando el método DELETE"
        }
        return Response(content)