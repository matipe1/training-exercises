# Array Slicing

Array Slicing is the process of extracting a portion of an array.

With slicing, we can easily access elements in the array. It can be done on one or more dimensions of an Array.

## Syntax of Array Slicing

    array[start : stop : step]

* start: index of the first element to be included in the slice
* stop: index of the last element (excluded in the slice)
* step: step size between each element in the slice

When we're slicing, there is optional to write the start, stop and step part. If you omit 'start', slicing
starts from the first element of the string, it's similar with 'stop', slicing will continue up to the last element.
But if you omit step, default step size is 1.

I'll give you a complicated example of slicing:

    my_list = [500, 400, 300, 200, 100]

    my_list_two = my_list[:1:-1]
    print(my_list_two)  # Output: [100, 200, 300]

I've given you this example because it has a different interesting things.

The slice has not a start parameter, a 1 as a stop parameter and a -1 as a step parameter.

It means that it starts from the first index element but with -1 as a step, it means that
the slicing will start from the end until the stop index that is 1.