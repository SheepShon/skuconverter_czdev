#NoEnv
SendMode Input
SetWorkingDir %A_ScriptDir%

^::
Loop, 10
{
    Send {F2}
    sleep 50
    Send ^A
    sleep 50
    Send ^c
    sleep 50
    Send +
    sleep 50
    Send ^v
    sleep 50
    Send {Down}
    Sleep 100
}