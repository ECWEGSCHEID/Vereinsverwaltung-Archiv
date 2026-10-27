from playwright.sync_api import sync_playwright
from http.server import ThreadingHTTPServer,SimpleHTTPRequestHandler
import threading,os,time
os.chdir('/mnt/data/dko_v26_build')
class Handler(SimpleHTTPRequestHandler):
 def log_message(self,*args):pass
server=ThreadingHTTPServer(('127.0.0.1',18961),Handler)
threading.Thread(target=server.serve_forever,daemon=True).start()
with sync_playwright() as p:
 b=p.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox'])
 page=b.new_page(viewport={'width':1920,'height':1080},accept_downloads=True)
 errors=[]
 page.on('pageerror',lambda e: errors.append(str(e)))
 page.goto('file:///mnt/data/dko_v26_build/doppel-ko.html',wait_until='domcontentloaded',timeout=30000)
 page.wait_for_timeout(1300)
 print('health',page.locator('#dko-js-health').inner_text()[:180]);print('roster',page.locator('#rosterStatus').inner_text()[:180] if page.locator('#rosterStatus').count() else 'n/a')
 print('buttons',page.locator('#create').count(),page.locator('#guestName').count());print('errors',errors[:4])
 print('title',page.title())
 print('candidate count',page.locator('input[type=checkbox]').count())
 page.locator('#example').click();page.locator('#create').click();page.wait_for_timeout(500)
 print('created players',page.locator('#sumPlayers').inner_text(),'matches',page.locator('#sumGames').inner_text(),'errors',errors[:3])
 b.close()
server.shutdown()
