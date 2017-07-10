import numpy as np
import pylab as py

def DWVD(s):
    """
    Discrete Wigner-Ville distribution based on paper:
    O'Toole, J., Mesbah, M., & Boashash, B. (2005). A discrete time and
    frequency Wigner-Ville distribution: properties and implementation.
    
    Input:
      s - signal 1D in callable array.
      
    Output:
      W - 2D numpy array of N x 2N size with frequencies on vertical axis.
    """
    
    # Setting arrays
    N = s.size
    W = np.zeros((N, 2*N), dtype=np.complex64)
    
    piN = np.pi/float(N)
    
    # For frequencies
    for k in range(N):
        
        piNk = piN*k
    
        # For time shifts
        for n in range(2*N):
            
            # Limiting computational range
            l1 = max(0, n-N+1)
            l2 = min(n, N-1)
            
            m = np.arange(l1, l2)
            v = np.sum( s[m]*s[n-m]*np.exp(-2j*m*piNk) )
            
            W[k, n] = np.exp(1j*piNk*n)*v
            
        
    return np.flipud(np.real(W))
        
# Generating time line
fs = 128.
tMin, tMax = 0, 2.
t = np.arange(tMin, tMax, 1./fs)
N = t.size

# Range of frequencies to display.
# Maximum frequency is fs/4 .
fMin, fMax = 1, 32
iF2, iF1 = N*(1-2*fMin/fs), N*(1-2*fMax/fs)

# Normalising function
norm = lambda x: np.sqrt(np.sum(x**2))
    
# Generating signal
s1 = np.exp(-10*(t-0.5)**2)*np.cos(2*np.pi*11*t)
s2 = np.cos(2*np.pi*6*(1+t)*t)
s = s2

# Wigner transformation
Wtf = wigner(s)
#~ Wtf[Wtf<0] = 0

# Plotting output
py.figure()

im = py.imshow(Wtf[iF1:iF2 ,:],
            interpolation="hermite",
            extent=[0, N/fs, fMin, fMax], aspect='auto')

py.xlabel('Time [s]')
py.ylabel('Frequency [1/s]')
py.title("Wigner-Ville distribution")
py.colorbar()

py.show()
