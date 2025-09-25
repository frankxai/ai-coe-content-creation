# AI COE Content Workflow

This folder stores the source modules used to assemble ACTIVE/ai-center-of-excellence-blog.md.

## Files
- ront-matter.md - YAML metadata, title, and introductory context.
- main-body.md - The primary article content through the conclusion (no social copy or appendices).
- social-kit.md - LinkedIn posts and the X thread that support the article.
- ppendix-role-checklists.md - Appendix A with role-based checklists.
- ppendix-data-tool-stack.md - Appendix B with data/tool stack upgrades.
- ppendix-vendor-questionnaire.md - Appendix C vendor due-diligence questionnaire.
- eferences.md - Footnote definitions for the full article.

## Assembly
Use scripts\assemble-ai-coe.ps1 to rebuild the publishable article:

`
powershell -ExecutionPolicy Bypass -File scripts/assemble-ai-coe.ps1
`

## Preflight Checks
Run preflight before assembling or committing to ensure the modules are healthy:

`
powershell -ExecutionPolicy Bypass -File scripts/preflight-ai-coe.ps1
`

The preflight verifies required sections exist, checks for non-ASCII characters, and confirms each footnote has a matching definition.

## Workflow Tips
1. Edit the module files instead of the assembled article.
2. Run the preflight script; fix any reported issues.
3. Assemble the final article into ACTIVE/ai-center-of-excellence-blog.md.
4. Review the assembled file, then version control your changes.


