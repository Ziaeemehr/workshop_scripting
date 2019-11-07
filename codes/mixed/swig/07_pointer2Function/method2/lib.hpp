double multiply(double x, double y)
{
    return x * y;
}

double myfun(double x, double y, double (*func)(double, double))
{
    // fprintf(stdout, "%g\n", multiply(x, y));
    return func(x, y);
}

// typedef double (*fptr_t)(double, double);
// fptr_t make_fptr()
// {
//     return multiply;
// }