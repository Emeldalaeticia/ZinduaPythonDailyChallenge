
import unittest
from unittest.mock import patch
from io import StringIO
from phonebook_app import add_contact, delete_contact, search_contact, print_contacts


class PhonebookAppTests(unittest.TestCase):

    def setUp(self):
        self.phonebook = {}

    def tearDown(self):
        self.phonebook = {}

    def test_add_contact(self):
        with patch('builtins.input', side_effect=['John', '1234567890']):
            add_contact(self.phonebook)
        self.assertIn("John", self.phonebook)
        self.assertEqual(self.phonebook["John"], "1234567890")

        with patch('builtins.input', side_effect=['John', '9876543210']):
            add_contact(self.phonebook)
        self.assertEqual(len(self.phonebook), 1)

    def test_delete_contact(self):
        self.phonebook["John"] = "1234567890"
        with patch('builtins.input', side_effect=['John']):
            delete_contact(self.phonebook)
        self.assertNotIn("John", self.phonebook)

        with patch('builtins.input', side_effect=['John']):
            delete_contact(self.phonebook)
        self.assertEqual(len(self.phonebook), 0)

    def test_search_contact(self):
        self.phonebook["John"] = "1234567890"
        with patch('builtins.input', side_effect=['John']), patch('sys.stdout', new_callable=StringIO) as stdout:
            search_contact(self.phonebook)
            self.assertEqual(stdout.getvalue().strip(), "John: 1234567890")

        with patch('builtins.input', side_effect=['Jane']), patch('sys.stdout', new_callable=StringIO) as stdout:
            search_contact(self.phonebook)
            self.assertEqual(stdout.getvalue().strip(), "Contact not found.")

    def test_print_contacts(self):
        with patch('sys.stdout', new_callable=StringIO) as stdout:
            print_contacts(self.phonebook)
            self.assertEqual(stdout.getvalue().strip(), "No contacts found.")

        self.phonebook["John"] = "1234567890"
        self.phonebook["Jane"] = "9876543210"
        with patch('sys.stdout', new_callable=StringIO) as stdout:
            print_contacts(self.phonebook)
            expected_output = "Contacts:\nJohn: 1234567890\nJane: 9876543210"
            self.assertEqual(stdout.getvalue().strip(), expected_output)


if __name__ == '__main__':
    unittest.main()
