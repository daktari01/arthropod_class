class Arthropod:
    """Arthropod class to demonstrate OOP concepts"""
    no_of_legs = 6

    def __init__(self, classification, genus, species, poisonus = True, locomotion = 'crawl'):
        self.genus = genus
        self.species = species
        self.poisonus = poisonus
        self.locomotion = locomotion
        self.classification = classification
             
    def scientific_name(self, genus, species):
        """Find the scientific name of the arthropod"""
        return '{} {}'.format(genus, species)

    def number_of_legs(self, classification):
        if classification == 'Insect':
            self.no_of_legs = 6
        elif classification == 'Arachnid':
            self.no_of_legs = 8
        elif classification == 'Myriapod':
            self.no_of_legs >= 11
        else:
            self.no_of_legs = 10
        
    def locomotion_type(self, locomotion):
        
        
            
            
            
        

    