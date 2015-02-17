#!/bin/bash

# Tyler McCraney

# Homework assignment 7
# 1. Write a shell script that downloads all of the pages on the EEB seminar website (1 through 800, example: https://www.eeb.ucla.edu/seminars.php?id=797) and saves it as 1.html, etc.
#    -Don't actually download all of the pages. Just write the shell script that would download them all.
#    -If you accidentally kick off a big task, use CTRL-C to cancel it.
#    -This can be accomplished with a single invocation of curl. Hint: man curl (or Google)

curl https://www.eeb.ucla.edu/seminars.php?id=[1-800] >> 1.html



