---
name: probe-l07
description: "Probe law cited per LAW.X.1 in frontmatter."
---

<!DOCTYPE probe_root [
<!ELEMENT probe_root (probe_a)>
<!ELEMENT probe_a (#PCDATA)>
<!ENTITY LAW.X.1 "Ex law one holds.">
]>

Body names <probe_root> and renders `probe_a` exactly as declared.
