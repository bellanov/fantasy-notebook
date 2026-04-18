"""
Simple Python Program.
"""

import logging

# Configure string format for consumption into logging platforms.
logging.basicConfig(
    level=logging.DEBUG, format="%(asctime)-15s %(levelname)-8s %(message)s"
)

# Initialize
logger = logging.getLogger("python-template")


def add(a: int, b: int) -> int:
    """Add two numbers."""
    logger.info("Adding two numbers")
    return a + b


def subtract(a: int, b: int) -> int:
    """Subtract two numbers."""
    logger.info("Subtracting two numbers")

    return a - b
