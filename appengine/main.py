from flask import Flask
from google.cloud import datastore, pubsub

publish_client = pubsub.PublisherClient()

topic = 'projects/gcpaceproject1/topics/visitorinfo'


app = Flask(__name__) 

dsclient = datastore.Client()
def savevisitorinfo(visitor):
  entity = datastore.Entity(key=dsclient.key('visitorinfo'))
  entity.update({
    'visitorname': visitor 
  })
  dsclient.put(entity)


@app.route('/')
def home():
  return '<body bgcolor="#F00"><center><h1>I AM SERVICE1</h1></center></body>'

@app.route('/visitor/<visitor>')
def visitorinfo(visitor):
    savevisitorinfo(visitor)
    bvisitor = visitor.encode("utf-8")
    publish_client.publish(topic, bvisitor)
    return '<body bgcolor="#FFFF00"><center><h1>Hello %s</h1></center></body>' %visitor
   

