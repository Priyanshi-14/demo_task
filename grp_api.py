from whatsapp_api_client_python import API
import pandas as pd

greenAPI = API.GreenApi(
    "7103835913", "e998663c7ab94d74a4c09a9eacdfb796a5735f0e27b84972a6"
)

def main():
    members = []
    data = pd.read_csv("./test.csv")
    print(len(data))
    for i in range(len(data)):
        print(i)
        members.append("91"+f"{data['Number'][i]}"+"@c.us")
    
    create_group_response = greenAPI.groups.createGroup(
        "TRH spartans", members
    )  
    
    if create_group_response.code == 200:
        print(create_group_response.data)
        send_message_response = greenAPI.sending.sendMessage(
            create_group_response.data["chatId"], "Hey TRH Members"
        )
        if send_message_response.code == 200:
            print(send_message_response.data)
        else:
            print(send_message_response.error)
    else:
        print(create_group_response.error)



if __name__ == '__main__':
    main()
    