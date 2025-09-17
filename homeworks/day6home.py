blog_views = [150, 800, 2500, 600, 1200, 450, 3000]
views=0
trending=0
for blogview in blog_views:
    if blogview>1000:
        print("Trending")
        trending=trending+1 # for counting how many trending blogs
    elif blogview>=500:
        print("Average")
    else:
        print("Low Traffic")
    views+=blogview # for calculating total views 
print(f"The total number of view is {views}.")
print(f"The number of Trending Post is {trending}.")
        

