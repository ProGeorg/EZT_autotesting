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


    @property
    def last_name_field(self):
        return self.wait_clickable_element_by_path('.//input[@name="last_name"]')

    @property
    def first_name_field(self):
        return self.wait_clickable_element_by_path('.//input[@name="first_name"]')

    @property
    def middle_name_field(self):
        return self.wait_clickable_element_by_path('.//input[@name="middle_name"]')

    def get_password_fields(self):
        return self.driver.find_elements_by_xpath('.//input[@name="passwod"]')