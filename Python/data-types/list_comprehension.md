# List Comprehension

This is an exercise in which there is an implementation of list comprehension.

---

## The exercise consists in...
Firstly, the user has to add 4 values (a, b, c, d) and these will be used later to
return an ordered collection (or list) of nested lists,or in other words, it returns 
a **permutation** of the three first elements (a, b, c).

But there is one condition, and it is that the nested list that has the elements and the sum
of these elements is equal to the last value added, won't be added to the collection.

---

### Another way
There is another easy way to return the same element, but I wanted to add a function and 
the if-name-main conditional because I'm in a learning path and I try to implement everything
I think that makes projects more efficient of professional.

*The other simpler way:*

    a = int(input("valor a: "))
    b = int(input("valor b: "))
    c = int(input("valor c: "))
    d = int(input("valor d: "))
    
    print([[i, j, k] for i in range(a + 1) for j in range(b + 1) for k in range(c + 1) if not (i+j+k) == d]])
        
### Conclusion of List Comprehension:

* The **benefit** is that you only have to use one line of code.
* But the **cons** is that sometimes is hard to understand.
    