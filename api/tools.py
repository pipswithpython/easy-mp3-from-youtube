import pytube
import webbrowser
import yt_dlp

class Video:

    def __init__(self, url):
        self.url = url
        self.yt = pytube.YouTube(url)

    def title(self):
        return self.yt.title
    
    def author(self):
        return self.yt.author
    
    def date(self):
        return self.yt.publish_date

    def views(self):
        return self.yt.views

    def thumbnail(self):
        return self.yt.thumbnail_url
    
    def download(self):
        title = self.title()
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': title+'.mp3',
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([self.url])
            pass
    
    def moneTagAds():
        url = 'https://groognub.net/4/7920277'
        return webbrowser.open_new_tab(url)