# Notes

1.  The function ```scheduler()``` takes a ```functionName``` and an integer as the time in milliseconds. The ```functionName``` needs to be a string, because that is how it later calls the function.

2.  The function ```eval()``` is used to convert the string into executable code, where the name of the function is used, to call the function.

3.  This code cannot call a function, that has parameters, only functions with nothing inside the parentesis ```()```