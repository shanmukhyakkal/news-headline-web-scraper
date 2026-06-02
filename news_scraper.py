from bs4 import BeautifulSoup

url = "https://news.ycombinator.com/"

try:
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")

        headlines = soup.find_all("span", class_="titleline")

        with open("headlines.txt", "w", encoding="utf-8") as file:
            for i, headline in enumerate(headlines, start=1):
                title = headline.get_text()
                print(f"{i}. {title}")
                file.write(f"{i}. {title}\n")

        print("\nHeadlines saved to headlines.txt")

    else:
        print("Failed to fetch webpage. Status Code:", response.status_code)

except Exception as e:
    print("Error:", e)
