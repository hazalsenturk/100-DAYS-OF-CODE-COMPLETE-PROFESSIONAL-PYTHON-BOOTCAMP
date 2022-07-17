numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# 🚨 Do Not Change the code above

#First *fork* your copy. Then copy-paste your code below this line 👇
#Finally click "Run" to execute the tests

result = [num for num in numbers if num%2==0]

#Write your code 👆 above:

print(result)










































#Write your code above this line 👆
# 🚨 Do NOT modify the code below this line 👇

with open('testing_copy.py', 'w') as file:
  file.write('def test_func():\n')
  with open('main.py', 'r') as original:
    f2 = original.readlines()[0:40]
    for x in f2:
      file.write("    " + x)

with open('testing_copy_2.py', 'w') as file:
  file.write('numbers = [9, 0, 32, 8, 2, 8, 64, 29, 42, 99]\n\n')
  file.write('def test_func():\n')
  with open('main.py', 'r') as original:
    f2 = original.readlines()[2:40]
    for x in f2:
      file.write("    " + x)

import testing_copy
import testing_copy_2

import unittest
from unittest.mock import patch
from io import StringIO
import os

class MyTest(unittest.TestCase):
  def test_1(self): 
    with patch('sys.stdout', new=StringIO()) as fake_out: 
      testing_copy.test_func()
      expected_print = "[2, 8, 34]\n"
      self.assertEqual(fake_out.getvalue(), expected_print) 

  def test_2(self): 
    with patch('sys.stdout', new = StringIO()) as fake_out:
      testing_copy_2.test_func()
      expected_print = "[0, 32, 8, 2, 8, 64, 42]\n"
      self.assertEqual(fake_out.getvalue(), expected_print) 


print('\n\n\n.\n.\n.')
print('Checking if what you printed is a list containing just the even numbers ...')
print('Running some tests on your code:')
print('.\n.\n.\n.')
unittest.main(verbosity=1, exit=False)

os.remove('testing_copy.py') 
os.remove('testing_copy_2.py') 