#!/bin/sh
set -e
GRUNT=$(which grunt)
NPM=$(which npm)
$NPM install
$GRUNT build
