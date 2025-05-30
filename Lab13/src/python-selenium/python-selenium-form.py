import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.core import driver
from webdriver_manager.firefox import GeckoDriverManager

class TestCalculator(unittest.TestCase):
    def setUp(self):
        """
        Inicjalizacja testu - uruchomienie przeglądarki Fifefox i otwarcie strony kalkulatora
        """
        self.service = Service(GeckoDriverManager().install())
        self.driver = webdriver.Firefox(service=self.service)
        self.driver.get('https://tgadek.bitbucket.io/app/calc/prod/index.html')

    def test_addition(self):
        """
        Test sprawdzający działanie operacji dodawania w kalkulatorze
        """
        # Given
        number1 = self.driver.find_element(By.ID, "number1")
        number1.send_keys("1")
        number2 = self.driver.find_element(By.ID, "number2")
        number2.send_keys("2")

        # When
        self.driver.find_element(By.CSS_SELECTOR, "input[type='button']").click()

        # Then
        result = self.driver.find_element(By.ID, "result").text
        self.assertEqual(result, "1 + 2 = 3")

    def test_empty_enter_1(self):
        # Given
        number1 = self.driver.find_element(By.ID, "number1")
        number1.send_keys("")
        number2 = self.driver.find_element(By.ID, "number2")
        number2.send_keys("2")

        # When
        self.driver.find_element(By.CSS_SELECTOR, "input[type='button']").click()

        # Then
        result = self.driver.find_element(By.ID, "result").text
        self.assertEqual(result, "Formularz zawiera niepoprawne dane!")

    def test_empty_enter_2(self):
        # Given
        number1 = self.driver.find_element(By.ID, "number1")
        number1.send_keys("2")
        number2 = self.driver.find_element(By.ID, "number2")
        number2.send_keys("")

        # When
        self.driver.find_element(By.CSS_SELECTOR, "input[type='button']").click()

        # Then
        result = self.driver.find_element(By.ID, "result").text
        self.assertEqual(result, "Formularz zawiera niepoprawne dane!")

    def test_empty_enters(self):
        # Given
        number1 = self.driver.find_element(By.ID, "number1")
        number1.send_keys("")
        number2 = self.driver.find_element(By.ID, "number2")
        number2.send_keys("")

        # When
        self.driver.find_element(By.CSS_SELECTOR, "input[type='button']").click()

        # Then
        result = self.driver.find_element(By.ID, "result").text
        self.assertEqual(result, "Formularz zawiera niepoprawne dane!")

    def test_sub_minus_number(self):
        # Given
        number1 = self.driver.find_element(By.ID, "number1")
        number1.send_keys("-10")
        number2 = self.driver.find_element(By.ID, "number2")
        number2.send_keys("20")

        # When
        self.driver.find_element(By.CSS_SELECTOR, "input[type='button']").click()

        # Then
        result = self.driver.find_element(By.ID, "result").text
        self.assertEqual(result, "-10 + 20 = 10")

    def test_sub_minus_numbers(self):
        # Given
        number1 = self.driver.find_element(By.ID, "number1")
        number1.send_keys("-10")
        number2 = self.driver.find_element(By.ID, "number2")
        number2.send_keys("-10")

        # When
        self.driver.find_element(By.CSS_SELECTOR, "input[type='button']").click()

        # Then
        result = self.driver.find_element(By.ID, "result").text
        self.assertEqual(result, "-10 + -10 = -20")


    def tearDown(self):
        """
        Zakończenie testu - zamknięcie przeglądarki
        """
        self.driver.quit()




class TestPortfolio(unittest.TestCase):
    def setUp(self):
        self.service = Service(GeckoDriverManager().install())
        self.driver = webdriver.Firefox(service=self.service)

    def test_font_size_p(self):
        self.driver.get('https://tgadek.bitbucket.io/app/portfolio/prod/experience.html')
        p = self.driver.find_element(By.TAG_NAME, 'p')

        self.assertEqual(p.value_of_css_property('font-size'),"18px")

    def test_index_header(self):
        self.driver.get('https://tgadek.bitbucket.io/app/portfolio/prod/index.html')
        header = self.driver.find_element(By.TAG_NAME, 'header')
        a = header.find_element(By.TAG_NAME, 'a')
        img = a.find_element(By.TAG_NAME, 'img')


        self.assertEqual(img.get_property('src'),"https://tgadek.bitbucket.io/app/portfolio/prod/img/it-design-logo.png")
        self.assertEqual(header.find_element(By.TAG_NAME, 'h1').text,"IT Design")

    def test_portfolio_header(self):
        self.driver.get('https://tgadek.bitbucket.io/app/portfolio/prod/portfolio.html')
        header = self.driver.find_element(By.TAG_NAME, 'header')
        a = header.find_element(By.TAG_NAME, 'a')
        img = a.find_element(By.TAG_NAME, 'img')

        self.assertEqual(img.get_property('src'),
                         "https://tgadek.bitbucket.io/app/portfolio/prod/img/it-design-logo.png")
        self.assertEqual(header.find_element(By.TAG_NAME, 'h1').text, "IT Design")

    def test_team_header(self):
        self.driver.get('https://tgadek.bitbucket.io/app/portfolio/prod/team.html')
        header = self.driver.find_element(By.TAG_NAME, 'header')
        a = header.find_element(By.TAG_NAME, 'a')
        img = a.find_element(By.TAG_NAME, 'img')

        self.assertEqual(img.get_property('src'),
                         "https://tgadek.bitbucket.io/app/portfolio/prod/img/it-design-logo.png")
        self.assertEqual(header.find_element(By.TAG_NAME, 'h1').text, "IT Design")


    def test_experience_header(self):
        self.driver.get('https://tgadek.bitbucket.io/app/portfolio/prod/experience.html')
        header = self.driver.find_element(By.TAG_NAME, 'header')
        a = header.find_element(By.TAG_NAME, 'a')
        img = a.find_element(By.TAG_NAME, 'img')

        self.assertEqual(img.get_property('src'),
                         "https://tgadek.bitbucket.io/app/portfolio/prod/img/it-design-logo.png")
        self.assertEqual(header.find_element(By.TAG_NAME, 'h1').text, "IT Design")

    def test_index_h2(self):
        self.driver.get('https://tgadek.bitbucket.io/app/portfolio/prod/index.html')
        h2 = self.driver.find_elements(By.TAG_NAME, 'h2')

        self.assertEqual(h2[0].text,"Profesjonalne Rozwiązania IT dla Twojej Firmy")

    # def test_send_mail(self):
    #     self.driver.get("https://tgadek.bitbucket.io/app/portfolio/prod/index.html")
    #
    #     email = self.driver.find_element(By.ID, "email")
    #     email.send_keys("test@gmail.com")
    #
    #     message = self.driver.find_element(By.ID, "message")
    #     message.send_keys("test")
    #
    #
    #     self.driver.find_element(By.TAG_NAME, "button").click()
    #
    #     messageBox = self.driver.find_element(By.ID, "messageBox")
    #
    #     self.assertEqual(messageBox.text, "Dziękujemy za przesłanie wiadomości. Odpowiemy do Państwa jak najszybciej :-)")


    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
