from phase_3 import MyApp
from helpers.widgets import tk_label, tk_options, tk_date_entry, tk_checkbox, tk_table
from helpers.utils import months_dict
import pandas as pd
import unittest
import pytest
import warnings
import requests

class widgetsModules(unittest.TestCase):

    @pytest.mark.asyncio
    # To start the tkinter window without launching it
    async def _start_app(self):
        self.main.mainloop()

    def setUp(self):
        warnings.filterwarnings("ignore")
        self.main = MyApp()
        self._start_app()

    def tearDown(self):
        self.main.destroy()
    
    # This test checks that a tkinter label is returned
    def test_tk_label(self):
        label = tk_label(self.main, "Test Label", 0, 0).winfo_class()
        expected = "Label"
        self.assertEqual(label, expected)
    
    # This test checks that a tkinter dropdown option is returned
    def test_options(self):
        drop_down = tk_options(self.main, 10, ["One"], 0, 0).winfo_class()
        expected = "Menubutton"
        self.assertEqual(drop_down, expected)
        
    # This test checks that a tkinter widget date is returned
    def test_date_entry(self):
        date = tk_date_entry(self.main, 0, 0).winfo_class()
        expected = "TEntry"
        self.assertEqual(date, expected)
        
    # This test checks that a checkbox is returned
    def test_checkbox(self):
        checkbox = tk_checkbox(self.main, 1, 'Test Checkbox', 0, 0).winfo_class()
        expected = "Checkbutton"
        self.assertEqual(checkbox, expected)
        
    # This test checks that a dictionary of 12 items is returned
    def test_month_dict(self):
        month_dict = months_dict()
        self.assertIsInstance(month_dict, dict)
        
        message = "There are only 12 months in a calendar year"
        month_dict_len = len(month_dict)
        expected = 12
        self.assertLessEqual(month_dict_len, expected, message)
        
        
if __name__ == "__main__":
    unittest.main(verbosity=2)