---
name: probe-n03
description: "Probe redeclare inside fence."
---

<!DOCTYPE probe_root [
<!ELEMENT probe_root (probe_a)>
<!ELEMENT probe_a (#PCDATA)>
<!-- begin subset demo -->
<!ENTITY R.3 "first inside">
<!ENTITY R.3 "second inside">
<!-- end subset demo -->
<!ENTITY LAW.PROBE.1 "First probe law holds.">
]>

Body names <probe_root> and renders `probe_a` per LAW.PROBE.1.
