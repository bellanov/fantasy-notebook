"""Test Calculator."""

import pytest

from python_template import calc as app


@pytest.mark.unit  # type: ignore
def test_add():
    """Test adding two numbers."""
    assert app.add(1, 2) == 3


@pytest.mark.unit  # type: ignore
def test_subtract():
    """Test subtracting two numbers."""
    assert app.subtract(2, 1) == 1
