from unittest import TestCase
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


class MyCollectionTest(TestCase):

    def test_that_item_can_be_added(self):
        c = df.MyCollection()
        a_value = 17
        self.assertFalse(c.has(a_value))
        c.add(a_value)

        self.assertTrue(c.has(a_value))


class ComparableTests(TestCase):

    def QQtest_that_files_with_same_length_are_called_equal(self):

        f1 = Comparable(fn1)


class TestExampleClass(TestCase):

    def test_that_class_can_be_created(self):
        c = df.ExampleClass()
        self.assertIsInstance(c, df.ExampleClass)
        # print("Success!")

