#include <iostream>
#include <stdio.h>
#include <vector>
#include <cmath>
#include <random>
#include <assert.h>

#include <gsl/gsl_rng.h>
#include <gsl/gsl_randist.h>
#include <gsl/gsl_sf_gamma.h>

#define RANDOM_GAUSS(S) gsl_ran_gaussian(gsl_rng_r, S)
#define INITIALIZE_RANDOM_CLOCK(seed)              \
    {                                              \
        gsl_rng_env_setup();                       \
        if (!getenv("GSL_RNG_SEED"))               \
            gsl_rng_default_seed = time(0) + seed; \
        gsl_rng_T = gsl_rng_default;               \
        gsl_rng_r = gsl_rng_alloc(gsl_rng_T);      \
    }
#define INITIALIZE_RANDOM_F(seed)             \
    {                                         \
        gsl_rng_env_setup();                  \
        if (!getenv("GSL_RNG_SEED"))          \
            gsl_rng_default_seed = seed;      \
        gsl_rng_T = gsl_rng_default;          \
        gsl_rng_r = gsl_rng_alloc(gsl_rng_T); \
    }
#define FREE_RANDOM gsl_rng_free(gsl_rng_r)

static const gsl_rng_type *gsl_rng_T;
static gsl_rng *gsl_rng_r;

using std::cout;
using std::endl;
using std::vector;

double rng_normal_skewed(const double alpha,
                         const double loc,
                         const double scale)
{
    // alpha control the skewness but it is different
    // loc and scale are the same parameters as in normal distribution

    double sigma = alpha / sqrt(1.0 + alpha * alpha);

    double u0 = RANDOM_GAUSS(1.0);
    double v0 = RANDOM_GAUSS(1.0);
    double u1 = sigma * u0 + sqrt(1.0 - sigma * sigma) * v0;

    if (u0 >= 0)
        return (u1 * scale + loc);
    return (-u1 * scale + loc);
}



// to calculate parameter alpha from skewness
double skewness_to_alpha(const double gamma)
{
    // The maximum (theoretical) skewness is obtained by setting delta =1 
    // in the skewness equation, giving gamma 0.9952717
    
    assert(std::abs(gamma) < 0.995217);

    double a = pow(std::abs(gamma), 2.0 / 3.0);
    double b = 0.5 * (4.0 - M_PI);
    double denom = 1.0 / (a + pow(b, 2.0 / 3.0));
    double delta = sqrt(0.5 * M_PI * a * denom);

    double alpha = delta / sqrt(1.0 - delta * delta);
    if (gamma >= 0)
        return alpha;
    return (-alpha);
}

int main()
{

    size_t n = 10000;
    constexpr double location = 0.0;
    constexpr double scale = 1.0;
    constexpr double skewness = 0.9;
    const double alpha = skewness_to_alpha(skewness);

    const int seed = 124;

    INITIALIZE_RANDOM_F(seed);
    for (size_t i = 0; i < n; i++)
    {
        cout << rng_normal_skewed(alpha, location, scale) << endl;
    }
    FREE_RANDOM;
}



// g++ 02_rng_with_skewness.cpp -lgsl -lgslcblas
// ./a.out>t
// plot in python
// pl.hist(np.loadtxt("t"), bins=100,  density=True); pl.show()


// to claculate the skewness
// from scipy.stats import skew
// skew(random_number_array)
