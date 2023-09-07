underwear = {
    'International': {
        1: 'XXS',
        2: 'XS',
        3: 'S',
        4: 'M',
        5: 'L',
        6: 'XL',
        7: 'XXL',
        8: 'XXXL'
    },
    'Ukraine': {
        1: 42,
        2: 44,
        3: 46,
        4: 48,
        5: 50,
        6: 52,
        7: 54,
        8: 56
    },
    'Germany': {
        1: 36,
        2: 38,
        3: 40,
        4: 42,
        5: 44,
        6: 46,
        7: 48,
        8: 50
    },
    'USA': {
        1: 8,
        2: 10,
        3: 12,
        4: 14,
        5: 16,
        6: 18,
        7: 20,
        8: 22
    },
    'France': {
        1: 38,
        2: 40,
        3: 42,
        4: 44,
        5: 46,
        6: 48,
        7: 50,
        8: 52
    },
    'UK': {
        1: 24,
        2: 26,
        3: 28,
        4: 30,
        5: 32,
        6: 34,
        7: 36,
        8: 38
    }
}

keyboard = input('Enter desired iternational size table output e.g. XXS, XS, S, M, L, XL, XXL, XXXL: ')

#function to get key from International size table
def get_int_key(value):
    for k,v in underwear.items():
        for i, patt in v.items():
            if patt == value:
                return i

#function to show all sizes according to inserted one
def show_all():
    for key, sub_dict in underwear.items():
        print(key, sub_dict[get_int_key(keyboard)])

show_all()

