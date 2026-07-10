# Cinematography for a Hallucinating Camera

> A field manual for directing image-to-video generation — written for anyone who has
> to get a film out of a model that dreams. No film school is assumed and none is
> needed: this pipeline exists to put production tools in anyone's hands, and a viewer
> with raw visual instinct can outdo a trained director here, because the model never
> went to film school either. The classical terms — lens, blocking, coverage, the
> 180-degree line — appear below as vocabulary this page teaches in passing: useful
> shorthand if you already carry it, a free glossary if you don't, an entry requirement
> never.

You do not have a camera. You have a machine that dreams a short motion out of a
single still, and it dreams badly the moment you ask it for something the still
does not already contain. Every rule below was paid for in failed generations on
this project. None of it is theory.

If you have never touched this repo: the pipeline here turns approved still images
into a shot-by-shot *motion script* (`_skills/robotiko-motion-script/SKILL.md`),
which tells a video model (Kling / Veo / Seedance) how each frame should come
alive. This document is the grammar underneath that script — the *why* behind the
rules the skill enforces.

---

## 1. The Medium's Real Physics

Forget the lens for a moment and learn what the machine actually is, because its
constraints are nothing like a camera's.

**There is no 3D scene.** A real camera moves through a space that exists whether
or not you point at it. The model has no space. It has one flat image and a
statistical guess about what "zoom out" or "pan left" tends to look like in its
training data. When the frame widens, the model is not *revealing* more of a room
that was always there — it is *inventing* pixels to fill the new area, drawn from
everything it has ever seen. That invention is the whole problem.

**There is no coverage.** On a set you shoot a wide, a medium, and a close, then
choose in the edit. Here every "angle" is a separate generation from a separate
still, and nothing guarantees the chrome on the android is the same chrome from
shot to shot. Continuity is not captured; it is *engineered*, frame by frame, with
reference images and reused frames.

**There is no persistence across the cut.** The model does not know that S12 and
S13 are the same character in the same room. Each clip is an island. Anything you
want to survive a cut — a body's damage state, a location's light, a color — has to
be re-declared or re-anchored every single time.

**The model abhors an empty frame.** Its deepest reflex is to *resolve ambiguity*.
A silhouette becomes a detailed face. A blurred shape becomes a labeled object.
A patch of fog becomes a mountain range. An old interior becomes a *decayed*
interior, complete with dripping water and cobwebs, because "retro/analog" reads to
it as "abandoned." This project's lessons file is a catalog of these reflexes:
Veo adding "water drops falling from ceiling, leaks, dripping moisture" to a clean
room; Tilt-Up on a wasteland "fabricating mountains and structures above the frame";
generators "clarifying" abstract silhouettes into photorealistic people. See the
VEO DECAY SPAWN and FRAME-LOCKED CAMERA MOVES rules in `_memory/lessons.md`.

**Spawn pressure is constant.** Background figures flicker into existence in almost
any populated-looking scene — phantom characters that cost real credits in retakes.
Every motion prompt on this project ends with an anti-spawn guard
(*"Do not add extra characters. Keep everything as pictured."*) for exactly this
reason. It is not belt-and-suspenders; it is load-bearing.

The single sentence that unlocks the whole medium:

> **A widening or traveling frame is an invitation for the model to hallucinate.
> Anything you ask the frame to reveal that the source still does not contain, the
> model will invent.**

Direct this camera and you are not choosing what to *show*. You are choosing what
to *withhold from its imagination*.

---

## 2. Translation Table — Classical Grammar Into This Medium

If you carry classical training, it still applies — every term just has to be
re-pointed. If you have never used these terms, read the table as a glossary you pick
up in passing: the middle column says what each tool did on a film set; the right
column is the only part this medium cares about. The intent survives; the mechanism
changes completely.

