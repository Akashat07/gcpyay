from google.appengine.ext import webapp
from google.appengine.ext.webapp import util
class MainHandler(webapp.RequestHandler):
 def get(self):
 self.response.out.write('SatShriAkal! Himanshu Pra \n Tuhadi UID hai -
21BCS3138 ')
def main():
 application = webapp.WSGIApplication([('/', MainHandler)],
 debug=True)
 util.run_wsgi_app(application)
if __name__ == '__main__':
 main()
