@echo off
set dir=%1
title Katana Virtual Enviroment Maker
color F0
if %ERRORLEVEL% LSS 0 GOTO begin
:begin
	echo creating Virtual Enviroment in %dir% 
	echo.
	echo.
	python -m venv %dir%
	echo.
	echo.
	echo Completed!
	exit
:error
	echo Syntax Error!
	echo Katana Virtual Enviroment Maker v0.1_public_beta
	echo Command's:
	echo.
	echo 	'"a Directory to create into"'
	echo.
	echo example:
	echo.
	echo	create_venv.bat C:\myApp\
	echo.
	pause