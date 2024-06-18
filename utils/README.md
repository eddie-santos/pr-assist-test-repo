# Utils

This module containers helper functions that can be imported,
primarily to be used in the webapp. Functions should only
appear here if they are imported. 

## Algorithms

Below we chronicle which algorithms are covered in `algorithms.py`,
and give some context about their historical significance, if applicable.

## Fibonacci

The algorithm is as follows:

1. Start with values `0` and `1`.
2. Sum the values to get the next number in the sequence.
3. Repeat step 2 until you have `n` terms in the sequence.

You should get `[0, 1, 1, 2, 3, 5, 8, ...]`

## Power

## Binary search

Given a list of values in monotically increasing order and a target
value, this finds where in the given list the value occurs,
returning the index.

It is implemented in as `binary_search(arr, target)`.