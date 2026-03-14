from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status

from .bot import handle_update, set_webhook
from .serializers import WebhookSerializer


class HandleUpdateView(APIView):
    def post(self, request: Request) -> Response:
        # Here you would handle the incoming update from Telegram
        # For example, you could parse the update and respond accordingly
        update_data = request.data
        # Process the update_data as needed
        print("Received update:", update_data)

        # Call the function to handle the update
        handle_update(update_data)
        
        # Respond with a success status
        return Response({"message": "Update received successfully"}, status=status.HTTP_200_OK)


class SetWebhookView(APIView):
    def post(self, request: Request) -> Response:
        serializer = WebhookSerializer(data=request.data)
        if serializer.is_valid():
            webhook_url = serializer.validated_data['webhook_url']
            set_webhook(webhook_url)
            # Respond with a success status
            return Response({"message": "Webhook set successfully"}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        