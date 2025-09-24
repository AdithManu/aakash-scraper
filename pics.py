import requests

ppl = [
  {
    "id": "9ad0e203-8107-40c4-bd58-844d9946ad3d",
    "displayName": "Aarna hadimfni(00008021985)",
    "userPrincipalName": "00008021985@aakashicampus.com",
    "userType": "Member"
  },
  {
    "id": "e0b06e95-51d5-4ff0-8855-c01ea08cc443",
    "displayName": "Aarna Vishal Thakur(00014585124)",
    "userPrincipalName": "00014585124@aakashicampus.com",
    "userType": "Member"
  },
  {
    "id": "d15d0a99-9569-4c6b-97e8-10f4bec72bdc",
    "displayName": "Aditya Tippannavar(00014601360)",
    "userPrincipalName": "00014601360@aakashicampus.com",
    "userType": "Member"
  },
  {
    "id": "995b12c7-120f-455b-a83b-7c453c6a20a0",
    "displayName": "Anwesha B (00013993542)",
    "userPrincipalName": "00013993542@aakashicampus.com",
    "userType": "Member"
  },
  {
    "id": "6b6d56ee-a32e-42af-bca7-3f466227bcc3",
    "displayName": "Arayna Shrivastav(00015167533)",
    "userPrincipalName": "00015167533@aakashicampus.com",
    "userType": "Member"
  },
  {
    "id": "02369557-29f7-4434-b0cd-080ab8489341",
    "displayName": "Bhargav Bharadwaj(00013566784)",
    "userPrincipalName": "00013566784@aakashicampus.com",
    "userType": "Member"
  },
  {
    "id": "011c0526-3547-4117-802d-467ec31caebe",
    "displayName": "CTushara Bindu(00014980856)",
    "userPrincipalName": "00014980856@aakashicampus.com",
    "userType": "Member"
  },
  
  {
    "id": "8c40055c-29c6-4daf-9a55-5bddfe8cc415",
    "displayName": "Insha Jawad Siddiqui (00014409049)",
    "userPrincipalName": "00014409049@aakashicampus.com",
    "userType": "Member"
  },
  {
    "id": "1805fe9b-d431-4de2-849e-af1f1af4e1a4",
    "displayName": "Kiran M(00008877376)",
    "userPrincipalName": "00008877376@aakashicampus.com",
    "userType": "Member"
  },
  {
    "id": "38c1bf80-b8c9-484d-8dcb-36f80a0c840a",
    "displayName": "Pragya Sharma(00015303685)",
    "userPrincipalName": "00015303685@aakashicampus.com",
    "userType": "Member"
  },
  {
    "id": "66e2c287-3ec3-423d-9692-bcd77ab44aa5",
    "displayName": "Pranjali Bharadwaj (00014712825)",
    "userPrincipalName": "00014712825@aakashicampus.com",
    "userType": "Member"
  },
  {
    "id": "dfae04e7-4093-4952-81b0-b8e226eab478",
    "displayName": "Prerana Rendale(00015482456)",
    "userPrincipalName": "00015482456@aakashicampus.com",
    "userType": "Member"
  },
  {
    "id": "f68f1f1f-1870-43c9-94bd-962f18afe807",
    "displayName": "Rishita Nandimandalam(00014319689)",
    "userPrincipalName": "00014319689@aakashicampus.com",
    "userType": "Member"
  },
  {
    "id": "4b98dff8-15c3-47fb-b6ab-db686121a117",
    "displayName": "Saranya Shukla (00014439652)",
    "userPrincipalName": "00014439652@aakashicampus.com",
    "userType": "Member"
  },
  {
    "id": "0b9db2b7-2db7-4475-a122-56e39fc594e4",
    "displayName": "Shaik Aafreen(00008186844)",
    "userPrincipalName": "00008186844@aakashicampus.com",
    "userType": "Member"
  },
  {
    "id": "9ab4f5b5-be3b-40f2-8956-b3078f2327b0",
    "displayName": "Shivaani Patil(00015652046)",
    "userPrincipalName": "00015652046@aakashicampus.com",
    "userType": "Member"
  },
  {
    "id": "e1b88113-c9e4-42c7-a6fb-7b8410978822",
    "displayName": "Smayan Chatterjee(00015346110)",
    "userPrincipalName": "00015346110@aakashicampus.com",
    "userType": "Member"
  },
  {
    "id": "2d3c84b5-0dcb-4b5a-9f10-b65be2907527",
    "displayName": "Syed Yusuf Rahman(00014633980)",
    "userPrincipalName": "00014633980@aakashicampus.com",
    "userType": "Member"
  },
  {
    "id": "a075e8e4-1c4c-4773-a84f-9d208ddd7d63",
    "displayName": "Syeda Afrin Dawood (00013702489)",
    "userPrincipalName": "00013702489@aakashicampus.com",
    "userType": "Member"
  },
  {
    "id": "86ca8580-818b-448e-a87e-b141f7be4985",
    "displayName": "Vikrant Patil(00014502711)",
    "userPrincipalName": "00014502711@aakashicampus.com",
    "userType": "Member"
  },
  {
    "id": "f8866d7f-6c35-4c4a-977a-e73fe7de96ec",
    "displayName": "Vrishti Shetty( 00010261626 )",
    "userPrincipalName": "00010261626@aakashicampus.com",
    "userType": "Member"
  }
,

  {
    "id": "e0b06e95-51d5-4ff0-8855-c01ea08cc443",
    "displayName": "Aarna Vishal Thakur(00014585124)",
    "userPrincipalName": "00014585124@aakashicampus.com",
    "userType": "Member"
  },
  {
    "id": "d15d0a99-9569-4c6b-97e8-10f4bec72bdc",
    "displayName": "Aditya Tippannavar(00014601360)",
    "userPrincipalName": "00014601360@aakashicampus.com",
    "userType": "Member"
  },
  {
    "id": "2ce65b57-db8f-4799-91e2-c4cad2612a51",
    "displayName": "Adweta Sahu(00014570652)",
    "userPrincipalName": "00014570652@aakashicampus.com",
    "userType": "Member"
  },
  {
    "id": "fe48690c-d490-4278-8ef9-6fe743956bc1",
    "displayName": "ANUSHKA TIWARY(00014542793)",
    "userPrincipalName": "00014542793@aakashicampus.com",
    "userType": "Member"
  },
  {
    "id": "7e7e4ee8-6783-44d8-844e-dc869684cb57",
    "displayName": "Avaneesh Prasanna(00013948052)",
    "userPrincipalName": "00013948052@aakashicampus.com",
    "userType": "Member"
  },
  
  {
    "id": "8c40055c-29c6-4daf-9a55-5bddfe8cc415",
    "displayName": "Insha Jawad Siddiqui (00014409049)",
    "userPrincipalName": "00014409049@aakashicampus.com",
    "userType": "Member"
  },
  {
    "id": "6e00ab46-bfd4-4eaf-b63c-898de374ec22",
    "displayName": "Kairaav Kingshuk(00011093100)",
    "userPrincipalName": "00011093100@aakashicampus.com",
    "userType": "Member"
  },
  {
    "id": "1805fe9b-d431-4de2-849e-af1f1af4e1a4",
    "displayName": "Kiran M(00008877376)",
    "userPrincipalName": "00008877376@aakashicampus.com",
    "userType": "Member"
  },
  {
    "id": "9de02bfe-2d00-4e9a-a75d-900c0aadab9d",
    "displayName": "Maalavika L(00008573884)",
    "userPrincipalName": "00008573884@aakashicampus.com",
    "userType": "Member"
  },
  {
    "id": "d2201bed-9f26-465b-b41c-2d8936346fcd",
    "displayName": "Narain Adithya S(00010792070)",
    "userPrincipalName": "00010792070@aakashicampus.com",
    "userType": "Member"
  },
  {
    "id": "5a2dbc80-9c50-42da-bef2-bb56d09b6823",
    "displayName": "NIDHEESH LAMBA.( 00010286269 )",
    "userPrincipalName": "00010286269@aakashicampus.com",
    "userType": "Member"
  },
  {
    "id": "06480322-cd75-4e06-bff2-813c17db0eff",
    "displayName": "Parinishtha Mukherjee(00014826992)",
    "userPrincipalName": "00014826992@aakashicampus.com",
    "userType": "Member"
  },
  {
    "id": "38c1bf80-b8c9-484d-8dcb-36f80a0c840a",
    "displayName": "Pragya Sharma(00015303685)",
    "userPrincipalName": "00015303685@aakashicampus.com",
    "userType": "Member"
  },
  {
    "id": "e48eac5b-e726-47b8-b730-a2c0630dad00",
    "displayName": "Pranav Vinnakota(00015581080)",
    "userPrincipalName": "00015581080@aakashicampus.com",
    "userType": "Member"
  },
  {
    "id": "d5b88a75-adef-45db-ab59-787818944ecb",
    "displayName": "Purvi Ambastha(00008450886)",
    "userPrincipalName": "00008450886@aakashicampus.com",
    "userType": "Member"
  },
  {
    "id": "bdda398c-b46b-4414-89a5-20b313fe3ef9",
    "displayName": "Rakshith D N(00014165628)",
    "userPrincipalName": "00014165628@aakashicampus.com",
    "userType": "Member"
  },
  {
    "id": "f68f1f1f-1870-43c9-94bd-962f18afe807",
    "displayName": "Rishita Nandimandalam(00014319689)",
    "userPrincipalName": "00014319689@aakashicampus.com",
    "userType": "Member"
  },
  {
    "id": "490f168a-c393-47ba-964a-12c3191d38de",
    "displayName": "S Dayanitha(00011222108)",
    "userPrincipalName": "00011222108@aakashicampus.com",
    "userType": "Member"
  },
  {
    "id": "155f205f-d507-45e6-93ec-2341e0628f52",
    "displayName": "Sagar N(00005574512)",
    "userPrincipalName": "00005574512@aakashicampus.com",
    "userType": "Member"
  },
  {
    "id": "23ed8dce-bc5b-49be-b511-e88c9cc0b3bc",
    "displayName": "Saksham Julka( 00010541759 )",
    "userPrincipalName": "00010541759@aakashicampus.com",
    "userType": "Member"
  },
  {
    "id": "2d3c84b5-0dcb-4b5a-9f10-b65be2907527",
    "displayName": "Syed Yusuf Rahman(00014633980)",
    "userPrincipalName": "00014633980@aakashicampus.com",
    "userType": "Member"
  },
  {
    "id": "9e86df5f-056d-4fb4-ac5e-b1dafc8165b4",
    "displayName": "Thanika Bajeesh(00008339378)",
    "userPrincipalName": "00008339378@aakashicampus.com",
    "userType": "Member"
  },
  {
    "id": "d3a512ed-0112-4c1c-94f7-07ed4d9e54a7",
    "displayName": "toshan patra(00006333700)",
    "userPrincipalName": "00006333700@aakashicampus.com",
    "userType": "Member"
  },
  {
    "id": "07f3c175-0170-4ccf-974d-d70a5f502084",
    "displayName": "Utkarsh M Gowda(00015072798)",
    "userPrincipalName": "00015072798@aakashicampus.com",
    "userType": "Member"
  }
]


