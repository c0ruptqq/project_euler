logs:=$(patsubst %.py, %.py.log, $(wildcard *.py))

all: $(logs)

%.py.log: %.py
	python3 $< > $@