# Decoupled Demo

This demo repository shows a minimal example of how to use _recouple_ on a _decoupled_ model. Please refer to the documentation shown at the main [decouple repository](https://github.com/svenkreiss/decouple) and the paper [arXiv:1401.0080 \[hep-ph\]](http://arxiv.org/abs/1401.0080) for more information about `decouple` and `recouple`. 

For this demo, effective likelihoods and template parametrizations are hosted on the web on this projects [github page](http://svenkreiss.github.com/decoupledDemo). Create a `virtualenv`, install the main `decouple` package and its dependencies, and then run `make`:

```
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt

make
```

`make` downloads the decoupled files from the web, runs `recouple` and creates plots.

![kVkF](plots/kVkF.png)
![kVkF](plots/kGlukGamma.png)