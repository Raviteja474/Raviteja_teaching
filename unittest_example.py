import unittest

class Video_Stream_720p(unittest.TestCase):

    def setUp(self):
        print("setup")
    #
    def test_1(self):
        print("Workload0")
    def test_2(self):
        print("Workload1")

    def test_3(self):
        print("Workload2")


    def tearDown(self):
        print("Teardown")


if __name__ == '__main__':
    unittest.main()

# setup
# Workload0
# Teardown
# setup
# Workload1
# Teardown
# setup
# Workload2
# Teardown