#!/bin/sh

sh mkpynb.sh
( cd iira2001 ; sh make.sh )
( cd iira6001 ; sh make.sh )

