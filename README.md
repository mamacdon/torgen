## torgen
Generates random Toronto-inspired street names using [textgenrnn](https://github.com/minimaxir/textgenrnn).

### Requirements
- Python 3
- GNU Make

### Installation
1. Checkout the repo and use pip to install dependencies
    ```
    git checkout git@github.com:mamacdon/torgen.git
    pip3 install -r requirements.txt
    ```
    **Note:** the `requirements.txt` probably installs a bunch of unneeded dependencies, but Python makes this hard and I'm not an expert
    
    If you have trouble, try following the [textgenrnn instructions](https://github.com/minimaxir/textgenrnn#usage). Once you have textgenrnn
    installed correctly, torgen should run.

2. Train the model. This only has to be done once (unless you change the input data)
    ```
    make train
    ```

### Running it 

Finally the fun part! Generate some street names:
```
make run
<lots of warnings from Tensorflow>…

Temperature 0.3
--------------------------------------------------------------------
Prince Park Place
Harborough Avenue
Roselle Court
Brooker Lane
Roses Avenue

Temperature 0.5
--------------------------------------------------------------------
Harborough Avenue
Haven Valley Crescent
Langate Crescent
Pedring Drive
Prince Ander Drive

Temperature 1
--------------------------------------------------------------------
Glensan Road
Mongota Drive
Edma Place
Petterbrath Street
Empletrey Road

Temperature 1.25
--------------------------------------------------------------------
Derlilan Boulevard
Shiper Street
Himberant Drive
Exy Avenue
Scockhavstone Avenue
```

### License
MIT
