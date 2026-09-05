# Calculator Project

simple example project for a good approach for a layered package with one framework-independent core. The console, Flask/API, and PyQt projects become thin entry points that call the same application services.


CLI-first Python calculator structured so its core logic can later be reused by Flask and PyQt interfaces.

## Initial structure

```text
calculator_project/
|-- .env.example
|-- .env
|-- .gitignore
|-- pyproject.toml
|-- README.md
|-- src/
|   `-- calculator/
|       |-- __init__.py
|       |-- config.py
|       |-- core/
|       |   |-- __init__.py
|       |   `-- calculator.py
|       |-- infrastructure/
|       |   |-- __init__.py
|       |   `-- oracle/
|       |       `-- __init__.py
|       `-- cli/
|           |-- __init__.py
|           `-- main.py
`-- tests/
    |-- __init__.py
    `-- test_calculator.py
```

The `core` package will contain reusable calculator logic. The `cli` package will contain command-line input and output only. Oracle-specific code will live under `infrastructure/oracle`.

## Reusable calculator

```python
from calculator import Calculator

calculator = Calculator()
result = calculator.add(10, 2)
```