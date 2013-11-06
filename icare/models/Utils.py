
import pymongo
from bson import Code
from icare.models.person_model import PersonModel


class Utils:

    def __init__(self, request):
        self.request = request

    def do_process(self):
        self.__process_anc__()
