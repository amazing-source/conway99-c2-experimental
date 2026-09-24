Add-Type -Namespace W -Name P -MemberDefinition '[DllImport("kernel32.dll")] public static extern uint SetThreadExecutionState(uint f);'
# ES_CONTINUOUS | ES_SYSTEM_REQUIRED | ES_DISPLAY_REQUIRED : ni veille, ni extinction d'ecran, tant que ce processus vit
while ($true) { [W.P]::SetThreadExecutionState(0x80000003) | Out-Null; Start-Sleep -Seconds 50 }
