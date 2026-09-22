---
name: probe-n06
description: "Probe backtick element mention."
---

<!DOCTYPE probe_root [
<!ELEMENT probe_root (probe_a)>
<!ELEMENT probe_a (#PCDATA)>
<!-- begin subset demo -->
<!ELEMENT n06_el (#PCDATA)>
<!-- end subset demo -->
<!ENTITY LAW.PROBE.1 "First probe law holds.">
]>

Body names <probe_root> and renders `probe_a`, also uses `n06_el` per LAW.PROBE.1.
