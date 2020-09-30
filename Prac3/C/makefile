.RECIPEPREFIX +=
CC = g++ #arm-linux-gnueabihf-g++
CFLAGS = -lm -lrt -g
INCLUDE = -ITools
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
    # a simple shell script to run CHeterodyning multiple times
    counter=$(REPEAT); \
    cd .. && python3 write_flags.py $(CFLAGS); \
    while [ $$counter -gt 0 ]; \
        do \
            C/bin/CHeterodyning; \
            counter=$$(( $$counter - 1)); \
        done

run_threaded_many:
    # a simple shell script to run CHeterodyning_threaded multiple times
    counter=$(REPEAT); \
    python3 mypy.py $(CFLAGS); \
    while [ $$counter -gt 0 ]; \
        do \
            bin/CHeterodyning; \
            counter=$$(( $$counter - 1)); \
        done