#include "CHeterodyning.h"

extern TYPE data [SAMPLE_COUNT];
extern TYPE carrier[SAMPLE_COUNT];

TYPE result [SAMPLE_COUNT];

int main(){
    printf("Running Unthreaded Test\n");
    printf("Precision sizeof %ld\n", sizeof(TYPE));
    

    printf("Total amount of samples: %ld\n", sizeof(data) / sizeof(data[0]));
    

    tic(); // start the timer
    for (int i = 0;i<SAMPLE_COUNT;i++ ){
        result[i] = data[i] * carrier[i];
    }
    double t = toc();
    printf("Time: %lf ms\n",t/1e-3);
    printf("End Unthreaded Test\n");

    // printing the execution times into a temporary txt file
    FILE *fptr = fopen("temp.txt", "a");
    fprintf(fptr, "%.5f,", t*1000);  // printing the times in ms, with 5 decimal places
    fclose(fptr);

    calc_error(py_res);

    return 0;
}

// This must not be optimised
#pragma GCC push_options
#pragma GCC optimize ("O0")
float calc_error(float array[SAMPLE_COUNT]){
    // using an array of floats because that's what python uses
    float average_deviation = 0.0;
    int invalid = 0;

    for (int i = 0; i<SAMPLE_COUNT; i++ ){
        if (array[i] != 0.00000000000000000000000000000000000000000000)   // to avoid division by zero errors
            average_deviation += fabs(result[i] - array[i])/array[i];
        else
            invalid+=1;
    }
    printf("%d", invalid);
    // on average, this is how much each result deviates from the python one
    average_deviation /= SAMPLE_COUNT;
    average_deviation *= 100;  // in %

    // printing the accuracy into a temporary txt file
    FILE *fptr = fopen("accuracy.txt", "w");
    fprintf(fptr, "%.10f,", average_deviation);  // printing the times with 7 decimal places
    fclose(fptr);

    // return the average error as a percentage
    return average_deviation;
}
#pragma pop_options