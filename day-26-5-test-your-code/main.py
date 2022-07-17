weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}
# 🚨 Don't change code above 👆


#First *fork* your copy. Then copy-paste your code below this line 👇
#Finally click "Run" to execute the tests

weather_f = {day:round(weather*1.8+32,2) for (day,weather) in weather_c.items()}

print(weather_f)























































#Write your code above this line 👆
# 🚨 Do NOT modify the code below this line 👇

with open('testing_copy.py', 'w') as file:
  file.write('def test_func():\n')
  with open('main.py', 'r') as original:
    f2 = original.readlines()[0:40]
    for x in f2:
      file.write("    " + x)

with open('testing_copy_2.py', 'w') as file:
  file.write('weather_c = {"Monday": 16, "Tuesday": 18, "Wednesday": 21, "Thursday": 33, "Friday": 29, "Saturday": 2, "Sunday": 10}\n\n')
  file.write('def test_func():\n')
  with open('main.py', 'r') as original:
    f2 = original.readlines()[10:40]
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
      expected_print = "{'Monday': 53.6, 'Tuesday': 57.2, 'Wednesday': 59.0, 'Thursday': 57.2, 'Friday': 69.8, 'Saturday': 71.6, 'Sunday': 75.2}\n"
      self.assertEqual(fake_out.getvalue(), expected_print) 

  def test_2(self): 
    with patch('sys.stdout', new = StringIO()) as fake_out:
      testing_copy_2.test_func()
      expected_print = "{'Monday': 60.8, 'Tuesday': 64.4, 'Wednesday': 69.8, 'Thursday': 91.4, 'Friday': 84.2, 'Saturday': 35.6, 'Sunday': 50.0}\n"
      self.assertEqual(fake_out.getvalue(), expected_print) 


print('\n\n\n.\n.\n.')
print('Checking if what you printed is a dictionary containing individual days as the key and the converted temperature as the value ...')
print('Running some tests on your code:')
print('.\n.\n.\n.')
unittest.main(verbosity=1, exit=False)

os.remove('testing_copy.py') 
os.remove('testing_copy_2.py') 
