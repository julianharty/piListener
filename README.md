piListener
==========

For monitoring Pis and their SD Cards


##App.coffee Requires running MongoDB server (run mongod --dbpath db/).


Run client.py from Pi.

Takes 2 parameters:

python client.py <URL of server (no HTTP://)> <isBoot?>

when boot python client.py atslash.com:4000 boot
when not boot python client.py atslash.com:4000
