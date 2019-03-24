SET CURDIR=%cd%
SET BASEDIR=%~dp0
REM SET IMAGE_NAME=image_name

REM Set the Image Name from the text file content
for /f %%i in ('type %BASEDIR%\..\ImageName.txt') do set IMAGE_NAME=%%i

echo Building Docker container %IMAGE_NAME%

cd %BASEDIR%\..\..\..
docker build -t %IMAGE_NAME% .
cd %CURDIR%