| Classical tool | What it did | The equivalent here |
|---|---|---|
| **Lens choice** (35mm vs 85mm) | Optically fixed field of view and compression | There is no lens. The "look" is a *prompt suffix* baked into every clip: `Shot on 35mm film, cinematic 16:9 framing, Kodachrome color palette, heavy film grain, shallow depth of field.` You do not select glass; you assert an aesthetic in words and hope the model honors it. Depth of field is a keyword, not an aperture. |
| **Blocking / actor movement** | Direct a body through space | You cannot choreograph. The reliable unit is *micro-motion*: one head turn, one hand, environmental drift (fog, dust, sparks, light flicker). Complex action fails — "character A does X while B does Y while camera does Z" produces morphing garbage. Simplify to the single key motion, or to the aftermath. |
| **The 180-degree rule** | Keep spatial continuity across a cut so screen-left stays screen-left | The model has no memory of the line — it cannot break a rule it never knew. *You* hold the line, in the writing: name screen directions explicitly ("toward the left side of the frame, screen-left"), and never let two consecutive shots contradict their spatial logic. Directional continuity is authored, not filmed. |
| **Montage** | Meaning from the collision of shots | Still true, but assembled downstream in the edit, not in-camera. The model gives you the shots; the beat-synced *cut* between them happens in CapCut, aligned to musical section boundaries from the metadata JSON. Do not ask one clip to *be* a montage. |
| **Coverage** | Shoot options, choose later | Replaced by *multi-clip + frame chaining*. A scene longer than a clip becomes several generations, each with its own camera move; continuity between them is carried by reusing the last frame of one clip as the start frame of the next (max 3 in a chain — error compounds beyond that). You buy your options one generation at a time. |
| **Camera move** (dolly, crane, zoom) | Physically travel the rig | A *semantic instruction* the model interprets loosely. "Zoom out" does not pull a real lens — it tells the model to imagine a wider frame, which is precisely when it invents. Moves that reveal new area (Tilt, Pan, Zoom Out, Crane) are the highest-risk category. Prefer moves that stay inside the frame, and when you must reveal, anchor the destination (Section 3, the S30 case). |
| **Match cut / eyeline** | Character looks, cut to what they see | The model needs an *anchor already in the frame*. A vague "his eyes shift toward something" produces random head-wobble. Name a target visible in the source still and lock the gaze onto it ("his gaze settles on the golden-brass figure in the distant background"). No anchor, no eyeline. |

The through-line: classical grammar assumes a camera that captures a world that
exists. This grammar assumes a model that fabricates a world to match your words.
Every translation is a shift from *capturing* to *constraining*.

---

## 3. Worked Cases — Real Prompts, Real Failures

Rules earn their place only when a produced shot forced them into existence. Three
did.

### 3a. EP06 monotony — how the Camera Diversity Rule was born

EP06 was generated before any diversity discipline existed. The result: **42% of
its clips were the same move, Slow Zoom In.** Watched end to end, the episode felt
like one long push — the camera had a single idea and repeated it until the
repetition became the only thing you noticed. That is not a style; it is a tic.

The fix became a hard rule in the motion-script skill
(`_skills/robotiko-motion-script/SKILL.md`, "Camera Move Diversity Rule"): no
single move exceeds 30% of clips; every five consecutive clips use at least three
different moves; the accent moves (Orbital, Handheld, Crane) are rationed to two or
three per episode; Static must be at least 15% of clips. The point is not variety
for its own sake — the skill is explicit that the quota is a *floor, not a
substitute for motivation*. But EP06 proved the floor has to exist, because the
path of least resistance in this medium is to reach for the one move that worked
last time.

**Lesson for you:** the model will happily let you shoot the whole film with one
move. Diversity is a decision you impose from outside; it never emerges on its own.

### 3b. EP07 — the earned Dolly In and the distance ladder

EP07 ("The Silence Protocol", `episode-07/03_direction/ep07_concept_notes.md`) is
the counter-example: camera restraint used as the entire spine of a film.

Its personality is **the Retreating Camera**. Dolly Out dominates (~25-30%); Static
fills the emptiness between (~20-25%). The character speaks a refrain five times —
*"...Here. But you... are NOT."* — and on each of the five, across five different
locations, the camera pulls **one rung more distant**. Bench, home, transit, mall,
bed: a consistent *distance ladder* that makes isolation legible through scale
alone, never through a performance.

