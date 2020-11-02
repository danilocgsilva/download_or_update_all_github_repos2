import sys

def getGivenUser() -> str:

    try:
        return sys.argv[1]
    except IndexError:
        return input("Please, give the Github name from address so I can fetch all your repositories: ")
