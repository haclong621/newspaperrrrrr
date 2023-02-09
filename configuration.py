
from parsers import Parser


class Configuration(object):
    def __init__(self):
        self.fetch_images = True


    @staticmethod
    def get_parser():
        return Parser
