import pytest
from pytest import raises
import random
import math
from simplemaths import SimpleMaths as sm
import yaml


class TestSimpleMaths(): 
    
    #YOU CANT HAVE INIT CONSTRUCTORS IN A TEST CLASS IN PYTHON. TEST CLASSES IN PYTHON ARE JUST 
    #THERE FOR STRUCTURAL REASONS.
#     def __init__(self, pos_int, pos_odd_int, neg_int, string, boolean, floating):
#         test_data = yaml.load(open('fixtures.yml'))
#         self.pos_int = test_data.get('positive')
#         self.pos_odd_int = test_data.get('positive_odd')
#         self.neg_int = test_data.get('negative')
#         self.string = test_data.get('string')
#         self.boolean = test_data.get('boolean')
#         self.floating = test_data.get('float')
    
    def test_constructor_positive(self):  # positive test on sm class constructor
        test_data = yaml.load(open('fixtures.yml'))
        pos_int = test_data.get('positive')[0]
        test_obj = sm(pos_int)
        assert test_obj.number == pos_int


    def test_constructor_boolean(self):
        test_data = yaml.load(open('fixtures.yml'))
        boolean = test_data.get('boolean')[0]
        with raises(TypeError):  # if TypeError is raised, the test passes
            test_obj = sm(boolean)


    def test_constructor_string(self):
        test_data = yaml.load(open('fixtures.yml'))
        string = test_data.get('string')[0]
        with raises(TypeError):  # if TypeError is raised, the test passes
            test_obj = sm(string)


    def test_constructor_float(self):
        test_data = yaml.load(open('fixtures.yml'))
        fl = test_data.get('float')[0]
        with raises(TypeError):  # if TypeError is raised, the test passes
            test_obj = sm(fl)  # random float between 1 and 10


    def test_square_positive(self):  # positive test on square method
        test_data = yaml.load(open('fixtures.yml'))
        pos_int = test_data.get('positive')[0]
        test_obj = sm(pos_int)
        test_obj_square = test_obj.square()
        assert(test_obj_square == math.pow(pos_int, 2))


    def test_factorial_positive(self):  # positive test on factorial method
        test_data = yaml.load(open('fixtures.yml'))
        pos_int = test_data.get('positive')[0]
        test_obj = sm(pos_int)
        test_obj_fact = test_obj.factorial()
        assert(test_obj_fact == math.factorial(pos_int))


    def test_power_positive(self):  # positive test on power method
        test_data = yaml.load(open('fixtures.yml'))
        pos_int = test_data.get('positive')[0]
        test_obj = sm(pos_int)
        test_power = random.randint(2, 5)
        test_obj_power = test_obj.power(test_power)
        assert(test_obj_power == math.pow(pos_int, test_power))


    def test_even_positive(self):  # positive test on odd/even method
        test_data = yaml.load(open('fixtures.yml'))
        pos_int = test_data.get('positive')[0]
        test_obj = sm(pos_int)
        obj_odd_even = test_obj.odd_or_even()
        odd_even_str = ""
        if (pos_int % 2) == 0:
            odd_even_str = 'Even'
        if (pos_int % 2) == 1:
            odd_even_str = "Odd"
        assert (obj_odd_even == odd_even_str)
        
    def test_odd_positive(self):  # positive test on odd/even method
        test_data = yaml.load(open('fixtures.yml'))
        pos_odd_int = test_data.get('positive_odd')[0]
        test_obj = sm(pos_odd_int)
        obj_odd_even = test_obj.odd_or_even()
        odd_even_str = ""
        if (pos_odd_int % 2) == 0:
            odd_even_str = 'Even'
        if (pos_odd_int % 2) == 1:
            odd_even_str = "Odd"
        assert (obj_odd_even == odd_even_str)
        


#     def test_square_root(self):  # positive test on square root method
#         test_obj_sqrt = test_obj.square_root()
#         assert (test_obj_sqrt == math.sqrt(integer))
