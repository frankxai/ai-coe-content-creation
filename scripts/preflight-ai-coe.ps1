$ErrorActionPreference = 'Stop'
$modules = @(
    'content/ai-coe/front-matter.md',
    'content/ai-coe/main-body.md',
    'content/ai-coe/social-kit.md',
    'content/ai-coe/appendix-role-checklists.md',
    'content/ai-coe/appendix-data-tool-stack.md',
    'content/ai-coe/appendix-vendor-questionnaire.md',
    'content/ai-coe/references.md'
)

foreach ($module in $modules) {
    if (-not (Test-Path $module)) {
        throw "Missing module file: $module"
    }
}

$parts = foreach ($module in $modules) {
    (Get-Content $module -Raw).Trim()
}
$combined = ($parts -join "`n`n")

$issues = @()
if ($combined -notmatch '## Social Amplification Kit') {
    $issues += 'Social Amplification Kit section missing.'
}
if ($combined -notmatch '## Appendix A:') {
    $issues += 'Appendix A section missing.'
}
if ($combined -notmatch '## Appendix B:') {
    $issues += 'Appendix B section missing.'
}
if ($combined -notmatch '## Appendix C:') {
    $issues += 'Appendix C section missing.'
}
if ($combined -match '[^\x00-\x7F]') {
    $issues += 'Found non-ASCII characters; ensure text uses plain ASCII.'
}
if ($combined -match '  LOI') {
    $issues += 'Missing amount before LOI.'
}
for ($i = 1; $i -le 8; $i++) {
    if ($combined -notmatch "\[\^$i\]") {
        $issues += "Reference marker [^$i] not found."
    }
    if ($combined -notmatch "\[\^$i\]:") {
        $issues += "Reference definition [^$i]: not found."
    }
}

if ($issues.Count -gt 0) {
    Write-Host 'Preflight failed:' -ForegroundColor Red
    $issues | ForEach-Object { Write-Host " - $_" -ForegroundColor Red }
    exit 1
}

Write-Host 'Preflight checks passed.' -ForegroundColor Green
