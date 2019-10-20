from typing import List, Tuple


class Term:
    """A term in the form coef*x**degree
    """
    coef: int
    degree: int

    def __init__(self, degree: int, coef: int):
        """An initializer for the Term class
        """
        self.degree = degree
        self.coef = coef

    def __eq__(self, item) -> bool:
        """An implementation of the sub magic method for Polynomial.
        """
        if item.degree == self.degree:
            return True
        else:
            return False

    def __str__(self) -> str:
        """Returns self in a string representation
        """

        if self.degree == 0:
            return str(self.coef)
        elif self.degree == 1 and self.coef == 1:
            return 'x'
        elif self.degree == 1:
            return f'{self.coef}x'
        elif self.coef == 1:
            return f'x^{self.degree}'
        else:
            return f'{self.coef}x^{self.degree}'

    def __mul__(self, term):
        """Outputs a term which is the product of self and term
        """

        coef = term.coef * self.coef
        degree = term.degree + self.degree

        return Term(degree, coef)


class Polynomial:
    """A polynomial that is composed of term objects
    """
    terms: List[Term]

    def __init__(self, terms: List[Term]):
        """An initializer for the Polynomial class
        """

        self.terms = terms

    def __len__(self) -> int:
        """Returns the number of Term objects in terms
        """

        return len(self.terms)

    def __contains__(self, item: Term) -> bool:
        """Returns true if a term equals an item is in self
        """

        for term in self.terms:
            if term == item:
                return True

    def __add__(self, poly):
        """Outputs a polynomial which is the sum of self and poly
        """

        output = Polynomial(self.terms)

        for term in poly.terms:

            value = True

            for i in range(len(self)):
                if self.terms[i] == term:
                    output.terms[i].coef += term.coef
                    value = False
            if value:
                output.terms.append(term)

        return output

    def __sub__(self, poly):
        """Outputs a polynomial which is the difference of self and poly
        """

        output = Polynomial(self.terms)

        for term in poly.terms:
            value = True
            for i in range(len(self)):
                if self.terms[i] == term:
                    output.terms[i].coef += term.coef * -1
                    value = False
            if value:
                output.terms.append(Term(term.degree, term.coef * -1))

        return output

    def __mul__(self, poly):
        """Outputs a polynomial which is the product of self and poly
        """

        new_poly = Polynomial([])

        for term_x in self.terms:
            for term_y in poly.terms:
                new_poly + Polynomial([term_x * term_y])

        return Polynomial(new_poly.terms)

    def _sort(self):
        """Sorts the terms in self.terms into descending order of degree
        """

        new_terms = []

        for _ in range(len(self)):
            biggest_degree = 0
            for i in range(1, len(self)):
                if self.terms[i].degree > self.terms[biggest_degree].degree:
                    biggest_degree = i

            new_terms.append(self.terms.pop(biggest_degree))

        self.terms = new_terms

    def __str__(self) -> str:
        """Returns self in a string representation
        """

        self._sort()

        output = ''
        for term in self.terms:
            if str(term)[0] == '-':
                output += ' - ' + str(term)[1:]
            else:
                output += ' + ' + str(term)

        if output[1] == '-':
            return '-' + output[3:]
        else:
            return output[3:]


def finder(n: int) -> Tuple[Polynomial, Polynomial]:
    """A recursive function to find the p and q polynomials at n
    """

    if n == 1:
        return Polynomial([Term(1, 1)]), Polynomial([Term(0, 1)])
    else:
        p_last, q_last = finder(n - 1)

        return Polynomial([Term(1, 1)]) * p_last - q_last * Polynomial([Term(0, 1), Term(2, -1)]), Polynomial([Term(1, 1)]) * q_last + p_last


if __name__ == '__main__':
    number = int(input('Please enter n: '))

    p, q = finder(number)
    print(f'q_{number}(x) = {q}')
    print(f'p_{number}(x) = {p}')
