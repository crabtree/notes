# Batch

## Generate numbers sequence

```batch
@ECHO OFF

set /a start=0
set /a end=100

for /l %%x in (%start%,1,%end%) do (
   echo %%x
)
```
