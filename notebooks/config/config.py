"""Environment Configuration.

Initialize the environment configuration using environment files defined locally.
"""

from dotenv import dotenv_values

from notebooks.domain.Configuration import EnvironmentConfiguration

config = EnvironmentConfiguration(
    config={
        # Define an environment file and load it into the configuration
        # **dotenv_values(".env.secrets")
        # Load shared development variables
        **dotenv_values(".env.shared")
    }
)


print(f"Config: {config.get_config()}")
