from sets import HashSet
import unittest


class SetTest(unittest.TestCase):
    def test_init(self):
        hs = HashSet([1, 2, 3])
        assert hs.ht is not None
        assert hs.ht.size == 3
        assert hs is not None

    def test_size(self):
        hs = HashSet([1, 2, 3])
        assert hs.ht.size == 3
        assert hs.size == 3
        assert len(hs) == 3
        hs.add(4)
        assert hs.ht.size == 4
        assert hs.size == 4
        assert len(hs) == 4
        hs.remove(2)
        assert hs.ht.size == 3
        assert hs.size == 3
        assert len(hs) == 3

    def test_get(self):
        hs = HashSet([1, 2, 3])
        assert hs.get(2) == 2
        with self.assertRaises(KeyError):
            hs.get(4)

    def test_contains(self):
        hs = HashSet([1, 2, 3])
        assert hs.contains(2) == True
        assert hs.contains(4) == False

    def test_add(self):
        hs = HashSet([1, 2, 3])
        assert hs.items() == [1, 2, 3]
        # normal add
        hs.add(4)
        assert hs.items() == [1, 2, 3, 4]
        assert hs.size == 4

        # try to add duplicate
        hs.add(4)
        assert hs.items() == [1, 2, 3, 4]
        assert hs.size == 4

    def test_remove(self):
        hs = HashSet([1, 2, 3])
        assert hs.items() == [1, 2, 3]
        assert hs.contains(3) == True
        assert hs.size == 3

        # remove item
        hs.remove(3)
        assert hs.items() == [1, 2]
        assert hs.contains(3) == False
        assert hs.size == 2

        with self.assertRaises(KeyError):
            hs.remove(3)

    def test_items(self):
        hs = HashSet([1, 2, 3])
        assert hs.items() == [1, 2, 3]
        hs.add(4)
        assert hs.items() == [1, 2, 3, 4]

    def test_union(self):
        hs1 = HashSet([1, 2, 3, 4])
        hs2 = HashSet([2, 3, 4, 5])

        union = hs1.union(hs2)
        assert union.items() == [1, 2, 3, 4, 5]

    def test_intersection(self):
        hs1 = HashSet([1, 2, 3, 4])
        hs2 = HashSet([2, 3, 4, 5])

        intersection = hs1.intersection(hs2)
        assert intersection.items() == [2, 3, 4]

    def test_difference(self):
        hs1 = HashSet([1, 2, 3, 4])
        hs2 = HashSet([3, 4, 5])

        difference = hs1.difference(hs2)
        assert difference.items() == [1, 2, 5]

    def test_is_subset(self):
        hs1 = HashSet([1, 2, 3, 4, 5])
        hs2 = HashSet([2, 3, 4])

        assert hs1.is_subset(hs2) == True
        hs2.add(6)
        assert hs1.is_subset(hs2) == False