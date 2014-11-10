#! /usr/bin/coffee

request = require 'request'
exec = require('child_process').exec
async = require 'async'

console.log 'Client: Updating!'
async.parallel [
  (cb)->require('getmac').getMac (err,macAddress)->cb null, macAddress
  (cb)->exec "sudo dumpe2fs -b /dev/sda3",(a,badblocks)->cb null, badblocks||new Error('Something went wrong!')
  (cb)->exec "uptime",(a,uptime)->cb null, uptime.split(',')[0].split('up ')[1]
  (cb)->exec "last",(a,lastBoot)->cb null, lastBoot.split('system boot')[lastBoot.split('system boot').length-1].split('    ')[1].split('(')[0]
], (e, results)->
  console.log results
  request.post
    method:'post'
    url:'http://localhost:4000'
    json:true
    body:
      mac:results[0]
      badBlocks:results[1]
      uptime:results[2]
      lastBoot:results[3]

