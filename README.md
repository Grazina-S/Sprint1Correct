# Basic calculator

The calculator performs basic arithmetical operations and stores the result of the last operation in memory. 

## Installation
pip install --index-url https://test.pypi.org/simple/grazincalculator

## Usage

- add - add any amount of numbers
- substract/divide - substracts/divide/multiply any amount of numbers. If memory is empty it will  take the first number from the list of arguments and use it as minuend/dividend. If memory is empty and only one argument is entered, minuend/dividend becomes 0.
- take nth degree root - when memory is empty, enter two arguments, number and a degree of the root. When memory is not empty, enter only degree of the root.
- reset - erase the memory of the calculator
