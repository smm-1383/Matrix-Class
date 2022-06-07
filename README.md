# Matrix

I wrote this class due to have a nice class which is pure python and its main idea came from calculating RREF of  matrices. I looked it up in github and  i saw some codes but none of them was completely what i want.

so i coded this class.
it also has a version which uses sympy and is not pure python.

## ps
[RREF](https://en.wikipedia.org/wiki/Row_echelon_form) explanation from wikipedia


## Why Fraction module is used?

```python
a = 0
for _ in range(10):
    a += 0.1
print(a)
```
a is not 1!

a is `0.9999999999999999`!

if you want to work with exact digits and little mistakes makes big differences in your project, `decimal` and `fraction` modules are great choices.

and also is so much cooler to see `12/7` instead of `1.7142857142857142`

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.
