# 2 Jan 2014
# Sven Kreiss, Kyle Cranmer

REMOTEADDR=http://svenkreiss.github.io/decoupledBoilerplate/data/

all:
	$(MAKE) download
	$(MAKE) recouple
	$(MAKE) plots



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



recouple:
	@echo Recouple done.




plots:
	@echo Plots done.
