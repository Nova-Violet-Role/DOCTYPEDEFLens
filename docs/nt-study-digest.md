# full-study digest: takeaways from every .nt file

## arguments.duo.nt

### assimilation-note
    > Continues arguments.nt skeleton; lines 201-829 still queued (getopts/getopt, arrays, error handling per ToC pattern).

## arguments.nt

### assimilation-note
    > Expansion permitted by user: quoting matrix + slicing demos kept verbatim in spirit, prose compressed so brackets allow one-gulp read.
    > Remainder lines 81-829 deferred to next gulp; structure above is the load-bearing skeleton.

## arguments.okto.nt

### release-binding
    > Stream 1 (trust): every vector above is a case the four trust
    > channels (user-args, tool-result, file-ref, ask-answer) close by
    > construction; the tutorial is the evidence the boundary answers.
    > Stream 4 (forms): heredoc delimiter choice is the shell half of the
    > quoted-vs-unquoted form discipline cc-form declares.

## arguments.pente.nt

### assimilation-note
    > Lines 561-829 still queued (getopts/getopt, strict mode, error tables).

## arguments.tessares.nt

### assimilation-note
    > Lines 441-829 still queued (getopts/getopt long-opts, error handling, strict-mode patterns per ToC).

## arguments.treis.nt

### assimilation-note
    > Direct precedent for our own generators: gate.yml / .nt / report.md emitted from matrix answers via unquoted-EOF heredoc with ${VAR:-default} fallbacks and quoted "$@" forwarding.
    > Lines 321-829 still queued.

## corpus-index.nt

### mechanisms
    empty-hook-invoked-at-once:
    strength: STRONGEST cross-corpus pattern found; five corpora, one idiom
    corpora:
    tei: TEI.extensions.ent declared empty, invoked on the next line
    svg: 49 .attrib collections and both redecl placeholders declared empty
    xmlschema: percent-p and percent-s redefinable in the consumer internal subset
    jats: the customization quartet, classes mixes models modules, one set per profile
    dita: every domain ships a .mod and .ent pair, the .ent declared ahead
    shape:
    > Declare the extension point EMPTY. Invoke it immediately. A consumer that
    > wants nothing pays nothing; a consumer that wants something declares it
    > BEFORE the include and the first declaration binds.
    release-binding: LAW.ASK.11 is this idiom already; stream 4 and stream 14 both depend on it holding
    precedence-by-named-slot:
    corpora:
    svg: prefw and postfw, TWO override points, before and after the framework, marked-section IGNORE by default
    xmlschema: the consumer internal subset as the single named override site
    dita: catalog.xml resolves identity to location, so a path is never hard-coded
    shape:
    > Precedence is a declared POSITION, not a race. First-wins is what happens
    > when nobody declared where an override belongs.
    release-binding:
    > Stream 4, depth as precedence: depth.dtd declares WHERE an override may
    > sit, the reverse read resolves which fired. This is the F14 fix in law.
    one-source-many-emissions:
    corpora:
    tei: ODD emits dtd, rng and rnc together; a quartet per module
    svg: svg11-tiny 197 lines modular AND svg11-tiny-flat 2808 lines, same profile, factor 14
    docbook: 5.0 ships dtd rng sch xsd nvdl at once
    dita: 188 files at v1_2 becoming 656 at v1_3, generated and catalogued
    lwdita: conductor.xml imports build-html and build-markdown, two outputs one source
    shape:
    > The fan-out is never hand-kept. One literate source, many emissions, a
    > catalog to resolve them.
    release-binding:
    > Stream 17: 143 commands to 429 files is this curve. It is survivable
    > ONLY as generation. DITA at 656 hand-kept files would have collapsed.
    parallel-tracks-aligned:
    corpora:
    daisy: four tracks, dtbook 82 elements text, dtbsmil 14 timing, ncx 18 navigation, oebpkg package
    [... +78 lines]

## daisy.nt

### release-binding
    > Stream 17 (parallel tracks): the four-track split is the precedent for
    > auditing legs that each cover one family and reference instead of
    > re-reading. Stream 9 (shared entities): oeb12.ent is the cautionary
    > witness, include narrowly and count the inclusions.

## dita-plugins.nt

