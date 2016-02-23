
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
    def loadCatalogNoneShouldThrowError(self):
        self.assertRaises(ValueError, StarCatalog.loadCatalog())
        
    def loadCatalogDNEShouldThrowError(self):
        self.assertRaises(ValueError, StarCatalog.loadCatalog("DNE.txt"))
        
    def loadCatalogOutOfBoundsMagnitudeShouldThrowError(self):
        self.assertRaises(ValueError, StarCatalog.loadCatalog("sao.txt", -45))
    
    # Test that loadCatalog populates when 
    #    starFile = "sao.txt" and Magnitude = 20
    #    starFile = "sao.txt" and Magnitude = 6.0 - default
    def loadCatalogValidShouldCreateList(self):
        self.assert_(StarCatalog.loadCatalog("sao.txt", 20) > 0, 'Catalog Populated')
    
    def loadCatalogDefaultShouldCreateList(self):
        self.assert_(StarCatalog.loadCatalog("sao.txt") > 0, 'Catalog Populated')
    
    # Test that emptyCatalog results in an empty list
    def emptyCatalogShouldResultInEmptyList(self):
        myStarCatalog = StarCatalog()
        myStarCatalog.loadCatalog("sao.txt")
        myStarCatalog.emptyCatalog()
        self.assert_(len(myCatalog) == 0, 'Catalog Emptied')