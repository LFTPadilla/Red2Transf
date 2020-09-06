#Taken from: https://www.journaldev.com/15899/python-unittest-unit-test-example
import unittest
from unittest import TestCase as tc 
import numpy as np
import back

class TestMyBack(tc):
    def test_generate_fragments(self):
        my_list = (np.array([['1500','0','0','1','0000000000000','0','0x2000'],
                             ['1500','0','0','1','0000010111001','1480','0x20b9'],
                             ['548','0','0','0','0000101110010','2960','0x172']]))
        
        to_compare = back.generate_fragments(3508,1500)
        self.assertEqual(my_list.tolist(), to_compare.tolist())

if __name__ == "__main__":
    unittest.main()