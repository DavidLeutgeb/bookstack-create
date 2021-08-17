import requests
import json

# Change this vars as you need

bookstack_url = "https://wiki.bookstack.local"  # Bookstack Base URL
header = {'Authorization': 'Token <<TokenID>>:<<TokenSecret>>'}  # API Token
verify_ssl = True  # Set to False if you have a selfsigned certificate

# create the structure of the book

chapters = {
    "Chapter 1": {
        "Page 1": "No content yet",
    },
    "Chapter 2": {
        "Page 1": "No content yet",
        "Page 2": "No content yet",
        "Page 3": "No content yet",
        "Page 4": "No content yet",
    },
}

# Initialize variables

book_name = input("Book Name: ")

book_create_url = bookstack_url + "/api/books"
chapter_create_url = bookstack_url + "/api/chapters"
site_create_url = bookstack_url + "/api/pages"
book_payload = {"name": book_name}

# Create Book

print("Create book " + book_name)
book_create = requests.post(book_create_url, data=book_payload, headers=header, verify=verify_ssl)
book_data = json.dumps(book_create.json(), separators=(',', ':'))
book_data_loads = json.loads(book_data)

for chapter in chapters:
    # Create chapters
    print("Create chapter " + chapter)
    chapter_create = requests.post(chapter_create_url, data={"book_id": book_data_loads['id'], "name": chapter}, headers=header, verify=verify_ssl)
    chapter_data = json.dumps(chapter_create.json(), separators=(',', ':'))
    chapter_data_loads = json.loads(chapter_data)

    for sites in chapters[chapter]:
        # Create pages
        print("Create page " + sites)
        requests.post(site_create_url, data={"chapter_id": chapter_data_loads['id'], "name": sites, "html": chapters[chapter][sites]}, headers=header, verify=verify_ssl)

print("Book " + book_name + " successfully created")
exit(0)
