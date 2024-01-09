; CleanDesktop.ahk

; Set the interval in milliseconds (1 hour = 3600000 milliseconds)
interval := 3600000

; Function to clean up the desktop
CleanDesktop() {
    ; Specify the path to your desktop
    desktopPath := "C:\Users\YourUsername\Desktop"

    ; List of file extensions to keep (add more if needed)
    keepExtensions := "*.lnk|*.txt|*.pdf|*.docx"

    ; Loop through files on the desktop
    Loop, Files, %desktopPath%\*.*, D
    {
        ; Check if the file extension is not in the keepExtensions list
        if not InStr(keepExtensions, A_LoopFileExt)
        {
            ; Delete the file
            FileDelete, %A_LoopFileFullPath%
        }
    }
}

; Set a timer to run CleanDesktop() every hour
SetTimer, CleanDesktop, %interval%

; Exit script when the user closes it
OnExit, ExitScript
ExitScript:
    ExitApp