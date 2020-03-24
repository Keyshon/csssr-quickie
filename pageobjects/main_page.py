class MainPage:
    default_url = "http://blog.csssr.ru/qa-engineer/"

    graph_header_blocks = {
        "details": "//div[contains(@class,'graphs-details')]/a",
        "imperfections": "//div[contains(@class,'graphs-errors')]/a",
        "maintenance": "//div[contains(@class,'graphs-support')]/a",
        "files": "//div[contains(@class,'graphs-files')]/a",
    }
    graph_content_blocks = {
        "details": "//div[contains(@class,'info-details')]",
        "imperfections": "//div[contains(@class,'info-errors')]",
        "maintenance": "//div[contains(@class,'info-support')]",
        "files": "//div[contains(@class,'info-files')]",
    }
    graph_header_active = "//div[contains(@class,'graph-active')]/a"