The whole grammar exists to set up a single reversal. The episode is engineered so
that its **first and only Dolly In** lands on the two words *"I AM COMING."* One
forward push, in an entire film of retreat. Because the pattern was built with
discipline, breaking it *means* something — the will asserting itself, rendered as
pure camera direction with no dialogue doing the work.

**Lesson for you:** in a medium where any move is one prompt away, restraint is the
scarce resource. A move withheld for six minutes hits harder than any move you
could stage. Establish a pattern precisely so you can break it once.

### 3c. THE S30 CASE — the reshoot that taught the anchor rule

This is the centerpiece, and it is worth telling in full because it is the clearest
demonstration of the medium's core failure and its cleanest fix.

**The setup.** EP09 shot S30, "Full Kintsugi"
(`episode-09/05_video/ep09_motion_script_v01.md`), is the widest interior reveal of
the episode — the fully-mended android, gold in its seams, self-luminous, revealed
in its workshop. The plan was **Mode A** (a single start frame,
`episode-09/04_visuals/raw/30.png`) with a **Slow Zoom Out** and this prompt:

> Full body: the @Kintsugi chrome android standing in the workshop — mismatched
> scavenged panels welded with gold in the seams, translucent digital skin
> revealing bioluminescent core. Self-luminous, lighting the space. Shadow as warm
> contrast on the wall. Shot on 35mm film, cinematic 16:9 framing, Kodachrome color
> palette, heavy film grain, shallow depth of field. Do not add extra characters.
> Keep everything as pictured.

A clean prompt. Correct suffix, correct anti-spawn guard, correct Element tag. On a
real camera it would be a trivial shot: dolly back, let the room breathe.

**The failure.** As the frame widened past the borders of the source still, the
model had to fill the new area — and it filled it by *inventing set dressing that
does not exist in the universe*. Objects, clutter, furniture, none of it canon,
all of it conjured to satisfy a widening frame. The anti-spawn guard did not save
it: that guard forbids extra *characters*, but the model was inventing *environment*,
and a Zoom Out is a standing invitation to do exactly that. **Four reshoots failed
the same way.** Same prompt, same guard, same hallucinated fill. This is the
medium's core physics from Section 1, live: *the frame revealed area the still did
not contain, so the model made it up.*

**The rescue.** The fix was not a better adjective. It was to stop asking the model
to imagine the destination and instead *hand it the destination as a frame that
already exists in the universe.* The move switched to **Mode B** (start + end
keyframes), and the end frame was an existing wide environmental keeper from the
episode's own set — `episode-09/04_visuals/raw/5.png`, the garage-door shot:
overcast grey sky, industrial factory buildings, a wire fence. The prompt was
rewritten for two-frame continuity (quoted verbatim; it names the end frame as
"5.jpg", the tool-side upload of that same keeper):

> Slow Zoom Out. Camera initiates a smooth, cinematic zoom out from the composition
> of start frame and transitions seamlessly into the wide environmental shot of end
> frame. The chrome android with the bioluminescent core from the first image
> REMAINS standing in its exact place inside the workshop, glowing softly. As the
> camera pulls back through the garage door, it reveals the overcast grey sky, the
> industrial factory buildings, and the wire fence exactly as pictured in 5.jpg.
> Perfect continuity between both frames. No extra elements, props, or characters
> are added. Constant 35mm film grain, Kodachrome color palette, 16:9 framing.

**It succeeded on the first try.** With the destination pinned to a real frame, the
model had nothing left to invent — the widening frame now had a known place to
travel *to*, so it interpolated between two truths instead of fabricating one.

**The pattern (memorize this):**

> A widening frame is an invitation to hallucinate. When the reveal matters, do not
> ask the model to imagine what lies beyond the source borders — anchor the
> destination with a frame that already exists in the universe, and make the shot an
> interpolation between two truths rather than an extrapolation into invention.

