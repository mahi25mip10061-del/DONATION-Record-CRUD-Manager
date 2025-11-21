# DONATION RECORDS CRUD MANAGER

donations = []
def add_donation():
    print("Add a new donation record")
    donor_name = input("Enter donor name: ")
    amount = float(input("Enter donation amount: "))
    date = input("Enter donation date (DD-MM-YYYY): ")
    phone_number = input("Enter donor phone number: ")
    donation = {
        "donor_name": donor_name,
        "amount": amount,
        "date": date,
        "phone_no": phone_number
    }
    donations.append(donation)
    print("Donation record added successfully!")

def view_donations():
    print("View all donation records")
    if not donations:
        print("No donation records found.")
        return
    for d in donations:
        print("Donor: {}, Amount: {}, Date: {}, Phone no: {}".format(d["donor_name"], d["amount"], d["date"], d["phone_no"]))

def update_donation():
    print("Update a donation record")
    donor_name = input("Enter donor name to update: ")
    for d in donations:
        if d["donor_name"] == donor_name:
            amount = float(input("enter new donation amount: "))
            date = input("Enter new donation date (DD-MM-YYYY): ")
            phone_number = input("enter donor's new phone number: ")
            d["amount"] = amount
            d["date"] = date
            d["phone_no"] = phone_number

            print("DONATION RECORD UPDATED SUCCESSFULLY!")
            return
    print("Donation record not found.")

def delete_donation():
    print("Delete a donation record")
    donor_name = input("enter donor's name to delete: ")
    for d in donations:
        if d["donor_name"] == donor_name:
            donations.remove(d)

            print("DONATION RECORD DELETED SUCCESSFULLY!")
            return
    print("Donation record not found.")

def main():
        print("------DONATION RECORDS MANAGER------")
        print("1. Add Donation Record")
        print("2. View Donation Records")
        print("3. Update Donation Record")
        print("4. Delete Donation Record") 

while True:
    main()
    choice = input("Enter your choice (1-4): ")
    if choice == '1':
        add_donation()
    elif choice == '2':
        view_donations()
    elif choice == '3':
        update_donation()
    elif choice == '4':
        delete_donation()
        break
    else:
        print("Invalid choice. Please try again.") 