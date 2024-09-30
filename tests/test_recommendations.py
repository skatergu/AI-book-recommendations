import unittest
from recommendation import recommend_by_filters

class TestRecommendation(unittest.TestCase):
    def test_recommend_by_genre(self):
        filters = {'genre': 'fantasy'}
        result = recommend_by_filters(filters)
        self.assertGreater(len(result), 0)
    
    def test_recommend_by_price(self):
        filters = {'price_range': [10, 15]}
        result = recommend_by_filters(filters)
        for book in result:
            self.assertGreaterEqual(book['Price'], 10)
            self.assertLessEqual(book['Price'], 15)

if __name__ == '__main__':
    unittest.main()
