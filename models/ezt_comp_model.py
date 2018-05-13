from pages.ezt_comp_page import EztCompPage


class EztCompModel(object):
    def __init__(self, app):
        self.app = app
        self.ecp = EztCompPage()

    def is_competition_loaded(self):
        return self.ecp.table_elements[0].is_displayed()