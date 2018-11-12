import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_300to470_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/008761B6-F5B4-E611-AC01-0CC47A706D26.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_300to470_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/08232329-18B5-E611-AD93-0CC47A7C3472.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_300to470_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/0EB64255-38B5-E611-BF9B-0025904C7A58.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_300to470_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/10648A17-24B5-E611-BCF4-9CB654ADA4C4.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_300to470_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/10DF83A0-08B5-E611-8460-0CC47A7C357E.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_300to470_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/12438F18-33B5-E611-969D-001E6739B849.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_300to470_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/16CE947E-EDB4-E611-BD94-0CC47AC087AE.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_300to470_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/18848AE1-D2B4-E611-85A1-001E673C83E7.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_300to470_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/18D91A07-13B5-E611-8F98-0CC47A4D7692.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_300to470_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/2240C897-63B5-E611-A302-002590DE6E7C.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_300to470_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/28CCE30D-40B5-E611-8863-9CB65404FC30.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_300to470_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/2A32C09A-23B5-E611-A90A-0CC47AC08BC8.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_300to470_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/2C14E281-54B5-E611-8911-0CC47A7C345C.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_300to470_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/307639D1-4CB5-E611-9E10-0CC47A78A4A6.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_300to470_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/385ED17A-61B5-E611-B461-001E6739CFA9.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_300to470_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/38AA975A-4CB5-E611-8390-0CC47A4D769E.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_300to470_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/3A6F2867-A6B5-E611-8C01-0CC47A4D75F2.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_300to470_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/44947C0D-4BB5-E611-B714-0025905A48B2.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_300to470_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/4A195C7A-14B5-E611-A55F-0025905A48F2.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_300to470_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/50ACBC85-F1B4-E611-A262-001E6739B969.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_300to470_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/520A3FB4-EAB4-E611-BB6C-9CB654AEBD76.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_300to470_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/5430E70A-CDB5-E611-9D8D-001E6739AC59.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_300to470_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/54E6F5A8-47B5-E611-94EC-0CC47A4C8F0C.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_300to470_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/588987B7-46B5-E611-860C-0025905A48B2.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_300to470_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/5A7EC44D-40B5-E611-B491-0CC47A4D76C0.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_300to470_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/6852E7D0-44B5-E611-AD18-0CC47AC08BC8.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_300to470_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/68D0E0EA-53B5-E611-9877-0025905B85FC.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_300to470_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/703ABD6E-4FB5-E611-AB34-0025905B85CA.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_300to470_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/709B8DBE-2DB5-E611-A617-001E67399C89.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_300to470_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/72C75655-CCB5-E611-BC02-0025905B8598.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_300to470_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/78729A9D-17B5-E611-8119-001E6739AB19.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_300to470_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/78A21282-44B5-E611-833F-0CC47A4D7628.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_300to470_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/7AFA19AB-55B5-E611-8D55-0CC47A4C8EE8.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_300to470_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/82D9BD64-20B5-E611-AA78-0025904C7F62.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_300to470_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/860D084F-CCB5-E611-84B7-0CC47A4D768E.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_300to470_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/8A9C223A-20B5-E611-893B-0025905A612C.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_300to470_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/9224345C-2AB5-E611-8376-001E673C7D8F.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_300to470_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/949EF104-DFB4-E611-8FAB-001E6739B849.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_300to470_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/961FE67C-49B5-E611-9C12-0025905B85EC.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_300to470_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/98AE3EF1-36B5-E611-9B4D-0025905B855A.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_300to470_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/9AF0E26B-38B5-E611-AB49-001E6739A959.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_300to470_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/9AFA3974-4CB5-E611-8071-001E673D0679.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_300to470_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/9C01E936-31B5-E611-8EA3-002618FDA26D.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_300to470_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/9E60A872-52B5-E611-B367-0025905A60B4.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_300to470_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/9EC98003-53B5-E611-826A-0025905A60B4.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_300to470_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/A05CE308-47B5-E611-82B3-0CC47A745298.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_300to470_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/A0E95302-05B5-E611-ACD2-001E6739BB01.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_300to470_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/A6C5DA5A-2AB5-E611-B154-0025904B8708.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_300to470_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/A8B61CEE-E4B4-E611-9171-001E673CFA89.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_300to470_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/BC88E2A7-E3B4-E611-A438-0CC47AC08BD4.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_300to470_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/C0683C0C-CDB5-E611-907A-0CC47A706FFE.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_300to470_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/C44F1496-30B5-E611-9BFC-0CC47A4D7666.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_300to470_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/C602CEC8-39B5-E611-B6BD-0025905B855E.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_300to470_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/C8AE02EE-E6B4-E611-8D2B-001E6739D281.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_300to470_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/C8FD21F1-47B5-E611-A0FA-0CC47AC08BC8.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_300to470_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/CA0D2BE8-08B5-E611-91F1-0CC47A7452D0.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_300to470_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/CC679676-49B5-E611-9CC6-0CC47A4C8F18.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_300to470_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/DA74F40C-21B5-E611-B5B8-0CC47A78A4B8.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_300to470_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/E2D8872B-4EB5-E611-BC66-0CC47A745284.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_300to470_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/EA88625F-19B5-E611-8466-003048FFD734.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_300to470_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/EC8D2757-3CB5-E611-A694-001E6739B849.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_300to470_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/EEF1F17D-44B5-E611-80C0-0CC47A78A3B4.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_300to470_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/F0588B62-CCB4-E611-BC7B-001E673C7FB1.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_300to470_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/F201B80B-4BB5-E611-9226-0CC47A4D7630.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_300to470_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/F2C3C436-3DB5-E611-8E82-0CC47A4C8F1C.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_300to470_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/F2CF24DE-42B5-E611-9853-0CC47A4D76B6.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_300to470_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/F4CEA08C-F4B4-E611-A6ED-001E673D21B9.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_300to470_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/F61350F0-26B5-E611-BBE2-001E6739A959.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_300to470_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/FC052760-2EB5-E611-AB81-0CC47AC08BD4.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_300to470_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/FEA76CA3-E3B4-E611-8DDB-001E67399C89.root',
] )
