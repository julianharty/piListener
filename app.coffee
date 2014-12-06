#! /usr/bin/coffee

express = require 'express'
app = express()
app.use require('body-parser').json()
request = require 'request'
db = require('mongojs')('test').collection 'rPiDevices'

app.post '/', (req, res)->
  console.log req.body
  db.insert(req.body)
  res.send 'Data Recieved.'

app.listen 4000
