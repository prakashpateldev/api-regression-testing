import pytest


@pytest.fixture
def browser(config):
    if config['browser'] == 'chrome':
        driver = Chrome()
    elif config['browser'] == 'firefox':
        driver = Firefox()
    else:
        raise Exception(f'"{config["browser"]}" is not a supported browser')
    driver.implicitly_wait(config['wait_time'])
    yield driver
    driver.quit()
