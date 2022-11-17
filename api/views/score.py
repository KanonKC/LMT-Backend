from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from ..google import getSheetScore

@api_view(['GET'])
def get_score(request):
    return Response({'result':getSheetScore()},status=status.HTTP_200_OK)