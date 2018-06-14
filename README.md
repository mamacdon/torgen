## torgen
Generates random Toronto-inspired street names using [textgenrnn](https://github.com/minimaxir/textgenrnn).

### Requirements
- Python 3
- GNU Make

### Installation
Checkout the source repo, `cd` to it then run:
```
git checkout git@github.com:mamacdon/torgen.git
pip3 install
```

Note: the `requirements.txt` probably installs a bunch of unneeded dependencies, but Python makes this hard and I'm not an expert

### Running it 
Train the model. This only has to be done once (unless you change the input files)
```
make train
```

Finally the fun part! Generate some street names:
```
make run
```

### License
MIT
