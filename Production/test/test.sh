  cmsRun \
  /uscms_data/d3/kdipetri/SUEP_10_2_21_treeMaker/CMSSW_10_2_21/src/TreeMaker/Production/test/runMakeTreeFromMiniAOD_cfg.py \
  scenario=Autumn18sig \
  inputFilesConfig=PrivateSamples.SUEP_2018_mMed-750_mDark-2_temp-2_decay-generic_13TeV-pythia8_n-100 \
  nstart=0 \
  nfiles=10 \
  outfile=Autumn18.SUEP_2018_mMed-750_mDark-2_temp-2_decay-generic_13TeV-pythia8_n-100 \
  numevents=100 \
  >& Autumn18.SUEP_2018_mMed-750_mDark-2_temp-2_decay-generic_13TeV-pythia8_n-100.log &
