#!/bin/sh

if test $2 = "" ; then
   lpr -P $2 $1
else
    lpr $1
fi