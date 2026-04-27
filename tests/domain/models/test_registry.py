"""Test Registry Model."""

import pytest

from notebooks.domain.models.Registry import ServiceRegistry


@pytest.mark.unit
def test_service_registry_get():
    """Test Service Registry - Get."""
    registry = ServiceRegistry()

    registry.register("foo", {"foo": "bar"})
    registry.register("bar", {"bar": "baz"})

    assert registry.get("foo") == {"foo": "bar"}
    assert registry.get("bar") == {"bar": "baz"}
