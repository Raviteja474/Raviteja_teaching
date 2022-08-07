import unittest
class Person:
    pass
person = Person()
class Person1:
    pass
person1 = Person1()


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(2,2,"same")
        # self.assertEqual(2,3,"Not same")
        # self.assertNotIsInstance(person,Person,"person is not object of class Person")
        self.assertNotIsInstance(person1,Person,"person is not object of class Person")
        self.assertNotIsInstance(person, Person, "person is not object of class Person")


if __name__ == '__main__':
    unittest.main()
