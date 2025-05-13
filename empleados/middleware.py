from django.http import HttpResponseForbidden
from django.conf import settings


class IPRestrictionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        allowed_ips = getattr(settings, 'ALLOWED_IPS', [])
        client_ip = self.get_client_ip(request)

        if allowed_ips and client_ip not in allowed_ips:
            return HttpResponseForbidden(
                "Acceso denegado. No está autorizado."
            )

        return self.get_response(request)

    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip
