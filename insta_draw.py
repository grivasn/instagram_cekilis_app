import streamlit as st
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import random

def wait_random(min_seconds=2, max_seconds=4):
    time.sleep(random.uniform(min_seconds, max_seconds))

def fetch_instagram_commenters(insta_username, insta_password, reel_url, max_duration=180, max_attempts=15):
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    # options.add_argument('--headless=new')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(options=options)
    driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
    driver.get(reel_url)

    unique_usernames = set()

    try:
        wait_random(5, 10)
        try:
            close_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, '[aria-label="Kapat"]'))
            )
            close_button.click()
            wait_random(1, 2)
        except Exception:
            pass

        login_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//a[normalize-space()="Giriş Yap"]'))
        )
        login_button.click()

        username_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "username")))
        password_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "password")))
        username_input.send_keys(insta_username)
        password_input.send_keys(insta_password + Keys.ENTER)
        wait_random(3, 5)

        try:
            not_now_button = WebDriverWait(driver, 15).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "._acan._acap._acas._aj1-._ap30"))
            )
            not_now_button.click()
            wait_random(2, 3)
        except Exception:
            pass

        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located(
                (By.XPATH, "//div[contains(@class, 'x1n2onr6') or @aria-label='Ana sayfa']")
            )
        )

        driver.get(reel_url)
        wait_random()

        try:
            show_comments_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "._acan._acap._acas._aj1-._ap30"))
            )
            show_comments_button.click()
            wait_random(2, 3)
        except Exception:
            pass

        try:
            comments_scroll_area = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'x5yr21d') and contains(@class, 'xw2csxc') and contains(@class, 'x1odjw0f') and contains(@class, 'x1n2onr6')]"))
            )
        except Exception:
            comments_scroll_area = None

        attempts = 0
        last_count = 0
        start_time = time.time()
        progress_text = st.empty()

        while attempts < max_attempts and (time.time() - start_time) < max_duration:
            comment_blocks = driver.find_elements(By.XPATH, "//div[contains(@class, 'x78zum5') and contains(@class, 'x1iyjqo2')]")

            for comment in comment_blocks:
                try:
                    user_element = comment.find_element(By.XPATH, ".//h2 | .//h3 | .//span[contains(@class, '_ap3a')]")
                    user_text = user_element.text.strip()
                    if user_text:
                        unique_usernames.add(user_text)
                except Exception:
                    continue

            if comments_scroll_area:
                driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", comments_scroll_area)
            else:
                driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")

            wait_random(2, 4)
            current_count = len(driver.find_elements(By.XPATH, "//div[contains(@class, 'x78zum5') and contains(@class, 'x1iyjqo2')]"))
            progress_text.info(f"Şu ana kadar {len(unique_usernames)} kullanıcı çekildi...")

            if current_count == last_count:
                attempts += 1
            else:
                attempts = 0
            last_count = current_count

        return sorted(unique_usernames)

    except Exception as e:
        st.error(f"Hata oluştu: {str(e)}")
        return []
    finally:
        driver.quit()

st.set_page_config(page_title="Instagram Çekiliş", layout="centered", page_icon="🎁")

st.markdown("""
    <style>
    .stTextInput>div>div>input {
        border-radius: 10px;
        padding: 10px;
        background-color: #f8f9fa;
    }
    .stButton>button {
        border-radius: 8px;
        background-color: #f4978e;
        color: white;
        font-weight: bold;
        padding: 10px 20px;
    }
    .stDataFrame {
        border-radius: 12px;
        overflow: hidden;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🎁 Instagram Çekiliş App")
st.markdown("Yorum yapan kullanıcıları çekip rastgele kazanan veya kazananları belirleyin.")

with st.form("insta_form"):
    reel_url = st.text_input("Reels Linki", placeholder="https://www.instagram.com/reel/...", key="reel")
    insta_username = st.text_input("Instagram Kullanıcı Adı", placeholder="kullaniciadi")
    insta_password = st.text_input("Instagram Şifre", type="password", placeholder="şifre")
    submit = st.form_submit_button("Yorumcuları Çek")

if submit:
    if not (reel_url and insta_username and insta_password):
        st.warning("Lütfen tüm alanları doldurun.")
    else:
        with st.spinner("Yorumlar çekiliyor..."):
            commenters = fetch_instagram_commenters(insta_username, insta_password, reel_url)
            if commenters:
                st.success(f"{len(commenters)} kullanıcı bulundu!")
                st.session_state["commenters"] = commenters
            else:
                st.error("Kullanıcı bulunamadı.")

if "commenters" in st.session_state:
    commenters = st.session_state["commenters"]
    st.subheader("📋 Kullanıcı Listesi")
    st.dataframe({"Kullanıcı Adı": commenters})

    st.markdown("---")
    st.subheader("🎲 Çekiliş")
    winner_count = st.slider("Kazanan Sayısı", 1, min(10, len(commenters)), 1)
    if st.button("Kazananları Belirle"):
        winners = random.sample(commenters, winner_count)
        st.session_state["winners"] = winners
        st.balloons()

if "winners" in st.session_state:
    st.subheader("🏆 Kazananlar")
    for i, winner in enumerate(st.session_state["winners"], 1):
        st.success(f"{i}. @{winner}")
