import unittest
from selenium import webdriver # type: ignore
from selenium.webdriver.common.keys import Keys # type: ignore
from selenium.webdriver.common.by import By # type: ignore
from selenium.webdriver.support.ui import Select # type: ignore
from selenium.webdriver.support.ui import WebDriverWait # type: ignore
from selenium.webdriver.chrome.options import Options # type: ignore
import time


class Registration(unittest.TestCase):

    @classmethod

    def setUpClass(cls):

        chrome_options = Options()
        chrome_options.add_experimental_option("prefs", {
            "credentials_enable_service": False,  # disable save-password service
            "profile.password_manager_enabled": False,  # disable password manager
            "autofill.profile_enabled": False
        })

        chrome_options.add_argument("--disable-save-password-bubble")
        chrome_options.add_argument("--disable-features=PasswordManagerEnabled")

        cls.driver = webdriver.Chrome(options=chrome_options)
        cls.driver.maximize_window()
        cls.driver.get("http://automationexercise.com")

    def test_a_navigate_to_url(cls):
        wait = WebDriverWait(cls.driver, 5)
        homepage = cls.driver.find_element(By.CLASS_NAME, "nav.navbar-nav")
        if homepage.is_displayed():
            print("Homepage accessed!")

    def test_b_go_to_signup(cls):

        wait2 = WebDriverWait(cls.driver, 5)
        signup = cls.driver.find_element(By.XPATH, '//*[@id="header"]/div/div/div/div[2]/div/ul/li[4]/a')
        signup.click()
        # cls.driver.implicitly_wait(2)
        time.sleep(2)
        form = cls.driver.find_element(By.CLASS_NAME, "signup-form")
        if form.is_displayed():
            print("Signing up now!")

    def test_c_signed_up(cls):

        cls.driver.implicitly_wait(2)
        signup = cls.driver.find_element(By.CLASS_NAME, "fa.fa-lock")
        signup.click()
        name = cls.driver.find_element(By.XPATH, '//*[@id="form"]/div/div/div[3]/div/form/input[2]')
        name.click()
        name.send_keys("Naman")
        email = cls.driver.find_element(By.XPATH, '//*[@id="form"]/div/div/div[3]/div/form/input[3]')
        email.click()
        email.send_keys("a498ismi89433@gmail.com")
        signButton = cls.driver.find_element(By.XPATH, '//*[@id="form"]/div/div/div[3]/div/form/button')
        signButton.click()
        cls.driver.implicitly_wait(2)

        acc_info = cls.driver.find_element(By.ID, "first_name")
        if acc_info.is_displayed():
            print("Now, we can fill out the complete details--")

    def test_d_details(cls):
        # cls.test_c_signed_up()
        radio = cls.driver.find_element(By.ID, "uniform-id_gender1")
        radio.click()

        passw = cls.driver.find_element(By.ID, "password")
        passw.send_keys("Zx2M5nQ@aZP")

        dd1 = Select (cls.driver.find_element(By.ID,"days"))
        dd1.select_by_visible_text("25")
        dd2 = Select (cls.driver.find_element(By.ID,"months"))
        dd2.select_by_visible_text("November")
        dd3 = Select (cls.driver.find_element(By.ID,"years"))
        dd3.select_by_visible_text("2003")
        
        print("Personal info filled!")

    def test_e_accountDetails(cls):
        checkbox = cls.driver.find_element(By.ID, "newsletter") 
        checkbox.click()

        fn = cls.driver.find_element(By.ID, "first_name") 
        fn.send_keys("naman")

        ln = cls.driver.find_element(By.ID, "last_name") 
        ln.send_keys("jain")

        comp = cls.driver.find_element(By.ID, "company") 
        comp.send_keys("HCL")

        add1 = cls.driver.find_element(By.ID, "address1")
        add1.send_keys("Hcl it city")

        add2 = cls.driver.find_element(By.ID, "address2") 
        add2.send_keys("Sultanpur Road")

        state = cls.driver.find_element(By.ID, "state") 
        state.send_keys("UP")

        city = cls.driver.find_element(By.ID, "city")
        city.send_keys("Lucknow")

        zipc = cls.driver.find_element(By.ID, "zipcode")
        zipc.send_keys("226002")

        mob = cls.driver.find_element(By.ID, "mobile_number")
        mob.send_keys("9889298892")

        createacc = cls.driver.find_element(By.XPATH, '//*[@id="form"]/div/div/div/div[1]/form/button')
        createacc.click()

        # cls.driver.implicitly_wait(2)
        wait4 = WebDriverWait(cls.driver, 5)
        created = cls.driver.find_element(By.XPATH, '//*[@id="form"]/div/div/div/div/a')
        # cls.driver.implicitly_wait(2)
        if created.is_displayed():
            print("Account Created Successfully!")
        created.click()


    def test_f_checkloggedin(cls):
        wait3 = WebDriverWait(cls.driver, 5)
        loggedin = cls.driver.find_element(By.XPATH, '//*[@id="header"]/div/div/div/div[2]/div/ul/li[10]/a')
        if loggedin.is_displayed():
            print("User is logged in")

    def test_g_deleteacc(cls):
        trash = cls.driver.find_element(By.XPATH, '//*[@id="header"]/div/div/div/div[2]/div/ul/li[5]/a')
        cls.driver.implicitly_wait(1)
        trash.click()

        wait5 = WebDriverWait(cls.driver, 5)
        deletedCnf = cls.driver.find_element(By.XPATH, '//*[@id="form"]/div/div/div/div/a')
        if deletedCnf.is_displayed():
            print("ACCOUNT SUCCESSFULLY DELETED!!")
        deletedCnf.click()

    @classmethod   
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()
