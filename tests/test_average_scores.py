import unittest
from dictionary_update import average_scores


class MyTestCase(unittest.TestCase):

    def test_average(self):
        # Arrange
self.scores_dict = {'Test 1': 31, 'Test 2': 34, 'Test 3': 54}
    expected = 39.6666666
    # Act
    actual = average_scores(self.scores_dict)
        # Assert
    self.assertAlmostEqual(expected, actual)
