import os
import allure
from allure_commons.types import AttachmentType


def add_screenshot(browser):
    png = browser.driver.get_screenshot_as_png()
    allure.attach(body=png, name='screenshot', attachment_type=AttachmentType.PNG, extension='.png')


def add_logs(browser):
    log = "".join(f'{text}\n' for text in browser.driver.get_log(log_type='browser'))
    allure.attach(log, 'browser_logs', AttachmentType.TEXT, '.log')


def add_html(browser):
    html = browser.driver.page_source
    allure.attach(html, 'page_source', AttachmentType.HTML, '.html')


def add_video(browser):
    selenoid_url = os.getenv("SELENOID_URL")
    video_url = f'https://{selenoid_url}/video/{browser.driver.session_id}.mp4'
    html = (
            f"<html><body>"
            f"<video width='100%' height='100%' controls autoplay>"
            f"<source src='{video_url}' type='video/mp4'>"
            f"</video></body></html>"
    )
    allure.attach(html, 'video_url' + browser.driver.session_id, AttachmentType.HTML, '.html')
