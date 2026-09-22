---
name: probe-n01
description: "Probe mismatched fence names."
---

<!DOCTYPE probe_root [
<!ELEMENT probe_root (probe_a)>
<!ELEMENT probe_a (#PCDATA)>
<!-- begin subset demo -->
<!ELEMENT n01_el (#PCDATA)>
<!ENTITY N.1 "n01 one">
<!-- end subset othermo -->
<!ENTITY LAW.PROBE.1 "First probe law holds.">
]>

Body names <probe_root> and renders `probe_a` per LAW.PROBE.1.
