#-*- coding:utf-8 -*-
from lightning import LightningRpc
import http.server
import io,shutil,urllib
import random
class RequestHandler(http.server.BaseHTTPRequestHandler):

		 Page = '''\
				 <html>
				 <body>
				 <p> Hello,web!</p>
				 </body>
				 </html>
		 '''
		 p = '2124'
		 #处理一个请求
		 def do_GET(self):

				 self.queryString = urllib.parse.unquote(self.path.split('?',1)[1])
				 params = urllib.parse.parse_qs(self.queryString)
				 print(params)
				 method = params["method"][0]
				 passwd = params["passwd"][0]
				 ##调用plightning
				 if (method == 'listinvoices' and passwd == '2124'):
				      lrpc = LightningRpc("/root/.lightning/lightning-rpc")
				      info5 = str(lrpc.getinfo())
				      print(' getinfo:'+info5)
				 elif (method == 'invoice' and passwd == '2124'):
				      bmount = params["bmount"][0]
				      content = params["content"][0]
				      lrpc = LightningRpc("/root/.lightning/lightning-rpc")
				      info5 = lrpc.invoice(bmount, "lbl{}".format(random.random()),content)
				      info5 = str(info5)
				      print(info5)
				 elif (method == 'decodepay' and passwd == '2124'):
				      bolt11 = params["bolt11"][0]
				      lrpc = LightningRpc("/root/.lightning/lightning-rpc")
				      info5 = lrpc.decodepay(bolt11)
				      info5 = str(info5)
				      print(info5)
				 elif (method == 'listpeers' and passwd == '2124'):
				      lrpc = LightningRpc("/root/.lightning/lightning-rpc")
				      info5 = lrpc.listpeers()
				      info5 = str(info5)
				      print(info5)
				 self.send_response(200)
				 self.send_header("Content-Type","text/html")
				 self.send_header("Content-Length",str(len(info5)))
				 self.end_headers()
				 self.wfile.write(info5.encode())
 

if __name__ == '__main__':

      serverAddress = ('', 9100)
      server = http.server.HTTPServer(serverAddress, RequestHandler)
      server.serve_forever()