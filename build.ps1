$exclude = @("venv", "NotepadAutomation.zip")
$files = Get-ChildItem -Path . -Exclude $exclude
Compress-Archive -Path $files -DestinationPath "NotepadAutomation.zip" -Force