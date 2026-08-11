# Anti-footguns

Each of these was a real mistake that cost a review round.

1. **Never overwrite a shared asset to satisfy a guidelines download.** The
   site's real `favicon.png` / `apple-touch-icon.png` are *not* the brand kit's
   "app icon" download, even if they look similar. Add a new file at its own
   path; repoint the kit's data at it. Conflating them silently changes the
   product's browser icon.

2. **Consume semantic tokens, not primitives.** The page must obey the same rule
   the codebase imposes on its own components.

3. **The data module is the single source** for both the page and the Markdown
   export — never hardcode copy in JSX.

4. **Figma URLs expire and may be blocked.** Download immediately; keep a
   regenerate-from-source fallback (mark + real font outlines).

5. **Licensed fonts are listed, never distributed.** Open fonts get real links.
   Say so in the archive README.

6. **Regenerate the archive** every time assets change, or the "Download all"
   button silently ships stale files.

7. **A merged PR is finished.** Follow-up work starts from the latest default
   branch as a fresh change; never stack new commits on already-merged history.
   (If a hosted git proxy refuses delete-pushes, remove a stray file via the
   platform API and delete the branch from the platform UI.)

8. **Off-grid values and off-language shapes get caught.** If the system is on an
   8 px grid or a fixed arc vocabulary, hand-built additions that break it read
   as wrong. Build within the documented grammar and have a human spot-check
   generative output.

9. **Match the project's separators and dash discipline.** A project may use `/`
   instead of `·` in eyebrows, and reviewers notice em-dash overuse. These are
   microtypography, not nitpicks — they are the difference between "in the brand"
   and "close to the brand".

10. **Don't claim done without the browser pass.** Typecheck-clean is necessary,
    not sufficient. Render it, click it, download it, read the bytes.
