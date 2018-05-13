from pages.page import Page


class EztMainPage(Page):
    @property
    def singin_btn(self):
        return self.wait_clickable_element_by_path('.//a[contains(@href, "login")]')

    @property
    def user_name(self):
        return self.wait_clickable_element_by_path('.//span[@class="Ez-user-name"]')

    @property
    def competition_tab(self):
        return self.wait_clickable_element_by_path('.//a[contains(@href, "competitions")]')