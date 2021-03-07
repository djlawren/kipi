#!/bin/bash

gunicorn -w 1 kipi:create_app
