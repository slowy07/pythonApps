# python linear algebra

## matrix and vector products

Function | Description
------------- | -------------
linalg.eigvals() | Compute the eigenvalues of a general matrix.
linalg.eigvalsh(a[, UPLO]) | Compute the eigenvalues of a complex Hermitian or real symmetric matrix.

## solving equations and iverting matices
Function | Description
------------- | -------------
matmul() | Matrix product of two arrays.
inner() | Inner product of two arrays.
outer() | Compute the outer product of two vectors.
linalg.multi_dot() | Compute the dot product of two or more arrays in a single function call, while automatically selecting the fastest evaluation order.
tensordot() | Compute tensor dot product along specified axes for arrays >= 1-D.
einsum() | Evaluates the Einstein summation convention on the operands.
einsum_path() | Evaluates the lowest cost contraction order for an einsum expression by considering the creation of intermediate arrays.
linalg.matrix_power() | Raise a square matrix to the (integer) power n.
kron() | Kronecker product of two arrays.

## special function
Function | Description
------------- | -------------
numpy.linalg.tensorsolve() | Solve the tensor equation a x = b for x.
numpy.linalg.inv() | Compute the (multiplicative) inverse of a matrix.
numpy.linalg.pinv() | Compute the (Moore-Penrose) pseudo-inverse of a matrix.
numpy.linalg.tensorinv() | Compute the ‘inverse’ of an N-dimensional array.
