"""
abcx
abcy
abcz

In this group, there are 6 questions to which anyone answered "yes": a, b, c, x, y, and z. (Duplicate answers to the same question don't count extra; each question counts at most once.)

Another group asks for your help, then another, and eventually you've collected answers from every group on the plane (your puzzle input). Each group's answers are separated by a blank line, and within each group, each person's answers are on a single line. For example:

abc

a
b
c

ab
ac

a
a
a
a

b

This list represents answers from five groups:

    The first group contains one person who answered "yes" to 3 questions: a, b, and c.
    The second group contains three people; combined, they answered "yes" to 3 questions: a, b, and c.
    The third group contains two people; combined, they answered "yes" to 3 questions: a, b, and c.
    The fourth group contains four people; combined, they answered "yes" to only 1 question, a.
    The last group contains one person who answered "yes" to only 1 question, b.

In this example, the sum of these counts is 3 + 3 + 3 + 1 + 1 = 11.

For each group, count the number of questions to which anyone answered "yes". What is the sum of those counts?

"""


def read_file(filename):
    """ just joining all the answers from the group and finding unique ones"""
    string = ''
    count = 0
    with open(filename, 'r') as file:
        for line in file.readlines():
            if line != '\n':
                line = line.strip()
                string += line
            else:
                count += len("".join(set(string)))
                string = ''

    # dont forget to count for the last line 
    count += len("".join(set(string)))
    return count


def compute_second(filename):
    """ just counting the intersection of answers from the group """
    string = ''
    count = 0
    with open(filename, 'r') as file:
        for line in file.readlines():
            if line != '\n':
                line = line.strip()
                if string != '':
                    string = string.intersection(set(line))
                else:
                    string = set(line)
            else:
                count += len(string)
                string = ''
    # dont forget to count for the last line 
    count += len(string)
    return count

def main():
    filename = 'input_day6.txt'
    count = read_file(filename)
    count_second = compute_second(filename)
    print(count_second)


if __name__ == "__main__":
    main()