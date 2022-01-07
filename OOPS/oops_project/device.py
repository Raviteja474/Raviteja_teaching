import logging
import constants
import abc
from abc import ABC

logging.basicConfig(level=logging.INFO)


class Buy:

    def __new__(cls, media_type, speed, *args, **kwargs):
        if media_type =="ROM":
            if speed == "High":
                return SSD(media_type,speed)
            else:
                return HDD(media_type,speed)
        else:
            if speed == "High":
                return SRAM(media_type,speed)
            else:
                return DRAM(media_type,speed)

class Device(ABC):
    def about(self):
        logging.info(f'I will store the data.')
    @abc.abstractmethod
    def purpose(self):
        pass

class RAM(Device):

    def purpose(self):
        logging.info(f'I will store volatile data.')

class DRAM(RAM):
    def __init__(self,transistor = constants.DRAM_transistor,NAND_SERIES=constants.DRAM_NAND_SERIES):
        self.transistor= transistor
        self.NAND_SERIES= NAND_SERIES

    def implementation(self):
        logging.debug(f"transistor : {self.transistor}")
        logging.debug(f"self.NAND_SERIES: {self.NAND_SERIES}")
        logging.info(f'It costs 5000.')


class SRAM(RAM):
    def __init__(self,transistor = constants.SRAM_transistor,NAND_SERIES=constants.SRAM_NAND_SERIES):
        self.transistor= transistor
        self.NAND_SERIES= NAND_SERIES

    def implementation(self):
        logging.debug(f"transistor : {self.transistor}")
        logging.debug(f"self.NAND_SERIES: {self.NAND_SERIES}")
        logging.info(f'It costs 6000.')


class ROM(Device):
    # TypeError: Can't instantiate abstract class SSD with abstract method purpose; must implement method
    def purpose1(self):
        logging.debug(f'I will store non-volatile data.')

class HDD(ROM):

    def __init__(self,transistor = constants.HDD_transistor,NAND_SERIES=constants.HDD_NAND_SERIES):
        self.transistor= transistor
        self.NAND_SERIES= NAND_SERIES

    def implementation(self):
        logging.debug(f"transistor : {self.transistor}")
        logging.debug(f"self.NAND_SERIES: {self.NAND_SERIES}")
        logging.info(f'It costs 7000.')

class SSD(ROM):
    #def __init__(self,transistor = constants.SSD_transistor,NAND_SERIES=constants.SSD_NAND_SERIES):

    def __init__(self,media_type,speed):
        self.media_type = media_type
        self.speed = speed
        self.transistor= constants.SSD_transistor
        self.NAND_SERIES= constants.SSD_NAND_SERIES

    def implementation(self):
        logging.info(f"media_type : {self.media_type}")
        logging.info(f"speed: {self.speed}")
        logging.debug(f"transistor : {self.transistor}")
        logging.debug(f"self.NAND_SERIES: {self.NAND_SERIES}")
        logging.info(f'It costs 8000.')
        logging.info(f'____________________________________________________________________')
