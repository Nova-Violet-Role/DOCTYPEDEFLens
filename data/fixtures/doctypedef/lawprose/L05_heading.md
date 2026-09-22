---
name: probe-l05
description: "Probe law in heading."
---

<!DOCTYPE probe_root [
<!ELEMENT probe_root (probe_a)>
<!ELEMENT probe_a (#PCDATA)>
<!ENTITY LAW.X.1 "Ex law one holds.">
]>

## Rendering per LAW.X.1

Body names <probe_root> and renders `probe_a` exactly as declared.
