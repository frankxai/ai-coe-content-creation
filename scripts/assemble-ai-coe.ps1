param(
    [string]$OutputPath = 'ACTIVE/ai-center-of-excellence-blog.md'
)

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

$content = ($parts -join "`n`n") + "`n"
Set-Content -Path $OutputPath -Value $content -NoNewline
Write-Host "Assembled" $OutputPath
