from device import *

device_obj_1 = Buy(media_type="ROM",speed="High")
device_obj_2 = Buy(media_type="ROM",speed="Low")
device_obj_3 = Buy(media_type="RAM",speed="High")
device_obj_4 = Buy(media_type="RAM",speed="Low")

device_objects = [device_obj_1,device_obj_2,device_obj_3,device_obj_4]
# Polymorphism
for device_obj in device_objects:
    device_obj.implementation()
    print("________________________________________________________________")
