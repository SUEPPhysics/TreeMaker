import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-1100_mLSP-1to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/00000/04514AAE-1E5C-E511-9BCC-000F53273500.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-1100_mLSP-1to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/00000/080F20AD-1E5C-E511-92CC-782BCB282C03.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-1100_mLSP-1to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/00000/1A55C7B2-1E5C-E511-91FF-782BCB281FC8.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-1100_mLSP-1to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/00000/24BC55AE-1E5C-E511-83D8-000F53273500.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-1100_mLSP-1to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/00000/28E59EBA-1E5C-E511-BFB7-B499BAAC09A0.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-1100_mLSP-1to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/00000/2E0CEEB1-1E5C-E511-B8DB-842B2B185470.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-1100_mLSP-1to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/00000/388F9DB1-1E5C-E511-915E-782BCB27C5C0.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-1100_mLSP-1to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/00000/3C51E8AF-1E5C-E511-8EA9-000F53273728.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-1100_mLSP-1to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/00000/40C900BC-1E5C-E511-861A-000F53273744.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-1100_mLSP-1to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/00000/4C5282AF-1E5C-E511-AD2F-842B2B18240B.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-1100_mLSP-1to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/00000/501913B3-1E5C-E511-9706-000F53273650.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-1100_mLSP-1to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/00000/54781EB8-1E5C-E511-BF00-000F530E4680.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-1100_mLSP-1to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/00000/780AFEB3-1E5C-E511-956E-A4BADB0F5175.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-1100_mLSP-1to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/00000/7CC589AF-1E5C-E511-8A14-842B2B2B0EC5.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-1100_mLSP-1to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/00000/849232AF-1E5C-E511-A669-782BCB6E1220.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-1100_mLSP-1to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/00000/867DD6AF-1E5C-E511-8E45-0026B95A0D29.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-1100_mLSP-1to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/00000/887806B0-1E5C-E511-9CFE-000F530E4780.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-1100_mLSP-1to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/00000/8CA66BAA-1E5C-E511-AD34-0002C92DB44E.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-1100_mLSP-1to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/00000/92CA5BAE-1E5C-E511-903E-782BCB408A71.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-1100_mLSP-1to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/00000/9A57E6BB-1E5C-E511-B2EA-000F53273744.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-1100_mLSP-1to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/00000/9E9114AF-1E5C-E511-B468-842B2B181F9F.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-1100_mLSP-1to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/00000/B89886B2-1E5C-E511-A931-009C02AB98A6.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-1100_mLSP-1to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/00000/B8988EAF-1E5C-E511-B3F6-842B2B2B0EC5.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-1100_mLSP-1to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/00000/BC807BAE-1E5C-E511-8EAA-000F53273724.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-1100_mLSP-1to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/00000/BE67A2AD-1E5C-E511-A1A7-782BCB282C03.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-1100_mLSP-1to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/00000/C8A75BAF-1E5C-E511-9129-842B2B1858FB.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-1100_mLSP-1to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/00000/D64C3073-1E5C-E511-B417-6C3BE5B59058.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-1100_mLSP-1to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/00000/E091F5AE-1E5C-E511-897F-842B2B181F9F.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-1100_mLSP-1to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/00000/E0A89FB6-1E5C-E511-A971-B499BAABFEB0.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-1100_mLSP-1to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/00000/E404BEB5-1E5C-E511-AB46-000F532734F8.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-1100_mLSP-1to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/00000/F4A00E96-1E5C-E511-91F8-6C3BE5B580B0.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-1100_mLSP-1to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/10000/18819679-365C-E511-A517-782BCB6E134C.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-1100_mLSP-1to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/10000/34295079-365C-E511-81F6-782BCB2820B2.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-1100_mLSP-1to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/10000/58FCC764-365C-E511-A7C6-00261894397F.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-1100_mLSP-1to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/10000/70A89177-365C-E511-9391-782BCB407C98.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-1100_mLSP-1to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/10000/74AB3879-365C-E511-AEDC-0026B95C01B2.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-1100_mLSP-1to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/10000/84BC33CB-3B5C-E511-B56E-6C3BE5B58058.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-1100_mLSP-1to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/10000/967E1A7A-365C-E511-8F54-782BCB285E3F.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-1100_mLSP-1to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/10000/9C3DAC7D-365C-E511-9E16-782BCB282B5F.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-1100_mLSP-1to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/10000/A0B07A79-365C-E511-8D7C-000F53273750.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-1100_mLSP-1to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/10000/A6DA2B75-365C-E511-A753-AC853D9DACD7.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-1100_mLSP-1to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/10000/C8290E72-365C-E511-90DB-B083FED73AA1.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-1100_mLSP-1to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/10000/F2A0917F-3B5C-E511-8D2E-6C3BE5B59150.root' ] );


secFiles.extend( [
               ] )
