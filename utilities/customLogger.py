import logging
import os

class LogGen():
    @staticmethod
    def loggen():
        #path specifies the place to download logs under logs directory with automation.log file name
        path = os.path.abspath(os.curdir)+ '/logs/automation.log'
        # path = os.path.join('/Users/maheshpatil/PycharmProjects/GuestDCRP/logs' , 'automation1.log')
        # print(path)
        #without force parameter the logs were not getting written in the log file
        logging.basicConfig(filename=path,
                            format='%(asctime)s:%(levelname)s:%(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', force=True)
        logger = logging.getLogger()
        logger.setLevel(logging.DEBUG)
        return logger

    # log levels Warn-> Debug -> info -> error -> fatal
    # if log level warn is specified it includes all the detailed info about remaing log levels
    # if log level Debug is specified, it includes Debug, info, error and fata
    # similarly for other levels, includes that level and other levels under it



