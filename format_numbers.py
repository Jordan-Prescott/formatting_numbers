#script for DC to edit the numbers fotmatiing for Magic

#Putting the data through the ringer
with open('Numbers.txt') as edit_numbers:
    numbers_contents = edit_numbers.read()
    numbers_contents = numbers_contents.replace(';', '')
    numbers_contents = numbers_contents.replace('.', '')
    numbers_contents = numbers_contents.replace('–', '-')    
    numbers_contents = numbers_contents.split('\n')

#Creating a list for the numbers
number_ranges = []
for number in numbers_contents:
    number_ranges.append(number)
#print(number_ranges)

#Formatting the numbers
formatted_numbers = []
for ranges in number_ranges:
    if ' - ' in ranges:
        prefix = ranges[0:7]
        num = ranges[0:13]
        did = ranges[13:16]
        complete_num = num + prefix + did
        #print(complete_num)
        formatted_numbers.append(complete_num)
    else:
        formatted_numbers.append(ranges)

with open('Numbers.txt', 'w') as gen_file:
    for item in formatted_numbers:
        gen_file.write('%s\n' % item)
