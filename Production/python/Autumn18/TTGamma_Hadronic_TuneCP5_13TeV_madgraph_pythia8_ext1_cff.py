import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIAutumn18MiniAOD/TTGamma_Hadronic_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/110000/022DD6D8-CDF9-8745-B37C-0BC56DD64323.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTGamma_Hadronic_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/110000/03221E58-FCE0-EE4C-B285-60B357BC5398.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTGamma_Hadronic_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/110000/05E15DD4-ADA9-E947-A5E5-CAD8A3348003.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTGamma_Hadronic_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/110000/0628D7D0-B398-7E4B-A869-AB2E7B9782FD.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTGamma_Hadronic_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/110000/07FDEF11-87EA-764A-8C42-AD113335979F.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTGamma_Hadronic_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/110000/0B909800-107E-074C-B790-23158A049B1A.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTGamma_Hadronic_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/110000/0E939119-1562-974C-82C6-64E12049A5E7.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTGamma_Hadronic_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/110000/10B1BF92-D3AF-F148-9FDA-A91C5CB4563B.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTGamma_Hadronic_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/110000/149437C0-1A43-2044-8530-C28485491B61.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTGamma_Hadronic_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/110000/16F72C5A-C312-E143-B312-B97FA96D1AB7.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTGamma_Hadronic_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/110000/18003A54-4D4F-8046-89F4-37C6E117EEC1.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTGamma_Hadronic_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/110000/1B6800B5-323E-0849-B196-AEC114EA3910.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTGamma_Hadronic_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/110000/2628C3B8-92CB-844B-AF6B-F84DB93E5FB6.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTGamma_Hadronic_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/110000/272E92D1-AAE5-2B47-83F5-C165DB7AD1C1.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTGamma_Hadronic_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/110000/298FDA76-232C-6740-B625-76FDD68EF960.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTGamma_Hadronic_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/110000/2BFFDFBF-BD35-884D-88AB-146FB337F36B.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTGamma_Hadronic_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/110000/2C1589F5-E45F-3240-8246-1C931789A5A6.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTGamma_Hadronic_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/110000/2EB5853E-B47E-E84F-A1F3-E1517AC9F20E.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTGamma_Hadronic_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/110000/32411CD5-DB80-B64B-AE0A-49C57E325A04.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTGamma_Hadronic_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/110000/3AC856EC-C619-9841-86FB-671626FF0378.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTGamma_Hadronic_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/110000/43977952-1253-5946-BB5E-AF2E72F2E5A5.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTGamma_Hadronic_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/110000/4747DB08-7422-A549-95D0-0B8082A34852.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTGamma_Hadronic_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/110000/4B2FC9A0-CC30-C84D-8FC5-A0317C46A457.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTGamma_Hadronic_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/110000/4C471C65-6948-3445-A247-1BD4F4F97B08.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTGamma_Hadronic_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/110000/5097EE0D-81A3-9E47-9504-AD9758D54BF2.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTGamma_Hadronic_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/110000/537F1BE8-0BF7-3945-949D-F3919423AF6D.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTGamma_Hadronic_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/110000/54A0694A-CA60-6443-A034-1918F619D0B8.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTGamma_Hadronic_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/110000/5E30D3F9-A678-7D4E-AE35-94ECA55B270F.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTGamma_Hadronic_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/110000/610715A3-5906-BD4F-B05A-DAC02151DC7E.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTGamma_Hadronic_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/110000/638B3850-E51B-BA42-B5F6-C5E8C2700E53.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTGamma_Hadronic_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/110000/6BD8982C-3CDD-8941-B05F-02282263495E.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTGamma_Hadronic_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/110000/6DDF349B-180C-924E-B74B-0C1C1A878C91.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTGamma_Hadronic_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/110000/742FAE07-0146-E748-BDEA-BEF7DDF014A4.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTGamma_Hadronic_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/110000/769D648C-EDC2-9648-BD88-5E6220FE9F3D.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTGamma_Hadronic_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/110000/7B5F863C-FB1D-CF45-9F2C-7D21F5A73B15.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTGamma_Hadronic_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/110000/8100EBA7-2B1A-F74D-8F96-42F29BB7564C.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTGamma_Hadronic_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/110000/82EA38DE-EDEB-B34E-8967-E5A183B14FE8.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTGamma_Hadronic_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/110000/84D7534F-D926-014A-B3D3-0B440209CC75.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTGamma_Hadronic_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/110000/85404F1B-793F-0A4D-8726-46E61EEE3FA2.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTGamma_Hadronic_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/110000/8A78E628-A207-304C-ACAD-FFCC6F503C52.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTGamma_Hadronic_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/110000/971B67FA-7B67-8B44-AA26-67C594F5CDED.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTGamma_Hadronic_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/110000/9A886837-97C1-7C4C-A504-580CC4EC983F.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTGamma_Hadronic_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/110000/9BEA5550-3F92-D048-A720-34D6CF23D3FF.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTGamma_Hadronic_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/110000/9CABA433-B335-6A47-9DCE-483DD3752E8A.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTGamma_Hadronic_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/110000/A1BF1F51-B37C-EE4E-A27B-CA0E10B09A0F.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTGamma_Hadronic_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/110000/A3EB0A7D-33E2-E54E-BFD1-D44596BB2261.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTGamma_Hadronic_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/110000/A4D57DCF-6EC2-A24B-A0A6-7E20F9AED643.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTGamma_Hadronic_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/110000/A6D4B6A3-46FC-0A41-A14B-B94996CA1D96.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTGamma_Hadronic_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/110000/AD6B58AB-A392-3C42-A552-C3B71ED29096.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTGamma_Hadronic_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/110000/AD7FD981-CA5F-B746-BC53-50940FF3C8C0.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTGamma_Hadronic_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/110000/B1B71919-209E-964D-863B-FC2E89492BF6.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTGamma_Hadronic_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/110000/B36E094F-E5BC-2B49-90C0-A7399D342D3C.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTGamma_Hadronic_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/110000/B6BD167C-E0F2-3849-ADFB-A7BB4C826818.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTGamma_Hadronic_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/110000/BAE8AFDE-2754-5043-8B57-01B8FC066C76.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTGamma_Hadronic_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/110000/BE32F60D-E227-914B-92CC-D741F141F31C.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTGamma_Hadronic_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/110000/BEE79E65-837D-3846-B09A-577F4927DBCC.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTGamma_Hadronic_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/110000/C65DCC74-ACFC-3C41-84EF-202ADE835053.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTGamma_Hadronic_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/110000/C679EB8A-5BB0-DB4B-8D04-7938D3EB42BE.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTGamma_Hadronic_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/110000/C8FC447B-CCD0-A54A-A968-CCD020F8EABA.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTGamma_Hadronic_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/110000/CC846AF3-2DBD-8348-A7D6-2D4F104F8FA9.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTGamma_Hadronic_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/110000/D0849F8B-1198-B24A-A252-DE77E41AF5BE.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTGamma_Hadronic_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/110000/D456343D-5EF4-F846-AAE1-B484B1D798F8.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTGamma_Hadronic_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/110000/D74CDAB9-A786-8643-B2E6-684E69F6CE4B.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTGamma_Hadronic_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/110000/D7CBBEFA-57D3-204A-A96B-8F694F1E9EC5.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTGamma_Hadronic_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/110000/DB87592B-0CE2-2045-BE19-F9295AD02956.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTGamma_Hadronic_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/110000/E31BB1A7-6187-404F-8AB5-44ACF715B80A.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTGamma_Hadronic_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/110000/F0F08AE7-4628-C24F-8F0C-6AF8BC3B5894.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTGamma_Hadronic_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/110000/F11F3F73-84F6-6B41-B14D-B2DFB63461A6.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTGamma_Hadronic_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/110000/F3C1D6AC-DAFE-154C-A783-8B8DAD90C9A0.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTGamma_Hadronic_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/110000/F6164749-3DE4-8143-AE68-234DA99721B4.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTGamma_Hadronic_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/110000/FB1A9C3E-5CB3-544F-AF4E-33E5FAC769B3.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTGamma_Hadronic_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/280000/012AAF5C-D73A-7D4E-AFE0-FECEC3032B86.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTGamma_Hadronic_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/280000/01F8EB77-C519-774D-A819-81A57B2BA27C.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTGamma_Hadronic_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/280000/04ECBB2F-8C93-D343-89B4-08F089060175.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTGamma_Hadronic_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/280000/0BC258B0-90F0-1749-A891-41F6BC69ED14.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTGamma_Hadronic_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/280000/120A7355-C4AE-AA47-B7B4-0006113E6D8A.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTGamma_Hadronic_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/280000/140E1B9A-CEE1-D143-8F7D-2697CF36044E.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTGamma_Hadronic_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/280000/1B904CDE-4DE3-9B4C-BABF-675382C3C68D.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTGamma_Hadronic_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/280000/1DE0568D-8D9A-FE41-8AE1-D5E5B8AD6737.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTGamma_Hadronic_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/280000/22CC0B9D-6CAB-1A4D-83F1-EC82C4AC8897.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTGamma_Hadronic_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/280000/23D82CE7-0085-F541-A3B9-94A4F8DF90F5.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTGamma_Hadronic_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/280000/283F7AF7-FC79-6F4C-BDDB-5B703EC3C4B7.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTGamma_Hadronic_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/280000/2B997772-CE53-234B-8C51-0563C5AD4056.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTGamma_Hadronic_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/280000/34ACD131-5096-3F48-9691-0C8B9F10202E.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTGamma_Hadronic_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/280000/3640F0B4-2CC2-FF42-8545-32F33BB2B323.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTGamma_Hadronic_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/280000/366FF48C-29EB-6044-B71F-942A2E033CF1.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTGamma_Hadronic_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/280000/3C07E05A-9FEA-824C-BC41-33197DFF3228.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTGamma_Hadronic_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/280000/41586E8F-F896-9C49-AE70-112185297738.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTGamma_Hadronic_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/280000/44B99F52-5B9C-B943-80A3-00671A514454.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTGamma_Hadronic_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/280000/44F35B69-207D-B747-A601-44FBAC42A3C7.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTGamma_Hadronic_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/280000/450E53D0-8455-5844-9E78-EA20FE48E554.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTGamma_Hadronic_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/280000/47D53889-594F-5848-9DF8-83BE3028F37F.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTGamma_Hadronic_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/280000/4A577AC3-B386-894E-B196-A72563F5230E.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTGamma_Hadronic_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/280000/4C89EC43-F880-EE4E-8DE0-FFDA8E00A897.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTGamma_Hadronic_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/280000/4EF22C40-0884-BB43-8F65-3DF164254F61.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTGamma_Hadronic_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/280000/4EF7DC3E-92FB-704E-BF41-8BC4CEBFECAF.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTGamma_Hadronic_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/280000/52F84946-C2C1-CA41-9C78-F617AE4AE289.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTGamma_Hadronic_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/280000/5E4B914F-433B-3C47-B102-5B1FB834D547.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTGamma_Hadronic_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/280000/5FE0CC05-6D77-484B-BF77-C8AB385BB778.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTGamma_Hadronic_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/280000/60AE4E88-058B-5D43-9980-F013CE767132.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTGamma_Hadronic_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/280000/60C2D5EC-C575-034D-B352-BFEDABDA2291.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTGamma_Hadronic_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/280000/6105A4F1-FB37-2541-9439-2DD64FC13176.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTGamma_Hadronic_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/280000/61E90B5B-6D4C-5C47-8D0B-CF59FE7C4534.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTGamma_Hadronic_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/280000/680803EA-B96B-AA41-9E1B-243CC3220521.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTGamma_Hadronic_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/280000/6BB8BCBC-DBE6-8C4C-A55E-C5B7655A1F4C.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTGamma_Hadronic_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/280000/6ED672C8-C39D-F24F-9CA1-1BEE4E184C3F.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTGamma_Hadronic_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/280000/75427FC2-FBE3-3346-9DA5-FCDBE30AD87E.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTGamma_Hadronic_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/280000/783CFFF7-2384-0940-BA98-7378457FF48C.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTGamma_Hadronic_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/280000/7E1A5818-A5BB-5643-B493-9A17F390875F.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTGamma_Hadronic_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/280000/8083FB09-D662-B447-9B15-1A0AD1F3153C.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTGamma_Hadronic_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/280000/8EF9EB16-B92F-1848-8637-AC18B5CE6C7A.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTGamma_Hadronic_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/280000/902090CF-18F0-2145-9AE9-139C05D37301.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTGamma_Hadronic_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/280000/96A9D876-8A14-3F4F-A73D-CF462B5A22AD.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTGamma_Hadronic_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/280000/99C6DB24-E407-6744-B094-D1198F7F7A5D.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTGamma_Hadronic_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/280000/9AFD7F23-D8C9-6746-9F4D-FEB1333AEFF1.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTGamma_Hadronic_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/280000/A1EA2ED8-1F27-3942-AE77-044CA93E658A.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTGamma_Hadronic_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/280000/A5592298-5523-3840-865D-B386D9E85B65.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTGamma_Hadronic_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/280000/A7FD9D54-4523-5844-9114-465816C502D9.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTGamma_Hadronic_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/280000/AB32BC15-A309-DC48-BA8E-836539AE0B16.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTGamma_Hadronic_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/280000/AD3DEEF5-9F49-8F47-A964-46C6BA77C837.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTGamma_Hadronic_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/280000/B1956F23-7669-1243-83A0-1CAAED775A9D.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTGamma_Hadronic_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/280000/B5B427BA-209E-084E-A0DC-16C3A658A4F2.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTGamma_Hadronic_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/280000/BABE1B84-27F1-164F-9423-445F44102585.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTGamma_Hadronic_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/280000/BC9CAB11-C099-1E43-9D31-98A27678F88A.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTGamma_Hadronic_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/280000/BDEED28C-C363-DF4D-BDEB-DF6544DD26A0.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTGamma_Hadronic_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/280000/BE9E04D4-83AA-D04D-A1D8-44304B11E90B.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTGamma_Hadronic_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/280000/CA82C11C-FC19-3742-81AF-F2D5C0159C16.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTGamma_Hadronic_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/280000/CD808814-427D-784F-B06E-15576B7CCBB3.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTGamma_Hadronic_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/280000/D06DBF29-4C25-FB44-A827-FCFFBF0E48C6.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTGamma_Hadronic_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/280000/D64487E3-850C-D943-BAEA-7E3A0695667F.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTGamma_Hadronic_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/280000/DE9DD344-8AA5-9E47-A886-0CBAC8B3D3EC.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTGamma_Hadronic_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/280000/E1E17DAF-77B3-DC43-8180-CD8C224E3669.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTGamma_Hadronic_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/280000/E364F103-BE33-7440-8EA4-A51020C7659B.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTGamma_Hadronic_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/280000/E4B13EAE-0E09-FD41-930D-787F12790E60.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTGamma_Hadronic_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/280000/E8598D8D-9277-8348-A2FD-AB682D671456.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTGamma_Hadronic_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/280000/E94B3B47-0BEF-1244-A5C6-6FADED753D85.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTGamma_Hadronic_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/280000/F0D9C90E-F7AC-3240-94A4-D1D550216943.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTGamma_Hadronic_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/280000/F3850E54-14AF-5C4D-ADC1-56D222AA80D1.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTGamma_Hadronic_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/280000/FAD5C67E-9199-2A47-9E50-D34E80C69433.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTGamma_Hadronic_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/280000/FB33EB7E-F0D5-EE43-9A28-F23A4AA2232A.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTGamma_Hadronic_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/280000/FBEF0643-FA8E-5E48-BDB5-F011D034421D.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTGamma_Hadronic_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/280000/FFBB453A-BE2E-DA41-80E0-C985C829A83A.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTGamma_Hadronic_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/280000/FFFDEC25-AAFF-5D41-AA99-669E82E51336.root',
] )
