./4-header.sh 0.0.0.0:5000/route_5 ; echo ""#!/bin/bash
# script that takes in a URL as an argument, sends a GET request to the URL, and displays the body of the response
curl -s "$1" -H "X-School-User-Id: 98"
