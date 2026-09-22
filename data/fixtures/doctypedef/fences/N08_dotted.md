---
name: probe-n08
description: "Probe dotted fence names."
---

<!DOCTYPE probe_root [
<!ELEMENT probe_root (probe_a)>
<!ELEMENT probe_a (#PCDATA)>
<!-- begin subset my.demo-v2 -->
<!ELEMENT n08_el (#PCDATA)>
<!ENTITY N.8 "n08 one">
<!-- end subset my.demo-v2 -->
<!ENTITY LAW.PROBE.1 "First probe law holds.">
]>

Body names <probe_root> and renders `probe_a`, `n08_el` per LAW.PROBE.1.
