calls = 0
def count_calls():
    global calls
    print(calls)


def string_info(name):
    global calls
    calls += 1
    print((len(name), name.upper(), name.lower()))
    return string_info


def is_contains(name1, name2):
    global calls
    calls += 1
    for i in range(len(name2)):
        name2[i] = name2[i].lower()
    if name1.lower() in name2:
        print(True)
    else:
        print(False)
    return is_contains

string_info('Capybara')
string_info('Armageddon')
is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])
is_contains('cycle', ['recycling', 'cyclic'])
count_calls()





