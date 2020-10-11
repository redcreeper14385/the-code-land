#!/bin/bash
CURRENT=$(df / | grep / | awk '{ print $5}' | sed 's/%//g')
THRESHOLD=5
SUBJECT="Storage Alert For YOUR Server"
MESSAGE="Storage is runnig low. Current Storage is ${CURRENT}"


if [ "$CURRENT" -gt "$THRESHOLD" ] ; then
	python3 send_email.py "admin@somedomain.com" "user@somedomian.com" "${SUBJECT}"  "${MESSAGE}"
fi
