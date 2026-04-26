"""Environment Configuration.

Initialize the environment configuration using environment files defined locally.
"""

from dotenv import dotenv_values

from notebooks.domain.Configuration import EnvironmentConfiguration

env_config = EnvironmentConfiguration(
    config={
        # Define an environment file and load it into the configuration
        # **dotenv_values(".env.secrets")
        # Load shared development variables
        **dotenv_values(".env.shared")
    }
)


print(f"Config: {env_config.get_config()}")
