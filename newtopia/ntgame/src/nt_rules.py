''' A collection of sub-routines related to Racial difference in newtopia. '''

''' Why not remove all this and make race an object?? You could then create a
race like 'Humnan' and create any race related rule inside the object.

So, for exmaple:

    Race.elite_offense = 9

    Then a province has a race and an army. To get a province's offense values
    you run a sub-routine that uses both it's Army object as well as it's Race
    object to get the answer.

    You can achieve the same thing for Build, Science etc.

    We can pull the game rules from an XML or JSON object here and provide
    convenience functions to the values. Alternatively, we could greate a game
    object that is stored in a sqllite DB (that's never touched).
'''

''' Normally this will return the number found in <army><specialists><off>4</...
'''
def off_spec_base():
    return 4


def def_spec_base():
    return 4
