from django.apps import AppConfig as DjangoApponfig


class AppConfig(DjangoApponfig):
    name = 'example'
    verbose_name = 'Example'
