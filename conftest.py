import pytest
from device_module import create_app

@pytest.fixture
def app():
    app = create_app()
    return app