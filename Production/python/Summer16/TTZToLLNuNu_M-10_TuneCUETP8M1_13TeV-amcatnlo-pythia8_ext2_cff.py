import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/100000/0666849A-CBE8-E611-ADD4-002590495244.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/100000/0ACB215D-D0E8-E611-9049-0CC47A4D75F4.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/100000/1094A76D-CAE8-E611-98D8-C4346BC8C638.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/100000/10B5A132-CCE8-E611-BD11-0CC47A78A496.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/100000/12994468-D1E8-E611-85F0-0025905B8592.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/100000/143960A7-47E9-E611-A05E-001E674FAF23.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/100000/1A27B34C-CAE8-E611-9F99-0CC47A4D767C.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/100000/1C796870-CFE8-E611-B8B8-0CC47A4D760C.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/100000/1CB90B58-D2E8-E611-8EA0-0CC47A4C8F12.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/100000/2077C831-CAE8-E611-AAB5-FA163EAE31AB.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/100000/24A14FA9-47E9-E611-A13E-00259075D708.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/100000/26BF5A40-C7E8-E611-8030-FA163EAE31AB.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/100000/2E44FF4A-49E9-E611-BFAF-02163E00B7D3.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/100000/2E642469-C8E8-E611-9813-001E67504755.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/100000/400C4F72-D0E8-E611-B0F3-0025905B860E.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/100000/400FF1A5-47E9-E611-A42C-0CC47A7C349C.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/100000/526EE6D4-D5E8-E611-A337-0025907D24F0.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/100000/54292EBE-C4E8-E611-9ACD-02163E00C2A6.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/100000/5E3153A4-47E9-E611-A1CA-FA163E78D122.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/100000/60F18D1D-CDE8-E611-B6A9-0CC47A4D767C.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/100000/622325BC-C7E8-E611-BEFB-0025904B2CA8.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/100000/6AE71C46-CAE8-E611-86AB-002590495244.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/100000/6C1574AB-46E9-E611-9DEA-0025907DC9D6.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/100000/6E1A3E2F-CFE8-E611-B4F1-0CC47A78A408.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/100000/74633A4C-D0E8-E611-B726-0CC47A7C3430.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/100000/76304256-D1E8-E611-8637-0025905B85A0.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/100000/76DB437B-CDE8-E611-B807-90B11C1453E1.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/100000/78096968-C7E8-E611-92C3-0025904B2CA8.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/100000/7AB317E6-CBE8-E611-A16C-02163E00B8BF.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/100000/7E88F251-CFE8-E611-9FF7-0CC47A4C8F10.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/100000/802FB304-CCE8-E611-8360-02163E00BA1F.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/100000/807DB768-CAE8-E611-8D37-FA163E1FFB66.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/100000/861BAC6E-C7E8-E611-B085-02163E00C839.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/100000/8E26B32A-C9E8-E611-8F4B-02163E013D69.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/100000/8E8C664F-D6E8-E611-B353-0025905B860E.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/100000/906CC0E6-C6E8-E611-B869-A0369F3016EC.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/100000/9E2D3660-C7E8-E611-B31E-02163E015D84.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/100000/9E6911A5-47E9-E611-A556-0CC47A745282.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/100000/A4BA58A3-D3E8-E611-97B1-0CC47A7C3430.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/100000/A80A941B-D6E8-E611-B81A-0CC47A4D76AC.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/100000/AC419F12-C6E8-E611-B028-FA163ED94D1D.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/100000/AED2671F-CCE8-E611-9995-0CC47A4D764A.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/100000/B0485DDB-CAE8-E611-AC3C-002590494FA8.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/100000/B2AB858D-D1E8-E611-BB27-0CC47A4D76AC.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/100000/B66D6468-CAE8-E611-B417-FA163EC3ED7A.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/100000/B83F1580-CEE8-E611-87A3-0CC47A4C8F26.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/100000/BA465861-D3E8-E611-BDB5-0CC47A7C3444.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/100000/BE16F8C6-C7E8-E611-A0E4-0CC47A04CFFC.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/100000/C654D94D-C9E8-E611-99E1-002590494D2A.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/100000/CE3BF168-CFE8-E611-A928-0025905A60A8.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/100000/D8B68189-D5E8-E611-AEC3-001E67A42BA2.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/100000/E436E5A0-C9E8-E611-BDE0-A0369F3102B6.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/100000/EA498815-C6E8-E611-84BF-FA163EA7F7B0.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/100000/ECB730E8-CBE8-E611-A20A-02163E0115B0.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/100000/EECF8FA7-47E9-E611-AF6F-002590E3A222.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/100000/F062D721-C9E8-E611-92D8-02163E013D69.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/100000/F64895D0-CAE8-E611-9068-0025907D2212.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/100000/FA115AA8-47E9-E611-8CE9-A4BF01025C02.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/100000/FA9FA0D2-CBE8-E611-B61E-001E675A659A.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/100000/FE7F4821-CEE8-E611-89FF-0025907D2212.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/60000/029E0770-E9E8-E611-8357-0CC47A4D76A0.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/60000/086CDF73-E9E8-E611-A14C-0025905B8572.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/60000/123039AA-49E9-E611-ACC4-0090FAA57C20.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/60000/143CC5FF-E1E8-E611-B199-0025905A48BC.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/60000/169396F8-E1E8-E611-8969-0CC47A4D768E.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/60000/1AEB2673-E9E8-E611-A773-0025905A48BC.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/60000/1EFBBFFF-E1E8-E611-9E1E-003048FFD79E.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/60000/28E7340E-4AE9-E611-952D-0025905B85BC.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/60000/36850D01-E2E8-E611-9106-0025905B855E.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/60000/38056273-E9E8-E611-B65D-0025905A60C6.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/60000/3A42F073-E9E8-E611-9803-0025905A60C6.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/60000/424B44F8-E1E8-E611-B184-0CC47A4C8E3C.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/60000/4C1E3672-E9E8-E611-B0FF-0025905A60AA.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/60000/5A7B3571-E9E8-E611-8D33-0CC47A4D769A.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/60000/6A6817E5-E1E8-E611-ADEC-782BCB537E8B.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/60000/6C9258C4-DBE8-E611-9656-0025905A6082.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/60000/6E80B6FC-E1E8-E611-A6D7-0CC47A74525A.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/60000/8002216F-E9E8-E611-A31A-0CC47A4D75F2.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/60000/88E933F7-E1E8-E611-9074-0CC47A74525A.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/60000/94391175-E9E8-E611-B2C5-0CC47A4D7664.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/60000/A287389A-4AE9-E611-A1F3-0025905A6110.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/60000/A6B0B0FE-E1E8-E611-892D-0CC47A4D7602.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/60000/AA2593C2-DBE8-E611-AB3C-0CC47A78A30E.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/60000/B6A71B00-E2E8-E611-8AE9-0025905B8586.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/60000/D2FACEFB-E1E8-E611-8D9D-0CC47A4D7628.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/60000/D6F33A72-E9E8-E611-95CD-0025905A60A0.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/60000/E29B4270-E9E8-E611-998B-0025905A60EE.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/60000/E855EA0F-E2E8-E611-8627-0090FAA57FA4.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/60000/EA6E7DFD-E1E8-E611-B9DB-0CC47A4D768C.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/60000/F2F21EFD-E1E8-E611-9607-0CC47A4D7662.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/60000/F4DEC1E6-EEE8-E611-8DCE-0025905A60C6.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/60000/FA3FD4F7-E1E8-E611-8C11-0CC47A4D7628.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/70000/0C51C29E-5BE9-E611-8247-0CC47A74527A.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/70000/AEFAE9C1-56E9-E611-9E24-0CC47A74527A.root',
] )
