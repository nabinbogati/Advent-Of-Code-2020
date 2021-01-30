"""
--- Part One ---
For example, suppose you have the following list:

1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc

Each line gives the password policy and then the password.
The password policy indicates the lowest and highest number of times a given letter must appear for the password to be valid.
For example, 1-3 a means that the password must contain a at least 1 time and at most 3 times.

In the above example, 2 passwords are valid. The middle password, cdefg, is not;
it contains no instances of b, but needs at least 1. The first and third passwords are valid:
they contain one a or nine c, both within the limits of their respective policies.

"""

DATA_MAP = {}

def read_file(filename):
    with open(filename, 'r') as file:
        for data in file.readlines():
            rule, value, passwd = data.strip().split(' ')
            start, end = rule.split('-')
            value = value.replace(':','').strip()
            passwd = passwd.lstrip().strip()

            DATA_MAP[passwd] = {'start': int(start), 'end': int(end), 'value': value}


def valid_passwords():
    valid = 0
    for password, meta in DATA_MAP.items():
        count = password.count(meta['value'])

        if count >= meta['start'] and count <= meta['end']:
            valid +=1
    
    return valid


"""
--- Part Two ---
Each policy actually describes two positions in the password, where 1 means the first character,
2 means the second character, and so on. (Be careful; Toboggan Corporate Policies have no concept
of "index zero"!) Exactly one of these positions must contain the given letter.
Other occurrences of the letter are irrelevant for the purposes of policy enforcement.

Given the same example list from above:

    1-3 a: abcde is valid: position 1 contains a and position 3 does not.
    1-3 b: cdefg is invalid: neither position 1 nor position 3 contains b.
    2-9 c: ccccccccc is invalid: both position 2 and position 9 contain c.

"""

def updated_valid_passwords():
    valid = 0
    for password, meta in DATA_MAP.items():
        if password[meta['start']-1] == meta['value'] and password[meta['end']-1] != meta['value']:
            valid += 1
        elif password[meta['end']-1] == meta['value'] and password[meta['start']-1] != meta['value']:
            valid += 1
        else:
            continue
    
    return valid


def main():
    filename = 'input_day2.txt'
    read_file(filename)
    valid_passwd_count = valid_passwords()
    updated_valid_passwd_count = updated_valid_passwords()

    print(valid_passwd_count, updated_valid_passwd_count)

if __name__ == "__main__":
    main()