import pytest
from app import roll_dice, roll_dice_multiple_times, probability_distribution
from collections import defaultdict

# Normal Test Cases
def test_roll_dice_standard():
    result = roll_dice(2, 6)
    assert 2 <= result <= 12  

def test_roll_dice_multiple_times_standard():
    results = roll_dice_multiple_times(2, 6, 3)
    assert len(results) == 3  
    for roll in results:
        assert 2 <= roll <= 12  

def test_probability_distribution_standard():
    probabilities = probability_distribution(1, 6)
    assert len(probabilities) == 6  
    assert all(1/6 == p for p in probabilities.values())  

# Edge Test Cases
def test_roll_dice_one_sided_die():
    result = roll_dice(1, 1)
    assert result == 1  

def test_roll_dice_multiple_times_zero_rolls():
    results = roll_dice_multiple_times(2, 6, 0)
    assert results == []  

def test_probability_distribution_zero_dice():
    probabilities = probability_distribution(0, 6)
    assert probabilities == {}  
