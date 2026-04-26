"""Configuration.

Model that represents a generic Configuration.
"""

from abc import ABC, abstractmethod


class Configuration(ABC):
    """Generic Configuration."""

    config: dict

    # Retrieve the Configuration
    @abstractmethod
    def get_config(self): ...

    # Set the Configuration
    @abstractmethod
    def set_config(self, value: dict): ...


class EnvironmentConfiguration(Configuration):
    """Environment Configuration."""

    def __init__(self, config: dict):
        """Initialize the Configuration."""
        self.config = config

    def get_config(self):
        """Retrieve the Configuration."""
        return self.config

    def set_config(self, value: dict):
        """Set the Configuration."""
        self.config = value
