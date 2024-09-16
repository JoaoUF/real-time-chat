import os

from channels.routing import ProtocolTypeRouter
from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from channels.security.websocket import OriginValidator
from apps.mschatroom import routing
from django.conf import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings.development")
django_asgi_app = get_asgi_application()

application = ProtocolTypeRouter(
    {
        "http": django_asgi_app,
        "websocket": AllowedHostsOriginValidator(
            AuthMiddlewareStack(URLRouter(routing.websocket_urlpatterns)),
            # settings.ALLOWED_HOSTS,
        ),
    }
)
