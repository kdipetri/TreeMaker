import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/data/Run2016B/SinglePhoton/MINIAOD/17Jul2018_ver1-v1/20000/1C269C00-559B-E811-9CE9-002590FCF738.root',
       '/store/data/Run2016B/SinglePhoton/MINIAOD/17Jul2018_ver1-v1/20000/48C9F10D-559B-E811-BAD6-002590FD5E82.root',
       '/store/data/Run2016B/SinglePhoton/MINIAOD/17Jul2018_ver1-v1/20000/622DF009-559B-E811-A843-AC1F6B8DD22E.root',
       '/store/data/Run2016B/SinglePhoton/MINIAOD/17Jul2018_ver1-v1/20000/66EDFAE0-549B-E811-ACDD-68B59972C052.root',
       '/store/data/Run2016B/SinglePhoton/MINIAOD/17Jul2018_ver1-v1/20000/6C0A34DF-549B-E811-9D43-1CB72C1B64E6.root',
       '/store/data/Run2016B/SinglePhoton/MINIAOD/17Jul2018_ver1-v1/20000/7AC625D3-549B-E811-BE1D-0425C5903030.root',
       '/store/data/Run2016B/SinglePhoton/MINIAOD/17Jul2018_ver1-v1/20000/7AD45288-5A9B-E811-82C1-C0BFC0E5682E.root',
       '/store/data/Run2016B/SinglePhoton/MINIAOD/17Jul2018_ver1-v1/20000/7E0B5D02-559B-E811-A8AB-34E6D7E38781.root',
       '/store/data/Run2016B/SinglePhoton/MINIAOD/17Jul2018_ver1-v1/20000/D6888DC5-549B-E811-B9CA-34E6D7E3878E.root',
       '/store/data/Run2016B/SinglePhoton/MINIAOD/17Jul2018_ver1-v1/20000/DCAA92D4-549B-E811-8A95-C0BFC0E5681E.root',
       '/store/data/Run2016B/SinglePhoton/MINIAOD/17Jul2018_ver1-v1/20000/F40DDECC-549B-E811-9057-0425C5902FB0.root',
       '/store/data/Run2016B/SinglePhoton/MINIAOD/17Jul2018_ver1-v1/40000/0033B2FE-E299-E811-B171-68B59972BF62.root',
       '/store/data/Run2016B/SinglePhoton/MINIAOD/17Jul2018_ver1-v1/40000/066D4558-D098-E811-972E-90E2BACBAD64.root',
       '/store/data/Run2016B/SinglePhoton/MINIAOD/17Jul2018_ver1-v1/40000/0C1EA708-DE99-E811-BDC8-68B59972BF62.root',
       '/store/data/Run2016B/SinglePhoton/MINIAOD/17Jul2018_ver1-v1/40000/26CF2D0C-DE99-E811-ADDD-002590FD583A.root',
       '/store/data/Run2016B/SinglePhoton/MINIAOD/17Jul2018_ver1-v1/40000/2A7AC0FC-CF98-E811-ACB8-C0BFC0E56826.root',
       '/store/data/Run2016B/SinglePhoton/MINIAOD/17Jul2018_ver1-v1/40000/2AC7F863-3998-E811-B152-1CB72C0A3DC1.root',
       '/store/data/Run2016B/SinglePhoton/MINIAOD/17Jul2018_ver1-v1/40000/2C7A1B78-E299-E811-B6B9-34E6D7E3879B.root',
       '/store/data/Run2016B/SinglePhoton/MINIAOD/17Jul2018_ver1-v1/40000/34720272-E399-E811-B65D-1CB72C1B63C2.root',
       '/store/data/Run2016B/SinglePhoton/MINIAOD/17Jul2018_ver1-v1/40000/34FFF4D4-CF98-E811-BD20-1CB72C1B64E6.root',
       '/store/data/Run2016B/SinglePhoton/MINIAOD/17Jul2018_ver1-v1/40000/3AD4D2F8-DD99-E811-AEEA-1CB72C1B63C2.root',
       '/store/data/Run2016B/SinglePhoton/MINIAOD/17Jul2018_ver1-v1/40000/40052312-DE99-E811-AF4F-1CB72C0A3D89.root',
       '/store/data/Run2016B/SinglePhoton/MINIAOD/17Jul2018_ver1-v1/40000/46AE45F5-CF98-E811-A4B1-1CB72C0A3DC5.root',
       '/store/data/Run2016B/SinglePhoton/MINIAOD/17Jul2018_ver1-v1/40000/5A3FD5AD-CE98-E811-9A41-90E2BACBAE58.root',
       '/store/data/Run2016B/SinglePhoton/MINIAOD/17Jul2018_ver1-v1/40000/5E70947E-E099-E811-8D99-34E6D7BEAF0E.root',
       '/store/data/Run2016B/SinglePhoton/MINIAOD/17Jul2018_ver1-v1/40000/60E502C7-E999-E811-AB1F-1CB72C0A3D89.root',
       '/store/data/Run2016B/SinglePhoton/MINIAOD/17Jul2018_ver1-v1/40000/62201994-2A98-E811-9753-34E6D7BEAF01.root',
       '/store/data/Run2016B/SinglePhoton/MINIAOD/17Jul2018_ver1-v1/40000/744996A6-CB95-E811-93C2-90E2BACBB038.root',
       '/store/data/Run2016B/SinglePhoton/MINIAOD/17Jul2018_ver1-v1/40000/7E9D636F-3998-E811-B5DE-0425C5DE7BF2.root',
       '/store/data/Run2016B/SinglePhoton/MINIAOD/17Jul2018_ver1-v1/40000/860BC92B-CE98-E811-801A-68CC6EA5BE6A.root',
       '/store/data/Run2016B/SinglePhoton/MINIAOD/17Jul2018_ver1-v1/40000/9060DDFB-1D97-E811-9B4D-002590FD5E3E.root',
       '/store/data/Run2016B/SinglePhoton/MINIAOD/17Jul2018_ver1-v1/40000/965F530E-DE99-E811-AAB3-002590FD5E88.root',
       '/store/data/Run2016B/SinglePhoton/MINIAOD/17Jul2018_ver1-v1/40000/96E503BA-CF98-E811-B5EC-90E2BAD1C730.root',
       '/store/data/Run2016B/SinglePhoton/MINIAOD/17Jul2018_ver1-v1/40000/9ABC4EC7-CE98-E811-8A39-34E6D7BDDEE8.root',
       '/store/data/Run2016B/SinglePhoton/MINIAOD/17Jul2018_ver1-v1/40000/9CD776F4-A595-E811-9094-1CB72C0A3DC5.root',
       '/store/data/Run2016B/SinglePhoton/MINIAOD/17Jul2018_ver1-v1/40000/A4C8D47C-7A96-E811-91C0-1CB72C0A3DC5.root',
       '/store/data/Run2016B/SinglePhoton/MINIAOD/17Jul2018_ver1-v1/40000/A6F69115-CF98-E811-A94C-AC1F6B8DBEC2.root',
       '/store/data/Run2016B/SinglePhoton/MINIAOD/17Jul2018_ver1-v1/40000/A8F52DFA-DD99-E811-BC53-C0BFC0E5681E.root',
       '/store/data/Run2016B/SinglePhoton/MINIAOD/17Jul2018_ver1-v1/40000/B26C4C30-CE97-E811-8FEF-90E2BAD1C9A8.root',
       '/store/data/Run2016B/SinglePhoton/MINIAOD/17Jul2018_ver1-v1/40000/BE0FC96F-E399-E811-9247-1CB72C0A3D89.root',
       '/store/data/Run2016B/SinglePhoton/MINIAOD/17Jul2018_ver1-v1/40000/C49B937C-DE99-E811-9E94-34E6D7BEAF28.root',
       '/store/data/Run2016B/SinglePhoton/MINIAOD/17Jul2018_ver1-v1/40000/CE519BA4-E999-E811-B0E2-C0BFC0E5686E.root',
       '/store/data/Run2016B/SinglePhoton/MINIAOD/17Jul2018_ver1-v1/40000/D40FBBA7-D297-E811-B4C0-1CB72C0A3DC1.root',
       '/store/data/Run2016B/SinglePhoton/MINIAOD/17Jul2018_ver1-v1/40000/D4B67C72-E399-E811-B76A-34E6D7BEAF28.root',
       '/store/data/Run2016B/SinglePhoton/MINIAOD/17Jul2018_ver1-v1/40000/D6E2E245-EA99-E811-BB88-1CB72C1B63C2.root',
       '/store/data/Run2016B/SinglePhoton/MINIAOD/17Jul2018_ver1-v1/40000/D8CFE1DC-8D99-E811-A5A8-C0BFC0E5682E.root',
       '/store/data/Run2016B/SinglePhoton/MINIAOD/17Jul2018_ver1-v1/40000/E2290A75-CE98-E811-8A3D-34E6D7BDDECE.root',
       '/store/data/Run2016B/SinglePhoton/MINIAOD/17Jul2018_ver1-v1/40000/E2DC7DE0-E599-E811-BB6C-34E6D7BDDEE8.root',
       '/store/data/Run2016B/SinglePhoton/MINIAOD/17Jul2018_ver1-v1/40000/E6020931-CE97-E811-8E26-C0BFC0E56866.root',
       '/store/data/Run2016B/SinglePhoton/MINIAOD/17Jul2018_ver1-v1/40000/FAF00CA1-CF98-E811-BB97-90E2BAD1C9A8.root',
       '/store/data/Run2016B/SinglePhoton/MINIAOD/17Jul2018_ver1-v1/40000/FC8CBA65-CE98-E811-B237-C0BFC0E56816.root',
       '/store/data/Run2016B/SinglePhoton/MINIAOD/17Jul2018_ver1-v1/40000/FE936E72-E599-E811-8ADE-002590FD583A.root',
       '/store/data/Run2016B/SinglePhoton/MINIAOD/17Jul2018_ver1-v1/90000/04C0E8A3-B096-E811-83D5-0425C5903034.root',
       '/store/data/Run2016B/SinglePhoton/MINIAOD/17Jul2018_ver1-v1/90000/06A58932-C796-E811-A7E0-90E2BAD57CD0.root',
       '/store/data/Run2016B/SinglePhoton/MINIAOD/17Jul2018_ver1-v1/90000/14BAD896-019A-E811-B1C3-002590FD583A.root',
       '/store/data/Run2016B/SinglePhoton/MINIAOD/17Jul2018_ver1-v1/90000/241CD7C4-8996-E811-9B10-0425C5DE7BEC.root',
       '/store/data/Run2016B/SinglePhoton/MINIAOD/17Jul2018_ver1-v1/90000/3479A0E7-8E97-E811-B8E2-34E6D7E3879B.root',
       '/store/data/Run2016B/SinglePhoton/MINIAOD/17Jul2018_ver1-v1/90000/36C08490-019A-E811-AE33-0425C5DE7BF0.root',
       '/store/data/Run2016B/SinglePhoton/MINIAOD/17Jul2018_ver1-v1/90000/3E35A7EA-9296-E811-B45A-68CC6EA5BD22.root',
       '/store/data/Run2016B/SinglePhoton/MINIAOD/17Jul2018_ver1-v1/90000/4ACAD693-019A-E811-BC2D-0425C5923ACA.root',
       '/store/data/Run2016B/SinglePhoton/MINIAOD/17Jul2018_ver1-v1/90000/5048C432-6396-E811-875A-1CB72C1B64E6.root',
       '/store/data/Run2016B/SinglePhoton/MINIAOD/17Jul2018_ver1-v1/90000/56FAF42A-B996-E811-B4D4-68B59972BF62.root',
       '/store/data/Run2016B/SinglePhoton/MINIAOD/17Jul2018_ver1-v1/90000/5E47CEFA-B096-E811-A496-1CB72C0A3DC5.root',
       '/store/data/Run2016B/SinglePhoton/MINIAOD/17Jul2018_ver1-v1/90000/70546C22-9096-E811-A02F-002590FD5E82.root',
       '/store/data/Run2016B/SinglePhoton/MINIAOD/17Jul2018_ver1-v1/90000/7C9FA809-6B96-E811-9FC5-0425C5902FB0.root',
       '/store/data/Run2016B/SinglePhoton/MINIAOD/17Jul2018_ver1-v1/90000/98877792-019A-E811-9B23-AC1F6B8DBE36.root',
       '/store/data/Run2016B/SinglePhoton/MINIAOD/17Jul2018_ver1-v1/90000/AC39FA8F-7396-E811-8944-AC1F6B8DBE02.root',
       '/store/data/Run2016B/SinglePhoton/MINIAOD/17Jul2018_ver1-v1/90000/ACACCE8E-019A-E811-8D7F-90E2BAD1BDF0.root',
       '/store/data/Run2016B/SinglePhoton/MINIAOD/17Jul2018_ver1-v1/90000/B0BF6ECB-9896-E811-889D-002590FD5E80.root',
       '/store/data/Run2016B/SinglePhoton/MINIAOD/17Jul2018_ver1-v1/90000/B2B936D0-6196-E811-8B8F-C0BFC0E5684E.root',
       '/store/data/Run2016B/SinglePhoton/MINIAOD/17Jul2018_ver1-v1/90000/E00CF6F0-6798-E811-8A96-0425C5902FCA.root',
       '/store/data/Run2016B/SinglePhoton/MINIAOD/17Jul2018_ver1-v1/90000/E0E8CE91-019A-E811-B832-0425C5DE7BEE.root',
       '/store/data/Run2016B/SinglePhoton/MINIAOD/17Jul2018_ver1-v1/90000/E6390393-019A-E811-8C12-0425C5DE7BE8.root',
       '/store/data/Run2016B/SinglePhoton/MINIAOD/17Jul2018_ver1-v1/90000/EA8C4214-AC96-E811-AF1F-002590FD030A.root',
       '/store/data/Run2016B/SinglePhoton/MINIAOD/17Jul2018_ver1-v1/90000/FE24CDD4-7896-E811-9FA4-1CB72C1B64E6.root',
] )