from platform import platform
from google_bot import FilesHandler, MLA
from google_bot.login import login
from google_bot import review
import os
from google_bot.HumanBehaviour import warmup
# from google_bot.configParsing import get_filename

cls = lambda: os.system('cls')
def menu():
    platform = None
    while platform not in ["1", "2"]:
        platform = input("Select Platform:\n1) Desktop\n2) Mobile\nPlatform: ")
        cls()
    platform = 'd' if platform == '1' else 'm' 

    choice = None
    while choice not in ["1", "2"]:
        choice = input("1) Create Accound and Login\n2) Warmup and Review\nChoice: ")
        cls()
    # n = int(input("Enter Number of Profiles/Reviews: "))
    return platform, choice, #n

def main():
    platform, choice = menu()
    mla_profiles_file = "Files/profiles_mobile.csv" if platform == 'm' else "Files/profiles_desktop.csv"
    mla_profiles = FilesHandler.read_csv(mla_profiles_file)
    mla_profiles = [profile['profile_id'] for profile in mla_profiles]

    if choice == '1':
        gmail_acc_filename = "Files/google_acc_desktop.csv" if platform == 'd' else  "Files/google_acc_mobile.csv"#get_filename('gmail_aacounts')
        accounts = FilesHandler.read_csv(gmail_acc_filename)
        for ind, account in enumerate(accounts):
            MLA.create_and_login(platform, account, ind)
    elif choice == '2':
        data = FilesHandler.get_gsheet_data()
        for mla_profile_id, reviewee in zip(mla_profiles, data):
            review.main(mla_profile_id, reviewee, platform)



if __name__ == "__main__":
    main()