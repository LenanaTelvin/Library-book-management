bookID = input("Enter Book ID: ") 
dueDate = int(input("Enter Due Date (as an integer): ")) 
returnDate = int(input("Enter Return Date (as an integer): "))  

# Calculate overdue days (ensuring it's non-negative)
daysOverdue = max(0, returnDate - dueDate)  

# Determine fine rate
if daysOverdue == 0:
    fineRate = 0
elif daysOverdue <= 7:
    fineRate = 20
elif daysOverdue <= 14:
    fineRate = 50
else:
    fineRate = 100  

# Calculate fine amount
fineAmount = daysOverdue * fineRate  

# Display output
print("\nLibrary Fine Info")
print(f"Book ID: {bookID}")
print(f"Return Date: {returnDate}")
print(f"Days Overdue: {daysOverdue}")
print(f"Fine Info: Ksh. {fineRate} per day")
print(f"Total Fine Amount: Ksh. {fineAmount}")
