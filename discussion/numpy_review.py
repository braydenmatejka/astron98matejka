import numpy as np

# list1 = np.arange(0, 2*np.pi, (2*np.pi)/1000)
x1 = np.linspace(0, 2*np.pi, 1000)

x2 = 2*x1

filt = np.arange(101)

evens = filt[filt % 2 == 0]
oddsby7 = filt[(filt % 2 == 1) & (filt % 7 == 0)]
by10and5 = filt[(filt % 5 == 0) & (filt % 10 == 0)]
greater42 = filt[filt > 42]
mult235 = filt[(filt % 2 == 0) | (filt % 3 == 0) | (filt & 5 == 0)]

print(by10and5)

