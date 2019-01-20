#Made in python using
#import glob
#for f in glob.glob('RunIIAutumn18MiniAOD/*_cff.py'):
#     print  "\'"+f.replace("_cff.py","").replace("/",".")+"\',"

flist = [
'RunIIAutumn18MiniAOD.TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8',
'RunIIAutumn18MiniAOD.TTToHadronic_TuneCP5_13TeV-powheg-pythia8',
'RunIIAutumn18MiniAOD.QCD_Pt_80to120_TuneCP5_13TeV_pythia8',
'RunIIAutumn18MiniAOD.QCD_Pt_120to170_TuneCP5_13TeV_pythia8',
'RunIIAutumn18MiniAOD.QCD_Pt_170to300_TuneCP5_13TeV_pythia8',
'RunIIAutumn18MiniAOD.QCD_Pt_300to470_TuneCP5_13TeV_pythia8',
'RunIIAutumn18MiniAOD.QCD_Pt_470to600_TuneCP5_13TeV_pythia8',
'RunIIAutumn18MiniAOD.QCD_Pt_470to600_TuneCP5_13TeV_pythia8_ext1',
'RunIIAutumn18MiniAOD.QCD_Pt_600to800_TuneCP5_13TeV_pythia8',
'RunIIAutumn18MiniAOD.QCD_Pt_800to1000_TuneCP5_13TeV_pythia8_ext1',
'RunIIAutumn18MiniAOD.QCD_Pt_1000to1400_TuneCP5_13TeV_pythia8',
'RunIIAutumn18MiniAOD.QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8',
'RunIIAutumn18MiniAOD.QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8_ext1',
'RunIIAutumn18MiniAOD.QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8',
'RunIIAutumn18MiniAOD.QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8_ext1',
'RunIIAutumn18MiniAOD.QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8',
'RunIIAutumn18MiniAOD.QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8',
'RunIIAutumn18MiniAOD.QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8_ext1',
'RunIIAutumn18MiniAOD.QCD_Pt-20to30_MuEnrichedPt5_TuneCP5_13TeV_pythia8',
'RunIIAutumn18MiniAOD.QCD_Pt-30to50_MuEnrichedPt5_TuneCP5_13TeV_pythia8',
'RunIIAutumn18MiniAOD.QCD_Pt-50to80_MuEnrichedPt5_TuneCP5_13TeV_pythia8',
'RunIIAutumn18MiniAOD.QCD_Pt-80to120_MuEnrichedPt5_TuneCP5_13TeV_pythia8',
'RunIIAutumn18MiniAOD.QCD_Pt-120to170_MuEnrichedPt5_TuneCP5_13TeV_pythia8',
'RunIIAutumn18MiniAOD.QCD_Pt-170to300_MuEnrichedPt5_TuneCP5_13TeV_pythia8',
'RunIIAutumn18MiniAOD.QCD_Pt-300to470_MuEnrichedPt5_TuneCP5_13TeV_pythia8',
'RunIIAutumn18MiniAOD.QCD_Pt-600to800_MuEnrichedPt5_TuneCP5_13TeV_pythia8',
'RunIIAutumn18MiniAOD.QCD_Pt-1000toInf_MuEnrichedPt5_TuneCP5_13TeV_pythia8',
'RunIIAutumn18MiniAOD.QCD_HT200to300_TuneCP5_13TeV-madgraphMLM-pythia8',
'RunIIAutumn18MiniAOD.QCD_HT300to500_TuneCP5_13TeV-madgraphMLM-pythia8',
'RunIIAutumn18MiniAOD.QCD_HT500to700_TuneCP5_13TeV-madgraphMLM-pythia8',
'RunIIAutumn18MiniAOD.QCD_HT700to1000_TuneCP5_13TeV-madgraphMLM-pythia8',
'RunIIAutumn18MiniAOD.QCD_HT1000to1500_TuneCP5_13TeV-madgraphMLM-pythia8',
'RunIIAutumn18MiniAOD.QCD_HT1500to2000_TuneCP5_13TeV-madgraphMLM-pythia8',
'RunIIAutumn18MiniAOD.QCD_HT2000toInf_TuneCP5_13TeV-madgraphMLM-pythia8',
'RunIIAutumn18MiniAOD.DYJetsToLL_M-50_HT-100to200_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8',
'RunIIAutumn18MiniAOD.DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8_ext1',
'RunIIAutumn18MiniAOD.ZJetsToNuNu_HT-100To200_13TeV-madgraph',
'RunIIAutumn18MiniAOD.ZJetsToNuNu_HT-200To400_13TeV-madgraph',
'RunIIAutumn18MiniAOD.ZJetsToNuNu_HT-600To800_13TeV-madgraph',
'RunIIAutumn18MiniAOD.ZJetsToNuNu_HT-800To1200_13TeV-madgraph',
'RunIIAutumn18MiniAOD.ZJetsToNuNu_HT-1200To2500_13TeV-madgraph',
'RunIIAutumn18MiniAOD.GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8',
'RunIIAutumn18MiniAOD.GJets_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8',
'RunIIAutumn18MiniAOD.GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8',
'RunIIAutumn18MiniAOD.GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8_ext1',
'RunIIAutumn18MiniAOD.GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8',
'RunIIAutumn18MiniAOD.GJets_DR-0p4_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8',
'RunIIAutumn18MiniAOD.ST_tW_top_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8_ext1',
'RunIIAutumn18MiniAOD.ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8_ext1',
'RunIIAutumn18MiniAOD.ST_tW_antitop_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8_ext1',
'RunIIAutumn18MiniAOD.ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8_ext1',
'RunIIAutumn18MiniAOD.TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8_ext1',
'RunIIAutumn18MiniAOD.TTWW_TuneCP5_13TeV-madgraph-pythia8_ext1',
'RunIIAutumn18MiniAOD.SMS-TChiWZ_ZToLL_mZMin-0p1_TuneCP2_13TeV-madgraphMLM-pythia8',
]
