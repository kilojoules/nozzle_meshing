#requires params.in, a space deliniated list of 4 numbers and a output name as the argument
ii=1
cp template.geo $1
for l in $(cat inputs$2.in) ; do echo "s/NUM$ii/$l/g" ; sed -ie "s/NUM$ii/$l/g" $1 ; ii=$[ii+1] ; done
../gmsh-2.12.0-Linux/bin/gmsh -3 $1
