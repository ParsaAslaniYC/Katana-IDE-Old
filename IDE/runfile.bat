@echo off
echo.
echo.
echo.
echo.
for /f "delims=" %%x in (dir.ini) do set directory=%%x

python %directory%
echo.
echo.
