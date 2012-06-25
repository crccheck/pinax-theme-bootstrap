from django.conf import settings


def theme_context(request):
    """
    make SITE_NAME available in the context

    Substitute for pinax.core.context_processors.pinax_settings

    """
    return {"SITE_NAME": getattr(settings, 'SITE_NAME', '')}
