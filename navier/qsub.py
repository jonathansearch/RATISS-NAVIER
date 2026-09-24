"""Concurrence Wootters (pur + mixte). MIT."""
import numpy as np

Y = np.array([[0, -1j], [1j, 0]], complex)


def concurrence(psi4):
    yy = np.kron(Y, Y)
    v = psi4.reshape(4)
    return float(abs(v.conj() @ yy @ v))


def concurrence_mixed(rho):
    yy = np.kron(Y, Y)
    r = rho @ yy @ rho.conj() @ yy
    ev = np.sort(np.real(np.linalg.eigvals(r)))[::-1]
    ev = np.maximum(ev, 0)
    return float(max(0, np.sqrt(ev[0]) - np.sqrt(ev[1]) - np.sqrt(ev[2]) - np.sqrt(ev[3])))
