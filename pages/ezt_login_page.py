from pages.page import Page


class EztLoginPage(Page):
    @property
    def login_field(self):
        return self.wait_clickable_element_by_path('.//input[@name="email"]')

    @property
    def password_field(self):
        return self.wait_clickable_element_by_path('.//input[@name="password"]')

    @property
    def submit_btn(self):
        return self.wait_clickable_element_by_path('.//input[@type="submit"]')