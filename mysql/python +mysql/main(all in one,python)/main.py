from dbhelper import DBHelper

def main():
    helper = DBHelper()

    while True:
        print("\nOptions:")
        print("1. Insert a new user")
        print("2. Fetch all users")
        print("3. Update a user")
        print("4. Delete a user")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            userid = input("Enter user ID: ")
            username = input("Enter user name: ")
            phone = input("Enter user phone: ")
            helper.insert_user(userid, username, phone)

        elif choice == '2':
            helper.fetch_all()

        elif choice == '3':
            userid = input("Enter user ID to update: ")
            username = input("Enter new user name: ")
            phone = input("Enter new user phone: ")
            helper.update_user(userid, username, phone)

        elif choice == '4':
            userid = input("Enter user ID to delete: ")
            helper.delete_user(userid)

        elif choice == '5':
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()


# write the name of class as dphelper.py



