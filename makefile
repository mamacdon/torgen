.PHONY: all clean corpus
TMPDIR := $(shell mktemp -d)

all:
	rmdir "$(TMPDIR)"

clean:
	echo deez nuts

train:
	python train.py

run: textgenrnn_weights.hdf5
	export PYTHONIOENCODING=UTF-8
	python gen.py