### mechanisms
    - plugin-contract: plugin.xml + integrator.xml + LICENSE + README in all three — the install surface our .claude-plugin/plugin.json mirrors (name/version/description/keywords)
    - conductor-5-lines: lwdita conductor.xml imports build-markdown.xml + build-html.xml and nothing else — two-output orchestration (Markdown AND HTML from one LwDITA source), the polyglot emission our .md+.nt pair copies
    - template-plus-build: build_<x>_template.xml beside build_<x>.xml — template/instance split, same cut as our forge-spec/installed-file split
    - fixtures-beside-code: docx/ sample/ basefiles/ test/ resources/ xsl/ lib/ carried inside the plugin — tests and samples ship with the grammar, as our controls/ do

## dita-shells.duo.nt

### what-this-teaches-the-release
    ent-mod-dtd-triple:
    > The DITA triple is NOT the same triple as our md, nt and yaml. DITA splits
    > by ROLE inside one grammar: entities, models, driver. Ours splits by
    > READER: human, model, tool. Both are called a triple and they are
    > orthogonal, which is worth declaring so nobody conflates them later.
    specialization-not-edit:
    > technicalContent never edits base. It declares new element types whose
    > content models are constrained versions of base's. This is the precedent
    > for stream 18, per-command LAW entities abolished: a command does not
    > legislate for itself, it SPECIALIZES a subset's law by constraining it.
    growth-is-the-warning:
    > 188 to 656 files across one minor version is what happens when every
    > vocabulary gets its own shell and every domain its own pair. Our 143
    > commands becoming 429 files is the same curve. DITA survives it because
    > the files are GENERATED from one source and catalogued; a hand-kept 656
    > would have collapsed. Read with tei.duo.nt: ODD emits the quartet, DITA
    > catalogues the shells, and neither hand-maintains the fan-out.

### gaps-remaining
    > Per-vocabulary content models are not transmigrated. bookmap, learning,
    > machineryIndustry, subjectScheme and xnal are named and counted, not read.
    > The plugin trio is covered by dita-plugins.nt and needs no second pass.

## dita-shells.nt

### mechanisms
    - grammar-per-schema-language: dtd/ + schema/ (XSD) side by side in every shell, rng/ added at v1_3 — three validators, one vocabulary; our cc-core contract audit is the equivalent third eye over src/ + built
    - specialization-shell: dita11 carries domains-ahead-of-DTDs (creators-audit measured 36 grammar files) — extension before base, the JATS customization-quartet idea in DITA dress
    - authoring-profile: xdita adds oxygen_templates + samples beside the shell — editor affordances versioned with the grammar, as our previews ride beside the questions

## dita-specializations.nt

### release-binding
    > Stream 18 (per-command laws abolished): specialization is the named
    > precedent, a command constrains a subset's law without editing the
    > subset, the way technicalContent constrains topic. Stream 9
    > (convergence): the 82-file specialization is the largest single
    > convergence input; converge the constraints, never the base.

## dita11.nt

### release-binding
    > Stream 9 (generation): this folder is the cost exhibit for
    > hand-kept dual grammars; every convergence argument cites it.
    > Stream 9 (corpus convergence): specialization .mod/.ent layering is
    > the DITA half of the convergence input beside TEI modules.

## ditaversion.nt

### release-binding
    > Stream 17 (429-file tree): 188-to-656 at 3.5x is the upper bound the
    > release's own growth is measured against; a scope amounting to less
    > than a DITA minor is routine, more is metamorphosis until proven.
    > Stream 4 (precedence): the four catalog.xml files are the catalog
    > discipline at scale, identity never hard-coded across 656 files.

## docbook-sch.nt

### release-binding
    > Stream 19 (convergence): the exclusion matrix is where DTD
    > convergence STOPS and the second instrument starts; the suite
    > already has it and calls it checker/. Name that line in the
    > release, per the ceiling-of-a-DTD mechanism, rather than meet it
    > at 11.0.0.

## docbook.nt

### release-binding
    > Stream 17 (429-file tree): DocBook 5.1 dropping dtd/ while doubling
    > rng/ is the precedent for retiring an emission without retiring the
    > vocabulary; the triple per artifact may likewise drop a form and keep
    > the source. Stream 9 (corpus convergence): the 4.x ent layering feeds
    > the shared-entity discipline beside DAISY.

## dtbook.nt

