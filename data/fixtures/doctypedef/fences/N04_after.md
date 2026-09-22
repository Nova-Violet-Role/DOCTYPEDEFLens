---
name: probe-n04
description: "Probe redeclare after fence."
---

<!DOCTYPE probe_root [
<!ELEMENT probe_root (probe_a)>
<!ELEMENT probe_a (#PCDATA)>
<!-- begin subset demo -->
<!ENTITY R.4 "first inside subset">
<!-- end subset demo -->
<!ENTITY R.4 "second after subset governs nothing">
<!ENTITY LAW.PROBE.1 "First probe law holds.">
]>

Body names <probe_root> and renders `probe_a` per LAW.PROBE.1.
