from django.shortcuts import render

from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from queen_phisher_AI.core import predict_phishing


from .serializers import UrlInputSerializer


# Create your views here.
class PredictPhishingUrl(GenericAPIView):
    serializer_class = UrlInputSerializer
    permissions = [AllowAny]

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            url = serializer.data.get('url')
            prediction, features_set = predict_phishing(url)
            return Response(
                {'is_phishing': bool(not prediction), 'features_set': features_set},
                status=status.HTTP_200_OK,
            )
        return Response(
            {'errors': serializer.errors},
            status=status.HTTP_400_BAD_REQUEST,
        )
