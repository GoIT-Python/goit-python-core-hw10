contacts = [{"Boris": "+380509876542"}, {"Doris": "+14186574850"}]


for contact in contacts:
    if contact.keys() == "Boris":
        contact.update({contact.key: "333333333333"})


print(contacts)
