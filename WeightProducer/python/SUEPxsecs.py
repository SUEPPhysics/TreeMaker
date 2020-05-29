import FWCore.ParameterSet.Config as cms

from TreeMaker.WeightProducer.MCSampleValues import MCSampleValuesHelper
XSValues = MCSampleValuesHelper.XSValues

SUEPxsecs = {
    "mMed-125"  : {
        "CrossSection" : XSValues(XS_13TeV=34.8),
    },
    "mMed-400"  : {
        "CrossSection" : XSValues(XS_13TeV=5.9),
    },
    "mMed-750"  : {
        "CrossSection" : XSValues(XS_13TeV=0.5),
    },
    "mMed-1000"  : {
        "CrossSection" : XSValues(XS_13TeV=0.17),
    },
}

