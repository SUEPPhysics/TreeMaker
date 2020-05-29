import FWCore.ParameterSet.Config as cms

from TreeMaker.WeightProducer.MCSample import MCSample

# suep signals
SUEPsamples = [
        MCSample("step4_MINIAOD_mMed-1000_mDark-2_temp-2_decay-darkPho_13TeV-pythia8_n-100", "", "", "Constant", 10000),
        MCSample("step4_MINIAOD_mMed-750_mDark-2_temp-2_decay-darkPho_13TeV-pythia8_n-100", "", "", "Constant", 10000),
        MCSample("step4_MINIAOD_mMed-400_mDark-2_temp-2_decay-darkPho_13TeV-pythia8_n-100", "", "", "Constant", 10000),
        MCSample("step4_MINIAOD_mMed-125_mDark-2_temp-2_decay-darkPho_13TeV-pythia8_n-100", "", "", "Constant", 10000),
        MCSample("step4_MINIAOD_mMed-1000_mDark-2_temp-2_decay-darkPhoHad_13TeV-pythia8_n-100", "", "", "Constant", 10000),
        MCSample("step4_MINIAOD_mMed-750_mDark-2_temp-2_decay-darkPhoHad_13TeV-pythia8_n-100", "", "", "Constant", 10000),
        MCSample("step4_MINIAOD_mMed-400_mDark-2_temp-2_decay-darkPhoHad_13TeV-pythia8_n-100", "", "", "Constant", 10000),
        MCSample("step4_MINIAOD_mMed-125_mDark-2_temp-2_decay-darkPhoHad_13TeV-pythia8_n-100", "", "", "Constant", 10000),
        MCSample("step4_MINIAOD_mMed-1000_mDark-2_temp-2_decay-generic_13TeV-pythia8_n-100", "", "", "Constant", 10000),
        MCSample("step4_MINIAOD_mMed-750_mDark-2_temp-2_decay-generic_13TeV-pythia8_n-100", "", "", "Constant", 10000),
        MCSample("step4_MINIAOD_mMed-400_mDark-2_temp-2_decay-generic_13TeV-pythia8_n-100", "", "", "Constant", 9900),
        MCSample("step4_MINIAOD_mMed-125_mDark-2_temp-2_decay-generic_13TeV-pythia8_n-100", "", "", "Constant", 10000),

]
