"""
    For example, consider the following rules:

light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.

These rules specify the required contents for 9 bag types. In this example, every faded blue bag is empty, every vibrant plum bag contains 11 bags (5 faded blue and 6 dotted black), and so on.

You have a shiny gold bag. If you wanted to carry it in at least one other bag, how many different bag colors would be valid for the outermost bag? (In other words: how many colors can, eventually, contain at least one shiny gold bag?)

In the above rules, the following options would be available to you:

    A bright white bag, which can hold your shiny gold bag directly.
    A muted yellow bag, which can hold your shiny gold bag directly, plus some other bags.
    A dark orange bag, which can hold bright white and muted yellow bags, either of which could then hold your shiny gold bag.
    A light red bag, which can hold bright white and muted yellow bags, either of which could then hold your shiny gold bag.

So, in this example, the number of bag colors that can eventually contain at least one shiny gold bag is 4.

"""
import re


def read_file(filename):
    bags_map = {}
    with open(filename, 'r') as file:
        for line in file.readlines():
            bags = line.strip().replace('bags', 'bag').replace('.','').split('contain')
            maps = {}

            if ',' in bags[1]:
                for bag in bags[1].strip().split(','):
                    bag = bag.strip()
                    groups = re.findall(r'(^\d+)(.*)', bag)
                    maps[groups[0][1].strip()] = int(groups[0][0])

                bags_map[bags[0].strip()] = maps
            
            if ',' not in bags[1]:
                if bags[1].strip() != "no other bag": 
                    groups = re.findall(r'(^\d+)(.*)', bags[1].strip())
                    maps[groups[0][1].strip()] = int(groups[0][0])
                    bags_map[bags[0].strip()] = maps
                else:
                    bags_map[bags[0].strip()] = {}

    return bags_map


def count_bag_colors(bags_map, bag_color):
    other_bags = [bag_color]
    count = 0

    for bag in other_bags:
        for key in bags_map:
            if bags_map[key].get(bag):
                if key not in other_bags:
                    other_bags.append(key)
                    count += 1

        
def main():
    filename = 'input_day7.txt'
    bag_color = 'shiny gold bag'
    bags_map = read_file(filename)
    count_bag_colors(bags_map, bag_color)


if __name__ == "__main__":
    main()
