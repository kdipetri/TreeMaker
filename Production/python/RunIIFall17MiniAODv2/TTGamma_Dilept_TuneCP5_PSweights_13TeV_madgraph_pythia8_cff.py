import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIFall17MiniAODv2/TTGamma_Dilept_TuneCP5_PSweights_13TeV_madgraph_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/80000/021A0186-3D6C-E811-9BF4-A0369FE2C1C8.root',
       '/store/mc/RunIIFall17MiniAODv2/TTGamma_Dilept_TuneCP5_PSweights_13TeV_madgraph_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/80000/02AFFBCD-C06B-E811-9E55-A0369FD0B38E.root',
       '/store/mc/RunIIFall17MiniAODv2/TTGamma_Dilept_TuneCP5_PSweights_13TeV_madgraph_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/80000/0427AD18-4F6C-E811-A8CD-A0369FE2C20C.root',
       '/store/mc/RunIIFall17MiniAODv2/TTGamma_Dilept_TuneCP5_PSweights_13TeV_madgraph_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/80000/04C16CA5-FF6B-E811-AC1C-A0369FE2C176.root',
       '/store/mc/RunIIFall17MiniAODv2/TTGamma_Dilept_TuneCP5_PSweights_13TeV_madgraph_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/80000/0882C322-946B-E811-BF98-A0369FD0B330.root',
       '/store/mc/RunIIFall17MiniAODv2/TTGamma_Dilept_TuneCP5_PSweights_13TeV_madgraph_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/80000/08917789-4B6C-E811-8611-A0369FE2C174.root',
       '/store/mc/RunIIFall17MiniAODv2/TTGamma_Dilept_TuneCP5_PSweights_13TeV_madgraph_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/80000/0C4EB82B-946B-E811-8DAB-AC1F6B0DE3F4.root',
       '/store/mc/RunIIFall17MiniAODv2/TTGamma_Dilept_TuneCP5_PSweights_13TeV_madgraph_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/80000/1023CE9B-616C-E811-9A8B-A0369FD0B24E.root',
       '/store/mc/RunIIFall17MiniAODv2/TTGamma_Dilept_TuneCP5_PSweights_13TeV_madgraph_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/80000/102656DE-2F6C-E811-9BD4-A0369FD0B1FE.root',
       '/store/mc/RunIIFall17MiniAODv2/TTGamma_Dilept_TuneCP5_PSweights_13TeV_madgraph_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/80000/10762033-4D6C-E811-B5D2-A0369FE2C0D2.root',
       '/store/mc/RunIIFall17MiniAODv2/TTGamma_Dilept_TuneCP5_PSweights_13TeV_madgraph_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/80000/1682EBDF-456C-E811-A7FE-A0369FE2C152.root',
       '/store/mc/RunIIFall17MiniAODv2/TTGamma_Dilept_TuneCP5_PSweights_13TeV_madgraph_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/80000/1E430F27-686B-E811-87A5-AC1F6B0DE4A8.root',
       '/store/mc/RunIIFall17MiniAODv2/TTGamma_Dilept_TuneCP5_PSweights_13TeV_madgraph_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/80000/2A719B98-8A6B-E811-ADDD-AC1F6B0DE4A8.root',
       '/store/mc/RunIIFall17MiniAODv2/TTGamma_Dilept_TuneCP5_PSweights_13TeV_madgraph_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/80000/2A86CC13-286C-E811-AF46-AC1F6B0F7B16.root',
       '/store/mc/RunIIFall17MiniAODv2/TTGamma_Dilept_TuneCP5_PSweights_13TeV_madgraph_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/80000/2C224F0E-3F6C-E811-B814-A0369FE2C11E.root',
       '/store/mc/RunIIFall17MiniAODv2/TTGamma_Dilept_TuneCP5_PSweights_13TeV_madgraph_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/80000/2C5F478F-3D6C-E811-A7D5-A0369FE2C216.root',
       '/store/mc/RunIIFall17MiniAODv2/TTGamma_Dilept_TuneCP5_PSweights_13TeV_madgraph_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/80000/32B61F3A-AE6B-E811-BCC7-A0369FE2C0D2.root',
       '/store/mc/RunIIFall17MiniAODv2/TTGamma_Dilept_TuneCP5_PSweights_13TeV_madgraph_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/80000/38BDCA66-E76B-E811-82A2-AC1F6B0DE3F4.root',
       '/store/mc/RunIIFall17MiniAODv2/TTGamma_Dilept_TuneCP5_PSweights_13TeV_madgraph_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/80000/3A5585F5-216C-E811-9704-AC1F6B0DE3F4.root',
       '/store/mc/RunIIFall17MiniAODv2/TTGamma_Dilept_TuneCP5_PSweights_13TeV_madgraph_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/80000/3AA56C84-516C-E811-99B3-A0369FE2C174.root',
       '/store/mc/RunIIFall17MiniAODv2/TTGamma_Dilept_TuneCP5_PSweights_13TeV_madgraph_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/80000/3C363A28-9E6B-E811-B424-A0369FD0B300.root',
       '/store/mc/RunIIFall17MiniAODv2/TTGamma_Dilept_TuneCP5_PSweights_13TeV_madgraph_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/80000/447E1E68-A26B-E811-8D73-A0369FE2C1A6.root',
       '/store/mc/RunIIFall17MiniAODv2/TTGamma_Dilept_TuneCP5_PSweights_13TeV_madgraph_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/80000/4E455746-3C6C-E811-BEC5-A0369FE2C188.root',
       '/store/mc/RunIIFall17MiniAODv2/TTGamma_Dilept_TuneCP5_PSweights_13TeV_madgraph_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/80000/4E783BB1-746B-E811-8F96-A0369FD0B3B8.root',
       '/store/mc/RunIIFall17MiniAODv2/TTGamma_Dilept_TuneCP5_PSweights_13TeV_madgraph_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/80000/501C89EB-406C-E811-B62E-A0369FD0B152.root',
       '/store/mc/RunIIFall17MiniAODv2/TTGamma_Dilept_TuneCP5_PSweights_13TeV_madgraph_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/80000/58481DCD-D36B-E811-80D6-A0369FE2C082.root',
       '/store/mc/RunIIFall17MiniAODv2/TTGamma_Dilept_TuneCP5_PSweights_13TeV_madgraph_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/80000/5AAB3195-376C-E811-9282-A0369FD0B198.root',
       '/store/mc/RunIIFall17MiniAODv2/TTGamma_Dilept_TuneCP5_PSweights_13TeV_madgraph_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/80000/5E9DCF91-516C-E811-AD99-A0369FD0B1AC.root',
       '/store/mc/RunIIFall17MiniAODv2/TTGamma_Dilept_TuneCP5_PSweights_13TeV_madgraph_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/80000/604E8ACE-476C-E811-93E5-A0369FE2C19A.root',
       '/store/mc/RunIIFall17MiniAODv2/TTGamma_Dilept_TuneCP5_PSweights_13TeV_madgraph_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/80000/644AE234-E96B-E811-9388-A0369FE2C1E8.root',
       '/store/mc/RunIIFall17MiniAODv2/TTGamma_Dilept_TuneCP5_PSweights_13TeV_madgraph_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/80000/645CBBED-356C-E811-8414-A0369FD0B1B0.root',
       '/store/mc/RunIIFall17MiniAODv2/TTGamma_Dilept_TuneCP5_PSweights_13TeV_madgraph_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/80000/66C3BD58-8D6B-E811-AAC7-A0369FE2C0D0.root',
       '/store/mc/RunIIFall17MiniAODv2/TTGamma_Dilept_TuneCP5_PSweights_13TeV_madgraph_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/80000/6CEB8B90-496C-E811-99DF-A0369FD0B168.root',
       '/store/mc/RunIIFall17MiniAODv2/TTGamma_Dilept_TuneCP5_PSweights_13TeV_madgraph_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/80000/6EECCA85-2B6C-E811-834B-AC1F6B0DE454.root',
       '/store/mc/RunIIFall17MiniAODv2/TTGamma_Dilept_TuneCP5_PSweights_13TeV_madgraph_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/80000/70798F19-3F6C-E811-A554-A0369FE2C0AC.root',
       '/store/mc/RunIIFall17MiniAODv2/TTGamma_Dilept_TuneCP5_PSweights_13TeV_madgraph_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/80000/70C6C103-816B-E811-A8F6-A0369FD0B242.root',
       '/store/mc/RunIIFall17MiniAODv2/TTGamma_Dilept_TuneCP5_PSweights_13TeV_madgraph_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/80000/72952E11-B36B-E811-B676-AC1F6B0DE294.root',
       '/store/mc/RunIIFall17MiniAODv2/TTGamma_Dilept_TuneCP5_PSweights_13TeV_madgraph_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/80000/7404D07D-A76B-E811-B8A3-A0369FE2C170.root',
       '/store/mc/RunIIFall17MiniAODv2/TTGamma_Dilept_TuneCP5_PSweights_13TeV_madgraph_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/80000/76338B76-3A6C-E811-8D0F-AC1F6B0F7B16.root',
       '/store/mc/RunIIFall17MiniAODv2/TTGamma_Dilept_TuneCP5_PSweights_13TeV_madgraph_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/80000/78BE0590-4B6C-E811-905A-A0369FD0B33E.root',
       '/store/mc/RunIIFall17MiniAODv2/TTGamma_Dilept_TuneCP5_PSweights_13TeV_madgraph_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/80000/7E207085-516C-E811-83D4-A0369FD0B300.root',
       '/store/mc/RunIIFall17MiniAODv2/TTGamma_Dilept_TuneCP5_PSweights_13TeV_madgraph_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/80000/8017C48A-316C-E811-8AD7-A0369FE2C1C8.root',
       '/store/mc/RunIIFall17MiniAODv2/TTGamma_Dilept_TuneCP5_PSweights_13TeV_madgraph_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/80000/8840BA82-2B6C-E811-B2B1-AC1F6B0DE33A.root',
       '/store/mc/RunIIFall17MiniAODv2/TTGamma_Dilept_TuneCP5_PSweights_13TeV_madgraph_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/80000/887B810A-C56B-E811-8808-A0369FD0B31E.root',
       '/store/mc/RunIIFall17MiniAODv2/TTGamma_Dilept_TuneCP5_PSweights_13TeV_madgraph_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/80000/94AF7A6C-426C-E811-907B-A0369FE2C0AC.root',
       '/store/mc/RunIIFall17MiniAODv2/TTGamma_Dilept_TuneCP5_PSweights_13TeV_madgraph_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/80000/9C0C538A-556C-E811-A625-A0369FE2C174.root',
       '/store/mc/RunIIFall17MiniAODv2/TTGamma_Dilept_TuneCP5_PSweights_13TeV_madgraph_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/80000/9E4E8660-536C-E811-8A48-AC1F6B0DE33A.root',
       '/store/mc/RunIIFall17MiniAODv2/TTGamma_Dilept_TuneCP5_PSweights_13TeV_madgraph_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/80000/A019D587-426C-E811-8F76-AC1F6B0DE4AE.root',
       '/store/mc/RunIIFall17MiniAODv2/TTGamma_Dilept_TuneCP5_PSweights_13TeV_madgraph_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/80000/A05E30A3-0E6C-E811-9539-A0369FE2C092.root',
       '/store/mc/RunIIFall17MiniAODv2/TTGamma_Dilept_TuneCP5_PSweights_13TeV_madgraph_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/80000/A08A7393-5E6C-E811-9C40-AC1F6B0DE4A8.root',
       '/store/mc/RunIIFall17MiniAODv2/TTGamma_Dilept_TuneCP5_PSweights_13TeV_madgraph_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/80000/A2565FC4-326C-E811-A96E-A0369FE2C1A0.root',
       '/store/mc/RunIIFall17MiniAODv2/TTGamma_Dilept_TuneCP5_PSweights_13TeV_madgraph_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/80000/A64CB733-7C6B-E811-9E71-A0369FE2C1A0.root',
       '/store/mc/RunIIFall17MiniAODv2/TTGamma_Dilept_TuneCP5_PSweights_13TeV_madgraph_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/80000/A8F67F1E-446C-E811-89E3-A0369FE2C184.root',
       '/store/mc/RunIIFall17MiniAODv2/TTGamma_Dilept_TuneCP5_PSweights_13TeV_madgraph_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/80000/ACA388FD-6F6B-E811-9F35-A0369FD0B3EC.root',
       '/store/mc/RunIIFall17MiniAODv2/TTGamma_Dilept_TuneCP5_PSweights_13TeV_madgraph_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/80000/ACDE47D4-8F6B-E811-90F6-A0369FE2C188.root',
       '/store/mc/RunIIFall17MiniAODv2/TTGamma_Dilept_TuneCP5_PSweights_13TeV_madgraph_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/80000/AE86FD37-546B-E811-B027-A0369FE2C126.root',
       '/store/mc/RunIIFall17MiniAODv2/TTGamma_Dilept_TuneCP5_PSweights_13TeV_madgraph_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/80000/B27563F2-356C-E811-BCA8-A0369FD0B32E.root',
       '/store/mc/RunIIFall17MiniAODv2/TTGamma_Dilept_TuneCP5_PSweights_13TeV_madgraph_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/80000/B4D34D83-B06B-E811-A2BC-AC1F6B0DE45C.root',
       '/store/mc/RunIIFall17MiniAODv2/TTGamma_Dilept_TuneCP5_PSweights_13TeV_madgraph_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/80000/B4E1A7EE-2C6C-E811-9A1A-A0369FD0B31E.root',
       '/store/mc/RunIIFall17MiniAODv2/TTGamma_Dilept_TuneCP5_PSweights_13TeV_madgraph_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/80000/B61F469D-6D6C-E811-821D-A0369FD0B1B0.root',
       '/store/mc/RunIIFall17MiniAODv2/TTGamma_Dilept_TuneCP5_PSweights_13TeV_madgraph_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/80000/B66E6115-4F6C-E811-B099-A0369FD0B290.root',
       '/store/mc/RunIIFall17MiniAODv2/TTGamma_Dilept_TuneCP5_PSweights_13TeV_madgraph_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/80000/B6EEED25-886B-E811-9121-A0369FE2C026.root',
       '/store/mc/RunIIFall17MiniAODv2/TTGamma_Dilept_TuneCP5_PSweights_13TeV_madgraph_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/80000/BA8FD072-636B-E811-BFFF-AC1F6B0DE2EA.root',
       '/store/mc/RunIIFall17MiniAODv2/TTGamma_Dilept_TuneCP5_PSweights_13TeV_madgraph_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/80000/BEBEDC1F-446C-E811-B451-A0369FE2C152.root',
       '/store/mc/RunIIFall17MiniAODv2/TTGamma_Dilept_TuneCP5_PSweights_13TeV_madgraph_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/80000/C04A646D-9B6B-E811-8B17-A0369FD0B12C.root',
       '/store/mc/RunIIFall17MiniAODv2/TTGamma_Dilept_TuneCP5_PSweights_13TeV_madgraph_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/80000/C421F7AD-606B-E811-AE36-A0369FE2C0AC.root',
       '/store/mc/RunIIFall17MiniAODv2/TTGamma_Dilept_TuneCP5_PSweights_13TeV_madgraph_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/80000/C8ACF457-2E6C-E811-8C11-A0369FE2C1C8.root',
       '/store/mc/RunIIFall17MiniAODv2/TTGamma_Dilept_TuneCP5_PSweights_13TeV_madgraph_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/80000/CA63A326-9E6B-E811-AC74-A0369FE2C0E0.root',
       '/store/mc/RunIIFall17MiniAODv2/TTGamma_Dilept_TuneCP5_PSweights_13TeV_madgraph_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/80000/CC2927B6-A46B-E811-9AA6-A0369FE2C146.root',
       '/store/mc/RunIIFall17MiniAODv2/TTGamma_Dilept_TuneCP5_PSweights_13TeV_madgraph_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/80000/D06A0A74-966B-E811-9BAC-A0369FD0B330.root',
       '/store/mc/RunIIFall17MiniAODv2/TTGamma_Dilept_TuneCP5_PSweights_13TeV_madgraph_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/80000/DABC3A47-D26B-E811-A102-A0369FE2C082.root',
       '/store/mc/RunIIFall17MiniAODv2/TTGamma_Dilept_TuneCP5_PSweights_13TeV_madgraph_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/80000/E20CF24E-516C-E811-871F-AC1F6B0F6758.root',
       '/store/mc/RunIIFall17MiniAODv2/TTGamma_Dilept_TuneCP5_PSweights_13TeV_madgraph_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/80000/E2902C16-3F6C-E811-AF0D-A0369FD0B306.root',
       '/store/mc/RunIIFall17MiniAODv2/TTGamma_Dilept_TuneCP5_PSweights_13TeV_madgraph_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/80000/E649598E-D86B-E811-976C-AC1F6B0DE22A.root',
       '/store/mc/RunIIFall17MiniAODv2/TTGamma_Dilept_TuneCP5_PSweights_13TeV_madgraph_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/80000/E8AA2A02-866B-E811-833F-A0369FE2C1A0.root',
       '/store/mc/RunIIFall17MiniAODv2/TTGamma_Dilept_TuneCP5_PSweights_13TeV_madgraph_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/80000/F0BEBAF9-406C-E811-9C99-A0369FD0B344.root',
       '/store/mc/RunIIFall17MiniAODv2/TTGamma_Dilept_TuneCP5_PSweights_13TeV_madgraph_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/80000/F2CA389B-B96B-E811-9DF7-A0369FE2C146.root',
       '/store/mc/RunIIFall17MiniAODv2/TTGamma_Dilept_TuneCP5_PSweights_13TeV_madgraph_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/80000/FAB27C11-196C-E811-9419-A0369FE2C0E0.root',
] )