### release-binding
    > Stream 4 (depth): level1-6 plus level plus h1-6 plus hd is depth
    > declared three ways in one file; the precedence encoding cites it as
    > the case depth-as-rank, depth-as-nesting and depth-as-heading coexist.
    > Stream 17 (fixtures): the 82-name census is the element battery for
    > sweeps that must name every element of a mid-size grammar.

## dtd-variants.hepta.nt

### release-binding
    > Stream 4 (depth as precedence): marked sections are the DTD-native
    > override slots beside prefw/postfw; every override the release
    > declares cites a slot, never a race. Stream 3 (forms): %p/%s is
    > why schematic spellings live in entities, never in prose.

## dtd-variants.hex.nt

### release-binding
    > Stream 1 (trust): the six vectors are the XML half of the trust
    > evidence beside the shell five; untrusted content rides CDATA or
    > PCDATA-escaped, never raw, never eval. Stream 4 (forms): PCDATA vs
    > CDATA vs NDATA is the content contract behind every form choice.

## dtds.nt

### release-binding
    > Stream 9 (generation): single-purpose files need no generation
    > discipline; the triple ships for artifacts with more than one
    > consumer, and these twelve have exactly one each.
    > Stream 17 (fixtures): the smallest multi-file battery for sweeps
    > beside the loose ten.

## jats.duo.nt

### release-binding
    > Stream 4 (depth as precedence): the quartet is the finest-grained
    > named-override discipline in the corpus; every override slot the
    > release declares cites it beside SVG prefw/postfw. Stream 1
    > (companions-gate): the four CG grant axes mirror the four slots,
    > role tier tools scope against classes mixes models modules.

## jats.nt

### assimilation-note
    > JATS header block (MODULE/VERSION/DATE/PUBLIC invocation/SYSTEM/PURPOSE/SPONSOR) is the documentation discipline our command frontmatter only partly matches — description+argument-hint vs MODULE+PURPOSE+CREATED-FOR.

## lwdita.nt

### release-binding
    > Stream 17 (429-file tree): conductor-plus-two-builders is the
    > minimal generation precedent the 429 proof cites after ODD and the
    > flat emissions. Stream 9 (triple): template-beside-build is the
    > discipline for keeping emissions reproducible.

## mathml-docbook-xhtml11.duo.nt

### what-this-teaches-the-release
    the-honest-ceiling:
    > Stream 19 converges the whole DTD family into every subset. DocBook 5.1 is
    > the proof that convergence has a ceiling: past a certain expressiveness the
    > answer is not a better DTD, it is a second instrument. The release should
    > say where that line falls for us rather than discover it at 11.0.0.
    the-transition-version:
    > 5.0 shipping both is the pattern for stream 14. Re-inline at publish AND
    > stamp for the future is exactly a transition version: the current cut and
    > the means to detect a stale one, carried together, for one release.
    nvdl-is-in-our-variant-chain:
    > NVDL sits at depth 10 of the 23-level ladder in 10.0.0.md and DocBook 5.0
    > and 5.1 both ship a docbook.nvdl. The ladder is not a list of formats the
    > release admires; at least one rung is a working dispatch mechanism in a
    > corpus on this disk.

### gaps-remaining
    > The 4.5 DTD content models and the 5.1 Schematron rule set are not
    > transmigrated. The version trajectory, the reason for it and the mapping onto
    > our own checker layering are what streams 14 and 19 needed.
    > MathML and XHTML11 keep the coverage mathml-docbook-xhtml11.nt already gave
    > them; neither needed a second pass for this release.

## mathml.nt

### release-binding
    > Stream 17 (429-file tree): the 97-to-38 consolidation is the
    > precedent that a generated tree may shrink across versions; count
    > emissions, never assume growth. Stream 9 (transforms): the pair
    > joins html2dita as the round-trip witnesses.

## office-dtds-daisy.duo.nt

