cd C:\Users\andre\GitHub\Daily-Coding-Problem\Automation
@echo off
set day=0
echo >"%temp%\%~n0.vbs" s=DateAdd("d",%day%,now) : d=weekday(s)
echo>>"%temp%\%~n0.vbs" WScript.Echo year(s)^& right(100+month(s),2)^& right(100+day(s),2)
for /f %%a in ('cscript /nologo "%temp%\%~n0.vbs"') do set "result=%%a"
 del "%temp%\%~n0.vbs"
 set "YYYY=%result:~0,4%"
 set "MM=%result:~4,2%"
 set "DD=%result:~6,2%"
 set "result=%yyyy%-%mm%-%dd%"
python automation.py %result%
cd C:\Users\andre\GitHub\Daily-Coding-Problem\%result%
type NUL > ASSIGNMENT.md
type NUL > NOTES.md
cd C:\Users\andre\GitHub\Daily-Coding-Problem\Automation
python automation2.py %result%
cd C:\Users\andre\GitHub\Daily-Coding-Problem\%result%
code-insiders .