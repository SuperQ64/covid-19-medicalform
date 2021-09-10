set ACRRD_PATH="C:\Program Files (x86)\Adobe\Acrobat Reader DC\Reader\AcroRd32.exe"
set PDF_PATH=%~dp0/out/%1
set PRINTER=%2
set DRIVER=%3
set PORT=%4

start "" %ACRRD_PATH% /t %PDF_PATH% %PRINTER% %DRIVER% %PORT%

timeout /t 10

taskkill /F /IM AcroRd32.exe