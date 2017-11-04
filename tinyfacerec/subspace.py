import numpy as np

def pca (X, y, num_components =0) :
    [n,d] = X. shape
    if ( num_components <= 0) or ( num_components >n):
        num_components = n
    mu = X. mean ( axis =0)
    X = X - mu
    if n>d:
        C = np. dot (X.T,X)
        [ eigenvalues , eigenvectors ] = np. linalg . eigh (C)
    else :
        C = np. dot (X,X.T)
        [ eigenvalues , eigenvectors ] = np. linalg . eigh (C)
        eigenvectors = np. dot (X.T, eigenvectors )
        for i in range (n):
            eigenvectors [:,i] = eigenvectors [:,i]/ np. linalg . norm ( eigenvectors [:,i])
    idx = np. argsort (- eigenvalues )   
    eigenvalues = eigenvalues [idx ]
    eigenvectors = eigenvectors [:, idx ]
# select only num_components
    eigenvalues = eigenvalues [0: num_components ]. copy ()
    eigenvectors = eigenvectors [: ,0: num_components ]. copy ()
    return [ eigenvalues , eigenvectors , mu]

def project (W, X, mu= None ):
    if mu is None :
        return np. dot (X,W)
    return np. dot (X - mu , W)


def reconstruct (W, Y, mu= None ):
    if mu is None :
        return np. dot (Y,W.T)
    return np. dot (Y, W.T) + mu

