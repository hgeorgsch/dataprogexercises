# Learning material in programming and data analysis.

This is the main development repository for new modules and courses
in programming and data analysis, including modules for business
studies, biology, and other departments as well as continuing 
education.

It is based on a shallow clone of git@github.com:jonasjul/IIFprog.git,
with other subprojects added.

## Contents

+ `dataprog-obsidian` is an obsidian vault with comprehensive notes 
  from several taught modules under development
+ `iir2001` is a Jupyter Book for IIRA2001 for IIF
+ `iir6001` is a Jupyter Book for IIRA6001 for EVU

## Build

+ `mkpynb.sh` makes Jupyter files from markdown (`jupytext`) and installs 
  them under under iira2001
+ `install.sh` installs slides from obsidian on the web page, but these
  have first to be built using obsidian
+ `iira2001/make.sh` builds the jupyter book, depending on the Jupyter
  files already being built by `mkpynb.sh` above
+ `iira6001/make.sh` builds the jupyter book, but this has not been updated
  and may not work

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
