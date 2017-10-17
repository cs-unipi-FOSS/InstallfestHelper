import unittest
from installfest import Person, PersonList, feedback_recipients
from datetime import datetime

class PersonImportTest(unittest.TestCase):

    p1 = None
    p2 = None

    def setUp(self):
        self.p1 = Person(registration_time="11/10/2017 11:06:54 μ.μ.",
                    email="kerk12gr@gmail.com",
                    name="Κυριάκος Γιαννάκης",
                    unipi_student="Ναι",
                    study_year="4o",
                    linux_experience="Intermediate",
                    fav_distro="ArchLinux",
                    Feedback_optin="Ναι")
        self.p2 = Person(registration_time="11/10/2017 11:06:54 π.μ.",
                    email="someoneelse@gmail.com",
                    name="Κυριάκος Γιαννάκης",
                    unipi_student="Ναι",
                    study_year="4o",
                    linux_experience="Intermediate",
                    fav_distro="ArchLinux",
                    Feedback_optin="Όχι")

    def test_am_pm_conversion(self):
        self.assertEqual(datetime.strftime(self.p1.registration_time, "%d/%m/%Y %I:%M:%S %p"), "11/10/2017 11:06:54 PM")
        self.assertEqual(datetime.strftime(self.p2.registration_time, "%d/%m/%Y %I:%M:%S %p"), "11/10/2017 11:06:54 AM")

    def test_person_list(self):
        plist = PersonList()
        self.assertEqual(plist.append(self.p1), None)
        self.assertEqual(plist.append(self.p2), None)
        with self.assertRaises(TypeError):
            plist.append("This is a string")
        self.assertEqual(plist.get_emails(), "kerk12gr@gmail.com, someoneelse@gmail.com")

    def test_feedback_recipients(self):
        plist = PersonList()
        plist.append(self.p1)
        plist.append(self.p2)
        flist = PersonList()
        flist.set_as_feedback_recipient_list(plist)
        self.assertEqual(flist.get_emails(), "kerk12gr@gmail.com")


if __name__ == "__main__":
    unittest.main()