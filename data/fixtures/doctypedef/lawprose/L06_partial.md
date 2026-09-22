---
name: probe-l06
description: "Probe one of two laws orphaned."
---

<!DOCTYPE probe_root [
<!ELEMENT probe_root (probe_a)>
<!ELEMENT probe_a (#PCDATA)>
<!ENTITY LAW.X.1 "Ex law one holds.">
<!ENTITY LAW.X.2 "Ex law two holds.">
]>

Body names <probe_root> and renders `probe_a` per LAW.X.1.
