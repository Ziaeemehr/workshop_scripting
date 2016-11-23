program hwtest
implicit none
real(8) :: r1, r2 ,s
r1 = 1.d0
r2 = 0.d0
s = hw1(r1, r2)
write(*,*) 'hw1, result:',s
write(*,*) 'hw2, result:'
call hw2(r1, r2)
call hw3(r1, r2, s)
write(*,*) 'hw3, result:', s

 contains
function hw1(r1, r2)
implicit none
real(8), intent(in) :: r1, r2
real(8) :: hw1
hw1 = sin(r1 + r2)
return
end

subroutine hw2(r1, r2)
implicit none
real(8),intent(in) :: r1, r2
real(8) :: s  ! result
s = sin(r1 + r2)
write(*,*) 'Hello, World! sin(', r1+r2, ')=', s
return
end

!     special version of hw1 where the result is
!     returned as an argument:

subroutine hw3(r1, r2, s)
implicit none
real(8), intent(in) :: r1, r2
real(8) :: s
!f2py intent(out) s
s = sin(r1 + r2)
return
end

end program