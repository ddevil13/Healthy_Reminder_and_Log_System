pip install -r ".\res\install\requirements.txt"
if %errorlevel%==1 start cmd /c "echo Setup Unsuccessfull.requirements.txt file does not exists. && pause
if %errorlevel%==0 start cmd /c "echo Setup Completed Successfully. && pause