### what-this-teaches-the-release
    the-polyglot-is-not-new:
    > Stream 17 makes every artifact a triple and calls it new. DAISY has shipped
    > a quartet since 2005. The difference worth declaring: DAISY's tracks are
    > DIFFERENT CONTENT aligned by time; ours are the SAME content in three
    > readings. Alignment is the shared problem, sameness is not.
    ncx-is-the-reverse-read:
    > navMap, navPoint, navLabel and content exist so a reader can enter the work
    > at any point and know where they are without reading from the start. That
    > is the same job the reverse read does for a cache: arrive anywhere, know
    > the position. ncx is a declared table of contents for a work too long to
    > read linearly, which is exactly what a 384-question intake is.
    one-entity-file-serves-the-package-only:
    > oeb12.ent is 48964 bytes of 254 entities and exactly ONE file includes it,
    > oebpkg12.dtd. Measured, not assumed. The shared-entity idea is real but its
    > reach here is narrow: the package track shares, the content tracks do not.
    > A claim that DAISY tracks share entities broadly would be false.
    versions-live-beside-each-other:
    > dtbook 2005-1, 2005-2 and 2005-3 all ship in the same folder. A consumer
    > names the version it was authored against and both remain readable. This is
    > the alternative to our re-inline-at-publish decision: not one current copy,
    > but every version kept and named. Worth weighing against stream 14 before
    > the stamp mechanism is written.

### gaps-remaining
    > dtbook's 82 element content models are not transmigrated, nor the smil timing
    > attributes. The four-track shape, the track sizes and the entity reach are what
    > streams 15 and 17 needed and are what this pass carries.

## office.nt

### release-binding
    > Stream 17 (audit legs): twelve drivers over shared features is the
    > closest precedent for one audit leg per family over shared checkers;
    > the leg names the driver, the features ride along.
    > Stream 4 (precedence): FIXED namespace URIs beside REQUIRED ids are
    > identity resolved in place, the catalog discipline without a catalog.

## ooxml.nt

### mechanisms
    - one-transform-per-construct: document.table, document.link, document.topic and numbering each own an .xsl; a construct is never split across files
    - xspec-discipline: the test names the transform under test and carries its own fixture stylesheet; the only .xspec in the whole example corpus
    - template-plus-build: build_template.xml is the recipe, build.xml the run; the recipe is versioned, the run is generated

### release-binding
    > Stream 17 (audit legs): the .xspec file is the corpus's only
    > transform-level test fixture; audit legs that check generated output
    > cite it as the shape. Stream 9 (generation): template-plus-build is
    > the smallest generation pair in the corpus beside TEI ODD.

## polyglot.pente.nt

### takeaway-measured
    > NestedText is the safe counterpart to YAML — same indentation philosophy, zero implicit typing, zero execution surface; >-tag analogues |-scalar; one file simultaneously Bash+Markdown+YAML+NestedText, each parser reading its own layer. (measured source lines 810-813)

## svg-modules.nt

### release-binding
    > Stream 11 (profiles): the 35/46/48 entity ladder is the measured
    > precedent for additive profiles; a matrix leg names its profile by
    > count, never by hope. Stream 4 (override points): prefw and
    > postfw stay the two named slots beside qname's 96.

## svg.duo.nt

### gaps-remaining
    > Per-module content models are still not transmigrated; 49 modules at roughly
    > 300 lines each is a pass of its own. The driver sizes, the flat-versus-modular
    > pair and the two redecl slots are what streams 4 and 17 needed.

## svg.nt

### assimilation-note
    > 55 files: 1 driver + profile variants (basic/tiny/full) + per-topic .mod + svgcatalog.xml.
    > Remainder (model, attribs, paint, text, filter, font, hyperlink, script) follows the same qname+attrib-collection skeleton; detail pass continues file-by-file from here.
    > Cube-preview relevance: structure elements (svg/g/defs/symbol/use) are the hosts the expanding-cube PNG/SVG mechanic annotates.

## tei-modules.nt

### release-binding
    > Stream 19 (convergence): the 1:1 invariant is the removability test
    > every converged subset must pass; a subset whose elements outlive
    > their file is not converged. Stream 9 (triple): twenty modules one
    > ODD source stays the generation precedent beside lwdita's conductor.

## tei.duo.nt

### gaps-remaining
    > Per-module content models are not yet transmigrated; this pass covers the folder
    > shape, the fragment attributes, the linking module and the generation discipline,
    > which is what streams 15 and 17 need. textcrit, transcr, msdescription and iso-fs
    > carry apparatus mechanisms worth a later pass for the record and ledger work.

## tei.nt

