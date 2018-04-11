import numpy as np
from subprocess import Popen
from nasa import nasa_nozzle
x_min = [0, 0, 0, 5]
x_max = [5, 5, 5, 10]
logg = open('nozzles.log', 'w')
logg.write('nozzle A_in A_throat A_out l_throat x0 x1 x2 x3\n')
t = np.linspace(0, 10, 100)
for ii in range(10, 38):
   # x[2] <= min(x[0], x[1])
   fl = open('inputs%i.in'%ii, 'w')
   while True:
      # x[0] and x[1] are > 0 and < a_up and 5 < x[3] < 10
      x = np.random.uniform(x_min, x_max, 4)
      if x[1] <= min(x[0], x[2]) and x[1] >= 0.1 * min(x[0], x[2]):
         y = nasa_nozzle(t, x)[1]
         logg.write(' '.join([str(ii)] + [str(s) for s in x]) + ' ' + ' '.join([str(s) for s in y]) + '\n')
         fl.write(' '.join([str(s) for s in y]) + '\n') 
         #Popen(['sudo', './converter.sh', '%i.geo' % ii])
         break
   fl.close()
   #print('sh ./converter.sh %i.geo' % ii)
logg.close()
