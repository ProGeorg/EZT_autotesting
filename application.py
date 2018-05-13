from models.ezt_comp_model import EztCompModel
from models.ezt_login_model import EztLoginModel
from models.ezt_main_model import EztMainModel
from models.general_model import GeneralModel


class Application(object):
    def __init__(self):
        pass

    @property
    def general(self): return GeneralModel(self)

    @property
    def ezt_main_page(self): return EztMainModel(self)

    @property
    def ezt_login_page(self): return EztLoginModel(self)

    @property
    def ezt_competition_page(self): return EztCompModel(self)