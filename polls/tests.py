from django.test import TestCase

# Create your tests here.

str_in = 'the [{cat)(-4)in(-3)(-5)(-11)(-11)(-4)(-3)(-11)(-6)'


def check_regex(input_str):
    if '(-' in input_str and ')' in input_str:
        x = input_str.index('(')
        y = input_str.index(')')
        if input_str[x + 2:y].isdigit():
            return [x, int(input_str[x + 1:y])]
    return None


index_arr = []
while check_regex(str_in) is not None:
    c = check_regex(str_in)
    index_arr.append(c)
    str_in = str_in.replace('(' + str(c[1]) + ')', '_', 1)

for i in range(len(index_arr)):
    c = index_arr[i]
    new_str = str_in[0:c[0]]
    str_in = str_in.replace(str_in[c[0]:c[0] + 1], new_str[c[1]:c[1] + 1], 1)

print(str_in)





