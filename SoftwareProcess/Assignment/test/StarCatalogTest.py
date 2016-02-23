
import unittest
from Assignment.prod.StarCatalog import StarCatalog

class TestingClass(unittest.TestCase):

    # Test that an instance of StarCatalog is creates
    def initTestShouldInitialize(self):
        myStarCatalog = StarCatalog()
        self.assertIsInstance(myStarCatalog, StarCatalog)
        
    # Test that loadCatalog throws ValueError when
    #   starFile = None
    #   starFile ="DNE.txt"
    #   Magnitude = -45
    #   Magnitude = 20
    def loadCatalogNoneShouldThrowError(self):
        self.assertRaises(ValueError, StarCatalog.loadCatalog())
        
    def loadCatalogDNEShouldThrowError(self):
        self.assertRaises(ValueError, StarCatalog.loadCatalog("DNE.txt"))
        
    def loadCatalogOutOfBoundsMagnitudeShouldThrowError(self):
        self.assertRaises(ValueError, StarCatalog.loadCatalog("sao.txt", -45))
    