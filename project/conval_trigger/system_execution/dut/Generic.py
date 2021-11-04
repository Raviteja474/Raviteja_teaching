import logging
import time


# logging.basicConfig(level=logging.DEBUG, filename=r'C:\Users\ravit\Desktop\samsung_joining\log_'+str(time.time())+r'.txt', filemode='a')

logging.basicConfig(level=logging.DEBUG)


class Generic:

    def __init__(self, length=2.5, width=2.8):
        print("This is a Generic device.")
        self.customer_name = "Generic"
        self.model_number = "MSVP100"
        self.spec = 140

if __name__ == "__main__":
    Generic()