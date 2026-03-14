from django.urls import path

from .views import HandleUpdateView, SetWebhookView


urlpatterns = [
    path('webhook/', HandleUpdateView.as_view(), name='handle_update'),
    path('set-webhook/', SetWebhookView.as_view(), name='set_webhook'),
]
