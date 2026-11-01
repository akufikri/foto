#!/usr/bin/env bash
# Lihat hit terbaru dari halaman bait.
set -u
TOKEN=${WEBHOOK_TOKEN:-a417e438-7807-402b-b8b0-14c0e8888897}
curl -sS "https://webhook.site/token/$TOKEN/requests?sorting=newest" | python3 "$(dirname "$0")/hits.py"
