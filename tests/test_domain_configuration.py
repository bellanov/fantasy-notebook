"""Test Environent Configuration."""

import pytest

from notebooks.domain.Configuration import EnvironmentConfiguration


@pytest.mark.unit
def test_environment_configuration_get():
    """Test Environment Configuration - Get."""
    env_config = EnvironmentConfiguration(config={"env": "production", "debug": False})
    assert env_config.get_config() == {"env": "production", "debug": False}


@pytest.mark.unit
def test_environment_configuration_set():
    """Test Environment Configuration - Set."""
    env_config = EnvironmentConfiguration(config={})
    env_config.set_config({"env": "development", "debug": True})
    assert env_config.get_config() == {"env": "development", "debug": True}
