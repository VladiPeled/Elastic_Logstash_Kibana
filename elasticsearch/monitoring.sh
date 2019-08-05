#!/usr/bin/env bash

yes y | bin/elasticsearch-keystore create
echo SLACK_CHANNEL_HOOK | bin/elasticsearch-keystore \
add --stdin xpack.notification.slack.account.monitoring.secure_url
