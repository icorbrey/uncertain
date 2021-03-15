"""Defines the `Uncertain` number type."""


class Uncertain:
    """An uncertain value."""

    value = None
    delta = None

    def __init__(self, value, delta):
        """Creates an uncertain value with the given value and delta."""

        if not _is_number(value):
            raise TypeError(f'unsupported value type: \'{_typestr(value)}\'')

        if not _is_number(delta):
            raise TypeError(f'unsupported delta type: \'{_typestr(delta)}\'')

        self.value = value
        self.delta = abs(delta)

    def round(self, value_places=0, delta_places=0):
        """Rounds the uncertain value to a given number of places."""

        return Uncertain(
            value=round(self.value, value_places),
            delta=round(self.delta, delta_places),
        )

    def __add__(self, other):
        if _is_operable(other):
            return _add(self, other)
        return _throw_operands('+', self, other)

    def __radd__(self, other):
        if _is_operable(other):
            return _add(other, self)
        return _throw_operands('+', other, self)

    def __sub__(self, other):
        if _is_operable(other):
            return _sub(self, other)
        return _throw_operands('-', self, other)

    def __rsub__(self, other):
        if _is_operable(other):
            return _sub(other, self)
        return _throw_operands('-', other, self)

    def __mul__(self, other):
        if _is_operable(other):
            return _mul(self, other)
        return _throw_operands('*', self, other)

    def __rmul__(self, other):
        if _is_operable(other):
            return _mul(other, self)
        return _throw_operands('*', other, self)

    def __truediv__(self, other):
        if _is_operable(other):
            return _div(self, other)
        return _throw_operands('/', self, other)

    def __rtruediv__(self, other):
        if _is_operable(other):
            return _div(other, self)
        return _throw_operands('/', other, self)

    def __pow__(self, other):
        if _is_operable(other):
            return _pow(self, other)
        return _throw_operands('**', self, other)

    def __str__(self):
        return f'{self.value} ± {self.delta}'

    __repr__ = __str__
    __floordiv__ = __truediv__
    __rfloordiv__ = __rtruediv__

    def relative_err(self):
        """Returns the uncertain value's relative error."""

        return self.delta / self.value


def _add(left, right):
    """Adds two operable values and returns the result."""

    if _is_number(left) or _is_number(right):
        return _add_certain(left, right)
    return _add_uncertain(left, right)


def _add_certain(left, right):
    """Adds two values, where one is certain and the other is uncertain, and
        returns the result."""

    if _is_number(left):
        return Uncertain(
            value=right.value + left,
            delta=right.delta,
        )
    else:
        return Uncertain(
            value=left.value + right,
            delta=left.delta,
        )


def _add_uncertain(left, right):
    """Adds two uncertain values and returns the result."""

    return Uncertain(
        value=left.value + right.value,
        delta=left.delta + right.delta,
    )


def _sub(left, right):
    """Subtracts two operable values and returns the result."""

    if _is_number(left) or _is_number(right):
        return _sub_certain(left, right)
    return _sub_uncertain(left, right)


def _sub_certain(left, right):
    """Subtracts two values, where one is certain and the other is uncertain,
        and returns the result."""

    if _is_number(left):
        return Uncertain(
            value=left - right.value,
            delta=right.delta,
        )
    else:
        return Uncertain(
            value=left.value - right,
            delta=left.delta,
        )


def _sub_uncertain(left, right):
    """Subtracts two uncertain values and returns the result."""

    return Uncertain(
        value=left.value - right.value,
        delta=left.delta + right.delta,
    )


def _mul(left, right):
    """Multiplies two operable values and returns the result."""

    if _is_number(left) or _is_number(right):
        return _mul_certain(left, right)
    return _mul_uncertain(left, right)


def _mul_certain(left, right):
    """Multiplies two values, where one is certain and the other is uncertain,
        and returns the result."""

    if _is_number(left):
        return Uncertain(
            value=right.value * left,
            delta=right.delta,
        )
    else:
        return Uncertain(
            value=left.value * right,
            delta=left.delta,
        )


def _mul_uncertain(left, right):
    """Multiplies two uncertain values and returns the result."""

    return Uncertain(
        value=left.value * right.value,
        delta=left.value * right.value *
        (left.relative_err() + right.relative_err())
    )


def _div(left, right):
    """Divides two operable values and returns the result."""

    if _is_number(left) or _is_number(right):
        return _div_certain(left, right)
    return _div_uncertain(left, right)


def _div_certain(left, right):
    """Divides two values, where one is certain and the other is uncertain, and
        returns the result."""

    if _is_number(left):
        return Uncertain(
            value=right.value / left,
            delta=right.delta,
        )
    else:
        return Uncertain(
            value=left.value / right,
            delta=left.delta,
        )


def _div_uncertain(left, right):
    """Divides two uncertain values and returns the result."""

    return Uncertain(
        value=left.value / right.value,
        delta=left.value / right.value *
        (left.relative_err() + right.relative_err())
    )


def _pow(uncertain, power):
    """Takes the given uncertain value to the given power and returns the result."""

    return Uncertain(
        value=uncertain.value ** power,
        delta=uncertain.value ** power * power * uncertain.relative_err()
    )


def _throw_operands(operator, left, right):
    """Throws a TypeError outlining the given operator and the types of the operands."""
    raise TypeError(
        f'unsupported operand types for {operator}: '
        f'\'{_typestr(left)}\' and \'{_typestr(right)}\''
    )


def _typestr(value):
    """Returns the name of the given value's type."""

    return type(value).__name__


def _is_uncertain(value):
    """Returns whether the given value is an Uncertain value."""

    return isinstance(value, Uncertain)


def _is_number(value):
    """Returns whether the given value is either an integer or a float."""

    return isinstance(value, (int, float))


def _is_operable(value):
    """Returns whether the given value can be operated on with Uncertain
        objects."""

    return _is_number(value) or _is_uncertain(value)
