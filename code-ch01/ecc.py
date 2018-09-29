from unittest import TestCase


class FieldElement:

    def __init__(self, num, prime):
        self.num = num
        self.prime = prime
        if self.num >= self.prime or self.num < 0:
            error = 'Num {} not in field range 0 to {}'.format(
                self.num, self.prime-1)
            raise RuntimeError(error)

    def __eq__(self, other):
        if other is None:
            return False
        return self.num == other.num and self.prime == other.prime

    def __ne__(self, other):
        # this should be the inverse of the == operator
        raise NotImplementedError

    def __repr__(self):
        return 'FieldElement_{}({})'.format(self.prime, self.num)

    def __add__(self, other):
        if self.prime != other.prime:
            raise RuntimeError('Cannot add two numbers in different Fields')
        num = (self.num + other.num) % self.prime # <2>
        return self.__class__(num, self.prime) # <3>

    def __sub__(self, other):
        if self.prime != other.prime:
            raise RuntimeError('Cannot add two numbers in different Fields')
        raise NotImplementedError

    def __mul__(self, other):
        if self.prime != other.prime:
            raise RuntimeError('Cannot add two numbers in different Fields')
        raise NotImplementedError

    def __pow__(self, n):
        raise NotImplementedError

    def __truediv__(self, other):
        if self.prime != other.prime:
            raise RuntimeError('Cannot add two numbers in different Fields')
        raise NotImplementedError


class FieldElementTest(TestCase):

    def test_ne(self):
        a = FieldElement(2, 31)
        b = FieldElement(2, 31)        
        c = FieldElement(15, 31)
        self.assertEqual(a, b)
        self.assertTrue(a != c)
        self.assertFalse(a != b)
    
    def test_add(self):
        a = FieldElement(2, 31)
        b = FieldElement(15, 31)
        self.assertEqual(a+b, FieldElement(17, 31))
        a = FieldElement(17, 31)
        b = FieldElement(21, 31)
        self.assertEqual(a+b, FieldElement(7, 31))

    def test_sub(self):
        a = FieldElement(29, 31)
        b = FieldElement(4, 31)
        self.assertEqual(a-b, FieldElement(25, 31))
        a = FieldElement(15, 31)
        b = FieldElement(30, 31)
        self.assertEqual(a-b, FieldElement(16, 31))

    def test_mul(self):
        a = FieldElement(24, 31)
        b = FieldElement(19, 31)
        self.assertEqual(a*b, FieldElement(22, 31))

    def test_pow(self):
        a = FieldElement(17, 31)
        self.assertEqual(a**3, FieldElement(15, 31))
        a = FieldElement(5, 31)
        b = FieldElement(18, 31)
        self.assertEqual(a**5 * b, FieldElement(16, 31))

    def test_div(self):
        a = FieldElement(3, 31)
        b = FieldElement(24, 31)
        self.assertEqual(a/b, FieldElement(4, 31))
        a = FieldElement(17, 31)
        self.assertEqual(a**-3, FieldElement(29, 31))
        a = FieldElement(4, 31)
        b = FieldElement(11, 31)
        self.assertEqual(a**-4*b, FieldElement(13, 31))
