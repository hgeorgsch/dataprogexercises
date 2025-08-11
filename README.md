# Educational examples of interdiscplinary use of programming

This is a repository of programming exercises demonstrating
practical use of programming in different subjects.
The foundation of the repository was three exercises received
from [Morten Munthe](https://www4.uib.no/finn-ansatte/Morten.Munthe)
at the [PRIS conference](https://www.hivolda.no/pris-konferansen-2025)
in Ørsta March 2025.
The examples are intended for secondary school (VGS in Norway),
demonstrating the use of python and jupyter to explore large datasets.

## Formatting and use

Each exercise is written in `md:myst` which is easily converted
to Jupyter notebook format using jupytext.
To use, say, the Genetics exercise, you can download the git repo,
and rund
```sh
pip install -r requirements
cd Genetikk
jupytext --sync Genetikk.md
jupyter lab Genetikk.ipynb
```

If you edit the file, Jupyter lab will update both the notebook
and markdown versions.
The reason for publishing in the `md:myst` format, is to make
better use of the version control in git, which is important
for the development process.

It is possible to use Jupyter notebook, but Jupyter lab
makes a better display of some of the markdown coding enabled
by `md:myst`.

## Available Exercises

Each directory contains one exercise, including required data
sets, and sometimes supplementary documentation.
Two exercises have been prepared for use,
+ [Genetikk](Genetikk/Genetikk.md)
+ [Jordskjelv](Jordskjelv/Jordskjelv.md)
Other directories contain work in progress.

## Contributors

Authors and contributors are listed in each individual exercise.

**Editor:** Hans Georg Schaathun,
Norwegian University of Science and Technology,
hasc@ntnu.no

**Licensing** See each individual exercise.
