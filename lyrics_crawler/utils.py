from bs4 import BeautifulSoup  # HTML 파싱
from selenium.webdriver.common.by import By  # HTML 요소를 선택(CSS 선택자, 클래스 등으로 요소 찾기)
from selenium.webdriver.support.wait import WebDriverWait  # 특정 조건을 만족할 때까지 기다리기
from selenium.webdriver.support import expected_conditions as EC  # 기다릴 조건을 정의


def close_popup(driver):
    try:
        close_btn = WebDriverWait(driver, 3).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "a._btn_close_1mry4_247"))
        )   # 팝업 닫는 버튼 나올 때까지 대기
        close_btn.click()
    except:
        pass

def load_parsed_page(driver, url):
    driver.get(url)
    close_popup(driver)
    driver.implicitly_wait(3)
    # time.sleep(3)과 같은 랜더링 대기, implicitly_wait은 설정한 시간(초) 안에 로드를 마치면 다음 동작으로 넘어감
    html = driver.page_source
    return BeautifulSoup(html, "html.parser")
