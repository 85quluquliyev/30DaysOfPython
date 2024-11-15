import string
class MedlineScraper:
    def __init__(self):
        self.base_url = "https://medlineplus.gov/druginfo/"
        
    def get_categories(self):
        letters = string.ascii_uppercase
        return letters

if __name__ == '__main__':
    scraper = MedlineScraper()
    print(scraper.get_categories())
