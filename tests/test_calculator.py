"""
Test suite for the Calculator class.
"""

import pytest
from calculator.calculator import Calculator, InvalidInputException

@pytest.fixture
def memo():
    return print('this is a memo')

class TestAddition:
    """Tests for the add method."""

    def test_input_a(self):
        calc = Calculator()
        a = 100_000_001
        b = 1.0

        # Act
        with pytest.raises(InvalidInputException) as exc_info:
            _ = calc.add(a, b)

        assert 'outside the valid range' in str(exc_info.value)

    def test_input_b(self):
        calc = Calculator()
        a = 1
        b = 100_000_001

        # Act
        with pytest.raises(InvalidInputException) as exc_info:
            _ = calc.add(a, b)

        assert 'outside the valid range' in str(exc_info.value)

    def test_add_positive_numbers(self, memo):
        """Test adding two positive numbers."""
        # Arrange
        calc = Calculator()
        a = 5
        b = 3
        expected = 8

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == expected

    def test_add_negative_numbers(self):
        """Test adding two negative numbers."""
        # Arrange
        calc = Calculator()
        a = -5
        b = -3
        expected = -8

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == expected

    def test_add_positive_and_negative(self):
        """Test adding positive and negative numbers."""
        # Arrange
        calc = Calculator()
        a = 5
        b = -3
        expected = 2

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == expected

    def test_add_negative_and_positive(self):
        """Test adding negative and positive numbers."""
        # Arrange
        calc = Calculator()
        a = -5
        b = 3
        expected = -2

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == expected

    def test_add_positive_with_zero(self):
        """Test adding positive number with zero."""
        # Arrange
        calc = Calculator()
        a = 5
        b = 0
        expected = 5

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == expected

    def test_add_zero_with_positive(self):
        """Test adding zero with positive number."""
        # Arrange
        calc = Calculator()
        a = 0
        b = 5
        expected = 5

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == expected

    def test_add_floats(self):
        """Test adding floating point numbers."""
        # Arrange
        calc = Calculator()
        a = 2.5
        b = 3.7
        expected = 6.2

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == pytest.approx(expected)

    def test_add_max_value(self):
        """Test adding floating point numbers."""
        # Arrange
        calc = Calculator()
        a = 100_000_000
        b = 10
        expected = 100_000_010

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == pytest.approx(expected)

    def test_add_min_value(self):
        """Test adding floating point numbers."""
        # Arrange
        calc = Calculator()
        a = -100_000_000
        b = 10
        expected = -99_999_990

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == pytest.approx(expected)


class TestSubtraction:
    """Tests for the subtract method."""

    def test_input_a(self):
        calc = Calculator()
        a = 100_000_001
        b = 1.0

        # Act
        with pytest.raises(InvalidInputException) as exc_info:
            _ = calc.subtract(a, b)

        assert 'outside the valid range' in str(exc_info.value)

    def test_input_b(self):
        calc = Calculator()
        a = 1
        b = 100_000_001

        # Act
        with pytest.raises(InvalidInputException) as exc_info:
            _ = calc.subtract(a, b)

        assert 'outside the valid range' in str(exc_info.value)

    def test_subtract_positive_numbers(self):
        """Test subtracting positive numbers."""
        # TODO: Implement
        # Arrange
        calc = Calculator()
        a = 2.5
        b = 3.7
        expected = -1.2

        # Act
        result = calc.subtract(a, b)

        # Assert
        assert result == pytest.approx(expected)


class TestMultiplication:
    """Tests for the multiply method."""

    def test_input_a(self):
        calc = Calculator()
        a = 100_000_001
        b = 1.0

        # Act
        with pytest.raises(InvalidInputException) as exc_info:
            _ = calc.multiply(a, b)

        assert 'outside the valid range' in str(exc_info.value)

    def test_input_b(self):
        calc = Calculator()
        a = 1
        b = 100_000_001

        # Act
        with pytest.raises(InvalidInputException) as exc_info:
            _ = calc.multiply(a, b)

        assert 'outside the valid range' in str(exc_info.value)

    def test_multiply_positive_numbers(self):
        """Test multiplying positive numbers."""
        # TODO: Implement
        # Arrange
        calc = Calculator()
        a = 2.5
        b = 2.0
        expected = 5.0

        # Act
        result = calc.multiply(a, b)

        # Assert
        assert result == pytest.approx(expected)


class TestDivision:
    """Tests for the divide method."""

    def test_input_a(self):
        calc = Calculator()
        a = 100_000_001
        b = 1.0

        # Act
        with pytest.raises(InvalidInputException) as exc_info:
            _ = calc.divide(a, b)

        assert 'outside the valid range' in str(exc_info.value)

    def test_input_b(self):
        calc = Calculator()
        a = 1
        b = 100_000_001

        # Act
        with pytest.raises(InvalidInputException) as exc_info:
            _ = calc.divide(a, b)

        assert 'outside the valid range' in str(exc_info.value)

    def test_divide_positive_numbers(self):
        """Test dividing positive numbers."""
        # TODO: Implement
        # Arrange
        calc = Calculator()
        a = 6.0
        b = 1.5
        expected = 4.0

        # Act
        result = calc.divide(a, b)

        # Assert
        assert result == pytest.approx(expected)

    def test_divide_zero(self):
        calc = Calculator()
        a = 6.0
        b = 0

        with pytest.raises(ValueError) as exc_info:
            _ = calc.divide(a, b)

        assert 'Cannot divide by zero' == str(exc_info.value)


class TestInput:
    def test_input(self):
        calc = Calculator()
        a = 100_000_001
        b = 1.0

        # Act
        with pytest.raises(InvalidInputException) as _:
            _ = calc.divide(a, b)