# Proof-grade runs (note 45): native cadical.exe 3.0.1 (C1's static win64 build, sha d0650d6a...) with a DRAT proof, then drat-trim.exe
# (C1's binary-mode patch, sha 2474cb83...); one at a time, Idle priority, 4 CPUs (fits the low mode). Proofs kept in sat\out.
# Log: logs\decl_proofs.log     usage: win_proofs.ps1 -list <file of CNF paths> [-cap seconds]
param([string]$list, [int]$cap = 900)
$lab = "C:\Users\RESEARCHER\Desktop\c2_experimental"; $log = "$lab\logs\decl_proofs.log"
foreach ($cnf in Get-Content $list) {
  if (-not $cnf.Trim()) { continue }
  $name = [IO.Path]::GetFileNameWithoutExtension($cnf); $prf = "$lab\sat\out\$name.drat"; $out = "$lab\sat\out\$name.cadical.out"
  if (Select-String -Path $log -Pattern "^\S+ $name " -Quiet -ErrorAction SilentlyContinue) { continue }
  $sha = (Get-FileHash $cnf -Algorithm SHA256).Hash.Substring(0,16).ToLower()
  $t0 = Get-Date
  $p = Start-Process -FilePath "$lab\tools\win64\cadical.exe" -ArgumentList '-q', "`"$cnf`"", "`"$prf`"" -RedirectStandardOutput $out -WindowStyle Hidden -PassThru
  $null = $p.Handle; Start-Sleep -Milliseconds 300; try { $p.PriorityClass = 'Idle'; $p.ProcessorAffinity = [IntPtr]0xF000 } catch {}
  if (-not $p.WaitForExit($cap * 1000)) { Stop-Process -Id $p.Id -Force; $p.WaitForExit(); $st = 'UNKNOWN'; $rc = 'cap' } else { $rc = $p.ExitCode; $st = if ($rc -eq 20) { 'UNSAT' } elseif ($rc -eq 10) { 'SAT' } else { 'rc' + $rc } }
  $secs = [int]((Get-Date) - $t0).TotalSeconds; $ver = ''; $pkb = 0
  if ($st -eq 'UNSAT') {
    $pkb = [int]((Get-Item $prf).Length / 1KB); $t1 = Get-Date
    $d = Start-Process -FilePath "$lab\tools\win64\drat-trim.exe" -ArgumentList "`"$cnf`"", "`"$prf`"", '-t', '200000' -RedirectStandardOutput "$out.drattrim" -WindowStyle Hidden -PassThru
    $null = $d.Handle; Start-Sleep -Milliseconds 300; try { $d.PriorityClass = 'Idle'; $d.ProcessorAffinity = [IntPtr]0xF000 } catch {}
    $d.WaitForExit(); $ver = (Select-String -Path "$out.drattrim" -Pattern '^s (VERIFIED|NOT VERIFIED)' | Select-Object -First 1).Line
    $ver = "$ver ($([int]((Get-Date) - $t1).TotalSeconds) s)"
  }
  Add-Content -Path $log -Value ("{0} {1} {2} {3}s cnf_sha {4} proof {5} KB {6}" -f (Get-Date -Format s), $name, $st, $secs, $sha, $pkb, $ver)
}
Add-Content -Path $log -Value ("{0} LIST DONE {1}" -f (Get-Date -Format s), $list)
