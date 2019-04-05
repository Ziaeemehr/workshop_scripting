# profiling:
python -m cProfile -o hh2.cprof hh2.py
snakeviz hh2.cprof
