# restore_working_github.ps1
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8

$gitConfigPath = "$env:USERPROFILE\.gitconfig"
if (Test-Path $gitConfigPath) {
    Remove-Item $gitConfigPath
    Write-Output ".gitconfig removed"
} else {
    Write-Output ".gitconfig not found"
}

git config --global user.email "you@example.com"
git config --global user.name "Your Name"

$url = "https://github.com"

echo "url=$url" | git credential reject

Write-Output "The script was executed successfully!"

