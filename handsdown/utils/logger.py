"""Utilities for stdout stream logger."""
from __future__ import annotations

import logging

from handsdown.constants import LOGGER_NAME


def get_logger(level: int | None = None) -> logging.Logger:
    """
    Get stdout stream logger.

    Arguments:
        level -- Desired logging level.

    Returns:
        A `logging.Logger` instance.

    """
    logger = logging.getLogger(LOGGER_NAME)
    if level is not None:
        logger.setLevel(level)

    if not logger.handlers:
        formatter = logging.Formatter(fmt="%(levelname)-8s %(message)s", datefmt="%H:%M:%S")
        handler = logging.StreamHandler()
        if level is not None:
            handler.setLevel(level)
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    return logger
