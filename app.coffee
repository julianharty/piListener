#! /usr/bin/coffee

express = require 'express'
app = express()
app.use require('body-parser').json()
request = require 'request'
#db = require('mongojs')('test').collection 'rPiDevices'


app.get '/', (req,res)->
  @foo = []
  db.distinct 'mac',(e,macs)->
    macs.map (value,index)->
      db.find mac:value, (e,data)->
        @foo.push data[data.length-1]
        if @foo.length>=macs.length then res.send @foo


app.post '/old', (req,res)->
  db.find mac:req.body.mac, (e,data)->
    console.log 'Someone is updating!',req.body
    tmp = req.body
    tmp.count = data.length
    db.insert tmp
    res.send 'Done!'

app.post '/', (req, res)->
  console.log req.body
  res.send 'Whoo!'

app.listen 4000
