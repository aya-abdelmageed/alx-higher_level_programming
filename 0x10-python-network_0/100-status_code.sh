#!/bin/bash
# displaying only the status code
curl -o /dev/null -sw "%{http_code}" $1
