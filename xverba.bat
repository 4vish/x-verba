@echo off
cd /d "%~dp0"
set PYTHONIOENCODING=utf-8
py -m x_verba.cli %*
