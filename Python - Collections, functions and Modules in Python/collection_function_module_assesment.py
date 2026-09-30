import datetime

users_db = {}
posts_db = []

def get_valid_input(prompt_text):
    while True:
        value = input(prompt_text).strip()
        if value:
            return value
        print("Error: Field cannot be empty. Please try again.")

def register_user():
    print("\n--- Register New Account ---")
    while True:
        username = get_valid_input("Enter Username: ")
        if username in users_db:
            print("Error: Username already exists. Try a different one.")
        else:
            password = get_valid_input("Enter Password: ")
            users_db[username] = password
            print(f"Success: Account '{username}' created!")
            break

def login_user():
    print("\n--- Login ---")
    attempts = 3
    while attempts > 0:
        username = input("Username: ").strip()
        password = input("Password: ").strip()
        
        if username in users_db and users_db[username] == password:
            print(f"\nWelcome, {username}!")
            return username
        else:
            attempts -= 1
            print(f"Invalid credentials. {attempts} attempts remaining.")
            
    print("Error: Account locked due to too many failed attempts.")
    return None

def create_post(current_user):
    print("\n--- Create a New Post ---")
    title = get_valid_input("Post Title: ")
    description = get_valid_input("Post Description: ")
    
    current_date = datetime.date.today().strftime("%d-%m-%Y")
    
    new_post = {
        "author": current_user,
        "title": title,
        "description": description,
        "date": current_date
    }
    posts_db.append(new_post)
    print("Success: Post published!")

def view_all_posts():
    print("\n--- All Posts ---")
    if not posts_db:
        print("No posts available.")
        return
        
    for post in posts_db:
        print("-" * 30)
        print(f"Author: {post['author']}")
        print(f"Title: {post['title']}")
        print(f"Date: {post['date']}")
        print(f"Description: {post['description']}")
    print("-" * 30)

def search_posts():
    print("\n--- Search Posts by Username ---")
    target_user = get_valid_input("Enter username to search: ")
    
    found_posts = [p for p in posts_db if p['author'] == target_user]
    
    if not found_posts:
        print(f"No posts found for user '{target_user}'.")
    else:
        print(f"\n--- Posts by '{target_user}' ---")
        for post in found_posts:
            print("-" * 30)
            print(f"Title: {post['title']} | Date: {post['date']}")
            print(f"Description: {post['description']}")
        print("-" * 30)

def main():
    while True:
        print("\n=== POSTBOARD MAIN MENU ===")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        
        choice = input("Select an option (1/2/3): ").strip()
        
        if choice == '1':
            register_user()
        elif choice == '2':
            logged_in_user = login_user()
            if logged_in_user:
                while True:
                    print(f"\n--- User Dashboard ({logged_in_user}) ---")
                    print("1. Create Post")
                    print("2. View All Posts")
                    print("3. Search Posts by Username")
                    print("4. Logout")
                    
                    sub_choice = input("Select an option: ").strip()
                    
                    if sub_choice == '1':
                        create_post(logged_in_user)
                    elif sub_choice == '2':
                        view_all_posts()
                    elif sub_choice == '3':
                        search_posts()
                    elif sub_choice == '4':
                        print(f"Logging out {logged_in_user}...")
                        break
                    else:
                        print("Invalid option. Please try again.")
        elif choice == '3':
            print("Exiting PostBoard. Goodbye!")
            break
        else:
            print("Invalid option. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()