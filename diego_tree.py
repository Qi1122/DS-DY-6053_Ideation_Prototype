from pptree import *

class DiegoIventory:

    def __init__(self, lifePath, function, head = None):
        self.lifePath = lifePath
        self.function = function
        self.interview = []
        if head:
            head.interview.append(self)

    def __str__(self):
        return self.lifePath

diego = DiegoIventory("DIEGO", " ")

careerPath = DiegoIventory("Career Path", " ", diego)
favoriteRources = DiegoIventory("Favorite Rources as UX designer", " ", diego)
interests = DiegoIventory("Interests", " ", diego)

# careerPath
italy = DiegoIventory("Italy", " ", careerPath)
college = DiegoIventory("diplomacy for bachelor degree", " ", italy)

london = DiegoIventory("London", " ", careerPath)
embassy = DiegoIventory("work for Italian embassy", " ", london)
startUp = DiegoIventory("work for a start up company as UX designer", " ", london)

newYork = DiegoIventory("New York", " ", careerPath)
tandon = DiegoIventory("IDM in Tandon NYU", " ", newYork)

#favoriteRources
nhNews = DiegoIventory("NH News", " ", favoriteRources)
yCombinator = DiegoIventory("Y Combinator", " ", favoriteRources)

#interests 
arduino = DiegoIventory("Arduino", " ", interests)
artusi = DiegoIventory("Artusi likes Wine project", " ", interests)

print_tree(diego, "interview", "lifePath")