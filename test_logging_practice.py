import logging
from selenium import webdriver
import pytest


def test_practa_logging():
    log = logging.getLogger(__name__)
    log.info("This is a information log")
    log.warning("This is a information log")
    log.critical("This is a information log")
    log.error("This is a information log")
