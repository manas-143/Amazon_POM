from configparser import ConfigParser


def read_configuration(category, key):
    config = ConfigParser()
    config.read("C:\\Users\\a98016118\\Desktop\\Amazon_POM\\configurations\\config.ini")
    return config.get(category, key)
