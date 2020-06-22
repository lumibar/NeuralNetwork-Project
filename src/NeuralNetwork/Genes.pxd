cdef unsigned int geneIndex

cdef class _Gene:
    cdef public int index
    cdef public bint enabled

cdef class Connect(_Gene):
    cdef public int start, end
    cdef public double weight, bias
    cpdef double value(self, double value)