from unittest import TestCase
import tempfile

import dupfinder as df

# Program som hittar dublett-filer.
# Behöver en fillista eller annan container, som kan traverseras.
# Behöver ett eller flera sätt att karakterisera filerna.
# 1. Längd
# 2. md5-summa
# 3. Själva filen
# 3.1  Första n bytes i filen
# 3.2  Hela filen

# Hur ska jag testa en funktion som hittar filer?

# TODO: Funktion som jämför två filer, och använder sig av extern funktion för jämförelsen

# TODO: en löv-cell beskrivning av en fil

class MakeTestFiles:
    pass

class HashTests(TestCase):
    def setUp(self):
        self.f = tempfile.NamedTemporaryFile()

    def tearDown(self):
        self.f.close()

    def testKnownStringHash(self):
        string  = b"abc"
        knownhash = "900150983cd24fb0d6963f7d28e17f72"
        self.f.write(string)
        self.f.flush()
        hash = df.hashfile(self.f.name)
        self.assertEqual(hash, knownhash)


class FileTests(TestCase):

    # TODO: platform-independent test files
    def test_object_creation(self):
        file = tempfile.NamedTemporaryFile()
        path = file.name
        fo = df.File(path)

    def test_that_file_has_a_length(self):
        aFile = tempfile.NamedTemporaryFile()
        l = 17 # arbitrary length
        aFile.write(b"x" * l)
        aFile.flush()

        fo = df.File(aFile.name)
        print("längden är", fo.length())
        self.assertEqual(fo.length(), l)

        aFile.close()



class MyCollectionTest(TestCase):

    def test_that_item_can_be_added(self):
        c = df.MyCollection()
        a_value = 17
        self.assertFalse(c.has(a_value))
        c.add(a_value)

        self.assertTrue(c.has(a_value))


class ComparableTests(TestCase):

    def QQtest_that_files_with_same_length_are_called_equal(self):
        pass


class TestExampleClass(TestCase):

    def test_that_class_can_be_created(self):
        c = df.ExampleClass()
        self.assertIsInstance(c, df.ExampleClass)
        # print("Success!")
