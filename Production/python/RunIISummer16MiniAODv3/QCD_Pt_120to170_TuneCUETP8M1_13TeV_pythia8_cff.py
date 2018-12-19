import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/00000/02A73FA3-9AC1-E811-9F34-001E6734B629.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/00000/061EB70A-04C2-E811-8AAD-AC1F6B1090A6.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/00000/0640ED93-04C2-E811-9C82-001E6734B68D.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/00000/1222C5ED-07C2-E811-8D06-001E672491BE.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/00000/1253066C-E5C1-E811-B426-001E6743E4BE.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/00000/148F1DB2-0DC2-E811-9CCB-001E6743E34C.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/00000/223D6178-06C2-E811-A8DE-001E672491BE.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/00000/429FF635-82C1-E811-9D89-001517EA9DC0.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/00000/48EEFA8A-0FC2-E811-B476-001E6734B6FB.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/00000/4E37FCFD-05C2-E811-880F-001E6743E4BE.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/00000/5C787C6B-05C2-E811-BDA4-001517FD2130.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/00000/68E80124-05C2-E811-8A95-001E671123F0.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/00000/6A9182DE-0FC2-E811-9D86-001E6743E504.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/00000/74AA0328-04C2-E811-A1AA-001517B7D750.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/00000/76F2ADFC-03C2-E811-882E-001E6734B56B.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/00000/78765425-04C2-E811-AF17-001517FD20F4.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/00000/7CC29AAB-A1C1-E811-8967-001E6743E504.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/00000/8034A619-FDC1-E811-BE74-001E6743E504.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/00000/8E92ED79-9EC1-E811-AD75-001E6743E554.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/00000/A4B7B7DA-69C2-E811-B3BD-001517EA8BE4.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/00000/A86C6BCF-90C1-E811-9276-001E67461EF4.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/00000/A898B581-08C2-E811-B2FE-001E6734AE95.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/00000/AA12FE73-0BC2-E811-9110-001E6734B629.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/00000/BC3B3586-04C2-E811-A8A5-001E6743E2DE.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/00000/D89DFFD9-0DC2-E811-B1B7-001517B83610.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/00000/DA32424C-CCC1-E811-A0B8-001E6734AFDA.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/00000/DEF25585-0BC2-E811-8D46-001E6734B485.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/00000/F0331FA7-04C2-E811-B7EA-001517EA9AA0.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/110000/46165301-C1C1-E811-B526-001E6734AE27.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/110000/4A26F9C7-D1C1-E811-999B-001E67461EF4.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/110000/5E3089D0-98C1-E811-9904-001E6743E2DE.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/110000/BCB59D57-F1C1-E811-81D4-001E6734B38B.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/0EDCAA07-8AC1-E811-9179-001E6743E4BE.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/109B7B0D-10C2-E811-871D-001517EA82B8.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/1238C26C-0CC2-E811-B0D1-001517EA8C8C.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/14EE9895-0EC2-E811-AC80-001E6711245C.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/32765EA9-11C2-E811-A545-001E6743E2DE.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/3430D171-D4C1-E811-A6F1-001E6734B56B.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/3C1A784A-03C2-E811-B153-001517EA91C0.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/601904DD-76C1-E811-9181-001E6734AFDA.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/6431C3E9-1FC2-E811-9763-001E6734B629.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/646C45BE-10C2-E811-9499-001517EA8BD4.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/74903294-05C2-E811-954A-001E67461EF4.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/7A45081F-0DC2-E811-93D9-00151764CCDC.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/7C17667A-9EC1-E811-BB02-001E6734AFDA.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/821D6A7E-FDC1-E811-A929-001E6743E554.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/90AAEFC4-13C2-E811-B49C-001E6734B56B.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/946A0DB5-8DC1-E811-BFD0-001E6724917D.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/967ACC9C-10C2-E811-88F4-001E6734AFDA.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/9EE62BE9-13C2-E811-872F-001E6734B5E8.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/BA5820AE-03C2-E811-8D86-001E6743E34C.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/C051D4EE-14C2-E811-96E9-001E6734AE27.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/DEED50E0-05C2-E811-9CD5-001517642260.root',
] )
