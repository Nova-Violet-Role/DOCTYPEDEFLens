---
name: probe-n02
description: "Probe unclosed fence."
---

<!DOCTYPE probe_root [
<!ELEMENT probe_root (probe_a)>
<!ELEMENT probe_a (#PCDATA)>
<!-- begin subset lone -->
<!ELEMENT n02_el (#PCDATA)>
<!ENTITY N.1 "n02 one">
<!ENTITY LAW.PROBE.1 "First probe law holds.">
]>

Body names <probe_root> and renders `probe_a` per LAW.PROBE.1.
