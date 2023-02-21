# Pascal's Triangle

This Technical Interview Prep contains tasks for working with Pascal's triangle.

## Tasks To Complete

+ [x] 0. **Pascal's Triangle**<br/>[0-pascal_triangle.py](0-pascal_triangle.py) contains a function `def pascal_triangle(n):` that returns a list of lists of integers representing the Pascal's triangle of `n`:
  + Returns an empty list if `n <= 0`.
  + You can assume `n` will be always an integer.

This version of the function includes a `try/except` block that attempts to convert the input to an integer. If the input cannot be converted to an integer (e.g., if it is a string or a float), an empty list is returned. Additionally, if the input is a non-positive integer, an empty list is also returned. These changes ensure that the function can handle a wider range of input and provide more informative error messages.