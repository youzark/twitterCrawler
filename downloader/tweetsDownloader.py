from multiprocessing import Queue,Pool
from picDownloader import picDownloader
import multiprocessing



def tweetDownloadFromArticalSessions(articleSessionQueue):
    with Pool(4) as ex:
        while True:
            if not articleSessionQueue.empty():
                articleSession = articleSessionQueue.get()
                ex.apply_async(func=downloadArticalSession,args=(articleSession))
            else:
                finishFlag = finishFlagQueue.get()
                if finishFlag:
                    break

def downloadArticalSession(articleSession):
    print("start downloading")
