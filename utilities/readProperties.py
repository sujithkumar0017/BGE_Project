import configparser
file = 'config.ini'
config = configparser.RawConfigParser()
config.read("Configuration/config.ini")


class ReadConfig:
    @staticmethod
    def getApplicationUrl():
        url = config.get("common info", "baseURL")
        return url

    @staticmethod
    def getUseremail():
        username = config.get("common info", "loginemail")
        return username

    @staticmethod
    def getPassword():
        password = config.get("common info", "password")
        return password
