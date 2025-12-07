# Calculator

A Python calculator implementation with comprehensive test coverage and input validation.

## Features

- **Basic Operations**: Addition, subtraction, multiplication, division
- **Advanced Operations**: Power, square root, modulo
- **Input Validation**: Ensures all inputs are within the range [-1,000,000, 1,000,000]
- **Error Handling**: Proper handling of edge cases (division by zero, negative square roots)
- **Comprehensive Testing**: 67 tests with 100% code coverage
- **AAA Test Pattern**: All tests follow Arrange-Act-Assert pattern for clarity

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Yutaro-Kashiwa/SystemDevelopment5th.git
cd SystemDevelopment5th
```

2. Create a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install pytest pytest-cov
```

## Usage

### Basic Usage

```python
from src.calculator.calculator import Calculator

# Create calculator instance
calc = Calculator()

# Basic operations
result = calc.add(5, 3)         # 8
result = calc.subtract(10, 3)   # 7
result = calc.multiply(4, 5)    # 20
result = calc.divide(10, 2)     # 5.0

# Advanced operations
result = calc.power(2, 3)       # 8
result = calc.square_root(16)   # 4.0
result = calc.modulo(10, 3)     # 1
```

### Input Validation

The calculator validates all inputs to ensure they are within the acceptable range:

```python
from src.calculator.calculator import Calculator, InvalidInputException

calc = Calculator()

# This will raise InvalidInputException
try:
    calc.add(2000000, 5)
except InvalidInputException as e:
    print(e)  # Input value 2000000 is outside the valid range [-1000000, 1000000]

# Values at boundaries work fine
result = calc.add(1000000, -1000000)  # 0
```

### Interactive CLI

Run the calculator in interactive mode:

```bash
python -m src.calculator.calculator
```

Available operations:
- `add`, `subtract`, `multiply`, `divide`
- `power`, `sqrt`, `modulo`
- `quit` to exit

## Testing

### Run All Tests

```bash
pytest tests/
```

### Run Tests with Verbose Output

```bash
pytest tests/test_calculator.py -v
```

### Generate Coverage Report

```bash
pytest --cov=src --cov-report=html tests/
```

View the HTML report:
```bash
open htmlcov/index.html
```

### Test Organization

Tests are organized into the following categories:
- **TestAddition**: Tests for addition operation
- **TestSubtraction**: Tests for subtraction operation
- **TestMultiplication**: Tests for multiplication operation
- **TestDivision**: Tests for division operation
- **TestPower**: Tests for power operation
- **TestSquareRoot**: Tests for square root operation
- **TestModulo**: Tests for modulo operation
- **TestInputValidation**: Tests for input validation
- **TestEdgeCases**: Tests for edge cases and boundaries

## Project Structure

```
SystemDevelopment5th/
├── src/
│   └── calculator/
│       ├── __init__.py
│       └── calculator.py          # Calculator implementation
├── tests/
│   ├── __init__.py
│   └── test_calculator.py         # Test suite (67 tests)
├── .gitignore
├── .coveragerc                    # Coverage configuration
├── setup.cfg                      # Project configuration
└── README.md
```

## API Documentation

### Calculator Class

#### Methods

**`add(a, b)`**
- Adds two numbers
- Raises `InvalidInputException` if inputs are outside valid range
- Returns: Sum of a and b

**`subtract(a, b)`**
- Subtracts b from a
- Raises `InvalidInputException` if inputs are outside valid range
- Returns: Difference of a and b

**`multiply(a, b)`**
- Multiplies two numbers
- Raises `InvalidInputException` if inputs are outside valid range
- Returns: Product of a and b

**`divide(a, b)`**
- Divides a by b
- Raises `InvalidInputException` if inputs are outside valid range
- Raises `ValueError` if b is zero
- Returns: Quotient of a and b

**`power(base, exponent)`**
- Raises base to the power of exponent
- Raises `InvalidInputException` if inputs are outside valid range
- Returns: base raised to the power of exponent

**`square_root(n)`**
- Calculates the square root of n
- Raises `InvalidInputException` if input is outside valid range
- Raises `ValueError` if n is negative
- Returns: Square root of n

**`modulo(a, b)`**
- Calculates a modulo b
- Raises `InvalidInputException` if inputs are outside valid range
- Raises `ValueError` if b is zero
- Returns: Remainder of a divided by b

### Constants

- `MAX_VALUE = 1000000`: Maximum allowed input value
- `MIN_VALUE = -1000000`: Minimum allowed input value

### Exceptions

**`InvalidInputException`**
- Raised when input values are outside the valid range [-1000000, 1000000]
- Inherits from `Exception`

## Development

### Running Tests During Development

```bash
# Watch mode (requires pytest-watch)
pip install pytest-watch
ptw
```

### Code Quality

The project follows Python best practices:
- Comprehensive docstrings for all methods
- Type hints where applicable
- Error handling for edge cases
- Input validation
- AAA test pattern

## Requirements

- Python 3.12+
- pytest 9.0+
- pytest-cov 7.0+

## License

This project is for educational purposes.

## Contributing

Contributions are welcome! Please ensure:
1. All tests pass
2. New features include tests
3. Tests follow AAA pattern
4. Code includes proper documentation

## Author

Yutaro Kashiwa

---

🤖 Generated with [Claude Code](https://claude.com/claude-code)
