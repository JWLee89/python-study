# Assertions

Source: 
1. [Python Tricks: A Buffet of Awesome Python Features 1st Edition](https://amzn.to/3g1eH4I)

Important points that I learned regarding assertions: 

## Dangers of assertions

1. **Assertions can be disabled**. 

Therefore, never write assertions to validate data, especially if the validation task
is to prevent erroneous inputs in sensitive or mission-critical operations.

From the book Python Tricks (example is modified), we can see that while the first test obviously passes,
we see something potentially strange in the second assert statement.

```python
assert 1 != 2, "Should never see this message since this test should always pass. "
print("Okay we established the obvious")
assert (1 == 2, 'should always fail')
print("Why is there no error?")
print("")
```

We get the following warning:

```python
SyntaxWarning: assertion is always true, perhaps remove parentheses?
assert (1 == 2, 'should always fail')
```

This is because we are passing a tuple to the assert statement, namely a tuple with two objects
`(1 == 2, 'should always fail')`. Non-empty tuples are truthy values in Python, which is why
we can potentially write erroneous assert statements if we are not careful.
