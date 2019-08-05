#!/usr/bin/env bash

yes y | bin/elasticsearch-keystore create
echo "https://hooks.slack.com/services/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" | bin/elasticsearch-keystore \
add --stdin xpack.notification.slack.account.monitoring.secure_url
