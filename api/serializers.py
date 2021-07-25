from rest_framework import serializers


class UrlInputSerializer(serializers.Serializer):
    url = serializers.URLField(required=True)

    class Meta:
        fields = ('url',)


class ReviewedUrlInputSerializer(serializers.Serializer):
    url = serializers.URLField(required=True)
    is_phishing_site = serializers.BooleanField(required=True)

    class Meta:
        fields = ('url', 'is_phishing_site',)
