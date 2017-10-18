import unittest
from arthropod import Arthropod, Arachnid, Insect


class TestArthropod(unittest.TestCase):
    """Tests the Arthropod class"""

    def test_arthropod_instance(self):
        carpenter_ant = Arthropod('Ant', 'Red speckled', False, 'crawl')
        self.assertIsInstance(carpenter_ant, Arthropod, msg = 'The object should be an instance of the Arthropod class')

    def test_arachnid_instance(self):
        tick = Arachnid('Tick', 'domestic_tick', False, 'crawl', True)
        self.assertIsInstance(tick, Arachnid, msg = 'The object should be an instance of the Arachnid class')

    def test_insect_instance(self):
        grasshopper = Insect('Grasshopper', 'green grasshopper', False, 'crawl', True)
        self.assertIsInstance(grasshopper, Insect, msg = 'The object should be an instance of the Insect class')


    def test_object_type(self):
        carpenter_ant = Arthropod('Ant', 'Red speckled', False, 'crawl')
        self.assertTrue((type(carpenter_ant) is Arthropod), msg = 'The object should be a type of Arthropod')
        tick = Arachnid('Tick', 'domestic_tick', False, 'crawl', True)
        self.assertTrue((type(tick) is Arachnid), msg = 'The object should be a type of Arachnid')
        grasshopper = Insect('Grasshopper', 'green grasshopper', False, 'crawl', True)
        self.assertTrue((type(grasshopper) is Insect), msg = 'The object should be a type of Insect')

    def test_default_poisonus_state(self):
        carpenter_ant = Arthropod('Ant', 'Red speckled')
        self.assertEqual(True, carpenter_ant.poisonus, msg="The arthropod's poisonus should be True if no poisonus state was passed as an argument")

    def test_default_locomotion(self):
        carpenter_ant = Arthropod('Ant', 'Red speckled')
        self.assertEqual('crawl', carpenter_ant.locomotion, msg="The arthropod's locomotion should be crawl if no locomotion was passed as an argument")
    
    def test_scientific_name(self):
        grasshopper = Insect('Grasshopper', 'green grasshopper', False, 'crawl', True)
        self.assertEqual('Grasshopper-green grasshopper', grasshopper.scientific_name(), msg="The scientific name for the object should be 'object.genus'-'object.species'")
    
if __name__ == '__main__':
    unittest.main(exit=False)