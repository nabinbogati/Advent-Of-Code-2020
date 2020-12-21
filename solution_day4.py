"""
The automatic passport scanners are slow because they're having trouble detecting which passports have all required fields. The expected fields are as follows:

    byr (Birth Year)
    iyr (Issue Year)
    eyr (Expiration Year)
    hgt (Height)
    hcl (Hair Color)
    ecl (Eye Color)
    pid (Passport ID)
    cid (Country ID)

Passport data is validated in batch files (your puzzle input). Each passport is represented as a sequence of key:value pairs separated by spaces or newlines. Passports are separated by blank lines.

Here is an example batch file containing four passports:

ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in

The first passport is valid - all eight fields are present. The second passport is invalid - it is missing hgt (the Height field).

The third passport is interesting; the only missing field is cid, so it looks like data from North Pole Credentials, not a passport at all! Surely, nobody would mind if you made the system temporarily ignore missing cid fields. Treat this "passport" as valid.

The fourth passport is missing two fields, cid and byr. Missing cid is fine, but missing any other field is not, so this passport is invalid.

According to the above rules, your improved system would report 2 valid passports.
"""

CREDENTIALS = []

def read_file(filename):
    data = {}
    with open(filename, 'r') as file:
        for line in file.readlines():
            if line == '\n':
                CREDENTIALS.append(data)
                data = {}
            else:
               for piece in line.strip().split(' '):
                   key, value = piece.split(':')
                   data[key] = value


def validate_passwords():
    valid_passwords = 0
    mandatory_keys = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'] # 'cid' is optional

    valid = False
    for passwords in CREDENTIALS:
        for key in mandatory_keys:
            if passwords.get(key):
                valid = True
            else:
                valid = False
                break

        if valid:
            valid_passwords += 1

    return valid_passwords


def main():
    filename = "input_day4.txt"
    read_file(filename)
    valid_passwords = validate_passwords()
    print(valid_passwords)


if __name__ == "__main__":
    main()
