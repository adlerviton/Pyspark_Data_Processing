"""
Test goes here

"""

from main import PDdescribe
import pandas as pd


def test_desc():
    """Function calling PDdescribe"""
    data = {'A': [1, 2, 3, 4, 5], 'B': [10, 20, 30, 40, 50]}
    
    # Call the function to be tested
    result = PDdescribe(data)
    assert result.shape == (8, 2)
