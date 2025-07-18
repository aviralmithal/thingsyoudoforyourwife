from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeoutError
import re


def load_all_banners(page):
    """
    Clicks the 'View More' button until all banners are loaded.
    """
    while True:
        try:
            load_more_button = page.locator("text='View More'")
            load_more_button.wait_for(timeout=3000)
            load_more_button.click()
            page.wait_for_timeout(2000)  # Wait for new banners to load
        except PlaywrightTimeoutError:
            print("All banners loaded (no more 'View More' button).")
            break


def login_to_site(page):
    """
    Automates login sequence to ThesisDriven platform.
    """
    page.goto("https://database.thesisdriven.com/real-estate-markets")
    page.click("text='Log In'")
    page.click("body > div.bubble-element.Page.baTaHlt.main-page.bubble-r-container.flex.column > div > div > div > button")
    page.fill('body > div.bubble-element.Page.baTaHlt.main-page.bubble-r-container.flex.column > div > div > div > div.bubble-element.Group.baTaJaQaL.bubble-r-container.flex.column > input', 'YOUR_EMAIL_HERE')
    page.fill('body > div.bubble-element.Page.baTaHlt.main-page.bubble-r-container.flex.column > div > div > div > div.bubble-element.Group.baTaJaQaR.bubble-r-container.flex.column > input', 'YOUR_PASSWORD_HERE')
    page.wait_for_timeout(5000)
    page.wait_for_url("https://database.thesisdriven.com")


def get_all_banner_links(page):
    """
    Extracts unique links from all loaded banner cards.
    """
    card_selector = "[class*='bubble-element group-item bubble-r-container flex row']"
    banner_locator = page.locator(card_selector)
    total = banner_locator.count()
    print(f"Found {total} banners")

    links = set()
    for i in range(total):
        link = banner_locator.nth(i).locator("a").first.get_attribute("href")
        if link:
            links.add(link)
            print(f"Collected link: {link}")
    return links


def download_csv_if_available(page, link):
    """
    If a CSV download option is available on the page, initiates download and saves the file.
    """
    page.goto(link)
    page.wait_for_timeout(1000)

    try:
        # Click sequence for opening the download panel
        # Click on theme button
        page.click("button.clickable-element.bubble-element.Button.baTaPoo", timeout=5000)
        # Check Multi family - Core check box
        page.click("div.bubble-element.RepeatingGroup.baTaRaFc.bubble-rg button", timeout=5000)
        #Click on Apply Filter
        page.click("button.clickable-element.bubble-element.Button.baTaRaFaW", timeout=5000)

        # Expect file download
        with page.expect_download(timeout=60000) as download_info:
            page.click("div.bubble-element.Group.baTaKaWaI.bubble-r-container.flex.column > div > div > button")

        download = download_info.value

        # Create a safe filename from the URL
        suffix = re.sub(r'\W+', '-', link.strip('/').split('/')[-1])
        filename = f"{suffix}.csv"

        download.save_as(filename)
        print(f"Downloaded: {filename}")
    except Exception as e:
        print(f"No CSV available for {link} or error occurred: {e}")


# Main execution block
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    login_to_site(page)
    page.goto("https://database.thesisdriven.com/real-estate-markets")

    load_all_banners(page)
    links = get_all_banner_links(page)

    for link in links:
        download_csv_if_available(page, link)

    browser.close()



