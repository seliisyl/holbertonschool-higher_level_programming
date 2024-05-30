#!/usr/bin/python3
"""
   function file for requests
"""

import requests
import csv


def fetch_and_print_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    # Print the status code of the response
    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        # Parse the fetched data into a JSON object
        posts = response.json()

        for post in posts:
            print(post['title'])


def fetch_and_save_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    if response.status_code == 200:
        # Parse the fetched data into a JSON object
        posts = response.json()

        # Structure the data into a list of dictionaries
        structured_data = [
                {'id': post['id'], 'title': post['title'], 'body':
                    post['body']}
                for post in posts
                ]

        # Define the CSV file name
        csv_file = 'posts.csv'

        # Write the data to a CSV file
        with open(csv_file, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['id', 'title', 'body'])
            writer.writeheader()
            writer.writerows(structured_data)

        print(f"Data has been saved to {csv_file}")


if __name__ == "__main__":
    fetch_and_print_posts()
    fetch_and_save_posts()