ids=[
    '00014310123',
'00014210433',
'00014256750',
'00015822965',
'00014562180',
'00014386009',
'00014591065',
'00013831631',
'00015032080',
'00014514970',
'00014172841',
'00014633980',
'00014506392',
'00014848349',
'00014419825',
'00014599152',
'00005536943',
'00014210511',
'00015115408',
'00005574512',
'00014209388',
'00014391410',
'00014319689',
'00014168959',
'00015173040',
'00014165628',
'00011912387',
'00008450886',
'00015364506',
'00014954476',
'00014331642',
'00014837702',
'00014414804',
'00014876505',
'00014826992',
'00013579998',
'00014454155',
'00014331535',
'00014472520',
'00014401114',
'00015752407',
'00013586858',
'00013523834',
'00013420820',
'00014458311',
'00013601386',
'00013641637',
'00014598715',
'00014125308',
'00014893640',
'00013777386',
'00014210378',
'00014350791',
'00013948052',
'00015087816',
'00015167533',
'00014917096',
'00014542793',
'00014110606',
'00012475510',
'00008535174',
'00014519488',
'00013908497',
'00014570652',
'00014601360',
'00014504187',
'00014436815',
'00014224638',
'00013778656',
'00011974852',
'00014585124',
'00008021985',
'00008910299',
'00014325409',
'00012803494',
'00014134464',
'00014627149',
'00013807697',
'00014572299',
'00015056429',
'00014759441',
'00015149350',
'00015054574',
'00014724770',
'00015088893',
'00015143923',
'00015006213',
'00008186844',
'00015102547',
'00014986721',
'00015032879',
'00015167899',
'00014980856',
'00014331646',
'00015082454',
'00015199313',
'00011589489',
'00015267982',
'00015072798',
'00015208738',
'00015269332',
'00015277391',
'00014757107',
'00015303685',
'00014836520',
'00015337499',
'00015320905',
'00005574507',
'00015247873',
'00014331620',
'00015368788',
'00015404314',
'00015397257',
'00015396907',
'00001018217',
'00015440493',
'00015201252',
'00015109452',
'00008942672',
'00015300676',
'00008363226',
'00015381624',
'00014502711',
'00015349920',
'00015484070',
'00015346110',
'00015351852',
'00015436104',
'00015476478',
'00015497521',
'00015482456',
'00014835608',
'00015412777',
'00015088823',
'00015497000',
'00015505112',
'00015524483',
'00015536508',
'00015429059',
'00015508849',
'00015557779',
'00015523502',
'00015562817',
'00015472227',
'00015530590',
'00015602089',
'00015468093',
'00015581228',
'00015615820',
'00012639536',
'00009374189',
'00015608288',
'00015676101',
'00015688310',
'00015652046',
'00015671408',
'00015562489',
'00015684695',
'00015581080',
'00015726198',
'00015685477',
'00015833600',
'00015772109',
'00015735659',
'00015782539',
]

# for person in ppl:
#     psid = person["userPrincipalName"].split("@")[0]
for psid in ids:
    r = requests.get(f"http://aakashleap.com:3131/Content/ScoreToolImage/Output{psid}.jpg")
    if r.status_code == 200:
        with open(f"pics-weekend-2/Output-{psid}.jpg", "wb") as f:
            f.write(r.content)

# import os
# for i in os.listdir("pictures"):
#     f = open(f"pictures/{i}", "rb")
#     print(len(f.read()))
#     if len(f.read()) == 0:
#         print(i)
#     f.close()
