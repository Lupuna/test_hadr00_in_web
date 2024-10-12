from django.conf import settings
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from hadr_exemple.serializers import HadrZeroZeroSerializer
import time


class HadrZeroZeroAPIView(APIView):
    def post(self, request):
        data = self.autocomplete(request.data)
        serializer = HadrZeroZeroSerializer(data=data)
        if serializer.is_valid():
            result = serializer.save()
            return Response(result, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def autocomplete(data: dict) -> dict:
        if not data.get('target_material'):
            data['target_material'] = settings.GEANT_COMMANDS_TEMPLATE_DEFAULT_PARAMETERS['target_material']
        if not data.get('target_radius'):
            data['target_radius'] = settings.GEANT_COMMANDS_TEMPLATE_DEFAULT_PARAMETERS['target_radius']
        if not data.get('target_length'):
            data['target_length'] = settings.GEANT_COMMANDS_TEMPLATE_DEFAULT_PARAMETERS['target_length']
        return data

