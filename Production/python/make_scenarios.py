import subprocess
import os


mMeds=[]
mMeds.append(125)
mMeds.append(400)
mMeds.append(750)
mMeds.append(1000)

decays=[]
decays.append("generic")
decays.append("darkPho")
decays.append("darkPhoHad")

temp=2
mDark=2

path="/store/user/kdipetri/SUEP/Production_v0.0/2018/MINIAOD/"


for mMed in mMeds:
    for decay in decays:
    
        sample="mMed-{}_mDark-{}_temp-{}_decay-{}_13TeV-pythia8".format(mMed,mDark,temp,decay)
        bash_command="eosls {}*{}*".format(path,sample,sample)
        fin  = "Autumn18sig/{}.txt".format(sample)
        fout = "Autumn18sig/{}_cff.py".format(sample)
    
        pfile = open(fout,"w")
        pfile.write("import FWCore.ParameterSet.Config as cms\n\n")
        pfile.write("maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )\n")
        pfile.write("readFiles = cms.untracked.vstring()\n")
        pfile.write("secFiles = cms.untracked.vstring()\n")
        pfile.write("source = cms.Source (\"PoolSource\",fileNames = readFiles, secondaryFileNames = secFiles)\n")
        pfile.write("readFiles.extend( [\n")

        #print(bash_command +" > Autumn18sig/{}.txt".format(sample))
        
        for line in open(fin,"r").readlines():
            f = path+line.strip()
            pfile.write("       '"+f+"',\n")


        pfile.write("] )\n")
        pfile.close()
