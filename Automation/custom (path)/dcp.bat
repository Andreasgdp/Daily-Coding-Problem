cd %USERPROFILE%\GitHub\Daily-Coding-Problem\Automation\custom (path)
python automation.py %1
cd %USERPROFILE%\GitHub\Daily-Coding-Problem\%1
type NUL > ASSIGNMENT.md
type NUL > NOTES.md
type NUL > %1.py
cd %USERPROFILE%\GitHub\Daily-Coding-Problem\Automation\custom (path)
python automation2.py %1
cd %USERPROFILE%\GitHub\Daily-Coding-Problem\%1
code-insiders .