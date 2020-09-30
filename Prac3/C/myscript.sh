# a simple shell script to run CHeterodyning multiple times
    counter=3; \
    python3 mypy.py $(CFLAGS); \
    while [ $$counter -gt 0 ]; \
        do \
            bin/CHeterodyning; \
            counter=$$(( $$counter - 1)); \
        done