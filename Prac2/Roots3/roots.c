/* Biction Method for finding
   ==========================
   This program uses the Bisection method for finding roots of a fuction F. The
   function needs to be defined in the implementation of the F routine below.

   References:
   This program is an adaption of the code provided by
   https://justcode.me/numerical-computing/bisection-method-algorithm-flowchart-code-c/
   More information about the Bisection root finding method can be found at the above link.

*/

/* Includes */
#include"stdio.h"
#include"math.h"
#include "Timer.h"
#include "Timer.cpp"

#define DEBUG_LEVEL 0
   /* DEBUG_LEVEL indicates how much debug information you want
      Level 0 --> no debug output
      Level 1 --> displays iterations */

// Set INTERATIVE to 1 if you want the program to ask for start/end values
int INTERACTIVE = 0;

double F (double x)
/** This is the function for which you want to find roots
    specify the function you have implemented in F_STRING */
{
    #define F_STRING "3*x^4 + 2*x^2 - 1 = 0"
    // specify two approximations. low and high value to search
    #define DEFAULT_X1  -10
    #define DEFAULT_X2  10
    // specify the number of iterations
    #define ITERATIONS 15
    return(3*(pow(x,4))+2*pow(x,2)-1);//This return the value of the function
}

int main()
/** Main function, entry point to the application. */
{
    tic();
    int iter = ITERATIONS; // iteration number
    // Print intro information
    printf("Calculate bisection method in C\n Function: ");
    printf(F_STRING "\n");
    // Get the two approximation values
    double x0 = DEFAULT_X1,
           x1 = DEFAULT_X2;
    if (INTERACTIVE) {
            printf("Enter the first approximation to the root\n");
            scanf("%lf",&x0);
            printf("Enter the second approximation to the root\n");
            scanf("%lf",&x1);
            printf("Enter the number of iterations you want to perform\n");
            scanf("%d",&iter);
    }

    // Variables to be used during the iterations
    int ctr=1; // current iteration
    double l1=x0;
    double l2=x1;
    double r,f1,f2,f3;

    // -------------------- Initial checks ------------------------------
    // Check if initail approximations are actually the roots themselves
    if(F(l1)==0) r=l1;
    else if(F(l2)==0) r=l2;
    else {
     // This implementas the bisection algorithm
    while(ctr <= iter) {
      f1=F(l1);
      r=(l1+l2)/2.0;
      f2=F(r);
      f3=F(l2);
      if(f2==0) {
          r=f2;
          break;
        }
      #if(DEBUG_LEVEL>=1)
        printf("The root after %d iteration is %lf\n",ctr,r);
      #endif
      if(f1*f2<0) l2=r;
      else if (f2*f3<0) l1=r;
      ctr++;
      }
    }
    // Display the appriximated root found
    printf("The time it took is %lf\n", toc());
    printf("The approximation to the root is %lf\n",r);
}
