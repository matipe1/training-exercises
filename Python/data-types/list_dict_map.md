# Lists , Dictionaries and Maps

This is an exercise where I'm using Lists as principal iterables and a dictionary
where I have all the functions which correspond to each brought function (as string).

## The exercise consists in...

The system has a main list as a variable. Based in this list, the system
receives as first input the amount of lines the person will bring to.
Then, each line has 7 possible functions to pass (to add into the main list)
and as an example the correct format is:
    
    3
    append 8
    insert 1 22
    print

    # Output: [8, 22]

This is how the lines has to be written, it's an exercise from Hackerrank and I thought
it is very useful to learn working with dictionaries, and still having practice with maps.

### Explanation of Some things inside the code

Firstly, I've created a dictionary with the indexes as strings equal to the names
of the functions I'll use. Each item of the dictionary has the correct form that the functions
will be called. 

Then, I will add, into the variable 'func', the index of the corresponding command brought. 
And into the variable 'arguments', I will add a tuple created with the **'map'** function, which consists in iterate
each item from the variable 'command' with sub index 1 (forward). It will have the format: (0, 5) for example.

Finally, there is a condition where I ask if the line has just one element, I mean just the function, it
will be executed, if it is the argument 'print', just execute the printing of the list and if it is a function
with at least one argument, it will be added inside the parentheses as a parameter, with a * before the variable,
it is to add an undefined amount of parameters.