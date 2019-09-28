from collections import defaultdict

colours = (
            ('Yasoob', 'Yellow'),
                ('Ali', 'Blue'),
                    ('Arham', 'Green'),
                        ('Ali', 'Black'),
                            ('Yasoob', 'Red'),
                                ('Ahmed', 'Silver'),
                                )

favourite_colours = defaultdict(list)
favourite_colours = defaultdict(str)

for name, colour in colours:
    #favourite_colours[name].append(colour)
    favourite_colours[name] = colour
    print(favourite_colours)
