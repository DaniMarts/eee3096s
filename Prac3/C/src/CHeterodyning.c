#include "CHeterodyning.h"

extern float data [SAMPLE_COUNT];
extern float carrier[SAMPLE_COUNT];

float result [SAMPLE_COUNT];

int main(){
    printf("Running Unthreaded Test\n");
    printf("Precision sizeof %ld\n", sizeof(float));
    

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
    fprintf(fptr, "%.22f,", t*1000);  // printing the times with 22 decimal places
    fclose(fptr);

    return 0;
}
