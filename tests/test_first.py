from time import sleep

import pytest


@pytest.yield_fixture(scope='session', autouse=True)
def init(app, env):
    print('SetUP')
    app.ezt_main_page.open_portal(env.Server.url)
    yield


class TestTest:
    def test_1(self, app, env):
        app.ezt_main_page.go_to_login_page()
        app.ezt_login_page.input_correct_credentials(env.User)
        assert app.ezt_main_page.is_user_logged()
        #sleep(3)

    def test_2(self, app):
        app.ezt_main_page.go_to_competition()
        assert app.ezt_competition_page.is_competition_loaded()