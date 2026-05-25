# Decoder

*A tool by [The PM Code](https://www.linkedin.com/company/the-pm-code/) — follow us on LinkedIn*

---

You are in the standup. Your engineer is talking. They say something like:

> "We need to add a message queue because the webhook processing is causing race conditions."

You nod. You write it down. You move on.

Later that afternoon, your manager asks what the sprint is focused on. You say "infrastructure work." They ask what kind. You pause.

You didn't understand what your engineer said. You understood the words. Not the meaning.

This happens to every PM. Not because they are not smart. Because no one built a tool for this moment.

---

## Decoder

Decoder is a Claude Code skill. Drop in a technical term, paste a doc, or describe what your engineer just said — and Decoder explains it at exactly the right depth for where you are. In a standup. Reading a spec. Making an approval call.

It does not just define things. It teaches them. With an analogy. With the non-obvious tradeoff. With one smart question you can bring back to the engineer.

Here is what it looks like in action:

```
You: my engineer just said we need to add a message queue because the
     webhook processing is causing race conditions — what does that mean

Decoder: Let me look this up first...

Your system receives a signal from outside — say, Stripe fires "payment
succeeded" — and immediately tries to do 5 things at once: update the
order, send the email, unlock the feature. Two of those tasks crash into
each other. That's the race condition.

Think of it like a deli counter. Right now, 100 customers are shouting
their orders at the kitchen simultaneously. A message queue gives everyone
a number. The counter works through tickets in order. No collisions.

One smart question to ask your engineer: "What's the failure behavior if
a message sits in the queue and never gets processed — does it retry
automatically or do we need to build that?"
```

You walked in not knowing what a race condition was. You walked out with the concept, the analogy, and a question that will make your engineer think.

---

## Three Modes

Decoder reads the context of your question and picks the right mode automatically. You never have to say which one you want.

**LIVE** — you are in the meeting right now. Short urgent phrasing, no time to spare. Decoder gives you the analogy and the bottom line in four sentences. Enough to stop nodding and start participating.

**ASYNC** — you are reading a doc, a spec, an RFC, or a PR. You dropped a URL or described something you saw. Decoder asks how deep you want to go, then teaches the full mechanism: how it works, the tradeoffs, and the thing most engineers hand-wave past.

**DECISION** — your team wants to approve a migration, adopt a new framework, or make an architectural call. Decoder asks the one clarifying question that changes the recommendation, then gives you a committed stance. Not "it depends." An actual answer.

---

## What Makes It Different

Most explanations give you a definition. Decoder gives you a character.

Not "a cache is like a sticky note." That tells you nothing about when the sticky note is wrong.

This: *"A cache is like a sous chef who memorizes the 10 most-ordered dishes so they are always half-prepped — fast until the menu changes and nobody tells them."*

Now you understand the mechanism. You understand the failure mode. You understand why your engineer might be nervous about cache invalidation.

Every explanation has one of these. A character with a specific job. A job that implies behavior. Behavior you remember.

---

## The Quiz Mechanic

In ASYNC mode, Decoder offers a quiz after the explanation. Not definition recall. Scenario-based application.

Something like:

> Your payment webhook is firing 100 times a second and your database can only handle 20 writes per second. What breaks, and what does a message queue fix?

If you get it right, you get the earned reveal — the non-obvious implication that even engineers miss. The thing people screenshot.

If you get it wrong, Decoder names what you got right first, then comes at the concept from a different angle with a new analogy. You leave feeling like you figured it out, not corrected.

---

## Install

**Option 1 — git clone**

```bash
git clone https://github.com/Anmoll-W/decoder ~/.claude/skills/decoder
```

**Option 2 — curl**

```bash
curl -fsSL https://raw.githubusercontent.com/Anmoll-W/decoder/main/SKILL.md \
  -o ~/.claude/skills/decoder/SKILL.md
```

Once installed, Decoder activates automatically inside Claude Code whenever you ask about a technical term, paste a doc, or signal that you are trying to understand something your engineer said.

No configuration. No setup. Just ask.

---

## Built For

PMs who want to actually understand what they are building. Not just manage the people building it.

Senior PMs who are tired of nodding. Junior PMs who are scared to ask. Anyone who has discovered — two days after the standup — that they approved something they did not understand.

Decoder does not make you an engineer. It makes you the PM who asks the question that changes the meeting.

---

*Built by [The PM Code](https://www.linkedin.com/company/the-pm-code/) — follow along as we build in public.*
