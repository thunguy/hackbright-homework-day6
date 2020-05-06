"""Print out all the melons in our inventory."""


from melons import melon_names, melon_seedlessness, melon_prices, melons


def print_melons(melons):
    """Print each melon with corresponding attribute information."""
    
    for melon_name, attributes in melons.items():
        print(melon_name.upper())

        for attribute, value in attributes.items():
            print(f'{attribute}: {value}')

        print('===================================')


print(print_melons(melons))