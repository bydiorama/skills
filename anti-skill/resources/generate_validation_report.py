#!/usr/bin/env python3
"""
generate_validation_report.py

Generates a formatted HTML validation report from a JSON findings file.
Usage:
    python generate_validation_report.py <findings.json> [--output <output.html>]

The findings.json should follow this structure:
{
  "context": {
    "output_type": "proposal",
    "declared_intent": "Win the Q3 infrastructure contract",
    "audience": "CTO and procurement team",
    "validation_depth": "Standard",
    "modes_applied": ["Intent Alignment", "Challenger", "Completeness"],
    "caveats": "Clarification round was skipped at user's request."
  },
  "executive_summary": "The proposal clearly articulates the technical solution but...",
  "findings": [
    {
      "title": "Missing cost breakdown",
      "severity": "critical",
      "mode": "Completeness & Gap Analysis",
      "what": "The proposal references 'competitive pricing' but never provides...",
      "why_it_matters": "Decision-makers cannot approve without concrete numbers.",
      "suggestion": "Add a detailed cost table in Section 4 with...",
      "perspectives": ["Decision-Maker", "Implementer"]
    }
  ],
  "strengths": [
    {
      "title": "Strong technical narrative",
      "detail": "The architecture section explains complex concepts accessibly."
    }
  ],
  "perspectives_explored": [
    {
      "name": "Skeptical Expert",
      "summary": "Raised concerns about scalability claims...",
      "notable_disagreements": "Disagrees with Implementer on timeline feasibility."
    }
  ],
  "next_steps": [
    "Add cost breakdown table (Critical finding #1)",
    "Revise scalability claims with concrete benchmarks",
    "Run a second validation pass after revisions"
  ]
}
"""

import json
import sys
import os
from datetime import datetime


def severity_color(severity: str) -> str:
    return {
        "critical": "#dc2626",
        "important": "#d97706",
        "minor": "#2563eb",
    }.get(severity.lower(), "#6b7280")


def severity_bg(severity: str) -> str:
    return {
        "critical": "#fef2f2",
        "important": "#fffbeb",
        "minor": "#eff6ff",
    }.get(severity.lower(), "#f9fafb")


def severity_border(severity: str) -> str:
    return {
        "critical": "#fecaca",
        "important": "#fde68a",
        "minor": "#bfdbfe",
    }.get(severity.lower(), "#e5e7eb")


def severity_icon(severity: str) -> str:
    return {
        "critical": "&#9888;",   # ⚠
        "important": "&#9679;",  # ●
        "minor": "&#9675;",      # ○
    }.get(severity.lower(), "&#8226;")


