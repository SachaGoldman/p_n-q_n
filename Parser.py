file = open('Output/p_500.txt', 'r')

file_data = file.read()

terms_and_signs = file_data.split(' ')

while '+' in terms_and_signs:
    terms_and_signs.remove('+')

while '-' in terms_and_signs:
    terms_and_signs.remove('-')

coefs = []

for item in terms_and_signs:
    coefs.append(item.split('x')[0])

for item in coefs:
    print(item)