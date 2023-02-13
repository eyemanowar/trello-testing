from browsermobproxy import Server
import pytest
from src.page_helpers.board_page import BoardPage
import pdb
import json
from selenium import webdriver
import time


@pytest.mark.tcid_alt
def test_alt():
    # make chrome log requests
    server = Server("/Users/user/Documents/browsermob-proxy-2.1.4/bin/browsermob-proxy")
    server.start()
    proxy = server.create_proxy(params={"trustAllServers": "true"})
    proxy_address = "--proxy=127.0.0.1:%s" % proxy.port
    service_args = [proxy_address, '--ignore-ssl-errors=yes', ]

    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument("--ignore-certificate-errors")
    options.add_argument("--proxy-server={0}".format(proxy.proxy))

    driver = webdriver.Chrome(options=options)
    proxy.new_har("https://trello.com/w/apitest88")

    page = BoardPage(driver)
    page.go('https://trello.com/w/apitest88')
    time.sleep(5)

    with open("/Users/user/Downloads/trello.com.har", "w", encoding="utf-8") as f:
        f.write(json.dumps(proxy.har))

    print("Quitting Selenium WebDriver")
    driver.quit()

    pdb.set_trace()
    har_file_path = "network_log1.har"
    with open('/Users/user/Downloads/trello.com.har', "r", encoding="utf-8") as f:
        logs = json.loads(f.read())

    # Store the network logs from 'entries' key and
    # iterate them
    network_logs = logs['log']['entries']
    for log in network_logs:

        # Except block will be accessed if any of the
        # following keys are missing
        try:
            # URL is present inside the following keys
            url = log['request']['url']

            # Checks if the extension is .png or .jpg
            if url[len(url) - 4:] == '.png' or url[len(url) - 4:] == '.jpg':
                print(url, end="\n\n")
        except Exception as e:
            # print(e)
            pass
