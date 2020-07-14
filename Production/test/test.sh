# Signal
  #cmsRun \
  #/uscms_data/d3/kdipetri/SUEP_10_2_21_treeMaker/CMSSW_10_2_21/src/TreeMaker/Production/test/runMakeTreeFromMiniAOD_cfg.py \
  #scenario=Autumn18sig \
  #inputFilesConfig=PrivateSamples.SUEP_2018_mMed-750_mDark-2_temp-2_decay-generic_13TeV-pythia8_n-100 \
  #nstart=0 \
  #nfiles=10 \
  #outfile=Autumn18.SUEP_2018_mMed-750_mDark-2_temp-2_decay-generic_13TeV-pythia8_n-100 \
  #numevents=100 \
  #>& Autumn18.SUEP_2018_mMed-750_mDark-2_temp-2_decay-generic_13TeV-pythia8_n-100.log &
# QCD 
  #cmsRun \
  #/uscms_data/d3/kdipetri/SUEP_10_2_21_treeMaker/CMSSW_10_2_21/src/TreeMaker/Production/test/runMakeTreeFromMiniAOD_cfg.py \
  #scenario=Autumn18 \
  #inputFilesConfig=Autumn18.QCD_HT500to700_TuneCP5_13TeV-madgraphMLM-pythia8 \
  #nstart=0 \
  #nfiles=10 \
  #outfile=Autumn18.QCD_HT500to700_TuneCP5_13TeV-madgraphMLM-pythia8 \
  #numevents=100 \
  #>& Autumn18.QCD_HT500to700_TuneCP5_13TeV-madgraphMLM-pythia8.log &
# Data
  #cmsRun \
  #/uscms_data/d3/kdipetri/SUEP_10_2_21_treeMaker/CMSSW_10_2_21/src/TreeMaker/Production/test/runMakeTreeFromMiniAOD_cfg.py \
  #scenario=2018PromptReco \
  #inputFilesConfig=Run2018D-PromptReco-v2.JetHT \
  #nstart=244 \
  #nfiles=1 \
  #outfile=Run2018D-PromptReco-v2.JetHT \
  ##numevents=1000 \
  #>& Run2018D-PromptReco-v2.JetHT.log &

python test_qcd.py
