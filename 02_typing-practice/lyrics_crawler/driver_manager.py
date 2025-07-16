from selenium import webdriver # 동적 웹사이트 다뤄야.. 브라우저 자동화 도구

def create_driver(headless=True):
    # 실제 구글 창이 뜸, 창 숨기는 옵션 추가
    options = webdriver.ChromeOptions()
    if headless:
        options.add_argument("headless")
        options.add_argument("--disable-gpu")

    # Chrome 웹드라이버 실행
    driver = webdriver.Chrome(options=options)
    return driver

def close_driver(driver):
    driver.quit()