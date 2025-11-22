# DONATION RECORDS CRUD MANAGER

donation_list = []
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
    donation_list.append(donation)
    print("Donation record added successfully!")

def view_donations():
    print("View all donation records")
    if not donation_list:
        print("No donation records found.")
        return
    for d in donation_list:
        print("Donor: {}, Amount: {}, Date: {}, Phone no: {}".format(d["donor_name"], d["amount"], d["date"], d["phone_no"]))

def update_donation():
    print("Update a donation record")
    donor_name = input("Enter donor name to update: ")
    for d in donation_list:
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
    for d in donation_list:
        if d["donor_name"] == donor_name:
            confirmation = input("Are you sure you want to delete this record? (yes/no): ")
            if confirmation.lower() != 'yes':
                print("Deletion cancelled")
            else:
                donation_list.remove(d)
                print("DONATION RECORD DELETED SUCCESSFULLY!")
                return
    print("Donation record not found.")

def main():
    print("------DONATION RECORDS MANAGER------")
    print("1. Add Donation Record")
    print("2. View Donation Records")
    print("3. Update Donation Record")
    print("4. Delete Donation Record") 
    print("5. Exit")

while True:
    main()
    choice = input("Enter your choice (1-5): ")
    if choice == '1':
        add_donation()
    elif choice == '2':
        view_donations()
    elif choice == '3':
        update_donation()
    elif choice == '4':
        delete_donation()
    elif choice == '5':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please try again.")