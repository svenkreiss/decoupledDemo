# Decoupled Demo

This demo repository shows a minimal example of how to use _recouple_ on a _decoupled_ model. Please refer to the documentation shown at the main [decouple repository](https://github.com/svenkreiss/decouple) and the paper for more information about `decouple.py` and `recouple.py`. 

Effective likelihoods and template parametrizations are hosted on the web. In this case, they are hosted on this projects [github page](http://svenkreiss.github.com/decoupledDemo). Before running `make`, adjust the `DECOUPLEPATH` in the `Makefile` to your location of _decouple_. Then run

```
make
```

which downloads the decoupled files from the web, runs `recouple.py` and creates plots.
