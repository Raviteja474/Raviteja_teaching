# 15 = 1, 2, 4, 8, 16
#
# 1111
#
# 11 -->
#
# 1011
#
# 136 - -->   1, 2, 4, 8, 16, 32, 64, 128
#
# 10001000
#
# 244 - -->   1, 2, 4, 8, 16, 32, 64, 128, 256
#
# 011110100
#
# a & b = __and__(a, b)

memory_devcies = ["DRAM", "SRAM", "SSD", "HDD"]

# print volatile devices

# iter, loop, condition
RAM_devices_1 = []
for device in memory_devcies:
    if "RAM" in device:
        RAM_devices_1.append(device)
print(RAM_devices_1)

RAM_devices = [device for device in memory_devcies if "RAM" in device]

print(RAM_devices)

# myDict = {k: v for (k, v) in zip(keys, values)}
memory_devcies_cost = {"DRAM": 5000, "SRAM": 4000, "SSD":7000, "HDD":8000}
# buy device less than 5001

devices= memory_devcies_cost.keys()
costs = memory_devcies_cost.values()

print(tuple(zip(devices,costs)))

buy_dict = {device:cost for (device,cost) in zip(devices,costs) if cost<5001}
print(buy_dict)