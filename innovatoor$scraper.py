#for counting the number of $ in innovatoor.com
import requests
from bs4 import BeautifulSoup

class InnovatoorScraper:
    def __init__(self, base_url):
        self.base_url = base_url

    def fetch_page_content(self, url):
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.content
        except requests.exceptions.RequestException as e:
            print(f"Error fetching page content: {e}")
            return None

    def parse_content_for_dollar_sign(self, html_content):
        soup = BeautifulSoup(html_content, 'html.parser')
        text = soup.get_text()
        occurrences = text.count('$')
        return occurrences

    def scrape_for_dollar_sign(self):
        html_content = self.fetch_page_content(self.base_url)
        if html_content:
            occurrences = self.parse_content_for_dollar_sign(html_content)
            print(f"The dollar sign '$' was found {occurrences} times on the page.")
        else:
            print("Failed to retrieve or parse the page content.")

if __name__ == "__main__":
    # URL of the Innovatoor website
    base_url = 'https://www.innovatoor.com'

    scraper = InnovatoorScraper(base_url)
    scraper.scrape_for_dollar_sign()


#for scraping elements containing $ in it

class InnovatoorScraper:
    def __init__(self, base_url):
        self.base_url = base_url

    def fetch_page_content(self, url):
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.content
        except requests.exceptions.RequestException as e:
            print(f"Error fetching page content: {e}")
            return None

    def parse_content_for_dollar_sign(self, html_content):
        soup = BeautifulSoup(html_content, 'html.parser')
        # Find all text elements that contain the dollar sign
        elements_with_dollar = soup.find_all(string=lambda text: '$' in text)
        return elements_with_dollar

    def scrape_for_dollar_sign(self):
        html_content = self.fetch_page_content(self.base_url)
        if html_content:
            elements_with_dollar = self.parse_content_for_dollar_sign(html_content)
            if elements_with_dollar:
                print("Found the following sections containing '$':")
                for element in elements_with_dollar:
                    print(f"- {element.strip()}")
            else:
                print("No sections containing '$' were found on the page.")
        else:
            print("Failed to retrieve or parse the page content.")

if __name__ == "__main__":
    # URL of the Innovatoor website
    base_url = 'https://www.innovatoor.com'

    scraper = InnovatoorScraper(base_url)
    scraper.scrape_for_dollar_sign()


#Scraping content in a given section

class InnovatoorDataScraper:
    def __init__(self, url):
        self.url = url

    def fetch_page_content(self):
        try:
            response = requests.get(self.url)
            response.raise_for_status()
            return response.content
        except requests.exceptions.RequestException as e:
            print(f"Error fetching page content: {e}")
            return None

    def parse_data_section(self, html_content):
        soup = BeautifulSoup(html_content, 'html.parser')
        data_section = soup.find(id='DATA')
        
        if data_section:
            return data_section.get_text(strip=True)
        else:
            return None

    def scrape_data_section(self):
        html_content = self.fetch_page_content()
        if html_content:
            data_content = self.parse_data_section(html_content)
            if data_content:
                print("Content in the section 'Data mining and Data extraction':")
                print(data_content)
            else:
                print("No content found in the section Data mining and Data extraction.")
        else:
            print("Failed to retrieve or parse the page content.")

if __name__ == "__main__":
    # URL of the Innovatoor website
    url = 'https://www.innovatoor.com'

    scraper = InnovatoorDataScraper(url)
    scraper.scrape_data_section()

