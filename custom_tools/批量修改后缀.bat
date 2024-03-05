@echo off
setlocal

set "source_dir=D:\train_data"
set "target_ext=.txt"

for %%F in ("%source_dir%\*.dump") do (
    ren "%%F" "%%~nF%target_ext%"
)

endlocal