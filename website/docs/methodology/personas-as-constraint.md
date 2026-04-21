# Personas as Design Constraint

Most projects use personas as marketing artifacts — a stock photo, a name, a list of demographics. They get written once and read never. An agentic vault treats personas differently: as the compiled test case every decision has to pass.

## The Shift

A persona in this methodology is not a market segment description. It is a single, specific, named person the project is built for. Their story is concrete enough that a design question can be answered against it.

The test isn't *"would this appeal to our target demographic?"* — too abstract, answerable with AI-generated marketing prose. The test is: *"does this serve this specific person we have described in detail?"* — concrete enough that the answer is usually obvious.

## The Companion Principle

A product good enough for the hardest design target is good enough for anyone. A product that only works for users with high adaptive capacity and abundant resources is a weaker product.

So the persona is not the average user. It's the hardest one to serve. The one with the least institutional trust, the most constrained resources, the most reason to walk away at the first sign of condescension.

Serving that person well is not charity. It's the specification. It produces a system with the robustness that easier personas would never have demanded.

## What Gets Written Down

A persona note is not a character sketch. It includes:

- **The wound.** What specific prior experience does this person bring? Not "bad at math" but *"a ninth-grade teacher told her she wasn't a math type."* The specificity changes the design.
- **The hidden competence.** What is this person already good at that the system can recognize and reflect back?
- **The institutional context.** Which trust signals are available, which are unavailable.
- **The affective signals.** Which tones will land. Which will cause the person to leave.
- **The design implications.** What does serving this person actually require of the system?

## The Common Failure Mode

AI sessions produce persona documents that are essentially demographic boilerplate — age, job title, income bracket, three bullet points of pain. These personas are not design constraints. They're stock photos. Any design decision can be justified against them, because they're too vague to reject anything.

A persona that can be used to reject a design decision is doing its job. A persona that can be used to justify any design decision is not a persona.

## Why This Belongs in the Methodology

Personas interact with every other protocol. [Decision records](decision-records.md) that don't name the persona served are weaker. [Reweave triggers](reweave-protocol.md) often look like *"does this new research change what this person needs?"* The vault's writing discipline exists partly to make persona documents compact enough that they get read, not skimmed.

The persona is the thing the decisions are for. Without it, the decisions are in service of nothing in particular.
