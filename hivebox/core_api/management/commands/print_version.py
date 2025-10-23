from django.core.management.base import BaseCommand
import environ
from pathlib import Path
from django.conf import settings

class Command(BaseCommand):
    help = "Affiche la version actuelle de l'API"

    def handle(self, *args, **option):
        env = environ.Env()
        environ.Env.read_env(Path(settings.BASE_DIR) / "app.env")
        version = env("VERSION", default="unknonw")
        self.stdout.write(f"API version : {version}")
