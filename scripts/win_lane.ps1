# Finish-line lane (note 46): for each type id of all_types_3308.json in -ids, export I(tau) (enc2_dimacs.py, given flags, --nolex)
# to a per-lane CNF, solve with cadical.exe (C1's win64 build) with a DRAT proof, check with drat-trim.exe, log one line.
# -highonly: runs only while logs\pc_mode.txt = high (a run interrupted by low mode is killed and retried later).
# usage: win_lane.ps1 -ids <file> -lane <name> -flags "<enc2 flags>" [-cap s] [-noproof] [-highonly]    log: logs\finish_A.log
param([string]$ids, [string]$lane, [string]$flags, [int]$cap = 3600, [switch]$noproof, [switch]$highonly, [string]$logname = 'finish_A.log')
$lab = "C:\Users\RESEARCHER\Desktop\c2_experimental"; $log = "$lab\logs\$logname"; $py = "$lab\.venv\Scripts\python.exe"
$tdir = "$lab\scripts\c1_tiers"; $types = "$lab\scripts\structures\all_types_3308.json"
$cnf = "$lab\sat\lane\$lane.cnf"; $prf = "$lab\sat\lane\$($lane)_ID.drat"; $out = "$lab\sat\lane\$lane.out"
New-Item -ItemType Directory -Force "$lab\sat\lane" | Out-Null; if (-not (Test-Path $log)) { New-Item -ItemType File -Path $log | Out-Null }
$piv = @{}; foreach ($t in (Get-Content $types -Raw | ConvertFrom-Json)) { $piv[[int]$t.id] = [int]$t.pivots }
$tag = ($flags -replace '\s+', '')
function Mode { try { (Get-Content "$lab\logs\pc_mode.txt" -Raw).Trim() } catch { 'low' } }
foreach ($line in Get-Content $ids) {
  if (-not $line.Trim()) { continue }; $id = [int]$line.Trim()
  if (Select-String -Path $log -Pattern "^\S+ \S+ id $id [^ ]+ $([regex]::Escape($tag)) " -Quiet -ErrorAction SilentlyContinue) { continue }
  while ($true) {
    if ($highonly) { while ((Mode) -ne 'high') { Start-Sleep -Seconds 30 } }
    $env:SAT_LOCAL_DIR = "..\structures"
    $e = Start-Process -FilePath $py -ArgumentList (@("enc2_dimacs.py", "`"$types`"", "$id", "`"$lab\sat\lane`"") + ($flags -split '\s+') + @("--nolex", "--out=`"$cnf`"")) -WorkingDirectory $tdir -WindowStyle Hidden -PassThru -Wait
    $sha = (Get-FileHash $cnf -Algorithm SHA256).Hash.Substring(0,16).ToLower(); $t0 = Get-Date
    $prf = $prf.Replace("_ID.drat", "_$id.drat")
    $cargs = if ($noproof) { @('-q', "`"$cnf`"") } else { @('-q', "`"$cnf`"", "`"$prf`"") }
    $p = Start-Process -FilePath "$lab\tools\win64\cadical.exe" -ArgumentList $cargs -RedirectStandardOutput $out -WindowStyle Hidden -PassThru
    $null = $p.Handle; Start-Sleep -Milliseconds 300; try { $p.PriorityClass = 'Idle'; $p.ProcessorAffinity = [IntPtr]$(if ($highonly) { 0xFFF0 } else { 0xF000 }) } catch {}
    $interrupted = $false
    while (-not $p.HasExited) {
      Start-Sleep -Seconds 5
      if ($highonly -and (Mode) -ne 'high') { Stop-Process -Id $p.Id -Force; $interrupted = $true; break }
      if (((Get-Date) - $t0).TotalSeconds -gt $cap) { Stop-Process -Id $p.Id -Force; break }
    }
    $p.WaitForExit(); if ($interrupted) { continue }
    $rc = $p.ExitCode; $st = if ($rc -eq 20) { 'UNSAT' } elseif ($rc -eq 10) { 'SAT' } elseif (((Get-Date) - $t0).TotalSeconds -ge $cap) { 'UNKNOWN' } else { 'rc' + $rc }
    $secs = [int]((Get-Date) - $t0).TotalSeconds; $ver = ''; $pkb = 0
    if ($st -eq 'UNSAT' -and -not $noproof) {
      $pkb = [int]((Get-Item $prf).Length / 1KB); $t1 = Get-Date
      $d = Start-Process -FilePath "$lab\tools\win64\drat-trim.exe" -ArgumentList "`"$cnf`"", "`"$prf`"", '-t', '200000' -RedirectStandardOutput "$out.drattrim" -WindowStyle Hidden -PassThru
      $null = $d.Handle; Start-Sleep -Milliseconds 300; try { $d.PriorityClass = 'Idle' } catch {}
      $d.WaitForExit(); $ver = (Select-String -Path "$out.drattrim" -Pattern '^s (VERIFIED|NOT VERIFIED)' | Select-Object -First 1).Line
      $ver = "$ver ($([int]((Get-Date) - $t1).TotalSeconds) s)"
    }
    if ($st -eq 'SAT') { Copy-Item $out "$lab\sat\lane\SAT_$($lane)_$id.out"; Copy-Item $cnf "$lab\sat\lane\SAT_$($lane)_$id.cnf" }
    Add-Content -Path $log -Value ("{0} {1} id {2} piv{3} {4} {5} {6}s cnf_sha {7} proof {8} KB {9}" -f (Get-Date -Format s), $lane, $id, $piv[$id], $tag, $st, $secs, $sha, $pkb, $ver)
    break
  }
}
Add-Content -Path $log -Value ("{0} {1} LIST DONE {2}" -f (Get-Date -Format s), $lane, $ids)

