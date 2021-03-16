# uncertain

Defines a mathematically uncertain number type for scientific applications.
Uncertain values can be added, subtracted, multiplied, and divided by each
other and by constant integer and floating point values. Additionally,
uncertain values can be taken to the power of some constant integer or
floating point value.

## Usage

```py
from uncertain import Uncertain

x = Uncertain(4.0, 0.1)
y = Uncertain(6.0, 0.2)

print(x)       # 4.0 ± 0.1
print(x.value) # 4.0
print(x.delta) # 0.1

print(x + y)  # 10 ± 0.3
print(x - y)  # -2 ± 0.3
print(x * y)  # 24.0 ± 1.4
print(x / y)  # 0.6666666666666666 ± 0.03888888888888889
print(x ** 2) # 16.0 ± 0.8

print((x / y).round(2, 3)) # 0.67 ± 0.039
print((x / y).round(4, 3)) # 0.6667 ± 0.039
```
