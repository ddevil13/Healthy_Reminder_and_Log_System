@echo off&cls
copy /Y .\res\backup\water.mp3 .\res\ring\water.mp3
copy /Y .\res\backup\eye.mp3 .\res\ring\eye.mp3
copy /Y .\res\backup\physical.mp3 .\res\ring\physical.mp3
if %errorlevel%==1 (cmd /c echo Stoped due to error %errorlevel% && pause) else (echo Processing Further)
python -V
if %errorlevel%==9009 (cmd /c echo Please Connect to Internet First and than run Setup.bat && pause) else (echo Processing Further)
ping -n 1 google.com
if %errorlevel%==1 (cmd /c echo Please Connect to Internet First and than run Setup.bat && pause) else (cmd /c .\res\install\install.bat)