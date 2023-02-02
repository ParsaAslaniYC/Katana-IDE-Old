@echo off
cls
echo.

echo Seemon Team, All Right's Reserved {2023}
echo Katana IDE alphaRelease Console
set restart=console
:first
echo.
echo \_________(%cd%)_________/
set /p command="_($)_ : "
echo.
%command%
echo.
goto first