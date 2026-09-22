---
name: probe-l03
description: "Probe law in comment only."
---

<!DOCTYPE probe_root [
<!ELEMENT probe_root (probe_a)>
<!ELEMENT probe_a (#PCDATA)>
<!ENTITY LAW.X.1 "Ex law one holds.">
]>

Body names <probe_root> and renders `probe_a` exactly as declared.
<!-- reviewer note: check LAW.X.1 before shipping -->
