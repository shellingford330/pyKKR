cimport numpy as np

cdef class MahaDist:
    cdef np.ndarray bandwidth
    cdef preprocessor
    cpdef np.ndarray get_distance_matrix(self, double[:, :] a, double[:, :] b=?)
    cpdef double[:, :] get_distance_matrix_c(self, double[:, :] a, double[:, :] b=?)
    cpdef np.ndarray get_distance_matrix_gradient(self, double[:, :] a, double[:, :] b=?)