### mechanisms
    - odd-single-source: tei.dtd generated from ODD 2019-01-29, v3.5.0 rev 3c0c64ec4 — one literate source emits DTD+RNG+RNC together (precedent: our build resolves src/ to commands/ the same direction)
    - qname-parameterization: <!ENTITY % n.TEI "TEI"> per element + <!ENTITY % NS ''> + <!ENTITY % TEI.extensions.ent ''> hook invoked immediately — extension point identical in shape to svg redecl placeholder
    - multi-schema-publishing: every module ships all three grammars; consumers pick DTD-validating, RNG or compact RNC

### assimilation-note
    > Triplet discipline is the model for our own subset/command/built triple (dtd/*.dtd + src/commands + commands/).

## tocjs.nt

### mechanisms
    - output-side-enhancement: the transform changes navigation, never content; content pipeline untouched
    - skin-sets: check, default, folders, local, menu variants of css/img; presentation as swappable sets
    - map-driven-sample: the sample is a ditamap plus topics, the same shape a companion audit leg walks

### release-binding
    > Stream 11 (preview): swappable presentation sets are the precedent
    > for preview skins; the cube expands the same under every skin.
    > Stream 17 (fixtures): the map-driven sample is the smallest runnable
    > audit fixture in the corpus.

## triple-proof.nt

### proof
    > 173 artifacts (145 commands + 23 skills + 5 agents) emitted nt+yaml
    > and verified with 0 findings: 346 emission files beside the 173
    > committed md sources and mirrors. Commands alone: 145 times 3 = 435
    > (145 md + 145 nt + 145 yaml). Skills and agents likewise. Supporting
    > prose (references, workflows, templates) is correctly refused: no
    > DOCTYPE, no emission. Generation, not authoring.

### bugs-found-by-proof
    > SKILL.md keyed as SKILL (basename) instead of its directory: fixed to
    > parent-dir key, control 6 trips it.
    > All 23 skills overwrote one SKILL.nt (302 files, not 346): fixed with
    > outName (parent dir), re-run shows 346.
    > 23 skill sigils missing from the registry: added as family sigil,
    > collision-free (no key ends in -dtd).

### release-binding
    > Stream 17 (429-file tree): the proof above is the generation half;
    > wiring into build/installer/gate is the next slice. Stream 9 keeps
    > the abolition design and the corpus convergence.

## xdita.nt

### release-binding
    > Stream 9 (polyglot triple): the four-way sample set is the precedent
    > that one content survives three-plus serializations; the triple per
    > artifact cites it beside TEI ODD. Stream 11 (preview): rendered .html
    > beside sources is the preview mechanic in miniature.

## xhtml-strict.nt

### assimilation-note
    > Typed-name pattern (ContentType vs ContentTypes, Charset vs Charsets) = precedent for Depth.dtd vs Type.dtd split: scalar vs list, each with its RFC-like authority note.
    > Strict vs transitional vs frameset diff still queued; .ent sample still queued.

## xhtml.duo.nt

### release-binding
    > Stream 9 (corpus convergence): the strict-inside-transitional
    > inclusion is the subset pattern for converging corpora without
    > copying them. Stream 17 (audit legs): html2dita is the precedent
    > for legs that read the built tree back into the source shape.

## xhtml.nt

### assimilation-note
    > Three-driver pattern (strict/transitional/frameset) = the DTD-variant precedent for the ramified gate-1/2/3 shape: one skeleton, three dispatched profiles.
    > .ent entity modules = precedent for per-topic .mod decomposition seen in svg/.
    > Next detail pass: strict vs transitional diff head + one .ent sample.

## xhtml11.nt

### mechanisms
    - driver-plus-one-model: a single .mod file holds the whole content model; the driver holds identity, namespaces and switches
    - entity-set-layering: latin-1, special and symbol sets stack; a profile takes the layers it needs
    - catalog-identity: xhtmlcatalog.xml resolves public identity to location, second witness beside DITA catalog.xml for precedence-by-named-slot
    - math-svg-flat: the 573705-byte math-plus-svg flat is the largest single emission in the corpus; a profile that needs everything pays everything

### release-binding
    > Stream 17 (429-file tree): the 8.3 factor joins the F20 pair as the
    > third witness that a maintained tree and its generated emission differ
    > by an order of magnitude, so the triple ships generated or not at all.
    > Stream 4 (depth as precedence): the catalog witness joins the named
    > override-slot discipline; no path is hard-coded where a catalog can
    > resolve it.
