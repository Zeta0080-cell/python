person = {"li":18,"wang":50,"zhang":20,"sun":22}
def find_max(dict):
    max_age = 0
    for key, value in dict.items():
        if value > max_age:
            max_age = value
            name = key
    print(name)
    print(max_age)
find_max(person)