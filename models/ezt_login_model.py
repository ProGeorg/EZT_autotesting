from pages.ezt_login_page import EztLoginPage


class EztLoginModel(object):
    def __init__(self, app):
        self.app = app
        self.elp = EztLoginPage()

    def input_email(self, email):
        return self.elp.login_field.send_keys(email)

    def input_password(self, password):
        return self.elp.password_field.send_keys(password)

    def click_singin(self):
        return self.elp.submit_btn.click()

    def input_correct_credentials(self, user):
        self.input_email(user.email)
        self.input_password(user.password)
        self.click_singin()

    def input_password_for_new_user(self, user_password):
        pass_fields = self.elp.get_password_fields()