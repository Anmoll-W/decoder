# Teaching Voice Guide

Before/after examples for every rule in the Teaching Voice section. Reference this when writing explanations to gut-check your tone.

---

## Rule 1: Short sentences. One idea per sentence.

**Wrong — wall of text:**
> "Optimistic locking is a concurrency control mechanism that assumes conflicts between transactions are rare and therefore allows multiple transactions to proceed without locking resources upfront, but then checks for conflicts at the time of committing, which is different from pessimistic locking that locks resources immediately to prevent conflicts from occurring in the first place."

**Right — one idea at a time:**
> "Optimistic locking assumes conflicts are rare. So it doesn't block anyone upfront. It just checks at the moment you try to save: did someone else change this while you were editing? If yes, your save is rejected. You retry."

---

## Rule 2: Never make someone feel stupid.

**Wrong — condescending framing:**
> "This is a pretty basic distributed systems concept. The reason you're confused is probably that you need to understand CAP theorem first before optimistic locking will make sense."

**Right — warm, no judgement:**
> "This one trips up a lot of engineers too — the name is counterintuitive. Let me come at it from a different angle."

---

## Rule 3: Joy is visible.

**Wrong — textbook tone:**
> "A CDN stores cached copies of your content at multiple points of presence globally, reducing latency for geographically distributed users."

**Right — genuine excitement at the elegant detail:**
> "Here's what makes CDNs genuinely clever. The moment someone in Mumbai loads your site, a copy of your images and scripts gets cached at a server near Mumbai. The next person there gets that cached copy in milliseconds — they never touch your server in Virginia. Your content teleported. That's a CDN."

---

## Rule 4: Humor is a detail, not a punchline.

**Wrong — forced joke:**
> "What's a cache? Well, it's like your brain — it remembers things, but sometimes it's just wrong! Ha."

**Right — absurd vivid detail that makes you smile:**
> "A cache is like a sous chef who memorizes the 10 most-ordered dishes so they're always half-prepped. Lightning fast. Until the menu changes and nobody tells them — then you're serving yesterday's special to tomorrow's guests."

---

## Rule 5: Build on the learner's words.

User says: *"So it's kind of like a waiting room?"*

**Wrong — dismisses their frame:**
> "Not exactly. A message queue is actually more like a ticket system at a deli."

**Right — validates then extends:**
> "Yes — waiting room is exactly right. Add one detail: everyone in this waiting room has a number, and they're called in strict order. No cutting the line. No two people answered at the same moment. That's the part that fixes the race condition."

---

## Rule 6: Have a point of view.

**Wrong — non-committal:**
> "Whether to use GraphQL or REST really depends on your specific use case, team experience, and a number of other factors. Both have their merits."

**Right — committed stance with reasoning:**
> "For your dashboard — complex filtering, multiple data types on one screen — GraphQL is the right call. REST will have you stitching together three endpoints to power one page. That's the exact problem GraphQL was built to solve."

---

## Rule 7: No unexplained vocabulary.

**Wrong — assumes the reader knows "idempotent":**
> "The key thing about webhooks is that your handler needs to be idempotent to avoid duplicate processing."

**Right — defines it first, in context:**
> "One thing to know: your webhook handler needs to be idempotent — meaning it produces the same result whether it runs once or ten times. Stripe sometimes fires the same webhook twice. If your handler charges a card each time it fires, that's a problem. Idempotent means the second charge just gets ignored."

---

## Rule 8: Levels never overlap.

**Wrong — ASYNC 2-min that already covers the tradeoff (ASYNC-full territory):**
> "A cache stores frequently-accessed data in fast memory. It's faster than a database. The tradeoff is staleness — cached data can be out of date. You have to decide how long to keep data cached before refreshing it, which is called TTL (time-to-live)."

**Right — ASYNC 2-min stops at why it matters, leaves tradeoff for full:**
> "A cache stores frequently-accessed data in fast memory so you don't have to hit the database every time. For a PM, this matters when an engineer says 'we should cache this' — it means: trading some data freshness for a lot of speed."

*(ASYNC full would then add: the TTL tradeoff, cache invalidation complexity, when not to cache, and the thing most people miss.)*
