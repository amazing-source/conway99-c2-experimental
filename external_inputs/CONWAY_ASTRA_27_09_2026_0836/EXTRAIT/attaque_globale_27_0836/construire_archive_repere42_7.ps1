$ErrorActionPreference = 'Stop'
Add-Type -AssemblyName System.IO.Compression
Add-Type -AssemblyName System.IO.Compression.FileSystem
$campaignCurrent = (Resolve-Path -LiteralPath $PSScriptRoot).Path
$outputRoot = Split-Path -Parent $campaignCurrent
$campaignPrior = Join-Path $outputRoot 'attaque_globale_27_0803'
$archiveTarget = Join-Path $outputRoot 'ATTAQUE_DIRECTE_27_0836_PREUVES_CERTIFICATS.zip'
$manifestTarget = Join-Path $campaignCurrent 'MANIFESTE_REPERE42_7.json'
$manifest = Get-Content -LiteralPath $manifestTarget -Raw -Encoding UTF8 | ConvertFrom-Json
$expected = @{}
foreach ($item in $manifest.files) { $expected[$item.path] = $item.sha256 }
$manifestHash = (Get-FileHash -LiteralPath $manifestTarget -Algorithm SHA256).Hash.ToLowerInvariant()
$expected['attaque_globale_27_0836/MANIFESTE_REPERE42_7.json'] = $manifestHash
$archiveStream = [System.IO.File]::Open($archiveTarget,[System.IO.FileMode]::Create,[System.IO.FileAccess]::Write)
$zip = [System.IO.Compression.ZipArchive]::new($archiveStream,[System.IO.Compression.ZipArchiveMode]::Create,$false)
try {
 foreach ($sourceFolder in @($campaignCurrent,$campaignPrior)) {
  $folderName = Split-Path -Leaf $sourceFolder
  foreach ($sourceFile in (Get-ChildItem -LiteralPath $sourceFolder -File | Sort-Object Name)) {
   if ($sourceFile.Extension -eq '.zip') { continue }
   $entryName = $folderName + '/' + $sourceFile.Name
   if (-not $expected.ContainsKey($entryName)) { throw ('Unmanifested input: '+$entryName) }
   $entry = $zip.CreateEntry($entryName,[System.IO.Compression.CompressionLevel]::Optimal)
   $dst = $entry.Open()
   $src = [System.IO.File]::OpenRead($sourceFile.FullName)
   try { $src.CopyTo($dst) } finally { $src.Dispose(); $dst.Dispose() }
  }
 }
} finally { $zip.Dispose(); $archiveStream.Dispose() }
$checkZip = [System.IO.Compression.ZipFile]::OpenRead($archiveTarget)
$checked = 0
$seen = @{}
try {
 foreach ($entry in $checkZip.Entries) {
  if ($seen.ContainsKey($entry.FullName)) { throw ('Duplicate entry: '+$entry.FullName) }
  $seen[$entry.FullName] = $true
  if (-not $expected.ContainsKey($entry.FullName)) { throw ('Unexpected entry: '+$entry.FullName) }
  $hashTool = [System.Security.Cryptography.SHA256]::Create()
  $stream = $entry.Open()
  try { $digest=[System.BitConverter]::ToString($hashTool.ComputeHash($stream)).Replace('-','').ToLowerInvariant() }
  finally { $stream.Dispose(); $hashTool.Dispose() }
  if ($digest -ne $expected[$entry.FullName]) { throw ('Hash mismatch: '+$entry.FullName) }
  $checked++
 }
} finally { $checkZip.Dispose() }
if ($checked -ne $expected.Count) { throw 'Entry count mismatch' }
$zipHash=(Get-FileHash -LiteralPath $archiveTarget -Algorithm SHA256).Hash.ToLowerInvariant()
$audit=[ordered]@{exact=$true;archive=(Split-Path -Leaf $archiveTarget);bytes=(Get-Item -LiteralPath $archiveTarget).Length;entries_checked=$checked;every_entry_sha256_matches=$true;manifest_sha256=$manifestHash;archive_sha256=$zipHash;scope='two complete own-conversation campaigns; no global g18/g20 exclusion'}
$auditPath=$archiveTarget+'.AUDIT.json'
$utf8NoBom=[System.Text.UTF8Encoding]::new($false)
[System.IO.File]::WriteAllText($auditPath,($audit | ConvertTo-Json -Depth 4),$utf8NoBom)
$audit | ConvertTo-Json -Depth 4
