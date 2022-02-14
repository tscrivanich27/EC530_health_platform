import pytest
import sys

sys.path.insert(0, 'EC530_Health_Platform/device_module.py')
from device_module import create_app

@pytest.fixture
def app():
    app = create_app()
    return app
