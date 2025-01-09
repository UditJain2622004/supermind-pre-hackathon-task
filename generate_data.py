import uuid
import random
import json
from datetime import datetime

# Define ranges for each post type
RANGES = {
    "image": {"views": (500, 5000), "likes": (50, 500), "comments": (5, 50), "shares": (1, 20)},
    "carousel": {"views": (1000, 7000), "likes": (100, 1000), "comments": (10, 100), "shares": (5, 50)},
    "video": {"views": (3000, 20000), "likes": (200, 5000), "comments": (20, 500), "shares": (10, 200)},
    "reel": {"views": (5000, 50000), "likes": (500, 10000), "comments": (50, 1000), "shares": (20, 500)},
}

def generate_post_data(post_type, count):
    data = []

    for _ in range(count):
        post = {
            "id": str(uuid.uuid4()),
            "post_type": post_type,
            "views": random.randint(*RANGES[post_type]["views"]),
            "likes": random.randint(*RANGES[post_type]["likes"]),
            "comments": random.randint(*RANGES[post_type]["comments"]),
            "shares": random.randint(*RANGES[post_type]["shares"]),
            "timestamp": datetime.now().isoformat()
        }
        data.append(post)
        
    return data

def generate_social_media_data(num_posts_per_type):
    post_types = ["image", "carousel", "video", "reel"]

    for post_type in post_types:
        posts = generate_post_data(post_type, num_posts_per_type)

        file_name = f"{post_type}_posts.json"
        with open(file_name, "w") as json_file:
            json.dump(posts, json_file, indent=4)

        print(f"Generated {num_posts_per_type} {post_type} posts and saved to {file_name}")

if __name__ == "__main__":
    num_posts_per_type = 10
    generate_social_media_data(num_posts_per_type)
