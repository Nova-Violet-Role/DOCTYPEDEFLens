---
name: probe-l00
description: "Probe law invoked directly."
---

<!DOCTYPE probe_root [
<!ELEMENT probe_root (probe_a)>
<!ELEMENT probe_a (#PCDATA)>
<!ENTITY LAW.X.1 "Ex law one holds.">
]>

Body names <probe_root> and renders `probe_a` per LAW.X.1.
