# Text Wrap

I submitted this exercise because I think it's important to start using some new modules or libraries like textwrap,
tkinter, math, as our own modules too. Because when you have a work, it's essential to know about using it, 
it's a basic thing you must know.

## Text wrapping and filling

This module provides some convenience functions due to these functions do all the work. If you're just wrapping 
or filling one or two text strings, there are two functions you should use:

* wrap(): wraps the single paragraph in text (a string) so every line is at most 'width' characters long.
Returns a list of output lines, without final newlines.

* fill(): wraps the single paragraph in text, and returns a single string containing the wrapped paragraph.
It's shorthand for "\n".join(wrap(text, ...))

### Conclusion

If I used wrap() function, it would return a list and not an output of each wrapped substring.

But, I consider it's important to have the list's point view, that's why I mentioned it.