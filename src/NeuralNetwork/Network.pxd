cdef class Network:
    cdef unsigned int nextNodeIndex, nextInputIndex
    cdef public list connectGenes, nodeGenes
    cdef public dict calculated