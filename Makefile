# 2 Jan 2014
# Sven Kreiss, Kyle Cranmer

# Adjust to your local installation of Decouple:
DECOUPLEPATH=~/physics/decouple/

# Keep unchanged for this example
REMOTEADDR=http://svenkreiss.github.io/decoupledDemo/data/



all:
	$(MAKE) download
	$(MAKE) recouple
	$(MAKE) plots

clean:
	rm -rf decoupled recoupled plots


decoupled/%:
	@echo Download $*
	mkdir -p decoupled
	wget -P decoupled/ $(REMOTEADDR)$*

download: \
		decoupled/2ph_effectiveLikelihood.root \
		decoupled/4l_effectiveLikelihood.root \
		decoupled/lvlv_effectiveLikelihood.root \
		\
		decoupled/2ph_templateParametrization.pickle \
		decoupled/4l_templateParametrization.pickle \
		decoupled/lvlv_templateParametrization.pickle
	@echo Downloads done.



COMBINPUT  = decoupled/2ph_effectiveLikelihood.root:profiledNLL:decoupled/2ph_templateParametrization.pickle:generic10_learningFull:2
COMBINPUT += decoupled/4l_effectiveLikelihood.root:profiledNLL:decoupled/4l_templateParametrization.pickle:generic10_learningFull:2
COMBINPUT += decoupled/lvlv_effectiveLikelihood.root:profiledNLL:decoupled/lvlv_templateParametrization.pickle:generic10_learningFull:2

OPTIONS_COMB = --skip_muTmuW --options_kVkF='--range=0.65,-1.7,1.5,2.0 --bins=200,200' --options_kGlukGamma='--range=0.6,0.4,1.8,1.6 --bins=200,200'

recouple:
	mkdir -p recoupled
	python $(DECOUPLEPATH)/Decouple/recouple.py -i "$(COMBINPUT)" -o recoupled/ $(OPTIONS_COMB) --template=10
	python $(DECOUPLEPATH)/Decouple/recouple.py -i "$(COMBINPUT)" -o recoupled/ $(OPTIONS_COMB) --template=10 --wideGauss=1.3
	@echo Recouple done.




plots:
	python plot.py
	@echo Plots done.
