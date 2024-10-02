import webbrowser as wb

def workauto():
    Chrome_path = 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe %s'
    URLS = ("google.com",
            "yahoo.com",
            "github.com/Eswari123-cloud",
            "youtube.com",
            "gmail.com")
    for url in URLS:
        wb.get(Chrome_path).open(url)


    workauto()    

            
