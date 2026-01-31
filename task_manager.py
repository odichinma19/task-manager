import sqlite3

# Connect to SQLite database
conn = sqlite3.connect("tasks.db")
cursor = conn.cursor()

# Create table if it doesn't exist
cursor.execute("""
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    description TEXT,
    status TEXT DEFAULT 'pending'
)
""")
conn.commit()


def add_task(title, description):
    cursor.execute("INSERT INTO tasks (title, description) VALUES (?, ?)", (title, description))
    conn.commit()
    print("Task added successfully!")


def view_tasks():
    cursor.execute("SELECT * FROM tasks")
    rows = cursor.fetchall()
    for row in rows:
        print(row)


def update_task(task_id, new_status):
    cursor.execute("UPDATE tasks SET status = ? WHERE id = ?", (new_status, task_id))
    conn.commit()
    print("Task updated successfully!")


def delete_task(task_id):
    cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    conn.commit()
    print("Task deleted successfully!")


def menu():
    while True:
        print("\n--- Task Manager ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task Status")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            title = input("Task title: ")
            description = input("Task description: ")
            add_task(title, description)

        elif choice == "2":
            view_tasks()

        elif choice == "3":
            task_id = int(input("Task ID: "))
            new_status = input("New status (pending/completed): ")
            update_task(task_id, new_status)

        elif choice == "4":
            task_id = int(input("Task ID: "))
            delete_task(task_id)

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    menu()
