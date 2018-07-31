"""Provides application for development purposes."""

from accounts.factory import create_web_app
from accounts.services import legacy, users

app = create_web_app()
