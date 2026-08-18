This directory contains several jupyter books sharing pages.

The shared pages are sorted in topical directories, and each book
has its own directory, with symlinks to the shared topics that are
used.  Some shared assets are files

Currently in August 2026 we have the following books
+ iira6001

and the shared pages
+ Exercises (markdown - no executable code)
+ Public (git subtree - exercises shared publicly on github)
+ notebook (mostly first half of IIRA6001)
+ notebook2 (mostly second half of IIRA6001)
+ norun (notebooks checked in with execution output)

Additionally, there are shared assets
+ figures
+ hgs.bib (file in root)

The exercises repo is symlinked from outside this subtree, and has to be
reinstalled when this subtree is made its own git repo.

## git subtrees

The exercise repository contains exercises published independently.
```
git remote add exercise  git@github.com:hgeorgsch/dataprogexercises.git
git subtree add --prefix Public exercise main
```

### Updating

```sh
git remote add public 	git@github.com:hgeorgsch/dataprogexercises.git
git subtree add --prefix Public public main
git subtree pull --prefix Public public main
git subtree push --prefix=Public public main
```

