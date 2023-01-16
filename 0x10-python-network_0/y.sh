#!/usr/bin/env bash

echo $(curl -Is www.google.com | grep "X-XSS-Protection" head | cut -d ':' -f 2 | tr -d ' \r')
