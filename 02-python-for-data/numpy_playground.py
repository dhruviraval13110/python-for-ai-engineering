"""Runnable NumPy fundamentals."""
import numpy as np

def main():
    X=np.array([[1,2],[3,4],[5,6]],dtype=float)
    print('shape:',X.shape)
    print('column means:',X.mean(axis=0))
    print('broadcasted center:',X-X.mean(axis=0))
    print('Gram matrix:',X.T@X)

if __name__=='__main__': main()