def generate_html(data: dict) -> str:
    ctx = data.get("context", {})
    findings = data.get("findings", [])
    strengths = data.get("strengths", [])
    perspectives = data.get("perspectives_explored", [])
    next_steps = data.get("next_steps", [])
    exec_summary = data.get("executive_summary", "No summary provided.")
    verified_claims = data.get("verified_claims", [])

    # Group findings by severity
    critical = [f for f in findings if f.get("severity", "").lower() == "critical"]
    important = [f for f in findings if f.get("severity", "").lower() == "important"]
    minor = [f for f in findings if f.get("severity", "").lower() == "minor"]

    # Count stats
    total = len(findings)
    n_verified = len(verified_claims)
    stats_line = (
        f"{len(critical)} critical, {len(important)} important, {len(minor)} minor"
        + (f", {n_verified} verified" if n_verified else "")
    )

    # Build findings HTML
    def render_finding(f, index):
        sev = f.get("severity", "unknown").lower()
        persp = f.get("perspectives", [])
        persp_html = ""
        if persp:
            tags = "".join(
                f'<span style="display:inline-block;background:#e0e7ff;color:#3730a3;'
                f'padding:2px 8px;border-radius:12px;font-size:0.75rem;margin-right:4px;">'
                f'{p}</span>'
                for p in persp
            )
            persp_html = f'<div style="margin-top:8px;">{tags}</div>'

        evidence = f.get("evidence", "")
        evidence_html = (
            f'<div style="margin-bottom:6px;background:#fefce8;border-radius:4px;'
            f'padding:6px 10px;border:1px solid #fde68a;">'
            f'<strong>Evidence:</strong> {evidence}</div>'
            if evidence
            else ""
        )

        return f"""
        <div style="background:{severity_bg(sev)};border:1px solid {severity_border(sev)};
                    border-left:4px solid {severity_color(sev)};border-radius:8px;
                    padding:16px;margin-bottom:12px;">
            <div style="display:flex;align-items:center;gap:8px;margin-bottom:8px;">
                <span style="color:{severity_color(sev)};font-size:1.1rem;">
                    {severity_icon(sev)}</span>
                <strong style="font-size:1rem;">{f.get('title', 'Untitled')}</strong>
                <span style="background:{severity_color(sev)};color:white;padding:2px 8px;
                      border-radius:12px;font-size:0.7rem;text-transform:uppercase;
                      letter-spacing:0.05em;">{sev}</span>
                <span style="color:#6b7280;font-size:0.8rem;margin-left:auto;">
                    {f.get('mode', '')}</span>
            </div>
            <div style="margin-bottom:6px;"><strong>What:</strong> {f.get('what', '')}</div>
            <div style="margin-bottom:6px;"><strong>Why it matters:</strong>
                {f.get('why_it_matters', '')}</div>
            {evidence_html}
            <div style="background:white;border-radius:6px;padding:10px;border:1px solid #e5e7eb;">
                <strong>Suggestion:</strong> {f.get('suggestion', '')}
            </div>
            {persp_html}
        </div>"""

    findings_html = ""
    if critical:
        findings_html += '<h2 style="color:#dc2626;margin-top:32px;">Critical Findings</h2>'
        for i, f in enumerate(critical):
            findings_html += render_finding(f, i)
    if important:
        findings_html += '<h2 style="color:#d97706;margin-top:32px;">Important Findings</h2>'
        for i, f in enumerate(important):
            findings_html += render_finding(f, i)
    if minor:
        findings_html += '<h2 style="color:#2563eb;margin-top:32px;">Minor Findings</h2>'
        for i, f in enumerate(minor):
            findings_html += render_finding(f, i)

    # Strengths
    strengths_html = ""
    if strengths:
        for s in strengths:
            strengths_html += f"""
            <div style="background:#f0fdf4;border:1px solid #bbf7d0;border-left:4px solid #16a34a;
                        border-radius:8px;padding:14px;margin-bottom:10px;">
                <strong style="color:#15803d;">{s.get('title', '')}</strong>
                <div style="margin-top:4px;color:#374151;">{s.get('detail', '')}</div>
            </div>"""

    # Verified claims
    verified_html = ""
    if verified_claims:
        for vc in verified_claims:
            source = vc.get("source", "")
            source_html = (
                f'<span style="color:#6b7280;font-size:0.85rem;"> — {source}</span>'
                if source
                else ""
            )
            verified_html += f"""
            <div style="background:#f0f9ff;border:1px solid #bae6fd;border-left:4px solid #0284c7;
                        border-radius:8px;padding:14px;margin-bottom:10px;">
                <strong style="color:#0369a1;">&#10003; {vc.get('claim', '')}</strong>
                <div style="margin-top:4px;color:#374151;">
                    {vc.get('detail', '')}{source_html}
                </div>
            </div>"""

    # Perspectives
    perspectives_html = ""
    if perspectives:
        for p in perspectives:
            disagree = p.get("notable_disagreements", "")
            disagree_html = (
                f'<div style="margin-top:6px;color:#92400e;font-style:italic;">'
                f'Disagreement: {disagree}</div>'
                if disagree
                else ""
            )
            perspectives_html += f"""
            <div style="background:#faf5ff;border:1px solid #e9d5ff;border-radius:8px;
                        padding:14px;margin-bottom:10px;">
                <strong style="color:#7c3aed;">{p.get('name', '')}</strong>
                <div style="margin-top:4px;">{p.get('summary', '')}</div>
                {disagree_html}
            </div>"""

    # Next steps
    next_steps_html = ""
    if next_steps:
        items = "".join(f"<li>{step}</li>" for step in next_steps)
        next_steps_html = f'<ol style="padding-left:20px;line-height:1.8;">{items}</ol>'

    # Modes applied
    modes_tags = "".join(
        f'<span style="display:inline-block;background:#f3f4f6;border:1px solid #d1d5db;'
        f'padding:4px 10px;border-radius:16px;font-size:0.8rem;margin:2px;">{m}</span>'
        for m in ctx.get("modes_applied", [])
    )

    caveats = ctx.get("caveats", "")
    caveats_html = (
        f'<div style="background:#fefce8;border:1px solid #fde68a;border-radius:8px;'
        f'padding:12px;margin-top:16px;color:#92400e;">'
        f"<strong>Caveats:</strong> {caveats}</div>"
        if caveats
        else ""
    )

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Validation Report</title>
<style>
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
         line-height: 1.6; color: #1f2937; background: #f9fafb; padding: 24px; }}
  .container {{ max-width: 800px; margin: 0 auto; background: white;
               border-radius: 12px; box-shadow: 0 1px 3px rgba(0,0,0,0.1);
               padding: 32px; }}
  h1 {{ font-size: 1.5rem; margin-bottom: 4px; }}
  h2 {{ font-size: 1.15rem; margin-bottom: 12px; }}
  .meta {{ color: #6b7280; font-size: 0.85rem; }}
  .summary-box {{ background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px;
                  padding: 16px; margin: 20px 0; }}
  .stats {{ display: flex; gap: 16px; margin: 16px 0; flex-wrap: wrap; }}
  .stat {{ background: #f3f4f6; border-radius: 8px; padding: 12px 16px; text-align: center; }}
  .stat-number {{ font-size: 1.5rem; font-weight: 700; }}
  .stat-label {{ font-size: 0.75rem; color: #6b7280; text-transform: uppercase;
                 letter-spacing: 0.05em; }}
  hr {{ border: none; border-top: 1px solid #e5e7eb; margin: 24px 0; }}
</style>
</head>
<body>
<div class="container">
    <h1>Validation Report</h1>
    <div class="meta">Generated {timestamp}</div>

    <div style="margin-top:20px;">
        <div><strong>Output type:</strong> {ctx.get('output_type', 'Not specified')}</div>
        <div><strong>Declared intent:</strong> {ctx.get('declared_intent', 'Not specified')}</div>
        <div><strong>Audience:</strong> {ctx.get('audience', 'Not specified')}</div>
        <div><strong>Depth:</strong> {ctx.get('validation_depth', 'Standard')}</div>
        <div style="margin-top:8px;"><strong>Modes:</strong> {modes_tags}</div>
    </div>

    {caveats_html}

    <div class="stats">
        <div class="stat">
            <div class="stat-number">{total}</div>
            <div class="stat-label">Total Findings</div>
        </div>
        <div class="stat">
            <div class="stat-number" style="color:#dc2626;">{len(critical)}</div>
            <div class="stat-label">Critical</div>
        </div>
        <div class="stat">
            <div class="stat-number" style="color:#d97706;">{len(important)}</div>
            <div class="stat-label">Important</div>
        </div>
        <div class="stat">
            <div class="stat-number" style="color:#2563eb;">{len(minor)}</div>
            <div class="stat-label">Minor</div>
        </div>
        {"<div class='stat'><div class='stat-number' style='color:#0284c7;'>" + str(n_verified) + "</div><div class='stat-label'>Verified</div></div>" if n_verified else ""}
    </div>

    <div class="summary-box">
        <h2>Executive Summary</h2>
        <p>{exec_summary}</p>
    </div>

    {findings_html}

    {"<hr><h2 style='color:#16a34a;'>Strengths</h2>" + strengths_html if strengths_html else ""}

    {"<hr><h2 style='color:#0369a1;'>Verified Claims</h2>" + verified_html if verified_html else ""}

    {"<hr><h2 style='color:#7c3aed;'>Perspectives Explored</h2>" + perspectives_html if perspectives_html else ""}

    {"<hr><h2>Suggested Next Steps</h2>" + next_steps_html if next_steps_html else ""}

    <hr>
    <div class="meta" style="text-align:center;">
        Anti-Skill Validation Engine &middot; Source-agnostic &middot; {stats_line}
    </div>
</div>
</body>
</html>"""


def main():
    if len(sys.argv) < 2:
        print("Usage: python generate_validation_report.py <findings.json> [--output <path>]")
        sys.exit(1)

    input_path = sys.argv[1]
    output_path = None

    if "--output" in sys.argv:
        idx = sys.argv.index("--output")
        if idx + 1 < len(sys.argv):
            output_path = sys.argv[idx + 1]

    if not output_path:
        base = os.path.splitext(input_path)[0]
        output_path = f"{base}_report.html"

    with open(input_path, "r") as f:
        data = json.load(f)

    html = generate_html(data)

    with open(output_path, "w") as f:
        f.write(html)

    print(f"Report generated: {output_path}")


if __name__ == "__main__":
    main()
