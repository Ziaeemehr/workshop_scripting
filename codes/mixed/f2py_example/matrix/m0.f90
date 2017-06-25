!FILE: M0.F90
SUBROUTINE mat(A,N)

! initialize a matrix and return it 

INTEGER N
REAL(8):: A(N*N)
    DO J=1,N
       DO I=1,N
          A((I-1)*N+J) = 1 
       ENDDO 
    ENDDO
END
! END FILE M0.F90
