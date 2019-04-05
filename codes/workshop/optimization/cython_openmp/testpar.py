def testpar(int n):
    cdef int i,numthreads 
    cdef int * squared
    cdef * tripled 
    cdef size_t size = 10

    with nogil.parallel(num_threads=4):
        numthreads = openmp.omp_get_num_threads()
        squared =  malloc(sizeof(int) * n)
        tripled =  malloc(sizeof(int) * n)
 
        for i in prange(n,schedule='dynamic'):
            squared[i] = i*i
            tripled[i]= i*i*i + squared[i]
 
        free(squared)
        free(tripled)