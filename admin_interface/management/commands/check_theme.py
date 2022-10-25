"""
Custom django command to load an admin theme
if no theme exists (first time)
"""
from django.core.management import call_command
from django.core.management.base import BaseCommand
import glob
from pathlib import Path
from admin_interface.models import Theme


class Command(BaseCommand):
    help: str = "Check if the database has an admin interface theme named 'UBP'. If not, the default is loaded."

    def add_arguments(self, parser):
        """
        Accept positional argument for theme name
        """
        parser.add_argument("theme", type=str)

    def handle(self, *args, **options):
        """
        Command that loads a theme by name.
        This theme is only loaded is the default theme "Django" is the only existing one.
        Availables themes are available inside "core/fixtures".
        """
        available_themes = [
            Path(p).stem for p in glob.glob("admin_interface/fixture/*.json")
        ]
        theme = options["theme"]
        if theme not in available_themes:
            self.stdout.write(
                f"No admin theme named '{theme}'. Available themes: {available_themes}"
            )

        theme_url = f"https://github.com/urbanplatform/ubp-admin-interface/admin_interface/fixtures/{theme}.json"
        if Theme.objects.count() == 1 and Theme.objects.first().name == "Django":
            self.stdout.write(
                f"No admin theme named '{theme}'. Installing from {theme_url}!"
            )
            call_command("loaddata", theme)
