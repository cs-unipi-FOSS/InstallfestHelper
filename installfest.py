# -*- coding: utf-8 -*-
"""
    The FeedbackParser was used right after the completion of the SLS GNU/Linux installfest in order to
    get the emails of the people that opted in for a feedback form (they would opt in from the original registration
    form and if the final field read "Ναι", then their email would be added to the final recipient list.
"""
from datetime import datetime
import csv
import argparse

parser = argparse.ArgumentParser(description="Registration form processing tool for Installfests.")
parser.add_argument("input_file", help="The CSV file with all the registered persons.")
parser.add_argument("--get-feedback-recipients", action="store_true", help="Return a list with all the feedback form recipients.")
parser.add_argument("--no-stats", action="store_true", help="Suppresses the 'Processed X Persons' message.")
# TODO Create an "output JSON" argument.


class Person:
    """ Represents a registered attendant. Contains all the info from the registration form. """
    def __init__(self, registration_time, email, name, unipi_student, study_year, linux_experience, fav_distro, Feedback_optin):
        reg_time_raw = registration_time[0:-4] + "AM" if registration_time[-4:] == "π.μ." else registration_time[0:-4] + "PM"  # Converts greek AM/PM to en_us.
        self.registration_time = datetime.strptime(reg_time_raw, "%d/%m/%Y %I:%M:%S %p")
        self.email = email  # No need to verify. Already verified by Google.
        self.name = name
        self.unipi_student = (unipi_student == "Ναι")
        self.study_year = study_year
        self.linux_experience = linux_experience
        self.fav_distro = fav_distro
        self.feedback_optin = (Feedback_optin == "Ναι")


class PersonList(list):
    """A custom list class designed for Person objects. Can be set as a feedback list."""
    FEEDBACK = False
    def set_as_feedback_recipient_list(self, personList):
        for person in personList:
            if person.feedback_optin:
                self.append(person)
        self.FEEDBACK = True


    def append(self, obj):
        if self.FEEDBACK:
            raise ValueError("You cannot append persons to a list designated as a feedback recipient_list")
        if type(obj) != Person:
            raise TypeError("Only Persons can be appended in a PersonList.")
        super(PersonList, self).append(obj)

    def get_emails(self):
        output = ""
        counter = 0
        for person in self:
            if counter != len(self) - 1:
                output += person.email + ", "
            else:
                output += person.email
            counter += 1
        return output

data = PersonList()
feedback_recipients = PersonList()


if __name__ == "__main__":
    args = parser.parse_args()

    with open(args.input_file) as registration_file:
        reg_reader = csv.reader(registration_file)
        first = True
        for row in reg_reader:
            if first:
                first = False
                continue
            p = Person(registration_time=row[0],
                       email=row[1],
                       name=row[2],
                       unipi_student=row[3],
                       study_year=row[4],
                       linux_experience=row[5],
                       fav_distro=row[6],
                       Feedback_optin=row[7])
            data.append(p)

    if not args.no_stats:
        print("Parsed", len(data), "registered persons.")
    if args.get_feedback_recipients:
        feedback_recipients.set_as_feedback_recipient_list(data)
        print(feedback_recipients.get_emails())
    else:
        print(data.get_emails())