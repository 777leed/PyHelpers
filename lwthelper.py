from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter
import requests
from bs4 import BeautifulSoup
import os
import sys
COLOR_RED = "\033[91m"
COLOR_GREEN = "\033[92m"
COLOR_YELLOW = "\033[93m"
COLOR_BLUE = "\033[94m"
COLOR_MAGENTA = "\033[95m"
COLOR_CYAN = "\033[96m"
COLOR_RESET = "\033[0m"
os.system("cls")
url = input(f"{COLOR_BLUE}INSERT THE URL OF YOUR VIDEO : \n -{COLOR_RESET}")
def VideoWriter(url):
    video_id = url.replace("https://www.youtube.com/watch?v=", "")
    print(f"{COLOR_GREEN}GETTING THE VIDEO ID {video_id}{COLOR_RESET}")
    transcript = YouTubeTranscriptApi.get_transcript(video_id, ['es'])
    print(f"{COLOR_GREEN}GETTING TRANSCRIPT DATA{COLOR_RESET}")
    formatter = TextFormatter()
    text_formatted = formatter.format_transcript(transcript)
    print(f"{COLOR_GREEN}RENDERING TRANSCRIPT TO TEXT FORM{COLOR_RESET}")
    response = requests.get(url)
    print(f"{COLOR_GREEN}REQUESTING YOUTUBE PAGE{COLOR_RESET}")
    html_content = response.text
    soup = BeautifulSoup(html_content, 'html.parser')
    print(f"{COLOR_MAGENTA}PARSING HTML DATA{COLOR_RESET}")
    title = soup.find('title').string.replace("//","")
    title = title.translate({ord(i):None for i in '/\?%*:|”<>'})
    print(f"{COLOR_YELLOW}TITLE FOUND!!{COLOR_RESET}")
    print(f"{COLOR_GREEN}CREATING FILE IN DIRECTORY{COLOR_GREEN}")
    with open("C:\\Users\\hp\\Documents\\Vault\\lwt\\Youtube Transcriptions\\Spanish After Hours\\{}.md".format(title), "w", encoding="utf-8") as f:
        f.write(text_formatted)
    return f"{COLOR_YELLOW}SUCCESS!!!{COLOR_GREEN}"

result = VideoWriter(url)
print(result)

