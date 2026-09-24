# Remise en etat de la machine apres la nuit de calcul (a lancer quand les calculs sont finis / quand l'utilisateur revient).
# 1. arret du processus anti-veille ; 2. economiseur d'ecran reactive (valeur d'origine : ScreenSaveActive = 1) ;
# 3. conteneurs Docker de nuit supprimes ; 4. .wslconfig d'origine restaure (puis wsl --shutdown) ; 5. la note reste sur le bureau (a supprimer a la main).
$lab = "C:\Users\RESEARCHER\Desktop\c2_experimental"
$pidFile = "$lab\logs\keep_awake_pid.txt"
if (Test-Path $pidFile) {
    $kid = ((Get-Content $pidFile) -replace '[^0-9]', '')
    try { Stop-Process -Id ([int]$kid) -ErrorAction Stop; "anti-veille arrete ($kid)" } catch { "anti-veille deja arrete" }
}
Add-Type -Namespace W2 -Name U -MemberDefinition '[DllImport("user32.dll")] public static extern bool SystemParametersInfo(uint a, uint b, System.IntPtr c, uint d);'
[W2.U]::SystemParametersInfo(0x0011, 1, [IntPtr]::Zero, 3) | Out-Null
"ScreenSaveActive = " + (Get-ItemProperty "HKCU:\Control Panel\Desktop").ScreenSaveActive
docker rm -f night_C night_D 2>$null | Out-Null; "conteneurs de nuit supprimes"
Copy-Item "$lab\logs\wslconfig_original_backup.txt" "$env:USERPROFILE\.wslconfig" -Force; ".wslconfig d'origine restaure (effectif apres : wsl --shutdown)"
