---
name: probe-n05
description: "Probe driver pattern before fence."
---

<!DOCTYPE probe_root [
<!ELEMENT probe_root (probe_a)>
<!ELEMENT probe_a (#PCDATA)>
<!ENTITY R.5 "driver value before include">
<!-- begin subset demo -->
<!ENTITY R.5 "subset default">
<!-- end subset demo -->
<!ENTITY LAW.PROBE.1 "First probe law holds.">
]>

Body names <probe_root> and renders `probe_a` per LAW.PROBE.1.
