import numpy as np
import matplotlib.pyplot as plt
def nasa_nozzle(t, x):
   t = t/10.;
   x[3] = x[3]/10.;

   mat = np.zeros((3, 3))
   mat[0, :] = [1, -1, 0]
   mat[1, :] = [1, 1, 0]
   mat[2, :] = [1, 1, np.cos((1./x[3] -1 ) * np.pi) - 1]

   a = np.dot(np.linalg.inv(mat), x[:3])

   s1 = a[0] + a[1] * np.cos(t * np.pi / x[3] - np.pi)
   s2 = a[0] + a[1] + a[2] * (np.cos(t * np.pi / x[3] - np.pi) - 1)

   s = np.append(s1[t < x[3]], s2[t >= x[3]])
   print(a, x[3], np.append(a, [x[3]]))
   return np.sqrt(s / np.pi), np.append(a, [x[3]])

t = np.linspace(0, 10, 100)
x = np.array([5. ** 2 * np.pi, 3. ** 2 * np.pi, 4. ** 2 * np.pi, 8.])
# A_in, A_throat, A_out, throat location
# x[3] >.5 and < 1
# x[0] and x[1] are > 0 and < a_up
# x[2] <= min(x[0], x[1])
# Generate ten different .msh files that satisfy this :)
# For a mesh file, we want to know which x's go with with it.
s = (nasa_nozzle(t, x))
plt.plot(t, s[0])
#plt.plot(t, s[0] ** 2 * np.pi)
plt.savefig('base.pdf')
plt.clf()
#fl = open('myfile.geo', 'r')
#   fl.write(s[0])
#fl.close()
print(s[0])
print('--')
print(s[1])
