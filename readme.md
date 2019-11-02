LIGGGHTSER is a program that is able to automatically read data file printed or dumped by LIGGGHTS software.

Function include:
1.read dirs and files under current working directory.
2.find log/print/dump file and recognize them.
3.read data from these file and build a easy way to calculate.(dump/contact/ave/ part finished)
4.add some common calculation into package(two typical part finished)
5.Write a GUI for the program.(frame finished)
6.Give a way to add custom functions.(under developement)

Project start on 16th Oct 2019
Auther: D
E-mail: wangdi931010@gmail.com
Github: https://github.com/DiWang1010

Program haven't been packing, to try the function, please enter ./LIGGGHTSER

cd ./LIGGGHTSER

and install package LIGGGHTSER

python setup.py build

python setup.py install

then you can use LIGGGHTSER as a package of python by:

import LIGGGHTSER

if you want to try GUI, please enter ./ui 

cd ./ui

and try

python lgser.py(need python 3.6 above)

required package:

pyqt5 related
numpy
matplotlib