cdef unsigned int geneIndex

cdef class _Gene:
    cdef public int index
    cdef public bint enabled

cdef class Connect(_Gene):
    cdef public unsigned int start, end
    cdef public double weight, bias

cdef class Node(_Gene):
    cdef public str nodeType