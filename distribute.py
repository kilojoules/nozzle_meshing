import numpy as np
import matplotlib.pyplot as plt
from subprocess import Popen
from nasa import nasa_nozzle
np.random.seed(1234)
x_min = [0.5, 0.5, 0.5, 5]
x_max = [5, 5, 5, 8]
logg = open('nozzles.log', 'w')
logg.write('nozzle A_in A_throat A_out l_throat h_in h_throat h_nozzle x0 x1 x2 x3\n')
t = np.linspace(0, 10, 100)
for ii in range(40):
   # x[2] <= min(x[0], x[1])
   fl = open('inputs%i.in'%ii, 'w')
   while True:
      # x[0] and x[1] are > 0 and < a_up and 5 < x[3] < 10
      x = np.random.uniform(x_min, x_max, 4) 
      x[:3] = x[:3] ** 2 * np.pi
      #x = np.array([5. ** 2 * np.pi, 3. ** 2 * np.pi, 4. ** 2 * np.pi, 8.])
      if True:
      #if x[1] <= min(x[0], x[2]) and x[1] >= 0.1 * min(x[0], x[2]):
         s = (nasa_nozzle(t, x))
         #plt.plot(t, s[0])
         #plt.show()
         #y = nasa_nozzle(t, x)[1]
         plt.plot(t, s[0])
         plt.axis('equal')
         plt.savefig('%i.pdf'%ii)
         plt.clf()
         logg.write(' '.join([str(ii)]) + ' ' + ' '.join([str(_) for _ in x]) + ' ' + ' '.join([str(_) for _ in np.sqrt(x/np.pi)[:3]]) + ' ' + ' '.join([str(_) for _ in s[1]]) + '\n')
         fl.write(' '.join([str(_) for _ in s[1]]) + '\n') 
         #Popen(['sudo', './converter.sh', '%i.geo' % ii])
         break
   fl.close()
   #print('sh ./converter.sh %i.geo' % ii)
logg.close()
