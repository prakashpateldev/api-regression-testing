import json

import pytest as pytest


@pytest.fixture(scope='session')
def config():
    with open(Tests/config.json) as config_file:
        data = json.load(config_file)
    return data