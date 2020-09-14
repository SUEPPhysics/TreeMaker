import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/user/kdipetri/SUEP/Production_v0.1/2018/MINIAOD/step4_MINIAOD_mMed-400_mDark-2_temp-2_decay-darkPhoHad_13TeV-pythia8_n-100_part-1.root',
       '/store/user/kdipetri/SUEP/Production_v0.1/2018/MINIAOD/step4_MINIAOD_mMed-400_mDark-2_temp-2_decay-darkPhoHad_13TeV-pythia8_n-100_part-2.root',
       '/store/user/kdipetri/SUEP/Production_v0.1/2018/MINIAOD/step4_MINIAOD_mMed-400_mDark-2_temp-2_decay-darkPhoHad_13TeV-pythia8_n-100_part-3.root',
       '/store/user/kdipetri/SUEP/Production_v0.1/2018/MINIAOD/step4_MINIAOD_mMed-400_mDark-2_temp-2_decay-darkPhoHad_13TeV-pythia8_n-100_part-4.root',
       '/store/user/kdipetri/SUEP/Production_v0.1/2018/MINIAOD/step4_MINIAOD_mMed-400_mDark-2_temp-2_decay-darkPhoHad_13TeV-pythia8_n-100_part-5.root',
       '/store/user/kdipetri/SUEP/Production_v0.1/2018/MINIAOD/step4_MINIAOD_mMed-400_mDark-2_temp-2_decay-darkPhoHad_13TeV-pythia8_n-100_part-6.root',
       '/store/user/kdipetri/SUEP/Production_v0.1/2018/MINIAOD/step4_MINIAOD_mMed-400_mDark-2_temp-2_decay-darkPhoHad_13TeV-pythia8_n-100_part-7.root',
       '/store/user/kdipetri/SUEP/Production_v0.1/2018/MINIAOD/step4_MINIAOD_mMed-400_mDark-2_temp-2_decay-darkPhoHad_13TeV-pythia8_n-100_part-8.root',
       '/store/user/kdipetri/SUEP/Production_v0.1/2018/MINIAOD/step4_MINIAOD_mMed-400_mDark-2_temp-2_decay-darkPhoHad_13TeV-pythia8_n-100_part-9.root',
       '/store/user/kdipetri/SUEP/Production_v0.1/2018/MINIAOD/step4_MINIAOD_mMed-400_mDark-2_temp-2_decay-darkPhoHad_13TeV-pythia8_n-100_part-10.root',
       '/store/user/kdipetri/SUEP/Production_v0.1/2018/MINIAOD/step4_MINIAOD_mMed-400_mDark-2_temp-2_decay-darkPhoHad_13TeV-pythia8_n-100_part-11.root',
       '/store/user/kdipetri/SUEP/Production_v0.1/2018/MINIAOD/step4_MINIAOD_mMed-400_mDark-2_temp-2_decay-darkPhoHad_13TeV-pythia8_n-100_part-12.root',
       '/store/user/kdipetri/SUEP/Production_v0.1/2018/MINIAOD/step4_MINIAOD_mMed-400_mDark-2_temp-2_decay-darkPhoHad_13TeV-pythia8_n-100_part-13.root',
       '/store/user/kdipetri/SUEP/Production_v0.1/2018/MINIAOD/step4_MINIAOD_mMed-400_mDark-2_temp-2_decay-darkPhoHad_13TeV-pythia8_n-100_part-14.root',
       '/store/user/kdipetri/SUEP/Production_v0.1/2018/MINIAOD/step4_MINIAOD_mMed-400_mDark-2_temp-2_decay-darkPhoHad_13TeV-pythia8_n-100_part-15.root',
       '/store/user/kdipetri/SUEP/Production_v0.1/2018/MINIAOD/step4_MINIAOD_mMed-400_mDark-2_temp-2_decay-darkPhoHad_13TeV-pythia8_n-100_part-16.root',
       '/store/user/kdipetri/SUEP/Production_v0.1/2018/MINIAOD/step4_MINIAOD_mMed-400_mDark-2_temp-2_decay-darkPhoHad_13TeV-pythia8_n-100_part-17.root',
       '/store/user/kdipetri/SUEP/Production_v0.1/2018/MINIAOD/step4_MINIAOD_mMed-400_mDark-2_temp-2_decay-darkPhoHad_13TeV-pythia8_n-100_part-18.root',
       '/store/user/kdipetri/SUEP/Production_v0.1/2018/MINIAOD/step4_MINIAOD_mMed-400_mDark-2_temp-2_decay-darkPhoHad_13TeV-pythia8_n-100_part-19.root',
       '/store/user/kdipetri/SUEP/Production_v0.1/2018/MINIAOD/step4_MINIAOD_mMed-400_mDark-2_temp-2_decay-darkPhoHad_13TeV-pythia8_n-100_part-20.root',
       '/store/user/kdipetri/SUEP/Production_v0.1/2018/MINIAOD/step4_MINIAOD_mMed-400_mDark-2_temp-2_decay-darkPhoHad_13TeV-pythia8_n-100_part-21.root',
       '/store/user/kdipetri/SUEP/Production_v0.1/2018/MINIAOD/step4_MINIAOD_mMed-400_mDark-2_temp-2_decay-darkPhoHad_13TeV-pythia8_n-100_part-22.root',
       '/store/user/kdipetri/SUEP/Production_v0.1/2018/MINIAOD/step4_MINIAOD_mMed-400_mDark-2_temp-2_decay-darkPhoHad_13TeV-pythia8_n-100_part-23.root',
       '/store/user/kdipetri/SUEP/Production_v0.1/2018/MINIAOD/step4_MINIAOD_mMed-400_mDark-2_temp-2_decay-darkPhoHad_13TeV-pythia8_n-100_part-24.root',
       '/store/user/kdipetri/SUEP/Production_v0.1/2018/MINIAOD/step4_MINIAOD_mMed-400_mDark-2_temp-2_decay-darkPhoHad_13TeV-pythia8_n-100_part-25.root',
       '/store/user/kdipetri/SUEP/Production_v0.1/2018/MINIAOD/step4_MINIAOD_mMed-400_mDark-2_temp-2_decay-darkPhoHad_13TeV-pythia8_n-100_part-26.root',
       '/store/user/kdipetri/SUEP/Production_v0.1/2018/MINIAOD/step4_MINIAOD_mMed-400_mDark-2_temp-2_decay-darkPhoHad_13TeV-pythia8_n-100_part-27.root',
       '/store/user/kdipetri/SUEP/Production_v0.1/2018/MINIAOD/step4_MINIAOD_mMed-400_mDark-2_temp-2_decay-darkPhoHad_13TeV-pythia8_n-100_part-28.root',
       '/store/user/kdipetri/SUEP/Production_v0.1/2018/MINIAOD/step4_MINIAOD_mMed-400_mDark-2_temp-2_decay-darkPhoHad_13TeV-pythia8_n-100_part-29.root',
       '/store/user/kdipetri/SUEP/Production_v0.1/2018/MINIAOD/step4_MINIAOD_mMed-400_mDark-2_temp-2_decay-darkPhoHad_13TeV-pythia8_n-100_part-30.root',
       '/store/user/kdipetri/SUEP/Production_v0.1/2018/MINIAOD/step4_MINIAOD_mMed-400_mDark-2_temp-2_decay-darkPhoHad_13TeV-pythia8_n-100_part-31.root',
       '/store/user/kdipetri/SUEP/Production_v0.1/2018/MINIAOD/step4_MINIAOD_mMed-400_mDark-2_temp-2_decay-darkPhoHad_13TeV-pythia8_n-100_part-32.root',
       '/store/user/kdipetri/SUEP/Production_v0.1/2018/MINIAOD/step4_MINIAOD_mMed-400_mDark-2_temp-2_decay-darkPhoHad_13TeV-pythia8_n-100_part-33.root',
       '/store/user/kdipetri/SUEP/Production_v0.1/2018/MINIAOD/step4_MINIAOD_mMed-400_mDark-2_temp-2_decay-darkPhoHad_13TeV-pythia8_n-100_part-34.root',
       '/store/user/kdipetri/SUEP/Production_v0.1/2018/MINIAOD/step4_MINIAOD_mMed-400_mDark-2_temp-2_decay-darkPhoHad_13TeV-pythia8_n-100_part-35.root',
       '/store/user/kdipetri/SUEP/Production_v0.1/2018/MINIAOD/step4_MINIAOD_mMed-400_mDark-2_temp-2_decay-darkPhoHad_13TeV-pythia8_n-100_part-36.root',
       '/store/user/kdipetri/SUEP/Production_v0.1/2018/MINIAOD/step4_MINIAOD_mMed-400_mDark-2_temp-2_decay-darkPhoHad_13TeV-pythia8_n-100_part-37.root',
       '/store/user/kdipetri/SUEP/Production_v0.1/2018/MINIAOD/step4_MINIAOD_mMed-400_mDark-2_temp-2_decay-darkPhoHad_13TeV-pythia8_n-100_part-38.root',
       '/store/user/kdipetri/SUEP/Production_v0.1/2018/MINIAOD/step4_MINIAOD_mMed-400_mDark-2_temp-2_decay-darkPhoHad_13TeV-pythia8_n-100_part-39.root',
       '/store/user/kdipetri/SUEP/Production_v0.1/2018/MINIAOD/step4_MINIAOD_mMed-400_mDark-2_temp-2_decay-darkPhoHad_13TeV-pythia8_n-100_part-40.root',
       '/store/user/kdipetri/SUEP/Production_v0.1/2018/MINIAOD/step4_MINIAOD_mMed-400_mDark-2_temp-2_decay-darkPhoHad_13TeV-pythia8_n-100_part-41.root',
       '/store/user/kdipetri/SUEP/Production_v0.1/2018/MINIAOD/step4_MINIAOD_mMed-400_mDark-2_temp-2_decay-darkPhoHad_13TeV-pythia8_n-100_part-42.root',
       '/store/user/kdipetri/SUEP/Production_v0.1/2018/MINIAOD/step4_MINIAOD_mMed-400_mDark-2_temp-2_decay-darkPhoHad_13TeV-pythia8_n-100_part-43.root',
       '/store/user/kdipetri/SUEP/Production_v0.1/2018/MINIAOD/step4_MINIAOD_mMed-400_mDark-2_temp-2_decay-darkPhoHad_13TeV-pythia8_n-100_part-44.root',
       '/store/user/kdipetri/SUEP/Production_v0.1/2018/MINIAOD/step4_MINIAOD_mMed-400_mDark-2_temp-2_decay-darkPhoHad_13TeV-pythia8_n-100_part-45.root',
       '/store/user/kdipetri/SUEP/Production_v0.1/2018/MINIAOD/step4_MINIAOD_mMed-400_mDark-2_temp-2_decay-darkPhoHad_13TeV-pythia8_n-100_part-46.root',
       '/store/user/kdipetri/SUEP/Production_v0.1/2018/MINIAOD/step4_MINIAOD_mMed-400_mDark-2_temp-2_decay-darkPhoHad_13TeV-pythia8_n-100_part-47.root',
       '/store/user/kdipetri/SUEP/Production_v0.1/2018/MINIAOD/step4_MINIAOD_mMed-400_mDark-2_temp-2_decay-darkPhoHad_13TeV-pythia8_n-100_part-48.root',
       '/store/user/kdipetri/SUEP/Production_v0.1/2018/MINIAOD/step4_MINIAOD_mMed-400_mDark-2_temp-2_decay-darkPhoHad_13TeV-pythia8_n-100_part-49.root',
       '/store/user/kdipetri/SUEP/Production_v0.1/2018/MINIAOD/step4_MINIAOD_mMed-400_mDark-2_temp-2_decay-darkPhoHad_13TeV-pythia8_n-100_part-50.root',
       '/store/user/kdipetri/SUEP/Production_v0.1/2018/MINIAOD/step4_MINIAOD_mMed-400_mDark-2_temp-2_decay-darkPhoHad_13TeV-pythia8_n-100_part-51.root',
       '/store/user/kdipetri/SUEP/Production_v0.1/2018/MINIAOD/step4_MINIAOD_mMed-400_mDark-2_temp-2_decay-darkPhoHad_13TeV-pythia8_n-100_part-52.root',
       '/store/user/kdipetri/SUEP/Production_v0.1/2018/MINIAOD/step4_MINIAOD_mMed-400_mDark-2_temp-2_decay-darkPhoHad_13TeV-pythia8_n-100_part-53.root',
       '/store/user/kdipetri/SUEP/Production_v0.1/2018/MINIAOD/step4_MINIAOD_mMed-400_mDark-2_temp-2_decay-darkPhoHad_13TeV-pythia8_n-100_part-54.root',
       '/store/user/kdipetri/SUEP/Production_v0.1/2018/MINIAOD/step4_MINIAOD_mMed-400_mDark-2_temp-2_decay-darkPhoHad_13TeV-pythia8_n-100_part-55.root',
       '/store/user/kdipetri/SUEP/Production_v0.1/2018/MINIAOD/step4_MINIAOD_mMed-400_mDark-2_temp-2_decay-darkPhoHad_13TeV-pythia8_n-100_part-56.root',
       '/store/user/kdipetri/SUEP/Production_v0.1/2018/MINIAOD/step4_MINIAOD_mMed-400_mDark-2_temp-2_decay-darkPhoHad_13TeV-pythia8_n-100_part-57.root',
       '/store/user/kdipetri/SUEP/Production_v0.1/2018/MINIAOD/step4_MINIAOD_mMed-400_mDark-2_temp-2_decay-darkPhoHad_13TeV-pythia8_n-100_part-58.root',
       '/store/user/kdipetri/SUEP/Production_v0.1/2018/MINIAOD/step4_MINIAOD_mMed-400_mDark-2_temp-2_decay-darkPhoHad_13TeV-pythia8_n-100_part-59.root',
       '/store/user/kdipetri/SUEP/Production_v0.1/2018/MINIAOD/step4_MINIAOD_mMed-400_mDark-2_temp-2_decay-darkPhoHad_13TeV-pythia8_n-100_part-60.root',
       '/store/user/kdipetri/SUEP/Production_v0.1/2018/MINIAOD/step4_MINIAOD_mMed-400_mDark-2_temp-2_decay-darkPhoHad_13TeV-pythia8_n-100_part-61.root',
       '/store/user/kdipetri/SUEP/Production_v0.1/2018/MINIAOD/step4_MINIAOD_mMed-400_mDark-2_temp-2_decay-darkPhoHad_13TeV-pythia8_n-100_part-62.root',
       '/store/user/kdipetri/SUEP/Production_v0.1/2018/MINIAOD/step4_MINIAOD_mMed-400_mDark-2_temp-2_decay-darkPhoHad_13TeV-pythia8_n-100_part-63.root',
       '/store/user/kdipetri/SUEP/Production_v0.1/2018/MINIAOD/step4_MINIAOD_mMed-400_mDark-2_temp-2_decay-darkPhoHad_13TeV-pythia8_n-100_part-64.root',
       '/store/user/kdipetri/SUEP/Production_v0.1/2018/MINIAOD/step4_MINIAOD_mMed-400_mDark-2_temp-2_decay-darkPhoHad_13TeV-pythia8_n-100_part-65.root',
       '/store/user/kdipetri/SUEP/Production_v0.1/2018/MINIAOD/step4_MINIAOD_mMed-400_mDark-2_temp-2_decay-darkPhoHad_13TeV-pythia8_n-100_part-66.root',
       '/store/user/kdipetri/SUEP/Production_v0.1/2018/MINIAOD/step4_MINIAOD_mMed-400_mDark-2_temp-2_decay-darkPhoHad_13TeV-pythia8_n-100_part-67.root',
       '/store/user/kdipetri/SUEP/Production_v0.1/2018/MINIAOD/step4_MINIAOD_mMed-400_mDark-2_temp-2_decay-darkPhoHad_13TeV-pythia8_n-100_part-68.root',
       '/store/user/kdipetri/SUEP/Production_v0.1/2018/MINIAOD/step4_MINIAOD_mMed-400_mDark-2_temp-2_decay-darkPhoHad_13TeV-pythia8_n-100_part-69.root',
       '/store/user/kdipetri/SUEP/Production_v0.1/2018/MINIAOD/step4_MINIAOD_mMed-400_mDark-2_temp-2_decay-darkPhoHad_13TeV-pythia8_n-100_part-70.root',
       '/store/user/kdipetri/SUEP/Production_v0.1/2018/MINIAOD/step4_MINIAOD_mMed-400_mDark-2_temp-2_decay-darkPhoHad_13TeV-pythia8_n-100_part-71.root',
       '/store/user/kdipetri/SUEP/Production_v0.1/2018/MINIAOD/step4_MINIAOD_mMed-400_mDark-2_temp-2_decay-darkPhoHad_13TeV-pythia8_n-100_part-72.root',
       '/store/user/kdipetri/SUEP/Production_v0.1/2018/MINIAOD/step4_MINIAOD_mMed-400_mDark-2_temp-2_decay-darkPhoHad_13TeV-pythia8_n-100_part-73.root',
       '/store/user/kdipetri/SUEP/Production_v0.1/2018/MINIAOD/step4_MINIAOD_mMed-400_mDark-2_temp-2_decay-darkPhoHad_13TeV-pythia8_n-100_part-74.root',
       '/store/user/kdipetri/SUEP/Production_v0.1/2018/MINIAOD/step4_MINIAOD_mMed-400_mDark-2_temp-2_decay-darkPhoHad_13TeV-pythia8_n-100_part-75.root',
       '/store/user/kdipetri/SUEP/Production_v0.1/2018/MINIAOD/step4_MINIAOD_mMed-400_mDark-2_temp-2_decay-darkPhoHad_13TeV-pythia8_n-100_part-76.root',
       '/store/user/kdipetri/SUEP/Production_v0.1/2018/MINIAOD/step4_MINIAOD_mMed-400_mDark-2_temp-2_decay-darkPhoHad_13TeV-pythia8_n-100_part-77.root',
       '/store/user/kdipetri/SUEP/Production_v0.1/2018/MINIAOD/step4_MINIAOD_mMed-400_mDark-2_temp-2_decay-darkPhoHad_13TeV-pythia8_n-100_part-78.root',
       '/store/user/kdipetri/SUEP/Production_v0.1/2018/MINIAOD/step4_MINIAOD_mMed-400_mDark-2_temp-2_decay-darkPhoHad_13TeV-pythia8_n-100_part-79.root',
       '/store/user/kdipetri/SUEP/Production_v0.1/2018/MINIAOD/step4_MINIAOD_mMed-400_mDark-2_temp-2_decay-darkPhoHad_13TeV-pythia8_n-100_part-80.root',
       '/store/user/kdipetri/SUEP/Production_v0.1/2018/MINIAOD/step4_MINIAOD_mMed-400_mDark-2_temp-2_decay-darkPhoHad_13TeV-pythia8_n-100_part-81.root',
       '/store/user/kdipetri/SUEP/Production_v0.1/2018/MINIAOD/step4_MINIAOD_mMed-400_mDark-2_temp-2_decay-darkPhoHad_13TeV-pythia8_n-100_part-82.root',
       '/store/user/kdipetri/SUEP/Production_v0.1/2018/MINIAOD/step4_MINIAOD_mMed-400_mDark-2_temp-2_decay-darkPhoHad_13TeV-pythia8_n-100_part-83.root',
       '/store/user/kdipetri/SUEP/Production_v0.1/2018/MINIAOD/step4_MINIAOD_mMed-400_mDark-2_temp-2_decay-darkPhoHad_13TeV-pythia8_n-100_part-84.root',
       '/store/user/kdipetri/SUEP/Production_v0.1/2018/MINIAOD/step4_MINIAOD_mMed-400_mDark-2_temp-2_decay-darkPhoHad_13TeV-pythia8_n-100_part-85.root',
       '/store/user/kdipetri/SUEP/Production_v0.1/2018/MINIAOD/step4_MINIAOD_mMed-400_mDark-2_temp-2_decay-darkPhoHad_13TeV-pythia8_n-100_part-86.root',
       '/store/user/kdipetri/SUEP/Production_v0.1/2018/MINIAOD/step4_MINIAOD_mMed-400_mDark-2_temp-2_decay-darkPhoHad_13TeV-pythia8_n-100_part-87.root',
       '/store/user/kdipetri/SUEP/Production_v0.1/2018/MINIAOD/step4_MINIAOD_mMed-400_mDark-2_temp-2_decay-darkPhoHad_13TeV-pythia8_n-100_part-88.root',
       '/store/user/kdipetri/SUEP/Production_v0.1/2018/MINIAOD/step4_MINIAOD_mMed-400_mDark-2_temp-2_decay-darkPhoHad_13TeV-pythia8_n-100_part-89.root',
       '/store/user/kdipetri/SUEP/Production_v0.1/2018/MINIAOD/step4_MINIAOD_mMed-400_mDark-2_temp-2_decay-darkPhoHad_13TeV-pythia8_n-100_part-90.root',
       '/store/user/kdipetri/SUEP/Production_v0.1/2018/MINIAOD/step4_MINIAOD_mMed-400_mDark-2_temp-2_decay-darkPhoHad_13TeV-pythia8_n-100_part-91.root',
       '/store/user/kdipetri/SUEP/Production_v0.1/2018/MINIAOD/step4_MINIAOD_mMed-400_mDark-2_temp-2_decay-darkPhoHad_13TeV-pythia8_n-100_part-92.root',
       '/store/user/kdipetri/SUEP/Production_v0.1/2018/MINIAOD/step4_MINIAOD_mMed-400_mDark-2_temp-2_decay-darkPhoHad_13TeV-pythia8_n-100_part-93.root',
       '/store/user/kdipetri/SUEP/Production_v0.1/2018/MINIAOD/step4_MINIAOD_mMed-400_mDark-2_temp-2_decay-darkPhoHad_13TeV-pythia8_n-100_part-94.root',
       '/store/user/kdipetri/SUEP/Production_v0.1/2018/MINIAOD/step4_MINIAOD_mMed-400_mDark-2_temp-2_decay-darkPhoHad_13TeV-pythia8_n-100_part-95.root',
       '/store/user/kdipetri/SUEP/Production_v0.1/2018/MINIAOD/step4_MINIAOD_mMed-400_mDark-2_temp-2_decay-darkPhoHad_13TeV-pythia8_n-100_part-96.root',
       '/store/user/kdipetri/SUEP/Production_v0.1/2018/MINIAOD/step4_MINIAOD_mMed-400_mDark-2_temp-2_decay-darkPhoHad_13TeV-pythia8_n-100_part-97.root',
       '/store/user/kdipetri/SUEP/Production_v0.1/2018/MINIAOD/step4_MINIAOD_mMed-400_mDark-2_temp-2_decay-darkPhoHad_13TeV-pythia8_n-100_part-98.root',
       '/store/user/kdipetri/SUEP/Production_v0.1/2018/MINIAOD/step4_MINIAOD_mMed-400_mDark-2_temp-2_decay-darkPhoHad_13TeV-pythia8_n-100_part-99.root',
       '/store/user/kdipetri/SUEP/Production_v0.1/2018/MINIAOD/step4_MINIAOD_mMed-400_mDark-2_temp-2_decay-darkPhoHad_13TeV-pythia8_n-100_part-100.root',
] )
