# test_chorusyarn.py
"""
Tests for ChorusYarn module.
"""

import unittest
from chorusyarn import ChorusYarn

class TestChorusYarn(unittest.TestCase):
    """Test cases for ChorusYarn class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ChorusYarn()
        self.assertIsInstance(instance, ChorusYarn)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ChorusYarn()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
