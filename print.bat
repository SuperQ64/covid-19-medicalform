@REM ACRRD_PATH = "C:\Program Files (x86)\Adobe\Acrobat Reader DC\Reader\AcroRd32.exe"
@REM PDF_PATH = %~dp0/out/%1  PRINTER_NAME = %2   DRIVER_NAME = %3    PORT_NAME = %4

start "" "C:\Program Files (x86)\Adobe\Acrobat Reader DC\Reader\AcroRd32.exe" /t %~dp0/out/%1 %2 %3 %4
timeout /t 10
taskkill /F /IM AcroRd32.exe