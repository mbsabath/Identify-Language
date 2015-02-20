__author__ = 'Ben'

def index(elem, s):
    """
    returns the first position of an element within a sequence
    :param elem: any type
    :param s: sequence
    :return: int
    """
    if elem not in s:
        return -1
    if s[0] == elem:
        return 0
    else:
        rest = index(elem, s[1:])
        return 1 + rest


def csv_seperate(s):
    """
    turns a line of a csv input as a string into a list of values
    :param s: string
    :return:list
    """
    if "," not in s:
        return [s]
    comma_index = index(',', s)
    return [s[0:comma_index]] + csv_seperate(s[comma_index + 1:])


def make_numeric(elem):
    """
    if possible, converts an argument to a float
    :param elem: any class
    :return: float or input type
    """
    try:
        return float(elem)
    except ValueError:
        return elem

csv = open("2gram_frequency.csv")
csv_string = csv.read()
list_of_lines = csv_string.split(sep="\n")
print(list_of_lines[0:3])
list_of_line_lists = [csv_seperate(x) for x in list_of_lines]
print(list_of_line_lists[1])
list_of_line_lists = [[y[1:-1] for y in x[0:2]] + [y for y in x[2:]] for x in list_of_line_lists]
cleaned_params = [[y for y in x if index(y, x) % 2 != 0] for x in list_of_line_lists]
print(cleaned_params[1])
#print(list(map(type, cleaned_params[1])))
cleaned_params = cleaned_params[1:-1]
#print(cleaned_params[0])
#test_list = [str(x[1]) for x in cleaned_params]
#print(test_list[1])
#code_lines = [("if bigram == " + x[0] + " or if bigram == " + x[0].lower() + ": return " + x[0] + "\n")
#                for x in cleaned_params]
code_lines = []
for sublist in cleaned_params:
    nextline = "if bigram == '" + sublist[0] + "' or bigram == '" + sublist[0].lower() + "': return " + sublist[1] + "\n"
    code_lines = code_lines + [nextline]

print(code_lines[0])
final_string = "def Eng_Bigram_Freq(bigram): \n"
for line in code_lines:
    nextline = "    "
    nextline = nextline + line
    final_string = final_string + nextline
print(final_string[0:300])
output = open('Eng_Bigram.py', mode='w')
output = output.write(final_string)
