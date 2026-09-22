---
name: probe-n00
description: "Probe fenced subset used."
---

<!DOCTYPE probe_root [
<!ELEMENT probe_root (probe_a)>
<!ELEMENT probe_a (#PCDATA)>
<!-- begin subset demo -->
<!ELEMENT n00_el (#PCDATA)>
<!ENTITY N.1 "n00 one">
<!-- end subset demo -->
<!ENTITY LAW.PROBE.1 "First probe law holds.">
]>

Body names <probe_root> and renders `probe_a`, `n00_el` per LAW.PROBE.1.
