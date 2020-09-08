from camelCase import *
import unittest

class TestCamelCase(unittest.TestCase):
    
    def test_valid_variable(self):
        valid_strings = ["this is a valid string", "this_is_a_valid_string", "this is 1 valid string"]
        
        for string in valid_strings:
            is_valid = is_valid_variable(string)
            self.assertTrue(is_valid)
    
    def test_invalid_variable(self):
        invalid_strings = ["_this is invalid", "this symbol is invalid: &", "so is this one: ₼", "1 thing I know is that this string is invalid"]
        
        for string in invalid_strings:
            is_valid = is_valid_variable(string)
            self.assertFalse(is_valid)
    
    def test_camel_single_word(self):
        inputs_and_expected_outputs = {
                "lower": "lower",
                "UPPER": "upper",
                "Title": "title",
                "loNGstRingofcharActErswITHranDOMCAPitALizAtioN": "longstringofcharacterswithrandomcapitalization",
                "S": "s"
            }
        
        for input_string, expected_output in inputs_and_expected_outputs.items():
            output = make_camel(input_string)
            self.assertEqual(output, expected_output)
    
    def test_camel_sentence(self):
        inputs_and_expected_outputs = {
                "all lower case": "allLowerCase",
                "ALL UPPER CASE": "allUpperCase",
                "All Title Case": "allTitleCase",
                "All regular capitalization": "allRegularCapitalization",
                "ranDOM CAPitALizAtioN": "randomCapitalization",
            }
        
        for input_string, expected_output in inputs_and_expected_outputs.items():
            output = make_camel(input_string)
            self.assertEqual(output, expected_output)
            
    def test_camel_whitespace(self):
        inputs = ["", " ", "     ", "\t", "\n"]
        expected_output = ""
        
        for string in inputs:
            output = make_camel(string)
            self.assertEqual(output, expected_output)


if __name__ == "__main__":
    unittest.main()
