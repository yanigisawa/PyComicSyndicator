from django.core.management import setup_environ
from django.utils import unittest
# import unittest

import testComicDbSettings
setup_environ(testComicDbSettings)
from comicdb.models import *

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.comic = Comic.objects.create(id=150000000, Name="Foo1", Url="Url1", ParserConstructor="Foo2")
        self.log = ComicLog.objects.create(ImageUrl="Url1", FetchDate="2011-04-01", ComicId=self.comic)

    def tearDown(self):
        self.comic.delete()
        self.log.dispose()

    def test_Basic(self):
        self.assertEqual(self.log.ImageUrl, "Url2")
        self.assertEqual(self.log.FetchDate, "4/2/2011")

if __name__ == "__main__":
    unittest.main()
