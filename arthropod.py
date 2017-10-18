class Arthropod:
    """Arthropod class to demonstrate OOP concepts"""

    def __init__(self, genus, species, poisonus = True, locomotion = 'crawl'):
        self.genus = genus
        self.species = species
        self.poisonus = poisonus
        self.locomotion = locomotion
             
    def scientific_name(self):
        """Find the scientific name of the arthropod"""
        return '{} {}'.format(self.genus, self.species)
        
    def locomotion_type(self):
        """Method to define how athropods move"""
        if self.genus == 'spider':
            self.locomotion = 'parachute'
        elif self.genus == 'ant':
            self.locomotion = 'crawl'
        elif self.genus == 'grasshopper':
            self.locomotion = 'hop'
        elif self.genus == 'bee':
            self.locomotion = 'fly'
        else:
            self.locomotion = 'crawl'

class Insect(Arthropod):
    """Class Insect extends class Arthropod"""
    def __init__(self, genus, species, poisonus, locomotion, edible):
        """Redefining Arthropod __init__ to include edible too"""
        super().__init__(genus, species, poisonus = False, locomotion = 'crawl')
        self.edible = edible
        
    def is_edible(self):
        '''Method to determine whether insect is edible or not'''
        if self.genus == 'termite':
            return True
        elif self.genus == 'ant':
            return False
        elif self.genus == 'grasshopper':
            return False
        elif self.genus == 'bee':
            return False
        else:
            return False

    def live_in_group(self):
        '''Method to determine whether insect lives in group or not'''
        if self.genus == 'termite':
            return True
        elif self.genus == 'ant':
            return False
        elif self.genus == 'grasshopper':
            return False
        elif self.genus == 'bee':
            return True
        #return False

class Arachnid(Arthropod):
    """Class Arachnid extends Arthropod"""
    def __init__(self, genus, species, poisonus, locomotion, pest):
        ''''Redefine __init__ to include pest'''
        super().__init__(genus, species, poisonus = True, locomotion = 'crawl')
        self.pest = pest

    def is_pest(self):
        '''Method to determine whether arachinid is pest or not'''
        if self.genus == 'spider':
            return False
        elif self.genus == 'tick':
            return True
        elif self.genus == 'scorpion':
            return False
        elif self.genus == 'mite':
            return True
        #return False

butterfly = Arachnid('Ant', 'Red speckled', False, 'fly', True)

#print(butterfly.scientific_name())
print(butterfly.is_pest())
    

            
            
        
        
            
            
            
        

    