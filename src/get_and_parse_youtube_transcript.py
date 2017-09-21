import os
import sys
import mechanize
from bs4 import BeautifulSoup
import pyperclip # for copying the file to the clipbord (control+c)

br = mechanize.Browser(factory=mechanize.RobustFactory())
br.set_handle_robots(False)
video_address = sys.argv[1] if len(sys.argv) == 2 else 'BHRQEFsAqpc'
youtube_link = 'http://video.google.com/timedtext?lang=en&v='
xml_link = '%s%s' %(youtube_link, video_address)

webpage = br.open(xml_link).read()
soupPage = BeautifulSoup(webpage, "xml")
soup = soupPage.find('transcript').findAll('text')
text_list = [x.string.encode('ascii','ignore').replace("&#39;","'") for x in soup]
text_line = " ".join(text_list).split(".")
pyperclip.copy("\n".join(text_line))

