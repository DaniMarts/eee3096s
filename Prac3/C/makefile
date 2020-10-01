.RECIPEPREFIX +=
CC = g++ #arm-linux-gnueabihf-g++
CFLAGS = -lm -lrt -O0 
INCLUDE = -ITools

# this bit-width and thread-count will be modified by run_tests.py, to run for different bit-widths and thread-counts, respectively
BIT_WIDTH = float
THREAD_COUNT = 32
REPEAT = 3  # the number of times the programs will run, for cache warming

PROG = bin/*
OBJS = obj/*


default:
    mkdir -p bin obj
    $(CC) $(INCLUDE) $(CFLAGS) -c src/CHeterodyning.c -o obj/CHeterodyning.o
    $(CC) $(INCLUDE) $(CFLAGS) -c Tools/Timer.cpp -o obj/Timer.o
    $(CC) -o bin/CHeterodyning obj/CHeterodyning.o obj/Timer.o $(CFLAGS)

threaded:
    mkdir -p bin obj
    $(CC) $(INCLUDE) $(CFLAGS) -c src/CHeterodyning_threaded.c -o obj/CHeterodyning_threaded.o
    $(CC) $(INCLUDE) $(CFLAGS) -c Tools/Timer.cpp -o obj/Timer.o
    $(CC) -o bin/CHeterodyning_threaded obj/CHeterodyning_threaded.o obj/Timer.o $(CFLAGS) -pthread

run:
    bin/CHeterodyning

run_threaded:
    bin/CHeterodyning_threaded
    

clean: 
    rm -rf $(PROG) $(OBJS) 

run_many:
    # a simple shell script to run CHeterodyning multiple times, writting the
    counter=$(REPEAT); \
    cd .. && python3 write_flags.py flags unthreaded $(BIT_WIDTH) $(CFLAGS) ; \
    while [ $$counter -gt 0 ]; \
        do \
            C/bin/CHeterodyning; \
            counter=$$(( $$counter - 1)); \
        done; \
    python3 write_flags.py values unthreaded $(BIT_WIDTH) $(CFLAGS); \
    rm temp.txt

run_threaded_many:
    # a simple shell script to run CHeterodyning_threaded multiple times
    counter=$(REPEAT); \
    cd .. && python3 write_flags.py flags $(THREAD_COUNT) threads $(BIT_WIDTH) $(CFLAGS) ; \
    while [ $$counter -gt 0 ]; \
        do \
            C/bin/CHeterodyning; \
            counter=$$(( $$counter - 1)); \
        done; \
    python3 write_flags.py values $(THREAD_COUNT) threads $(BIT_WIDTH) $(CFLAGS); \
    rm temp.txt

