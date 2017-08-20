# Implementation in Python, based on unit tests.


class WarehouseImpl:
    def __init__(self):
        self.inventory = {}

    def add(self, good, count):
        try:
            self.inventory[good] += count
        except KeyError:
            self.inventory[good] = count

    def getInventory(self, good):
        return self.inventory[good]

class Order:
    def __init__(self, good, count):
        self.good = good
        self.count = count
        self.filled = False

    def fill(self, usedWarehouse):
        inStock = usedWarehouse.getInventory(self.good)
        if self.count <= inStock:
            usedWarehouse.add(self.good, -self.count)
            self.filled = True

    def isFilled(self):
        return self.filled
