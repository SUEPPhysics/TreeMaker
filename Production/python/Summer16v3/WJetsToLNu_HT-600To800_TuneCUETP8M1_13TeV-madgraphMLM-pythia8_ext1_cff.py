import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv3/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/100000/04237516-5FEA-E811-968F-001E67A3F8A8.root',
       '/store/mc/RunIISummer16MiniAODv3/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/100000/0AD0197B-57EA-E811-9C69-001E67A4055F.root',
       '/store/mc/RunIISummer16MiniAODv3/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/100000/10CE1472-48EA-E811-BB4B-001E67DFF4F6.root',
       '/store/mc/RunIISummer16MiniAODv3/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/100000/2A205F36-5FEA-E811-B727-A4BF0102572F.root',
       '/store/mc/RunIISummer16MiniAODv3/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/100000/2C83B279-4FEA-E811-9217-001E67DFFB31.root',
       '/store/mc/RunIISummer16MiniAODv3/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/100000/3C92253C-5FEA-E811-B22E-90B11C070100.root',
       '/store/mc/RunIISummer16MiniAODv3/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/100000/481A789C-4FEA-E811-965C-A4BF0101DB3E.root',
       '/store/mc/RunIISummer16MiniAODv3/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/100000/8A439041-5EEA-E811-86C4-EC0D9A0B3370.root',
       '/store/mc/RunIISummer16MiniAODv3/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/100000/CEB97E40-DEEA-E811-9ADF-001E67A3EF70.root',
       '/store/mc/RunIISummer16MiniAODv3/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/100000/E4DE7AF6-50EA-E811-89B3-001E67E6965D.root',
       '/store/mc/RunIISummer16MiniAODv3/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/100000/F466F22D-64EA-E811-AD13-001E67DFF5D7.root',
       '/store/mc/RunIISummer16MiniAODv3/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/100000/F872874E-5DEA-E811-AEED-001E67DFFB4F.root',
       '/store/mc/RunIISummer16MiniAODv3/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/120000/04260585-2BEA-E811-9A30-001E67A3EB1A.root',
       '/store/mc/RunIISummer16MiniAODv3/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/120000/04F54A94-2FEA-E811-8984-A4BF010114DB.root',
       '/store/mc/RunIISummer16MiniAODv3/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/120000/060EB9F6-43EA-E811-9928-001E67E5A38B.root',
       '/store/mc/RunIISummer16MiniAODv3/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/120000/0A27E0C6-43EA-E811-AF44-90B11C12D371.root',
       '/store/mc/RunIISummer16MiniAODv3/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/120000/0EB4FB1D-2CEA-E811-AC13-A4BF0102572F.root',
       '/store/mc/RunIISummer16MiniAODv3/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/120000/101177FD-44EA-E811-9ACC-001E675A690A.root',
       '/store/mc/RunIISummer16MiniAODv3/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/120000/10B58FE7-48EA-E811-AB79-001E67A42175.root',
       '/store/mc/RunIISummer16MiniAODv3/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/120000/10BD49F8-43EA-E811-BCEB-A4BF0101DCC9.root',
       '/store/mc/RunIISummer16MiniAODv3/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/120000/18B6E603-9AEA-E811-9B38-EC0D9A0B30D0.root',
       '/store/mc/RunIISummer16MiniAODv3/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/120000/18EA41B9-3CEA-E811-9BC4-90B11C094A7E.root',
       '/store/mc/RunIISummer16MiniAODv3/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/120000/1A26D472-2BEA-E811-8B28-001E67E0061C.root',
       '/store/mc/RunIISummer16MiniAODv3/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/120000/1C0B4EEC-32EA-E811-851D-0026182FD776.root',
       '/store/mc/RunIISummer16MiniAODv3/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/120000/1CDA6AA9-43EA-E811-B0D9-001E67A40604.root',
       '/store/mc/RunIISummer16MiniAODv3/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/120000/266AD240-2DEA-E811-9F3A-001E67A3FE66.root',
       '/store/mc/RunIISummer16MiniAODv3/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/120000/2E15287B-2BEA-E811-8517-001E67DDC2CC.root',
       '/store/mc/RunIISummer16MiniAODv3/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/120000/2E73C687-45EA-E811-95EE-001E67DDD0AA.root',
       '/store/mc/RunIISummer16MiniAODv3/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/120000/325F4187-2BEA-E811-B580-001E675A67BB.root',
       '/store/mc/RunIISummer16MiniAODv3/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/120000/327BA774-43EA-E811-B949-EC0D9A0B3370.root',
       '/store/mc/RunIISummer16MiniAODv3/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/120000/38FEB264-2DEA-E811-83E8-001E67A3EF70.root',
       '/store/mc/RunIISummer16MiniAODv3/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/120000/3A8D9925-2CEA-E811-AC7E-001E67E68BBD.root',
       '/store/mc/RunIISummer16MiniAODv3/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/120000/3E99B3A8-29EA-E811-AE20-EC0D9A0B3190.root',
       '/store/mc/RunIISummer16MiniAODv3/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/120000/42475C14-2CEA-E811-BDA8-001E67DDC0FB.root',
       '/store/mc/RunIISummer16MiniAODv3/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/120000/48320B46-2DEA-E811-8652-A4BF01027688.root',
       '/store/mc/RunIISummer16MiniAODv3/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/120000/4A0E868F-2BEA-E811-AF41-001E67D80528.root',
       '/store/mc/RunIISummer16MiniAODv3/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/120000/4A8744FD-2BEA-E811-B272-EC0D9A0B3330.root',
       '/store/mc/RunIISummer16MiniAODv3/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/120000/4C46EB05-25EA-E811-A9EA-EC0D9A0B3330.root',
       '/store/mc/RunIISummer16MiniAODv3/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/120000/4EC33A14-25EA-E811-9FD5-001E67DDC88A.root',
       '/store/mc/RunIISummer16MiniAODv3/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/120000/4EEAE4B7-32EA-E811-8BC4-A4BF01013D12.root',
       '/store/mc/RunIISummer16MiniAODv3/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/120000/4EFD1A85-2BEA-E811-8A51-001E67A400F0.root',
       '/store/mc/RunIISummer16MiniAODv3/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/120000/52025436-42EA-E811-B960-001E67A3EC05.root',
       '/store/mc/RunIISummer16MiniAODv3/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/120000/52F34D11-45EA-E811-BA2E-001E67DFF5D7.root',
       '/store/mc/RunIISummer16MiniAODv3/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/120000/56F6CFC0-43EA-E811-82E8-001E67D89532.root',
       '/store/mc/RunIISummer16MiniAODv3/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/120000/5CFF3F6F-2AEA-E811-9851-A4BF010122D7.root',
       '/store/mc/RunIISummer16MiniAODv3/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/120000/5E21EC84-2BEA-E811-A5D5-001E675A69DC.root',
       '/store/mc/RunIISummer16MiniAODv3/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/120000/5E944253-25EA-E811-B997-001E67DDD348.root',
       '/store/mc/RunIISummer16MiniAODv3/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/120000/604E6A3A-2DEA-E811-B0C5-A4BF0126D535.root',
       '/store/mc/RunIISummer16MiniAODv3/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/120000/6891EE20-2CEA-E811-9D02-001E67DFF5D7.root',
       '/store/mc/RunIISummer16MiniAODv3/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/120000/6A927BBA-43EA-E811-A64D-001E67D80528.root',
       '/store/mc/RunIISummer16MiniAODv3/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/120000/6AB1D605-3DEA-E811-BFD4-0026182FD776.root',
       '/store/mc/RunIISummer16MiniAODv3/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/120000/6AFBE625-2CEA-E811-89E5-001E67A39C17.root',
       '/store/mc/RunIISummer16MiniAODv3/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/120000/6E674F02-2CEA-E811-8051-EC0D9A0B3340.root',
       '/store/mc/RunIISummer16MiniAODv3/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/120000/6EB0DAFB-44EA-E811-9DDF-001E67DDD348.root',
       '/store/mc/RunIISummer16MiniAODv3/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/120000/7066F6C7-40EA-E811-8AD3-90B11C06954E.root',
       '/store/mc/RunIISummer16MiniAODv3/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/120000/78296E38-42EA-E811-9BA6-001E67A42175.root',
       '/store/mc/RunIISummer16MiniAODv3/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/120000/7E2809A8-32EA-E811-B8CC-001E67A3EB1A.root',
       '/store/mc/RunIISummer16MiniAODv3/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/120000/80620280-2FEA-E811-B33A-001E67A3EC05.root',
       '/store/mc/RunIISummer16MiniAODv3/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/120000/840BC074-43EA-E811-AA88-EC0D9A0B3380.root',
       '/store/mc/RunIISummer16MiniAODv3/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/120000/842150F1-2FEA-E811-879E-001E675A6653.root',
       '/store/mc/RunIISummer16MiniAODv3/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/120000/88D80732-2CEA-E811-9472-A4BF0102A5F9.root',
       '/store/mc/RunIISummer16MiniAODv3/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/120000/8AD0FB81-2FEA-E811-BEEE-001E675A5244.root',
       '/store/mc/RunIISummer16MiniAODv3/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/120000/8E2ECCDF-44EA-E811-AC31-EC0D9A0B30D0.root',
       '/store/mc/RunIISummer16MiniAODv3/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/120000/8EE1B72F-42EA-E811-A481-001E67DDC119.root',
       '/store/mc/RunIISummer16MiniAODv3/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/120000/90595CDB-40EA-E811-88C6-001E67A402C1.root',
       '/store/mc/RunIISummer16MiniAODv3/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/120000/90895CD4-44EA-E811-B0A0-001E675A6725.root',
       '/store/mc/RunIISummer16MiniAODv3/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/120000/9091EAFC-2BEA-E811-8CFA-001E675A6653.root',
       '/store/mc/RunIISummer16MiniAODv3/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/120000/92C06564-2CEA-E811-B23C-001517FB25E4.root',
       '/store/mc/RunIISummer16MiniAODv3/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/120000/946C87FF-2FEA-E811-935E-485B3919F14E.root',
       '/store/mc/RunIISummer16MiniAODv3/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/120000/947115AB-32EA-E811-B56F-A4BF01027688.root',
       '/store/mc/RunIISummer16MiniAODv3/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/120000/94EE8D80-2BEA-E811-AF92-001E67DFF4F6.root',
       '/store/mc/RunIISummer16MiniAODv3/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/120000/962165B9-45EA-E811-B3F5-A4BF0101DB93.root',
       '/store/mc/RunIISummer16MiniAODv3/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/120000/9684E2AD-34EA-E811-B42A-001E67A3F8A8.root',
       '/store/mc/RunIISummer16MiniAODv3/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/120000/985FD76A-3CEA-E811-8BF6-001E67DDC24A.root',
       '/store/mc/RunIISummer16MiniAODv3/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/120000/9C1428F9-2BEA-E811-B734-248A07C6D770.root',
       '/store/mc/RunIISummer16MiniAODv3/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/120000/9E6BB9CA-29EA-E811-9DAC-001E67A3E95D.root',
       '/store/mc/RunIISummer16MiniAODv3/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/120000/A0FCBB0F-2CEA-E811-8293-EC0D9A0B3360.root',
       '/store/mc/RunIISummer16MiniAODv3/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/120000/A28CDC7C-2FEA-E811-9FF4-001E67A3EB1A.root',
       '/store/mc/RunIISummer16MiniAODv3/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/120000/A813266A-2FEA-E811-A8B2-001E67A42026.root',
       '/store/mc/RunIISummer16MiniAODv3/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/120000/A84C3891-12EA-E811-A0D9-A4BF01013D12.root',
       '/store/mc/RunIISummer16MiniAODv3/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/120000/A87E77C3-32EA-E811-807D-A4BF01025B08.root',
       '/store/mc/RunIISummer16MiniAODv3/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/120000/AA422F33-2CEA-E811-A9BF-001E67DDD0B9.root',
       '/store/mc/RunIISummer16MiniAODv3/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/120000/AC957026-25EA-E811-A445-001E67A404B0.root',
       '/store/mc/RunIISummer16MiniAODv3/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/120000/AEF47DC7-29EA-E811-8CAB-001E67DDBEDA.root',
       '/store/mc/RunIISummer16MiniAODv3/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/120000/B45A686C-42EA-E811-859C-001517F7F510.root',
       '/store/mc/RunIISummer16MiniAODv3/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/120000/B479D994-2FEA-E811-93BF-A4BF0101DD64.root',
       '/store/mc/RunIISummer16MiniAODv3/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/120000/BA3DCB81-45EA-E811-8D48-001E67E6920C.root',
       '/store/mc/RunIISummer16MiniAODv3/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/120000/BA91225B-2FEA-E811-B7CC-EC0D9A0B3340.root',
       '/store/mc/RunIISummer16MiniAODv3/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/120000/BC21455E-45EA-E811-9D8D-EC0D9A0B3330.root',
       '/store/mc/RunIISummer16MiniAODv3/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/120000/BC7294E7-43EA-E811-8ADC-001517FB1990.root',
       '/store/mc/RunIISummer16MiniAODv3/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/120000/BEE25AAF-43EA-E811-8958-A4BF0102A4F5.root',
       '/store/mc/RunIISummer16MiniAODv3/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/120000/C0F6436D-27EA-E811-9AFD-90B11C06CD59.root',
       '/store/mc/RunIISummer16MiniAODv3/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/120000/C649F0D0-22EA-E811-AECB-001E67DDC4AC.root',
       '/store/mc/RunIISummer16MiniAODv3/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/120000/C6EF9446-49EA-E811-AC0A-A4BF0101F533.root',
       '/store/mc/RunIISummer16MiniAODv3/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/120000/CA6741D9-29EA-E811-A601-001E67586629.root',
       '/store/mc/RunIISummer16MiniAODv3/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/120000/CCFA64D8-44EA-E811-A465-001E67DDC4AC.root',
       '/store/mc/RunIISummer16MiniAODv3/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/120000/CEC3F17B-2BEA-E811-AE75-001E67DDCC81.root',
       '/store/mc/RunIISummer16MiniAODv3/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/120000/D0BFCA47-42EA-E811-95DB-A4BF01013F8D.root',
       '/store/mc/RunIISummer16MiniAODv3/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/120000/D0E659A9-43EA-E811-849F-001E675A4759.root',
       '/store/mc/RunIISummer16MiniAODv3/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/120000/D2B60CA5-40EA-E811-AC18-001E675A4759.root',
       '/store/mc/RunIISummer16MiniAODv3/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/120000/D6A30795-3CEA-E811-BCA7-A4BF010298CF.root',
       '/store/mc/RunIISummer16MiniAODv3/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/120000/D6AB9E1E-46EA-E811-9CBD-485B3919F0B5.root',
       '/store/mc/RunIISummer16MiniAODv3/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/120000/D807525E-45EA-E811-A4F2-EC0D9A0B3320.root',
       '/store/mc/RunIISummer16MiniAODv3/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/120000/DAF4F608-2AEA-E811-9899-001517FBE024.root',
       '/store/mc/RunIISummer16MiniAODv3/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/120000/E0063BCA-43EA-E811-ADEE-90B11C064AD8.root',
       '/store/mc/RunIISummer16MiniAODv3/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/120000/E03FB814-25EA-E811-87F0-001E67E6965D.root',
       '/store/mc/RunIISummer16MiniAODv3/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/120000/E430A966-42EA-E811-8ED3-001517FB1B60.root',
       '/store/mc/RunIISummer16MiniAODv3/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/120000/E65938DB-40EA-E811-B0C0-001517FAAB30.root',
       '/store/mc/RunIISummer16MiniAODv3/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/120000/E80E69AB-29EA-E811-90CA-EC0D9A0B32F0.root',
       '/store/mc/RunIISummer16MiniAODv3/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/120000/E8B029D9-43EA-E811-BD85-90E6BA693E13.root',
       '/store/mc/RunIISummer16MiniAODv3/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/120000/E8BEC929-2CEA-E811-8D5C-A4BF01027688.root',
       '/store/mc/RunIISummer16MiniAODv3/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/120000/EADB0B56-2BEA-E811-BB29-EC0D9A0B32F0.root',
       '/store/mc/RunIISummer16MiniAODv3/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/120000/EC7DD9AD-34EA-E811-A539-001E67A3F8A8.root',
       '/store/mc/RunIISummer16MiniAODv3/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/120000/EC8D9FAC-32EA-E811-A3AD-001E675A6AA9.root',
       '/store/mc/RunIISummer16MiniAODv3/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/120000/F0CE3DCC-43EA-E811-95F1-A4BF010120C5.root',
       '/store/mc/RunIISummer16MiniAODv3/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/120000/F2481E69-2CEA-E811-B125-001E67A402B2.root',
       '/store/mc/RunIISummer16MiniAODv3/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/120000/F2AB2D33-2CEA-E811-A5E2-001E67DDD0B9.root',
       '/store/mc/RunIISummer16MiniAODv3/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/120000/F429DF1F-2CEA-E811-A2A9-001E67A3EC00.root',
       '/store/mc/RunIISummer16MiniAODv3/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/120000/F4CF5F80-40EA-E811-8DDC-EC0D9A0B3340.root',
       '/store/mc/RunIISummer16MiniAODv3/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/120000/F820722D-2CEA-E811-A98E-001E67A3EAB1.root',
       '/store/mc/RunIISummer16MiniAODv3/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/120000/FE5FED57-2DEA-E811-9A0D-A4BF01025C07.root',
       '/store/mc/RunIISummer16MiniAODv3/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/120000/FEB35F42-45EA-E811-8DCD-001517FB0F60.root',
       '/store/mc/RunIISummer16MiniAODv3/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/120000/FED3E298-6EEA-E811-87CE-90B11C070100.root',
       '/store/mc/RunIISummer16MiniAODv3/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/120000/FEFAEA55-B4EA-E811-B1CE-901B0E5427BA.root',
] )