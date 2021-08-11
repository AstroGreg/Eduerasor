from webdriver_manager.chrome import ChromeDriverManager
from termcolor import colored
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class Edueraser:
    def __init__(self):
        self.link = "https://edublend.ucll.be/MBI26A/Exercise/QSet/"
        self.chrome_options, self.driver = webdriver.ChromeOptions(),  webdriver.Chrome(ChromeDriverManager().install())
        self.login()
    def erase_all_excersis(self):
         for page in [21,20,18,16,14,10,6,5,4,3,2,1]:
            self.driver.get(f"{self.link}{page}") # ga naar de pagina waar de set van vragen zich bevinden.
            questions = [li.find_element_by_tag_name("a").get_attribute("href") for li in self.driver.find_element_by_class_name("row").find_elements_by_tag_name("li")]
            for question in questions:  # itereer door de set van vragen
                self.driver.get(question)
                #  map(lambda inputtag: inputtag.clear(), self.driver.find_elements_by_tag_name("input"))
                for inputtag in self.driver.find_elements_by_tag_name("input"):
                    inputtag.clear()
                self.driver.find_element_by_id("validateButton").click()
         # delete alle inputvelden van de vraag
         self.quit()
    def login(self):
        self.driver.get("https://edublend.ucll.be")
        print(colored("\n-------------------------------------------------\nLogin on Tolede/edublend using the chrome Driver!\nThe automation will only function on the chrome tab that just popped up.\nin case you entered wrong credentials or got a pop up. \nYou should keep navigating (reload/moveback) on the intial screen automated by the chrome driver.\n-------------------------------------------------" , "green"))

        WebDriverWait(self.driver, 10000).until(ec.title_is("EduBlend homepage")) # 10 000 seconden om in te loggen. Dat moet lukken
    def quit(self):
        self.driver.close()
if __name__ == '__main__':
    edueraser = Edueraser()
    edueraser.erase_all_excersis()
