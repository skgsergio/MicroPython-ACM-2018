import pyb


def test():
    millis = pyb.millis
    endTime = millis() + 10000
    count = 0
    while millis() < endTime:
        count += 1
    print("Count: ", count)


@micropython.native
def test_native():
    millis = pyb.millis
    endTime = millis() + 10000
    count = 0
    while millis() < endTime:
        count += 1
    print("Count native: ", count)


@micropython.viper
def test_viper():
    millis = pyb.millis
    endTime = int(millis()) + 10000
    count = 0
    while int(millis()) < endTime:
        count += 1
    print("Count viper: ", count)
