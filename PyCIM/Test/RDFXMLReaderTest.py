# Copyright (C) 2010-2011 Richard Lincoln
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to
# deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
# sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.

import unittest

from PyCIM import cimread

from os.path import dirname, join

RDFXML_FILE = join(dirname(__file__), "Data", "EDF_AIGUE_v9.xml")

class RDFXMLReaderTestCase(unittest.TestCase):
    """Test CIM RDF/XML parsing.
    """

    def setUp(self):
        """The test runner will execute this method prior to each test.
        """
        pass


    def testParse(self):
        """Test CIM RDF/XML parsing.
        """
        d = cimread(RDFXML_FILE)

        self.assertEqual(len(d), 5660)

if __name__ == "__main__":
    import logging
    logging.basicConfig(level=logging.INFO)
    unittest.main()