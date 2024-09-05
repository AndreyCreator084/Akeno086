calls = 0

def count_calls():
    global calls
    calls += 1

def  string_info(string):
    count_calls()
    w = []
    w.append(len(string))
    w.append(string.upper())
    w.append(string.lower())
    return w

def is_contains(string_info, is_contains):
    string_info.lower()
    new_is_contains = []
    count_calls()
    for i in is_contains:
        new_is_contains.append(i.lower())
    return (string_info.lower() in new_is_contains)


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)
