import cython

cdef unsigned int geneIndex

@cython.locals(x=cython.double,i=cython.int)
cdef double _dot(list a, list b)

cdef class _Gene:
    cdef public unsigned int index
    cdef public bint enabled

cdef class Connect(_Gene):
    cdef public unsigned int start,end
    cdef public double weight, bias
    cpdef double value(self,list inputs, network)

cdef class Node(_Gene):
    cdef public str nodeType, activation
    cdef public unsigned int inputIndex
    @cython.locals(x=cython.list, y=cython.double, connect=Connect)
    cpdef double value(self,list inputs, network)