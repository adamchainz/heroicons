import django
from django.conf import settings
from django.template import Context, Template


settings.configure(
    ROOT_URLCONF=__name__,  # Make this module the urlconf
    SECRET_KEY="insecure",
    TEMPLATES=[
        {
            "BACKEND": "django.template.backends.django.DjangoTemplates",
            "APP_DIRS": False,
        },
    ],
    INSTALLED_APPS=["heroicons"],
)
urlpatterns = []
django.setup()


def test_success_outline_simple():
    template = Template(
        "{% load heroicons %}" + '{% heroicon_outline "academic-cap" %}'
    )

    result = template.render(Context())

    assert result.startswith(
        '<svg width="24" height="24" fill="none" viewBox="0 0 24 24" '
        + 'stroke="currentColor">'
    )
    assert "<path" in result
    assert result.endswith("</svg>\n")


def test_success_outline_complete():
    template = Template(
        "{% load heroicons %}"
        + '{% heroicon_outline "academic-cap" size=48 class="h-4 w-4" '
        + 'data_controller="academia" %}'
    )

    result = template.render(Context())

    assert result.startswith(
        '<svg width="48" height="48" class="h-4 w-4" data-controller="academia" '
        + 'fill="none" viewBox="0 0 24 24" stroke="currentColor">'
    )
    assert "<path" in result
    assert result.endswith("</svg>\n")


def test_success_solid_complete():
    template = Template(
        "{% load heroicons %}"
        + '{% heroicon_solid "academic-cap" size=40 class="h-4 w-4 inline" %}'
    )

    result = template.render(Context())

    assert result.startswith(
        '<svg width="40" height="40" class="h-4 w-4 inline" '
        + 'viewBox="0 0 20 20" fill="currentColor">'
    )
    assert "<path" in result
    assert result.endswith("</svg>\n")
