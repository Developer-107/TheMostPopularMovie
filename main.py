from time import sleep
import smtplib
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# Setting driver up
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.imdb.com/chart/moviemeter/?ref_=nv_mv_mpm")
sleep(4)

# Clicking on the first movie in rating
menu = driver.find_element(By.CLASS_NAME, "ipc-title-link-wrapper")
menu.click()
sleep(2)

# Fetching values
name_of_the_most_popular_movie = driver.find_element(By.CLASS_NAME, "hero__primary-text").text
description_of_the_most_popular_movie = driver.find_element(By.CLASS_NAME, "sc-865706aa-1").text
director_name = driver.find_element(By.CLASS_NAME, "ipc-metadata-list-item__list-content-item").text
rating = driver.find_element(By.CLASS_NAME, "sc-d541859f-1").text

driver.quit()

# Making dictionary
most_popular_movie = {
    "Name" : name_of_the_most_popular_movie,
    "Description" : description_of_the_most_popular_movie,
    "Director" : director_name,
    "Rating" : rating,
}



# creates SMTP session
s = smtplib.SMTP('smtp.gmail.com', 587)

# start TLS for security
s.starttls()

# Authentication
s.login("sender_email_id", "sender_email_id_password")

# message to be sent
message = ("Hey, \n "
           f"I'm Reaching out to you to tell you that the most popular movie on IMDb is {most_popular_movie["Name"]}. \n "
           f"It's Directed by {most_popular_movie["Director"]} and currently is holding {most_popular_movie["Rating"]} out 10 point rating \n"
           f"Plot: {most_popular_movie["Description"]} \n"
           f"Soo... Maybe we could watch that, can't we? \n"
           f"I'll wait to your answer \n \n \n"
           f"Your IMDB checker buddy")

# sending the mail
s.sendmail("sender_email_id", "receiver_email_id", message)

# terminating the session
s.quit()