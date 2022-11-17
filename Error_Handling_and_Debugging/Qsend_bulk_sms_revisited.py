def send_sms(number):
    print("Message is successfully sent to " + number)
    return True

def get_phone_number(person):
    customers = ["Jerry Seinfeld","George Constanza","Elaine Benes","Cosmo Kramer",
               "Jim Halpert","Pam Beesly","Michael Scott","Dwight Schrute",
               "Rachel Green", "Monica Geller", "Ross Geller", "Phoebe Buffay",
               "Joey Tribbiani", "Chandler Bing"]
    numbers = ["+1 960-454-6956", "+1 844-833-4965", "+1 543-920-5729", "+1 556-673-6702",
               "+1 867-767-7664", "+1 410-570-7381", "+1 657-220-6601", "+1 940-573-6702",
               "+1 813-856-3347", "+1 527-324-1403", "+1 687-801-6781", "+1 208-702-5161",
               "+1 908-665-3975", "+1 444-970-5300"]

    return numbers[customers.index(person)]

def send_bulk_sms(arr):
    for person in arr:
        try:
            number = get_phone_number(person)
            send_sms(number)
        except ValueError:   #Visual Studio Code is helping us about to choose which error should we use (ValueError: 'Maurice Moss' is not in list).
            print("Person can not found in the number list: " + person)
            
print(send_bulk_sms(["Pam Beesly", "George Constanza", "Elaine Benes", "Michael Scott", "Maurice Moss"]))