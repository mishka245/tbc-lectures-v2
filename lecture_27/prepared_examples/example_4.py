import os
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get("OPEN_AI_KEY"),  # This is the default and can be omitted
)

def get_sentiment(text):
    """
    Determines if the sentiment of the given text is negative, neutral, or positive
    using ChatGPT.

    Args:
        text (str): The input text to analyze.

    Returns:
        str: The sentiment of the text ('negative', 'neutral', or 'positive').
    """
    try:
        # Define the prompt for ChatGPT
        prompt = f"გააანალიზე შემდეგი ტექსტი და მითხარი ნეგატიურია, პოზიტიურია თუ ნეიტრალური მისი შინაარსი. მიპასუხე მხოლოდ ერთი სიტყვა. \n\n{text}"

        response = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            model="gpt-4o-mini",
        )

        # Extract and return the sentiment
        sentiment = response.choices[0].message.content
        return sentiment
    except Exception as e:
        raise e
        # return f"Error: {e}"



def main():
    # URL of the website to scrape
    url = "https://www.interpressnews.ge/ka/"  # Replace with the target website's URL

    # Send an HTTP GET request to the URL
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')

        titles = soup.find_all("div", itemtype='http://schema.org/Article')
        # Print the titles
        print("Article Titles:")
        stats = {
            "ნეგატიური": 0,
            "პოზიტიური": 0,
            "ნეიტრალური": 0
        }
        for title in titles:
            news_url = urljoin(url, title.a["href"])
            text = title.a.h2.text
            sentiment = get_sentiment(text)
            sentiment = sentiment.strip(".")
            if sentiment in stats:
                stats[sentiment] += 1
            else:
                print("Unknown sentiment:", sentiment)
            print(sentiment, text, news_url)

        print(stats)

    else:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")

if __name__ == "__main__":
    main()