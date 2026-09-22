---
name: probe-n07
description: "Probe redeclare across fences."
---

<!DOCTYPE probe_root [
<!ELEMENT probe_root (probe_a)>
<!ELEMENT probe_a (#PCDATA)>
<!-- begin subset alfa -->
<!ENTITY R.7 "first in alfa">
<!-- end subset alfa -->
<!-- begin subset beta -->
<!ENTITY B.7 "beta text">
<!-- end subset beta -->
<!ENTITY R.7 "second after beta governs nothing">
<!ENTITY LAW.PROBE.1 "First probe law holds.">
]>

Body names <probe_root> and renders `probe_a` per LAW.PROBE.1.
