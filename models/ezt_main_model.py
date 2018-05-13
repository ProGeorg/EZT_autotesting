from pages.ezt_main_page import EztMainPage


class EztMainModel(object):
    def __init__(self, app):
        self.app = app
        self.emp = EztMainPage()

    def go_to_login_page(self):
        return self.emp.singin_btn.click()

    def open_portal(self, url):
        return self.emp.driver.get(url)

    def is_user_logged(self):
        return self.emp.user_name.is_displayed()

    def go_to_competition(self):
        return self.emp.competition_tab.click()