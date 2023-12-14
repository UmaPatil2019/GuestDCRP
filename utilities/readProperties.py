#to read data from config.ini, import configparser package
import configparser
import os

#RawConfigParser is class available in configparser package which is called to create an object
config = configparser.RawConfigParser()
#gives root path of the project, GuestDCRP, from there, navigates to configurations -> config.ini
#and reads the data from there
config.read(os.path.abspath(os.curdir)+'/configurations/config.ini')

class ReadConfig:
    @staticmethod
    def getApplicationURL():
        #confg object gets commonInfo data and stores here
        url = config.get('commonInfo', 'baseURL')
        return url

