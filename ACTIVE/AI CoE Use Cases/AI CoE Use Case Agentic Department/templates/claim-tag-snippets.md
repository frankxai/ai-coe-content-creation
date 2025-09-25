# Claim Tag Snippets Template
# Use these XML tags to annotate claims in content drafts for validation

## Basic Claim Tag
<claim id="c1">
  <text>Claim text here</text>
  <source href="https://example.com" date="2024-01-01" type="oracle-doc"/>
  <confidence>high</confidence>
  <qualification>Optional qualification text</qualification>
</claim>

## Examples by Confidence Level

### High Confidence (Oracle Doc)
<claim id="c1">
  <text>OCI Generative AI Service supports model hosting and fine-tuning.</text>
  <source href="https://docs.oracle.com/en-us/iaas/GenerativeAI/index.html" date="2024-06-01" type="oracle-doc"/>
  <confidence>high</confidence>
</claim>

### Medium Confidence (POC)
<claim id="c2">
  <text>Significant speedups observed in genomic processing workflows on OCI.</text>
  <source href="internal-poc-genetics-2024" date="2024-09-15" type="internal-POC"/>
  <confidence>medium</confidence>
  <qualification>Results vary by workload, data size, and optimization level.</qualification>
</claim>

### Low Confidence (Expert Opinion)
<claim id="c3">
  <text>AI-driven genomics could reduce drug discovery timelines by years.</text>
  <source href="https://www.nature.com/articles/s41587-023-01735-6" date="2023-04-01" type="peer-reviewed"/>
  <confidence>low</confidence>
  <qualification>Based on industry trends; actual outcomes depend on implementation and regulatory factors.</qualification>
</claim>

## Usage in Content
Insert tags inline with text for easy scanning:

Genomic data processing can see <claim id="c1"><text>significant speedups</text><source href="internal-poc" type="internal-POC"/><confidence>medium</confidence><qualification>varies by workload</qualification></claim> when migrating to OCI.

## Validation Workflow
1. Generator inserts tags in drafts
2. Validator scans tags, verifies sources
3. Updates confidence/qualification as needed
4. Removes tags from final published content
