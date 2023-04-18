import webbrowser
import time

print("Hi! This is an auto-bypasser for the Krnl key.")
print("If there is an error in the script, please report it to the creator.")

while True:
    # ask user to confirm
    confirmation = input("Do you want to run the bypasser? (y/n): ")

    # check confirmation
    if confirmation.lower() == "y":
        print("Confirmed. Running bypasser...")
        # list of websites to open
        websites = [
            "https://linkvertise.com/48193/krnlc4/1",
            "https://linkvertise.com/48193/krnlkey/1",
            "https://linkvertise.com/48193/thekrnlkey/1",
            "https://linkvertise.com/48193/krnlc3/1",
            "https://cdn.krnl.place/getkey.php"
        ]

        # loop through each website and open it in a new tab
        for site in websites:
            webbrowser.open_new_tab(site)
            if site != websites[-1]: # wait for 25 seconds before opening the next website
                time.sleep(2)

        print("Goodbye! Your bypassing is done. Hope it helped!")
        time.sleep(5)  # delay script exit by 5 seconds
        break

    elif confirmation.lower() == "n":
        print("Sorry to see you go. Goodbye!")
        time.sleep(5)  # delay script exit by 5 seconds
        break

    else:
        print("Oops, you didn't enter y or n. Try again!")
