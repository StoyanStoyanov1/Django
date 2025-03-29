from django.shortcuts import render
from datetime import date

all_posts = [
    {
        "slug": "hike-in-the-mountains",
        "image": "mountains.jpg",
        "author": "Maximilian",
        "date": date(2017, 7, 21),
        "title": "Mountain Hiking",
        "excerpt": "There's nothing like the views you get when hiking in the mountains! And I wasn't even prepared for what happened while I was enjoying the view!",
        "content": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam at sapien nec eros luctus tincidunt. Integer euismod, nulla ac dapibus fermentum, nunc eros facilisis felis, nec tincidunt sapien velit vel felis. Vestibulum at arcu eu quam elementum consequat.",
    },
    {
        "slug": "sunset-at-the-beach",
        "image": "coding.jpg",
        "author": "Samantha",
        "date": date(2018, 5, 14),
        "title": "Sunset at the Beach",
        "excerpt": "Watching the sunset by the ocean is an experience like no other. The colors, the sound of the waves, and the fresh breeze create a perfect moment.",
        "content": "Curabitur nec arcu in leo venenatis pharetra at a felis. Aliquam at ante vel erat tincidunt facilisis. Fusce commodo, sapien at aliquet fermentum, augue libero volutpat ligula, nec placerat lacus odio eget purus.",
    },
    {
        "slug": "adventure-in-the-forest",
        "image": "woods.jpg",
        "author": "Daniel",
        "date": date(2019, 9, 3),
        "title": "Adventure in the Forest",
        "excerpt": "Exploring the deep forest was an adventure full of surprises. From hidden waterfalls to wildlife encounters, every moment was breathtaking!",
        "content": "Proin fringilla ligula at eros tincidunt, non feugiat augue pellentesque. Nulla facilisi. Suspendisse sit amet metus vitae odio malesuada gravida. Phasellus volutpat mi in nunc porta, vel dapibus urna tincidunt."
    }
]

def get_date(post):
    return post.get('date')

def starting_page(request):
    sorted_posts = sorted(all_posts, key=get_date)
    latest_posts = sorted_posts[-3:]
    return render(request, "blog/index.html", {
        "posts": latest_posts
    })

def posts(request):
    return render(request, "blog/all-posts.html", {
        "all_posts": all_posts,
    })

def post_detail(request, slug):
    identified_post = next(post for post in all_posts if post['slug'] == slug)
    return render(request, "blog/post-detail.html", {
        "post": identified_post
    } )