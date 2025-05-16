# Bridgekeeper Revisited

So the Monty Python bridgekeeper returns for more antics. This time, though,
it's functional!

Your job is simply to implement the body of two functions. The rest of the
program is already written for you.
```
def get_yesno(prompt):
    ...
```
Replace the ellipsis placeholder with real code. The idea is that you will take
the supplied `prompt` parameter value and pass it as the prompt argument to
`input()`. You get the user's response to the input and return a bool value
according to the follows rules:

  - If the response is `y` or `yes` (exactly...don't worry about capitalized
    versions) then your function should return `True`.
  - Otherwise assume the answer is no and return `False`.

```
def get_number(prompt):
    ...
```
This is very similar, but you want to return an int instead of a bool. This is
also quite simple. Just `try` to convert the user's input using `int()` and
return it. If you get an exception during the conversion, then simply return the
special "no value" value of `None`.

That's it. But obviously examine `main()` to see how these functions are used.
And of cousre test it to make sure that the bridgekeeper behaves as expected.
A full run might look something like this:
```
What is your name? Paul
Hello Paul! You silly English knight!
Do you want to cross this bridge? y
Okay then. To cross you must answer a very difficult math problem.
It's very hard. And if you miss it, I will toss you off the bridge
and you will fall to your certain death.
Are you absolutely certain you want to cross this bridge? y
What do you get when you add 1 and 4? 5
Oh! You got it right. Fine. Cross and be gone!
```