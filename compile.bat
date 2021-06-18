@echo off
@echo Start Compile

set VERSION=v1_0_0
set APP_NAME=CHcan_main
@rem set ICO_PATH=
set SCRIPT=%APP_NAME%.pyw

set NUITKA_CMD=python -m nuitka
@rem set NUITKA_FLAG=--standalone --follow-imports --remove-output --mingw64 --windows-disable-console --windows-icon-from-ico=%ICO_PATH% --plugin-enable=tk-inter
set NUITKA_FLAG=--standalone --follow-imports --remove-output --mingw64 --windows-disable-console --plugin-enable=tk-inter

set COMPILE_CMD=%NUITKA_CMD% %NUITKA_FLAG% %SCRIPT%

set MOVE_SRC_PATH=libsuv.dll
set MOVE_DEST_PATH=%APP_NAME%.dist
set DEST_PATH=Release\%VERSION%

set COPY_CMD=cp %MOVE_SRC_PATH% %MOVE_DEST_PATH%

set MOVE_CMD=mv %MOVE_DEST_PATH% %DEST_PATH%

%COMPILE_CMD% & %COPY_CMD% & %MOVE_CMD%
