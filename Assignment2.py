#Post class

class Post:
    def __init__(self, id, content, scheduled_time, platform):
        self.id = id
        self.content = content
        self.scheduled_time = scheduled_time
        self.platform = platform

    def edit_content(self, new_content):
        self.content = new_content

    def change_scheduled_time(self, new_time):
        self.scheduled_time = new_time

    def display_post_details(self):
        print(f"ID: {self.id}, Content: {self.content}, Scheduled Time: {self.scheduled_time}, Platform: {self.platform}")

#Schedular class

class Scheduler:
    def __init__(self):
        self.posts = {}

    def add_post(self, post):
        if post.id in self.posts:
            print("Post already exists")
        else:
            self.posts[post.id] = post
            print("Post added successfully.")

    def remove_post(self, post_id):
        if post_id not in self.posts:
            print("No posts for this ID.")
        else:
            del self.posts[post_id]
            print("Post removed successfully.")

    def view_all_posts(self):
        if not self.posts:
            print("No posts available.")
        else:
            for post in self.posts.values():
                post.display_post_details()

#File operations

    def save_to_file(self, filename):
        with open(filename, "w") as file:
            for post in self.posts.values():
                details = f"{post.id}|{post.content}|{post.scheduled_time}|{post.platform}\n"
                file.write(details)
        print("Posts saved to file successfully.")

    def load_from_file(self, filename):
        try:
            with open(filename, "r") as file:
                for line in file:
                    id, content, scheduled_time, platform = line.strip().split('|')
                    post = Post(id, content, float(scheduled_time), platform)
                    self.add_post(post)
            print("Posts loaded from file successfully.")
        except FileNotFoundError:
            print("File not found.")


#Menu system

def main():
    database = Scheduler()
    print("....Welcome to the Scheduler....")

    while True:
        print("\nMenu:")
        print("1.Add new post")
        print("2.Edit post content and scheduled time")
        print("3.Remove post")
        print("4.View all scheduled posts")
        print("5.Save posts to a file")
        print("6.Load posts from a file")
        print("7.Exit")

        option = input("Enter your option: ")

        if option == "1":
            id = input("Enter post ID: ")
            content = input("Enter post content: ")
            scheduled_time = float(input("Enter scheduled time: "))
            platform = input("Enter the platform: ")

            post = Post(id, content, scheduled_time, platform)
            database.add_post(post)

        elif option == "2":
            id = input("Enter post ID to edit: ")
            if id in database.posts:
                new_content = input("Enter new content: ")
                new_time = float(input("Enter new scheduled time: "))

                post = database.posts[id]
                post.edit_content(new_content)
                post.change_scheduled_time(new_time)
                print("Post updated successfully.")
            else:
                print("Post not found.")

        elif option == "3":
            id = input("Enter post ID to remove: ")
            database.remove_post(id)

        elif option == "4":
            database.view_all_posts()

        elif option == "5":
            filename = input("Enter filename to save posts: ")
            database.save_to_file(filename)

        elif option == "6":
            filename = input("Enter filename to load posts: ")
            database.load_from_file(filename)

        elif option == "7":
            print("Exiting. Goodbye!")
            break

        else:
            print("Invalid option. Please try again.")

main()
