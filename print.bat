set ACRRD_PATH="C:\Program Files (x86)\Adobe\Acrobat Reader DC\Reader\AcroRd32.exe"
set PDF_PATH=%1

start "" "AcroRd32.exe"

@REM timeout /t 2

%ACRRD_PATH% /p %PDF_PATH%

taskkill /F /IM AcroRd32.exe