"""
Custom django command to load an admin theme
if no theme exists (first time)
"""
import os
from django.core.management import call_command
from django.core.management.base import BaseCommand

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
        theme = options["theme"]
        theme_url = f"https://github.com/urbanplatform/ubp-admin-interface/admin_interface/fixtures/{theme}.json"
        if Theme.objects.count() == 1 and Theme.objects.first().name == "Django":
            fixture_location = f"admin_interface/fixtures/{theme}.json"
            if os.path.exists(fixture_location):
                self.stdout.write(
                    f"No admin theme named '{theme}'. Installing from {theme_url}!"
                )
                call_command("loaddata", fixture_location)
            else:
                self.stdout.write(
                    f"Specified theme '{theme}' does not exist. Please check 'https://github.com/urbanplatform/ubp-admin-interface/core/fixtures' for available themes"
                )