This is now doctrine on the project. It generalizes past S30: the reference-first
principle (generate the location/state a shot needs *before* you shoot against it),
and the "use a prior frame as the base image" technique for chaining a consistent
pull-out (EP09's dawn sequence pulled `5.png` -> S36 -> S37 -> S38, each wider frame
based on the previous one so the world stayed identical as the camera receded) are
the same insight applied earlier in the process. See the REFERENCE-FIRST and USE A
PRIOR FRAME AS THE BASE IMAGE rules in `_memory/lessons.md`.

### On reshoots — the honest number

You will not get every shot on the first generation. Image generation is where the
universe is created — dense prompts carrying scene detail, character state,
symbolic weight, plus reference images fed alongside. That complexity can confuse
generation tools. Across nine episodes, the experiential rule of thumb — an
observation from the edit bay, not instrumented telemetry — is that roughly
**65–70% of image prompts land on the first try**. The rest need a retry or prompt
revision: simplify the prompt, swap a few words, drop a detail the tool
misreads. Video generation from a strong approved image is a different story —
the universe is already built, it just flows — roughly **~80% first-pass**
(the figure ADR-0007 records as lived observation, not telemetry). When references were *missing* — EP09's
gold-body scenes were written against the wrong (damaged) base before the Kintsugi
reference existed — that first-pass rate collapsed and nearly every shot needed a
manual rescue, at eight-to-ten regenerations each. The tax is real and it is
front-loaded onto whatever you failed to prepare. Budget credits for it, and treat
"this prompt needs a better frame" as a normal, healthy discovery at generation
time, not a failure.

---

## 4. One Move Per Clip — and Why

Every shot on this project carries exactly one camera move from a fixed vocabulary.
Never "Pan Left + Zoom In." This is not a stylistic preference; it is a hard
constraint of the medium.

A real rig can dolly and pan and rack focus at once because a human operator holds
the intent together. The model has no operator. Two simultaneous move-instructions
are two conflicting statistical pulls on the same frame, and the result is neither
move done cleanly — it is a smeared average, or the model picks one and ignores the
other, or it morphs. The reliable unit of motion in this medium is *singular*: one
camera move, plus one or two atmospheric elements (drifting fog, a light flicker,
sparks). That is the whole budget for a clip.

This is also why the motion-strength scale on this project tops out in practice
around the middle for most shots and why the strongest emotional beats are often
*Static* — the "Still Hold," camera stopped completely at the peak. In a medium
where every added instruction is a chance to hallucinate, doing *less* per clip is
not timidity. It is the reliability strategy. One clean move beats three fighting
ones every time.

---

## 5. Honest Limits

This grammar is real, but it is the grammar of *single-still animation*, and it is
worth being precise about what that is not.

- **There is no true lens language.** You cannot request a 35mm anamorphic
  compression and get its optics; you get a *keyword* the model approximates. Focal
  length, aperture, and real depth cues are suggestions, not controls.
- **There is no true blocking.** You animate a still. You cannot walk a character
  across a room and around a table on a path you choose — you get one motion, kept
  simple, or you cut. Everything richer is stitched in the edit.
- **The camera cannot truly travel.** "Dolly In" and "Zoom In" both read to the
  model as "make a tighter frame"; the grounded-vs-optical distinction a real
  operator feels is mostly lost. Reveal moves (out, up, across) remain the danger
  zone of Section 1 no matter how you phrase them.
- **Continuity is manual labor, not a property of the system.** Every bit of it —
  character state, location, color, screen direction — is engineered per clip with
  references, reused frames, and explicit prompt language. Nothing carries across a
  cut for free.
- **The machine has no taste.** It cannot tell an earned Still Hold from a lazy one,
  or a motivated Dolly In from a quota-filling one. That judgment is the one thing
  it will never supply, which is exactly why the human approval gates in this
  pipeline — dramaturgy, the visual reference gate, and the motion script (see
  `docs/getting-started.md`) — sit where they do.

Direct within these limits honestly and the medium is extraordinary: a one-person
crew producing cinematic motion at a scale it could never have shot alone. Pretend the
limits are not there — ask the frame to reveal what the still never held — and the
camera will dream you something that was never in the film. The whole craft is
knowing the difference.

---

*The Moon has no light of its own. But in reflecting the Sun, it illuminates the night.*
