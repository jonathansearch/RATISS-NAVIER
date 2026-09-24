"""Kernels SPH 3D (Müller et al. 2003). MIT."""
import numpy as np


def poly6(r, h):
    c = 315.0 / (64.0 * np.pi * h ** 9)
    return c * (h * h - r * r) ** 3


def spiky_grad(d, r, h):
    c = -45.0 / (np.pi * h ** 6)
    return (c * (h - r) ** 2 / np.maximum(r, 1e-12))[:, None] * d


def visco_lap(r, h):
    return 45.0 / (np.pi * h ** 6) * (h - r)
