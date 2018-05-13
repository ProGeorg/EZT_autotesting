from pages.page import Page


class EztCompPage(Page):
    @property
    def competition_table(self):
        return self.wait_element_by_path('.//div[@class="rt-table"]')

    @property
    def table_elements(self):
        return self.competition_table.find_elements_by_xpath('.//div[@class="rt-tr-group"]')