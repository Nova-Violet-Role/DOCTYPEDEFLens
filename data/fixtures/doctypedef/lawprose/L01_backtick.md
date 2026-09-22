---
name: probe-l01
description: "Probe law invoked in backticks."
---

<!DOCTYPE probe_root [
<!ELEMENT probe_root (probe_a)>
<!ELEMENT probe_a (#PCDATA)>
<!ENTITY LAW.X.1 "Ex law one holds.">
]>

Body names <probe_root> and renders `probe_a` (`LAW.X.1` governs this line).
