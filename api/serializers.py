from rest_framework import serializers


class WebhookSerializer(serializers.Serializer):
    webhook_url = serializers.URLField(required=True)
