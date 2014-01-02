#!/usr/bin/env python

#  Created on: January 2, 2014

__author__ = "Sven Kreiss, Kyle Cranmer"
__version__ = "0.1"


import optparse
parser = optparse.OptionParser(version=__version__)
parser.add_option("-q", "--quiet", dest="verbose", action="store_false", default=True, help="Quiet output.")
options,args = parser.parse_args()


import ROOT
ROOT.gROOT.SetBatch( True )
import glob, re, os

import helperStyle
import PyROOTUtils

from Plot.utils import SMMarker, getContours, getSmallestBinMarker, getInterpolatedMinimumMarker, drawContours, drawH, draw_muTmuW_frame, draw_kVkF_frame, draw_kGlukGamma_frame







blackSolid = ROOT.TLine( 1.2,1.2,1.4,1.4 )
blackSolid.SetLineWidth( 2 )
blackSolidThin = ROOT.TLine( 1.2,1.2,1.4,1.4 )
blackSolidThin.SetLineWidth( 1 )
blackDashed = ROOT.TLine( 1.2,1.2,1.4,1.4 )
blackDashed.SetLineWidth( 2 )
blackDashed.SetLineStyle( ROOT.kDashed )
blackDashedThick = ROOT.TLine( 1.2,1.2,1.4,1.4 )
blackDashedThick.SetLineWidth( 3 )
blackDashedThick.SetLineStyle( ROOT.kDashed )
blackDotted = ROOT.TLine( 1.2,1.2,1.4,1.4 )
blackDotted.SetLineWidth( 2 )
blackDotted.SetLineStyle( ROOT.kDotted )
graySolid = ROOT.TLine( 1.2,1.2,1.4,1.4 )
graySolid.SetLineColor( ROOT.kGray )
graySolid.SetLineWidth( 2 )













def draw_CouplingContour( 
		model, opts, 
		color = ROOT.kRed, 
		lineStyle1s=ROOT.kSolid, lineStyle2s=ROOT.kDashed,
		lineWidth1s=2, lineWidth2s=2,
		couplingType = 'kVkF',
	):
	c68 = drawContours( 'recoupled/'+couplingType+'_profiledContour_'+model+'.root', couplingType, color = color, lineStyle=lineStyle1s, lineWidth=lineWidth1s, drawSmallestBinMarker=True )
	c95 = drawContours( 'recoupled/'+couplingType+'_profiledContour_'+model+'.root', couplingType, color = color, lineStyle=lineStyle2s, lineWidth=lineWidth2s, level=6.0, levelName="95" )

	return c68




def counting_kVkF( opts ):
	c68_nominal = draw_CouplingContour(opts['modelNominal'],opts, color=ROOT.kBlue)
	c68_alt     = draw_CouplingContour(opts['modelAlt'],    opts, color=ROOT.kRed)

	leg2 = PyROOTUtils.Legend( 0.67, 0.35, textSize=0.03, valign="bottom" )
	if c68_nominal: leg2.AddEntry( c68_nominal[0], "nominal", "L" )
	if c68_alt:     leg2.AddEntry( c68_alt[0], "uncertainties x1.3", "L" )
	leg2.Draw()

	leg = PyROOTUtils.Legend( 0.67, 0.2, textSize=0.03, valign="bottom" )
	leg.AddEntry( SMMarker, "Standard Model", "P" )
	leg.AddEntry( blackSolid, "68% CL", "L" )
	leg.AddEntry( blackDashed, "95% CL", "L" )
	leg.Draw()




def counting_kGlukGamma( opts ):
	c68_nominal = draw_CouplingContour(opts['modelNominal'],opts,couplingType='kGlukGamma', color=ROOT.kBlue)
	c68_alt     = draw_CouplingContour(opts['modelAlt'],    opts,couplingType='kGlukGamma', color=ROOT.kRed)

	leg2 = PyROOTUtils.Legend( 0.67, 0.77, textSize=0.03 )
	if c68_nominal: leg2.AddEntry( c68_nominal[0], "nominal", "L" )
	if c68_alt:     leg2.AddEntry( c68_alt[0], "uncertainties x1.3", "L" )
	leg2.Draw()

	leg = PyROOTUtils.Legend( 0.67, 0.90, textSize=0.03 )
	leg.AddEntry( SMMarker, "Standard Model", "P" )
	leg.AddEntry( blackSolid, "68% CL", "L" )
	leg.AddEntry( blackDashed, "95% CL", "L" )
	leg.Draw()















def main():
	os.system('mkdir -p plots')

	draw_kVkF_frame( 
		counting_kVkF, 
		"plots/kVkF.eps", 
		opts={
			'modelNominal': 'template10_etasgeneric10_learningFull',
			'modelAlt': 'template10_etasgeneric10_learningFull_wideGauss1.3'
		}, 
		r=[0.65,-1.7,1.5,2.0],
	)
	draw_kGlukGamma_frame( 
		counting_kGlukGamma, 
		"plots/kGlukGamma.eps", 
		opts={
			'modelNominal': 'template10_etasgeneric10_learningFull',
			'modelAlt': 'template10_etasgeneric10_learningFull_wideGauss1.3'
		},  
		r=[0.8,0.6,1.9,1.6],
	)



if __name__ == "__main__":
	main()
