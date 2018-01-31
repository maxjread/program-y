import unittest

from programy.mappings.person import PersonCollection

class PersonTests(unittest.TestCase):

    def test_load_persons(self):
        person_text = """
        " with you "," with me2 "
        " with me "," with you2 "
        """

        collection = PersonCollection()
        self.assertIsNotNone(collection)

        collection.load_from_text(person_text)

        #self.assertEqual("(^with me | with me | with me$)", collection.person(" with me "))
        self.assertEqual(collection.personalise_string(" with me "), "with you2")

    def test_replace_person(self):
        person_text = """
        " with me "," with you2 "
        " are you "," am I2 "
        """

        collection = PersonCollection()
        self.assertIsNotNone(collection)

        collection.load_from_text(person_text)

        #self.assertEqual("(^with me | with me | with me$)", collection.person(" with me "))
        self.assertEqual(collection.personalise_string("Hello are you with me"), "Hello am I2 with you2")
