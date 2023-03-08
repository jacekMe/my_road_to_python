""" The followin is a recursive algorithm for generating the lyrics of the 
popular folk song '99 bottles of beer on the wall'."""


def bottles_of_beer(bob):
    """
    Displays the lyrics of the song 99 bottles of beer one the wall.
    :param bob: must be a positive number"""

    if bob < 1:
        print("""No more beer bottles on the wall
            There are no more beer bottles.""")
        return
    tmp = bob
    bob -= 1
    print("""{} beer bottles on the wall.
    {} bottles of beer. Take one and pass it around {} bottles of beer. Take one and pass it around.""".format(tmp, tmp, bob))

    bottles_of_beer(bob)

bottles_of_beer(99)