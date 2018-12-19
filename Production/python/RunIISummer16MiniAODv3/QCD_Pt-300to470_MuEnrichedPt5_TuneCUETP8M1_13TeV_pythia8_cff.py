import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-300to470_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/110000/0CDDAA3C-11E8-E811-AABB-0242AC130002.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-300to470_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/110000/0E43B444-2EE8-E811-9386-0242AC130002.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-300to470_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/110000/0E652AD7-12E8-E811-BEF3-0242AC130002.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-300to470_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/110000/461088F3-14E8-E811-A6BE-0242AC130002.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-300to470_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/110000/729D8B3E-17E8-E811-84CB-0242AC130002.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-300to470_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/110000/7676B9DD-12E8-E811-9A54-0242AC130002.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-300to470_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/110000/8289D04E-0CE8-E811-8F39-0242AC130002.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-300to470_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/110000/9EE0F8B1-12E8-E811-BC64-0242AC130002.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-300to470_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/110000/AAA4AFA4-11E8-E811-9A35-0242AC130002.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-300to470_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/110000/B239DADB-12E8-E811-AA09-0242AC130002.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-300to470_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/110000/B6752BD2-12E8-E811-8BC1-0242AC130002.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-300to470_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/110000/F4BA445C-87E8-E811-82A3-0242AC130002.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-300to470_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/0041E299-8DE8-E811-90AA-0242AC130002.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-300to470_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/00D22F93-1FE8-E811-A577-0242AC130002.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-300to470_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/08EA1BCC-16E8-E811-A6BF-0242AC130002.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-300to470_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/0EC0F81D-5CE8-E811-BD16-0242AC130002.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-300to470_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/12B3D8CD-16E8-E811-A4E5-0242AC130002.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-300to470_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/14A3E056-20E8-E811-990C-0242AC130002.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-300to470_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/18D750F2-18E8-E811-848C-0242AC130002.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-300to470_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/1CCE58BF-16E8-E811-8078-0242AC130002.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-300to470_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/201E1E9F-1DE8-E811-9FED-0242AC130002.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-300to470_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/203288CC-17E8-E811-BFC2-0242AC130002.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-300to470_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/228D390B-2AE8-E811-A24A-D067E5F91B8A.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-300to470_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/24E47078-18E8-E811-8E69-0242AC130002.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-300to470_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/3220536B-26E8-E811-824B-0242AC130002.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-300to470_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/347709AB-95E8-E811-AD45-0242AC130002.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-300to470_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/36ABE80F-21E8-E811-8897-0242AC130002.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-300to470_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/383D7E60-1AE8-E811-89C3-0242AC130002.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-300to470_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/3CE0BACB-16E8-E811-9E9A-0242AC130002.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-300to470_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/44F29684-17E8-E811-AD6C-0242AC130002.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-300to470_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/50A8C9F9-25E8-E811-9A51-0242AC130002.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-300to470_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/5C6389FA-25E8-E811-9271-0242AC130002.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-300to470_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/5E7912DB-21E8-E811-BF89-0242AC130002.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-300to470_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/660DA3CC-17E8-E811-82D4-0242AC130002.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-300to470_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/68BEFD0F-21E8-E811-9B24-0242AC130002.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-300to470_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/68D545FC-25E8-E811-A9C3-0242AC130002.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-300to470_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/6EFEDA6C-1EE8-E811-9D0A-0242AC130002.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-300to470_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/86D3A9E2-1EE8-E811-8C21-0242AC130002.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-300to470_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/88460EF3-25E8-E811-B864-0242AC130002.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-300to470_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/94FDAF4A-23E8-E811-AEC1-0242AC130002.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-300to470_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/9896D9F1-1EE8-E811-BB9B-0242AC130002.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-300to470_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/9E822F7D-32E8-E811-A7EA-0242AC130002.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-300to470_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/A2A01215-18E8-E811-99F4-0242AC130002.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-300to470_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/AE1E0759-19E8-E811-9E37-0242AC130002.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-300to470_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/B84FE3D4-17E8-E811-A69F-0242AC130002.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-300to470_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/B8D604A1-1BE8-E811-94E2-0242AC130002.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-300to470_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/C01CD5E8-1EE8-E811-8867-0242AC130002.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-300to470_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/C037C28D-26E8-E811-AD2F-0242AC130002.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-300to470_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/C0FBC44B-1AE8-E811-A0E6-0242AC130002.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-300to470_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/C41B972F-18E8-E811-9E8D-0242AC130002.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-300to470_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/C6B319EC-25E8-E811-B516-0242AC130002.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-300to470_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/CA433E43-16E8-E811-8A17-0242AC130002.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-300to470_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/CE39BC2D-1DE8-E811-9978-0242AC130002.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-300to470_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/CE8EA950-21E8-E811-BB1F-0242AC130002.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-300to470_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/CEED39F8-1BE8-E811-A772-0242AC130002.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-300to470_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/D000F328-18E8-E811-A398-0242AC130002.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-300to470_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/D07694A3-49E8-E811-9108-0242AC130002.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-300to470_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/D0B873C9-16E8-E811-9DCE-0242AC130002.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-300to470_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/D438FEF1-25E8-E811-8378-0242AC130002.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-300to470_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/D62B77F4-1EE8-E811-A2BA-0242AC130002.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-300to470_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/DC7D03E7-5BE8-E811-9490-0242AC130002.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-300to470_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/DCCD08CD-16E8-E811-AC02-0242AC130002.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-300to470_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/ECD85EF7-2FE8-E811-B26D-0242AC130002.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-300to470_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/EE00D738-1FE8-E811-90A2-0242AC130002.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-300to470_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/EEFD26CC-16E8-E811-A41D-0242AC130002.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-300to470_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/F0753263-18E8-E811-B170-0242AC130002.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-300to470_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/F21EE1AF-21E8-E811-B852-0242AC130002.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-300to470_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/FC31E2AF-21E8-E811-9E42-0242AC130002.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-300to470_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/FE557BCE-16E8-E811-8898-0242AC130002.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-300to470_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/FE59CCFB-25E8-E811-88C2-0242AC130002.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-300to470_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/FEBF9D25-15E8-E811-9BA6-0242AC130002.root',
] )
