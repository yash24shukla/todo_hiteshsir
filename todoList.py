# run this file

import backend


# importing the backend coding part
def main():
    # setting a terminator variable for while loop
    run = 1

    # creating database
    backend.create_table()

    # while loop to run the program until the selection of the exit option
    while run:
        # printing the the options
        print('\n')
        print('1. Insert new task in todo list \n'
              '2. View the todo list \n'
              '3. Delete the task \n'
              '4. Exit \n')
        # taking input of the option
        x = input("Choose any option: ")

        # selecting the action based on the option
        if x == "1":
            # taking the input to add the new task
            task = str(input("Enter your task: "))

            # entering data in database
            backend.data_entry(task)
        elif x == "2":
            # printing the data
            backend.printData()
        elif x == "3":
            # taking the index input to delete the task
            indexToDelete = int(input("\nenter the index of the task that you want to delete: "))

            # deleting the task
            backend.deleteTask(indexToDelete)
        elif x == "4":
            # setting the terminator variable to terminate the loop
            run = 0
        else:
            # if the user will not choose valid option then it will show this
            print("Pls Enter Valid Option!")


    #closing the connection from the database
    backend.closeCursor()


if __name__ == '__main__': main()
