# Learning material in programming and data analysis.

This is the main development repository for new modules and courses
in programming and data analysis, including modules for business
studies, biology, and other departments as well as continuing 
education.

It is based on a shallow clone of git@github.com:jonasjul/IIFprog.git 

## git subtrees

Two other repositories have been included as subtrees

The exercise repository contains exercises published independently.
```
git remote add exercise 	git@github.com:hgeorgsch/dataprogexercises.git
git subtree add --prefix exercises exercise main
```

The iira2001 book repository started independently, but was included
because of duplication.  The assumoption is that the iira2001 repo
is superfluous and can be retired.
```
git remote add iira2001	git@git.ntnu.no:iirevu/iira2001h25-book.git 
git subtree add --prefix iira2001 iira2001 main
```
