## Installfest Helper

[![Build Status](https://travis-ci.org/cs-unipi-FOSS/InstallfestHelper.svg?branch=master)](https://travis-ci.org/cs-unipi-FOSS/InstallfestHelper)

Developed by Kyriakos Giannakis - Software Libre Society, University of Piraeus.

This is a little helper script that helped us with organizing the GNU/Linux installfest that took place on Oct 16, 2017 at the University of Piraeus.

### Features:
- Reads an attendant CSV list.
- Organizes the attendants into lists.
- Extracts emails from the list.
- Extracts the emails of those who opted in for the feedback form.

### Usage guidelines:
- Clone (`git clone https://github.com/cs-unipi-FOSS/InstallfestHelper.git`) or download as zip.
- Move to InstallfestHelper folder (`cd /path/to/InstallfestHelper`).
- Allow installfest.py as executable (`chmod +x installfest.py`).
- Run `python installfest.py CSVfile` where _CSVfile_ is your input file.
- Run `python installfest.py -h` or `python installfest.py --help` to see the help message.
- The parameter _--get-feedback-recipients_ returns a list with all the feedback from recipients.
- The parameter _--no-stats_ suppresses the 'Processed # Persons' message.

### TODO:
- Extract the emails into a file.
- Format each attendant's data to JSON.
