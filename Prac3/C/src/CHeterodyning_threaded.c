#include "CHeterodyning_threaded.h"

TYPE result [SAMPLE_COUNT];

// This is each thread's "main" function.  It receives a unique ID
void* Thread_Main(void* Parameter){
    int ID = *((int*)Parameter);
    //tic();
    int y;
    //Divide up array into number of threads
    for(y = ID*(SAMPLE_COUNT/Thread_Count); y < (ID+1)*(SAMPLE_COUNT/Thread_Count); y++){
        result[y]=0;
        result[y] += carrier[y]*data[y];
    }
    return 0;
}


// Point of entry into program
int main(){
    int j;
    // Initialise everything that requires initialisation
    tic();
    // Spawn threads...
    int       Thread_ID[Thread_Count]; // Structure to keep the thread ID
    pthread_t Thread   [Thread_Count]; // pThreads structure for thread admin

    for(j = 0; j < Thread_Count; j++){ //spawn threads
        Thread_ID[j] = j;
        pthread_create(Thread+j, 0, Thread_Main, Thread_ID+j);
    }

    // Printing stuff is a critical section...
    pthread_mutex_lock(&Mutex);
    printf("Threads created :-)\n");
    pthread_mutex_unlock(&Mutex);

    tic();
    // Wait for threads to finish
    for(j = 0; j < Thread_Count; j++){
        if(pthread_join(Thread[j], 0)){
            pthread_mutex_lock(&Mutex);
            printf("Problem joining thread %d\n", j);
            pthread_mutex_unlock(&Mutex);
        }
    }

  // No more active threads, so no more critical sections required
	double t = toc();
  printf("All threads have quit\n");
  printf("Time taken for threads to run = %lg ms\n", t/1e-3);

	// printing the execution times into a temporary txt file
	FILE *fptr = fopen("temp.txt", "a");
	fprintf(fptr, "%.5f,", t*1000);  // printing the times with 7 decimal places
	fclose(fptr);

  calc_error(py_res);

  return 0;
}
//------------------------------------------------------------------------------


// This must not be optimised
#pragma GCC push_options
#pragma GCC optimize ("O0")
float calc_error(float array[SAMPLE_COUNT]){
    // using an array of floats because that's what python uses
    float error = 0.0;

    for (int i = 0; i<SAMPLE_COUNT; i++ ){
        error += pow(result[i] - array[i], 2);
    }
    // on average, this is how much each result deviates from the python one
    error /= SAMPLE_COUNT;

    // printing the accuracy into a temporary txt file
    FILE *fptr = fopen("accuracy.txt", "w");
    fprintf(fptr, "%lg,", error);  // printing the error to a file
    fclose(fptr);

    // return the error
    return error;
}
#pragma pop_options