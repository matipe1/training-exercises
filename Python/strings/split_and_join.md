# Split and Join
These methods are from strings built-in functions of Python.

## Split
This method splits a string at the specified separator and returns a list of substrings.

Example:

    cars = 'Mercedez Benz-BMW-Tesla'
    
    print(cars.split('-')  # Output: ['Mercedez Benz', 'BMW', 'Tesla']

This method has 2 optional parameters, the first is the **separator** and the second the **maxsplit**

* Separator: Delimiter at which splits occur. If not provided, the string is split into whitespaces
* Maxsplit: Maximun number of splits. If not provided, there is no split number's limit

## Join
This method returns a string by joining all the elements of an iterable (list, string, tuple), 
separated by the given separator.

This method provides a flexible way to create strings from iterable objects.
It joins each element of an iterable by a string separator and returns a 
concatenated string.

Example:

    text = ['Python', 'is', 'a', 'fun', 'programming', 'language']

    print(' '.join(text))  # Output: Python is a fun programming language

This method has just one obligatory parameter, it's the **iterable**

* Iterable: List, Tuple, String, Dictionary, Set, or File objects and objects you define with a method
  (__iter__() or __getitem()__)
