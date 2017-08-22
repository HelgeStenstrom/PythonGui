from unittest import TestCase
import tempfile
# http://docs.python.org/3/library/tempfile.html
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


class HashTests(TestCase):
    def setUp(self):
        self.f = tempfile.NamedTemporaryFile()

    def tearDown(self):
        self.f.close()

    def testKnownStringHash(self):
        string = b"abc"
        knownhash = "900150983cd24fb0d6963f7d28e17f72"
        self.f.write(string)
        self.f.flush()
        # TODO: Förstå varför filen inte tycks bli skriven i Windows. Filen finns, men utan innehåll.
        hash = df.hashfile(self.f.name)
        self.assertEqual(hash, knownhash)


class FileTests(TestCase):

    def test_object_creation(self):
        file = tempfile.NamedTemporaryFile()
        path = file.name
        fo = df.File(path)

    def test_that_file_has_a_length(self):
        a_file = tempfile.NamedTemporaryFile()
        l = 17  # arbitrary length
        a_file.write(b"x" * l)
        a_file.flush()

        fo = df.File(a_file.name)
        print("längden är", fo.length())
        self.assertEqual(fo.length(), l)

        a_file.close()


class DupFinderTests(TestCase):

    def fileWriter(self, name, contents):
        self.dir = tempfile.TemporaryDirectory().name
        f = tempfile.NamedTemporaryFile(prefix=name)
        f.write(contents)
        f.flush()
        return f

    def setUp(self):
        self.contents1 = b"one"
        self.contents2 = b"two"
        self.contents3 = b"three"
        self.fileWriter("f1", self.contents1)
        self.fileWriter("f2a", self.contents2)
        self.fileWriter("f2b", self.contents2)
        self.fileWriter("f3a", self.contents3)
        self.fileWriter("f3b", self.contents3)
        self.fileWriter("f3c", self.contents3)

    def test_that_dups_are_found(self):
        dir = self.dir
        print("scanning ", dir)
        dups = df.findDups(dir)
        print("dups:", dups)


class MyCollectionTest(TestCase):

    def test_that_item_can_be_added(self):
        c = df.MyCollection()
        a_value = 17
        self.assertFalse(c.has(a_value))
        c.add(a_value)

        self.assertTrue(c.has(a_value))
