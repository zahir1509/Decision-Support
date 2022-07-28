import csv
import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

#add all hotel URLs here
URL = ["https://www.agoda.com/the-fullerton-bay-hotel/hotel/singapore-sg.html"]

driver = webdriver.Chrome()

# Prepare CSV file
csvFile = open("hotel_review.csv", "w", newline='', encoding="utf-8")
csvWriter = csv.writer(csvFile)
csvWriter.writerow(['City','Hotel Name','Address','Overall Rating','Review Rating','Date','Title','Review'])

for hotelpage in URL:

    driver.get(hotelpage)

    time.sleep(10) # Wait for reviews to load

    driver.find_element_by_xpath("//div[@class='SearchBoxTextDescription__title']").click() #Click to close the popup for checkin date

    time.sleep(3)

    driver.find_element_by_xpath("//select[@class='Review-sortingSelect']/option[text()='Most recent']").click() #Sort by most recent
    
    reviewcounter = 0 #Initialise Review counter 

    time.sleep(1)

    for page in range(6) :

        time.sleep(2)
        allreviews = driver.find_elements_by_xpath("//div[@class='Review-comment']") #Get all reviews in the page
        reviewcounter = reviewcounter + len(allreviews)

        # Loop through the reviews found
        for i in range(len(allreviews)):

            # Get City, Hotel Name, Review Title, Review Text, Score and Review Date
            try: #to bypass reviews empty bodies
                temp_review = allreviews[i].find_element_by_xpath(".//p[@class='Review-comment-bodyText']")
                review = temp_review.text
                city = driver.find_element_by_xpath("//span[@class='sc-hGbfJK dLuMxG']").text[15:]
                hotelname = driver.find_element_by_xpath("//h1[@class='breadcrumb-regionName breadcrumbRegionName__h1']").text[5:]
                address = driver.find_element_by_xpath("//span[@class='sc-jSgupP Fpaqn HeaderCerebrum__Address']").text
                hotelrating = driver.find_element_by_xpath("//span[@class='sc-jSgupP gfEOpa']").text
                score = allreviews[i].find_element_by_xpath(".//div[@class='Review-comment-leftScore']").text
                reviewdate = allreviews[i].find_element_by_xpath(".//span[@class='Review-statusBar-date ']").text[8:]
                title = allreviews[i].find_element_by_xpath(".//p[@class='Review-comment-bodyTitle']").text[:-1]
                review = allreviews[i].find_element_by_xpath(".//p[@class='Review-comment-bodyText']").text

                csvWriter.writerow((city, hotelname, address, hotelrating, score, reviewdate, title, review)) #write to csv

            except NoSuchElementException:
                pass
            

        print(f'Page {page+1} done. {reviewcounter} reviews were scraped for {hotelname} in {city}.')
        #time.sleep(1)

        #go to next page of reviews
        driver.find_element_by_xpath('//i[@class="ficon ficon-24 ficon-carrouselarrow-right"]').click()


# Close CSV file and Chrome Window
csvFile.close()
driver.close()

