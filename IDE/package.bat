@echo off
cd python\python37-32\Scripts\temp\
install.bat
echo code = "%errorlevel%"
timeout /t 10