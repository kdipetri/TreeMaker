import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv3/SVJ_Zprime_Scan_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_SVJ_PSWeight_94X_mcRun2_asymptotic_v3-v1/110000/028EA946-C6DB-EA11-BCE1-FA163E51F734.root',
       '/store/mc/RunIISummer16MiniAODv3/SVJ_Zprime_Scan_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_SVJ_PSWeight_94X_mcRun2_asymptotic_v3-v1/110000/18C93437-F8E1-EA11-B28C-0242AC1C0500.root',
       '/store/mc/RunIISummer16MiniAODv3/SVJ_Zprime_Scan_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_SVJ_PSWeight_94X_mcRun2_asymptotic_v3-v1/110000/283A19BD-F8E1-EA11-99A3-0025904405AC.root',
       '/store/mc/RunIISummer16MiniAODv3/SVJ_Zprime_Scan_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_SVJ_PSWeight_94X_mcRun2_asymptotic_v3-v1/110000/285DA56E-84DC-EA11-A4D6-FA163EC4FBE7.root',
       '/store/mc/RunIISummer16MiniAODv3/SVJ_Zprime_Scan_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_SVJ_PSWeight_94X_mcRun2_asymptotic_v3-v1/110000/2AD6B073-F8E1-EA11-B5C1-6C2B59915F7C.root',
       '/store/mc/RunIISummer16MiniAODv3/SVJ_Zprime_Scan_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_SVJ_PSWeight_94X_mcRun2_asymptotic_v3-v1/110000/96EA3AC3-ADDC-EA11-B295-0CC47A4D769A.root',
       '/store/mc/RunIISummer16MiniAODv3/SVJ_Zprime_Scan_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_SVJ_PSWeight_94X_mcRun2_asymptotic_v3-v1/110000/BA2DE67B-1EE2-EA11-921A-A0369FD0B196.root',
       '/store/mc/RunIISummer16MiniAODv3/SVJ_Zprime_Scan_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_SVJ_PSWeight_94X_mcRun2_asymptotic_v3-v1/110000/D482C4E3-E1DC-EA11-B8D3-B02628DE9830.root',
       '/store/mc/RunIISummer16MiniAODv3/SVJ_Zprime_Scan_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_SVJ_PSWeight_94X_mcRun2_asymptotic_v3-v1/110000/DC4CA3C6-F8E1-EA11-A9C4-FA163EDE855A.root',
       '/store/mc/RunIISummer16MiniAODv3/SVJ_Zprime_Scan_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_SVJ_PSWeight_94X_mcRun2_asymptotic_v3-v1/110000/FEC1B668-E8DC-EA11-9C45-0CC47AF9B1D6.root',
       '/store/mc/RunIISummer16MiniAODv3/SVJ_Zprime_Scan_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_SVJ_PSWeight_94X_mcRun2_asymptotic_v3-v1/1110000/D45AEC04-27DB-EA11-9BC7-FA163E4B949E.root',
       '/store/mc/RunIISummer16MiniAODv3/SVJ_Zprime_Scan_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_SVJ_PSWeight_94X_mcRun2_asymptotic_v3-v1/20000/006EBA9E-74C3-EA11-BEF4-FA163EFE2B28.root',
       '/store/mc/RunIISummer16MiniAODv3/SVJ_Zprime_Scan_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_SVJ_PSWeight_94X_mcRun2_asymptotic_v3-v1/20000/0847F279-ECD4-EA11-A2EE-0025905A608E.root',
       '/store/mc/RunIISummer16MiniAODv3/SVJ_Zprime_Scan_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_SVJ_PSWeight_94X_mcRun2_asymptotic_v3-v1/20000/0C7B5EBB-1FD5-EA11-9DEF-D4AE5269DC07.root',
       '/store/mc/RunIISummer16MiniAODv3/SVJ_Zprime_Scan_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_SVJ_PSWeight_94X_mcRun2_asymptotic_v3-v1/20000/0C87D404-BDD5-EA11-A32C-002590E7D7E2.root',
       '/store/mc/RunIISummer16MiniAODv3/SVJ_Zprime_Scan_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_SVJ_PSWeight_94X_mcRun2_asymptotic_v3-v1/20000/0CD37793-74C3-EA11-B234-FA163E642E93.root',
       '/store/mc/RunIISummer16MiniAODv3/SVJ_Zprime_Scan_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_SVJ_PSWeight_94X_mcRun2_asymptotic_v3-v1/20000/0E56ED66-56C3-EA11-B40F-FA163E914724.root',
       '/store/mc/RunIISummer16MiniAODv3/SVJ_Zprime_Scan_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_SVJ_PSWeight_94X_mcRun2_asymptotic_v3-v1/20000/0EEDF3AF-EFD4-EA11-AEE1-A0369FF882FA.root',
       '/store/mc/RunIISummer16MiniAODv3/SVJ_Zprime_Scan_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_SVJ_PSWeight_94X_mcRun2_asymptotic_v3-v1/20000/1052FFB1-50C3-EA11-B530-FA163ECBC71E.root',
       '/store/mc/RunIISummer16MiniAODv3/SVJ_Zprime_Scan_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_SVJ_PSWeight_94X_mcRun2_asymptotic_v3-v1/20000/12989FD3-BBD5-EA11-8A02-6C2B599C8F63.root',
       '/store/mc/RunIISummer16MiniAODv3/SVJ_Zprime_Scan_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_SVJ_PSWeight_94X_mcRun2_asymptotic_v3-v1/20000/12D6FC3B-B3D5-EA11-956E-A0369FF8852E.root',
       '/store/mc/RunIISummer16MiniAODv3/SVJ_Zprime_Scan_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_SVJ_PSWeight_94X_mcRun2_asymptotic_v3-v1/20000/14FF65B7-C6D5-EA11-ACB4-0CC47AFC3C9C.root',
       '/store/mc/RunIISummer16MiniAODv3/SVJ_Zprime_Scan_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_SVJ_PSWeight_94X_mcRun2_asymptotic_v3-v1/20000/18EC4599-19D5-EA11-987A-008CFA0A58F8.root',
       '/store/mc/RunIISummer16MiniAODv3/SVJ_Zprime_Scan_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_SVJ_PSWeight_94X_mcRun2_asymptotic_v3-v1/20000/1A17DA3C-F1D4-EA11-9B03-6CC2173D8740.root',
       '/store/mc/RunIISummer16MiniAODv3/SVJ_Zprime_Scan_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_SVJ_PSWeight_94X_mcRun2_asymptotic_v3-v1/20000/1A31A16A-ECD4-EA11-86E7-0CC47A7EED28.root',
       '/store/mc/RunIISummer16MiniAODv3/SVJ_Zprime_Scan_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_SVJ_PSWeight_94X_mcRun2_asymptotic_v3-v1/20000/1E632441-F3D4-EA11-974A-008CFA197EB0.root',
       '/store/mc/RunIISummer16MiniAODv3/SVJ_Zprime_Scan_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_SVJ_PSWeight_94X_mcRun2_asymptotic_v3-v1/20000/1E8FF01F-F3D5-EA11-8894-AC1F6B5676BA.root',
       '/store/mc/RunIISummer16MiniAODv3/SVJ_Zprime_Scan_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_SVJ_PSWeight_94X_mcRun2_asymptotic_v3-v1/20000/244283EB-2CD5-EA11-9F04-F4E9D497BBE0.root',
       '/store/mc/RunIISummer16MiniAODv3/SVJ_Zprime_Scan_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_SVJ_PSWeight_94X_mcRun2_asymptotic_v3-v1/20000/2EE0250C-56C3-EA11-A57A-FA163E3D6563.root',
       '/store/mc/RunIISummer16MiniAODv3/SVJ_Zprime_Scan_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_SVJ_PSWeight_94X_mcRun2_asymptotic_v3-v1/20000/32CA47AB-74C3-EA11-9C33-FA163EC25E50.root',
       '/store/mc/RunIISummer16MiniAODv3/SVJ_Zprime_Scan_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_SVJ_PSWeight_94X_mcRun2_asymptotic_v3-v1/20000/38C12842-1FD6-EA11-BFBE-B02628344E20.root',
       '/store/mc/RunIISummer16MiniAODv3/SVJ_Zprime_Scan_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_SVJ_PSWeight_94X_mcRun2_asymptotic_v3-v1/20000/3A300B24-F5D4-EA11-AA69-BC97E1290A31.root',
       '/store/mc/RunIISummer16MiniAODv3/SVJ_Zprime_Scan_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_SVJ_PSWeight_94X_mcRun2_asymptotic_v3-v1/20000/3ABEF166-BAD5-EA11-A98B-AC1F6BD5A08A.root',
       '/store/mc/RunIISummer16MiniAODv3/SVJ_Zprime_Scan_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_SVJ_PSWeight_94X_mcRun2_asymptotic_v3-v1/20000/42110EB0-B8D5-EA11-872A-001E675A6AB3.root',
       '/store/mc/RunIISummer16MiniAODv3/SVJ_Zprime_Scan_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_SVJ_PSWeight_94X_mcRun2_asymptotic_v3-v1/20000/42AEE589-78D6-EA11-9135-E0071B73B6C0.root',
       '/store/mc/RunIISummer16MiniAODv3/SVJ_Zprime_Scan_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_SVJ_PSWeight_94X_mcRun2_asymptotic_v3-v1/20000/4822A9F3-69D9-EA11-AD8A-0023AEEEB226.root',
       '/store/mc/RunIISummer16MiniAODv3/SVJ_Zprime_Scan_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_SVJ_PSWeight_94X_mcRun2_asymptotic_v3-v1/20000/48EB23C8-C3D5-EA11-8D5A-549F3525DD6C.root',
       '/store/mc/RunIISummer16MiniAODv3/SVJ_Zprime_Scan_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_SVJ_PSWeight_94X_mcRun2_asymptotic_v3-v1/20000/4E9A2C53-74C3-EA11-98CC-FA163EF8A78B.root',
       '/store/mc/RunIISummer16MiniAODv3/SVJ_Zprime_Scan_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_SVJ_PSWeight_94X_mcRun2_asymptotic_v3-v1/20000/52E6D641-8BC3-EA11-B011-FA163E4241EB.root',
       '/store/mc/RunIISummer16MiniAODv3/SVJ_Zprime_Scan_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_SVJ_PSWeight_94X_mcRun2_asymptotic_v3-v1/20000/5CA9098B-74C3-EA11-AFB6-FA163E62A2CB.root',
       '/store/mc/RunIISummer16MiniAODv3/SVJ_Zprime_Scan_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_SVJ_PSWeight_94X_mcRun2_asymptotic_v3-v1/20000/5E6F3FA0-EBD4-EA11-9224-AC1F6BAC7C2A.root',
       '/store/mc/RunIISummer16MiniAODv3/SVJ_Zprime_Scan_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_SVJ_PSWeight_94X_mcRun2_asymptotic_v3-v1/20000/5E825F2E-EED4-EA11-9989-0025904AC2CC.root',
       '/store/mc/RunIISummer16MiniAODv3/SVJ_Zprime_Scan_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_SVJ_PSWeight_94X_mcRun2_asymptotic_v3-v1/20000/68DCCB9D-EAD4-EA11-9464-1C34DA5D1C51.root',
       '/store/mc/RunIISummer16MiniAODv3/SVJ_Zprime_Scan_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_SVJ_PSWeight_94X_mcRun2_asymptotic_v3-v1/20000/6E6356C2-EAD4-EA11-B85A-1C34DA5D1C51.root',
       '/store/mc/RunIISummer16MiniAODv3/SVJ_Zprime_Scan_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_SVJ_PSWeight_94X_mcRun2_asymptotic_v3-v1/20000/74CA6465-74C3-EA11-BB03-FA163E10D9C3.root',
       '/store/mc/RunIISummer16MiniAODv3/SVJ_Zprime_Scan_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_SVJ_PSWeight_94X_mcRun2_asymptotic_v3-v1/20000/764488F5-ECD4-EA11-AA86-B496913C0E08.root',
       '/store/mc/RunIISummer16MiniAODv3/SVJ_Zprime_Scan_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_SVJ_PSWeight_94X_mcRun2_asymptotic_v3-v1/20000/7CB98ECA-22D5-EA11-AD47-0025901AFEA2.root',
       '/store/mc/RunIISummer16MiniAODv3/SVJ_Zprime_Scan_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_SVJ_PSWeight_94X_mcRun2_asymptotic_v3-v1/20000/82069597-F9C3-EA11-97B8-FA163EDF3236.root',
       '/store/mc/RunIISummer16MiniAODv3/SVJ_Zprime_Scan_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_SVJ_PSWeight_94X_mcRun2_asymptotic_v3-v1/20000/86C8D716-BFD5-EA11-9E24-52540043F7D0.root',
       '/store/mc/RunIISummer16MiniAODv3/SVJ_Zprime_Scan_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_SVJ_PSWeight_94X_mcRun2_asymptotic_v3-v1/20000/8AA7EF8C-74C3-EA11-89B8-FA163EED890C.root',
       '/store/mc/RunIISummer16MiniAODv3/SVJ_Zprime_Scan_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_SVJ_PSWeight_94X_mcRun2_asymptotic_v3-v1/20000/8ACB0EC3-55C3-EA11-B6AF-FA163EF0AD90.root',
       '/store/mc/RunIISummer16MiniAODv3/SVJ_Zprime_Scan_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_SVJ_PSWeight_94X_mcRun2_asymptotic_v3-v1/20000/96A32999-ECD4-EA11-BC19-0025905A60A8.root',
       '/store/mc/RunIISummer16MiniAODv3/SVJ_Zprime_Scan_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_SVJ_PSWeight_94X_mcRun2_asymptotic_v3-v1/20000/9C4CE6E4-20D5-EA11-ADB6-0CC47A4D7650.root',
       '/store/mc/RunIISummer16MiniAODv3/SVJ_Zprime_Scan_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_SVJ_PSWeight_94X_mcRun2_asymptotic_v3-v1/20000/9EC344ED-EBD4-EA11-A79D-B083FED12B5C.root',
       '/store/mc/RunIISummer16MiniAODv3/SVJ_Zprime_Scan_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_SVJ_PSWeight_94X_mcRun2_asymptotic_v3-v1/20000/A20ED37F-74C3-EA11-8E29-FA163E60E8D0.root',
       '/store/mc/RunIISummer16MiniAODv3/SVJ_Zprime_Scan_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_SVJ_PSWeight_94X_mcRun2_asymptotic_v3-v1/20000/A4B6A35A-74C3-EA11-B974-FA163EE8C95B.root',
       '/store/mc/RunIISummer16MiniAODv3/SVJ_Zprime_Scan_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_SVJ_PSWeight_94X_mcRun2_asymptotic_v3-v1/20000/A4ED8F91-74C3-EA11-A705-FA163EC34356.root',
       '/store/mc/RunIISummer16MiniAODv3/SVJ_Zprime_Scan_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_SVJ_PSWeight_94X_mcRun2_asymptotic_v3-v1/20000/A69AB060-CDD5-EA11-AC64-CCC5E5EF4F6E.root',
       '/store/mc/RunIISummer16MiniAODv3/SVJ_Zprime_Scan_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_SVJ_PSWeight_94X_mcRun2_asymptotic_v3-v1/20000/AA7731A7-55C3-EA11-98AF-FA163E1A82C4.root',
       '/store/mc/RunIISummer16MiniAODv3/SVJ_Zprime_Scan_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_SVJ_PSWeight_94X_mcRun2_asymptotic_v3-v1/20000/AAC8A9B4-74C3-EA11-BD30-FA163EA1AF8E.root',
       '/store/mc/RunIISummer16MiniAODv3/SVJ_Zprime_Scan_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_SVJ_PSWeight_94X_mcRun2_asymptotic_v3-v1/20000/B026FC0C-EBD4-EA11-914F-0CC47AFF0470.root',
       '/store/mc/RunIISummer16MiniAODv3/SVJ_Zprime_Scan_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_SVJ_PSWeight_94X_mcRun2_asymptotic_v3-v1/20000/BA57EB51-D8C3-EA11-8E7F-FA163E0B0E4C.root',
       '/store/mc/RunIISummer16MiniAODv3/SVJ_Zprime_Scan_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_SVJ_PSWeight_94X_mcRun2_asymptotic_v3-v1/20000/BC94121F-9BD7-EA11-A16A-A0369FD0B124.root',
       '/store/mc/RunIISummer16MiniAODv3/SVJ_Zprime_Scan_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_SVJ_PSWeight_94X_mcRun2_asymptotic_v3-v1/20000/C00E246C-BBD5-EA11-A90D-A0369FC5FC9C.root',
       '/store/mc/RunIISummer16MiniAODv3/SVJ_Zprime_Scan_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_SVJ_PSWeight_94X_mcRun2_asymptotic_v3-v1/20000/C23CD9E1-10D5-EA11-AE13-0242AC130002.root',
       '/store/mc/RunIISummer16MiniAODv3/SVJ_Zprime_Scan_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_SVJ_PSWeight_94X_mcRun2_asymptotic_v3-v1/20000/C2D00ADD-57C3-EA11-8C18-FA163EF76866.root',
       '/store/mc/RunIISummer16MiniAODv3/SVJ_Zprime_Scan_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_SVJ_PSWeight_94X_mcRun2_asymptotic_v3-v1/20000/C666323A-09D5-EA11-AA80-0CC47A5FBE25.root',
       '/store/mc/RunIISummer16MiniAODv3/SVJ_Zprime_Scan_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_SVJ_PSWeight_94X_mcRun2_asymptotic_v3-v1/20000/CCB68A73-56C3-EA11-89C2-FA163EC26E29.root',
       '/store/mc/RunIISummer16MiniAODv3/SVJ_Zprime_Scan_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_SVJ_PSWeight_94X_mcRun2_asymptotic_v3-v1/20000/D0E42E41-B9D5-EA11-B8BF-FA163E32771A.root',
       '/store/mc/RunIISummer16MiniAODv3/SVJ_Zprime_Scan_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_SVJ_PSWeight_94X_mcRun2_asymptotic_v3-v1/20000/D28307CD-EBD4-EA11-982A-0CC47AD98B90.root',
       '/store/mc/RunIISummer16MiniAODv3/SVJ_Zprime_Scan_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_SVJ_PSWeight_94X_mcRun2_asymptotic_v3-v1/20000/D8088F96-ECD4-EA11-9C47-0025905A60B2.root',
       '/store/mc/RunIISummer16MiniAODv3/SVJ_Zprime_Scan_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_SVJ_PSWeight_94X_mcRun2_asymptotic_v3-v1/20000/DE57F1AE-74C3-EA11-B100-FA163E4E99DE.root',
       '/store/mc/RunIISummer16MiniAODv3/SVJ_Zprime_Scan_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_SVJ_PSWeight_94X_mcRun2_asymptotic_v3-v1/20000/E05561D7-54C3-EA11-ACCB-FA163E7FF6AC.root',
       '/store/mc/RunIISummer16MiniAODv3/SVJ_Zprime_Scan_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_SVJ_PSWeight_94X_mcRun2_asymptotic_v3-v1/20000/E084430B-BCD5-EA11-A601-509A4C748063.root',
       '/store/mc/RunIISummer16MiniAODv3/SVJ_Zprime_Scan_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_SVJ_PSWeight_94X_mcRun2_asymptotic_v3-v1/20000/E096D368-EFD4-EA11-8625-0242AC1C0514.root',
       '/store/mc/RunIISummer16MiniAODv3/SVJ_Zprime_Scan_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_SVJ_PSWeight_94X_mcRun2_asymptotic_v3-v1/20000/E0ECDA95-94C3-EA11-A3B9-FA163E7317F8.root',
       '/store/mc/RunIISummer16MiniAODv3/SVJ_Zprime_Scan_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_SVJ_PSWeight_94X_mcRun2_asymptotic_v3-v1/20000/E22EA384-ECD4-EA11-B1E1-246E96D14C70.root',
       '/store/mc/RunIISummer16MiniAODv3/SVJ_Zprime_Scan_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_SVJ_PSWeight_94X_mcRun2_asymptotic_v3-v1/20000/E4BE40E8-EAD4-EA11-9E09-0025905C2CE6.root',
       '/store/mc/RunIISummer16MiniAODv3/SVJ_Zprime_Scan_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_SVJ_PSWeight_94X_mcRun2_asymptotic_v3-v1/20000/E6237DE5-8CD8-EA11-AF46-A4BF0112BDD2.root',
       '/store/mc/RunIISummer16MiniAODv3/SVJ_Zprime_Scan_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_SVJ_PSWeight_94X_mcRun2_asymptotic_v3-v1/20000/E82614E3-D2D5-EA11-A10B-0CC47AFF02AC.root',
       '/store/mc/RunIISummer16MiniAODv3/SVJ_Zprime_Scan_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_SVJ_PSWeight_94X_mcRun2_asymptotic_v3-v1/20000/EADBE018-EDD4-EA11-90A7-F4E9D4A37DB0.root',
       '/store/mc/RunIISummer16MiniAODv3/SVJ_Zprime_Scan_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_SVJ_PSWeight_94X_mcRun2_asymptotic_v3-v1/20000/EC3D3749-AAC3-EA11-B7A8-FA163EED31B5.root',
       '/store/mc/RunIISummer16MiniAODv3/SVJ_Zprime_Scan_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_SVJ_PSWeight_94X_mcRun2_asymptotic_v3-v1/20000/F06969B9-50C3-EA11-9AEF-FA163EFD8B29.root',
       '/store/mc/RunIISummer16MiniAODv3/SVJ_Zprime_Scan_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_SVJ_PSWeight_94X_mcRun2_asymptotic_v3-v1/20000/F29B2B7C-74C3-EA11-A742-FA163E2F1134.root',
       '/store/mc/RunIISummer16MiniAODv3/SVJ_Zprime_Scan_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_SVJ_PSWeight_94X_mcRun2_asymptotic_v3-v1/20000/F2FB6832-70D8-EA11-B9E5-A0369FE2C19A.root',
       '/store/mc/RunIISummer16MiniAODv3/SVJ_Zprime_Scan_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_SVJ_PSWeight_94X_mcRun2_asymptotic_v3-v1/20000/F48126FD-FED4-EA11-84F2-E0071B7A4550.root',
       '/store/mc/RunIISummer16MiniAODv3/SVJ_Zprime_Scan_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_SVJ_PSWeight_94X_mcRun2_asymptotic_v3-v1/20000/F658A8D9-EAD4-EA11-8B7E-FA163E605630.root',
       '/store/mc/RunIISummer16MiniAODv3/SVJ_Zprime_Scan_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_SVJ_PSWeight_94X_mcRun2_asymptotic_v3-v1/20000/F8DB72E6-E7D5-EA11-960A-002590E3A024.root',
       '/store/mc/RunIISummer16MiniAODv3/SVJ_Zprime_Scan_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_SVJ_PSWeight_94X_mcRun2_asymptotic_v3-v1/20000/FA02E19D-12D5-EA11-8ADB-003048CB8584.root',
       '/store/mc/RunIISummer16MiniAODv3/SVJ_Zprime_Scan_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_SVJ_PSWeight_94X_mcRun2_asymptotic_v3-v1/20000/FE4EC2BD-55C3-EA11-8D7D-FA163E33D49C.root',
] )
