import mysql.connector
from functools import reduce

# DB Connection

conn = mysql.connector.connect(

    host="127.0.0.1", 
    user="root",
    password="1234",
    database="expense_db"
)

cursor = conn.cursor()


# 1. Add User

def add_user(name):
    query = "INSERT INTO users (name) VALUES (%s)"
    cursor.execute(query, (name,))
    conn.commit()
    print("User Added Successfully")




# 2. Add Expense

def add_expense(user_id, amount, category, description, date):
    query = """INSERT INTO expenses 
               (user_id, amount, category, description, date)
               VALUES (%s, %s, %s, %s, %s)"""
    
    values = (user_id, amount, category, description, date)
    cursor.execute(query, values)
    conn.commit()
    print("Expense added")



# 3. View Expenses (JOIN)

def view_expenses(user_id):
    query = """
    SELECT users.name, expenses.amount, expenses.category, expenses.description, expenses.date
    FROM expenses
    JOIN users ON users.user_id = expenses.user_id
    WHERE users.user_id = %s
    """
    cursor.execute(query, (user_id,))
    result = cursor.fetchall()

    for row in result:
        print(row)



# Data

add_user("Sanjay") 

add_expense(1, 2000, "Food", "Hotel", "2026-04-01")
add_expense(1, 1500, "Travel", "Bus", "2026-04-02")
add_expense(1, 3000, "Shopping", "Dress", "2026-04-03")

print("\nAll Expenses:")
view_expenses(1)



# 4. Filter by Category

def filter_category(user_id, category):
    query = "SELECT amount FROM expenses WHERE user_id=%s AND category=%s"
    cursor.execute(query, (user_id, category))
    return cursor.fetchall()



# 5. Total Expense (map + reduce)

def total_expense(user_id):
    query = "SELECT amount FROM expenses WHERE user_id=%s"
    cursor.execute(query, (user_id,))
    amounts = [x[0] for x in cursor.fetchall()]

    total = reduce(lambda a, b: a + b, amounts, 0)
    return total



# 6. Category-wise Spending

def category_wise(user_id):
    query = "SELECT category, amount FROM expenses WHERE user_id=%s"
    cursor.execute(query, (user_id,))
    data = cursor.fetchall()

    result = {}
    for cat, amt in data:
        result[cat] = result.get(cat, 0) + amt

    return result
print("\nCategory Wise: ")
print(category_wise(1))



# 7. Highest Expense

def highest_expense(user_id):
    query = "SELECT amount, category FROM expenses WHERE user_id=%s"
    cursor.execute(query, (user_id,))
    data = cursor.fetchall()

    return max(data, key=lambda x: x[0])
print("\nHighest Expense:")
print(highest_expense(1))


# 8. Smart Insight

def smart_insight(user_id):
    data = category_wise(user_id)
    highest = max(data, key=data.get)
    return f"You are spending too much on {highest}"
print("\nSmart Insight:")
print(smart_insight(1))