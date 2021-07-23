# How to contribute

Thank you for taking the time to read this! I hope we can work together to improve this flake8 plugin.

## Testing

We use pytest for our tests, and require 100% coverage. (Yes, i know this doesn't mean there aren't any bugs, but hey, it doesn't hurt!)

## Submitting changes

Please send a [GitHub Pull Request to gagelarsen](https://github.com/gagelarsen/flake8-typehinting/pull/new/master) with a clear list of what you've done (read more about [pull requests](http://help.github.com/pull-requests/)). When you send a pull request, we would love to see examples. We can always use more test coverage. Please follow our coding conventions (below) and make sure all of your commits are atomic (one feature per commit).

Always write a clear log message for your commits. One-line messages are fine for small changes, but bigger changes should look like this:

    $ git commit -m "A brief summary of the commit
    > 
    > A paragraph describing what changed and its impact."

## Coding conventions

Start reading our code and you'll get the hang of it. We optimize for readability:

  * You must use type hints.
  * Each flake8 check should be in it's own function.
  * If adding a new check it must be part of the pep484 standard.

Thanks,
Gage Larsen
