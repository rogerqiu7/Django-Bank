#!/usr/bin/env python
import os
import sys

# This file is the main entry point for managing your Django project
# It allows you to run commands like `runserver`, `migrate`, `createsuperuser`, etc.
if __name__ == "__main__":

    # Sets the default settings module for Django
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_bank.settings")
    try:

        # Imports Django's command-line utility (raises error if Django isn't installed properly)
        from django.core.management import execute_from_command_line
    except ImportError as exc:

        # Custom error message if Django isn't found
        raise ImportError("Couldn't import Django.") from exc

    # Executes the command-line command (e.g., runserver, migrate, etc.)
    execute_from_command_line(sys.argv)
