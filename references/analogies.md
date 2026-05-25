# Character Analogy Bank

Use these when the concept matches. The goal: a character with a specific job, where the job implies the concept's behavior — not just its structure. Always prefer a fresh analogy over a recycled one.

---

## Infrastructure & Servers

**Load balancer**
A maître d' who scans the dining room, spots which sections have capacity, and points every new guest exactly there — nobody waits at the entrance while a table sits empty in the back.

**CDN (Content Delivery Network)**
A chain of local post offices that keeps copies of popular packages nearby. You don't wait for a letter from head office — the nearest branch already has your most-requested items on the shelf.

**Cache**
A sous chef who memorizes the 10 most-ordered dishes so they're always half-prepped — blazing fast until the menu changes and nobody tells them. Stale cache = stale food going out.

**Server**
A personal assistant who sits at a desk all day waiting for requests. When one arrives, they pick it up, do the work, and hand back a result. They can only handle one thing at a time — unless you hire more of them.

**Microservices**
A restaurant where every station — grill, pastry, bar — is its own independent kitchen with its own staff. The expeditor (API gateway) takes your order and routes each item to the right station. Faster to scale one station. Harder to coordinate when the pastry kitchen goes dark.

**Serverless function**
A freelance delivery driver who only shows up when there's a package to deliver. You don't pay them to sit around between orders. When a request comes in, a driver appears, handles it, and disappears. Fast to scale. Cold start is the waiting time before the first driver arrives.

---

## Data & Databases

**Database index**
The index at the back of a textbook. Without it, finding "optimistic locking" means reading every page. With it, you go straight to page 47. The index costs extra space to maintain — but every lookup is instant.

**Optimistic locking**
A shared Google Doc with version numbers. You and a colleague both open the same document. You both edit. When you hit Save, the system checks: is this still version 12? If your colleague already saved and it's now version 13, your save is rejected. You retry. Nobody was blocked — just caught at the commit.

**Pessimistic locking**
The same Google Doc, but when you open it, you lock it. Your colleague sees "read only" until you close it. Perfectly safe. Completely slow — especially if you opened it and went to lunch.

**Database transaction**
A bank transfer: debit one account, credit another. If either step fails, neither happens. The database refuses to live in a world where the money left one account but never arrived in the other.

**Eventual consistency**
Posting a photo on Instagram and calling your friend in another city to ask if she can see it. She refreshes — nothing. You see it. Thirty seconds later, you both see it. Instagram didn't wait for every server in every region to confirm receipt. They said "saved" and synced in the background.

**Sharding**
A library that's grown too large for one building, so they split the collection: A–M in Building 1, N–Z in Building 2. Every librarian knows the rule. Books are found faster. But moving a book that crosses the boundary is now a project.

---

## APIs & Communication

**API (Application Programming Interface)**
A hotel concierge who takes your request — restaurant reservation, taxi, spa booking — knows exactly which department handles it, and comes back with the answer. You never go to the kitchen yourself. The concierge is the interface. The kitchen is the implementation.

**Webhook**
A hotel's fire alarm. It doesn't wait for guests to ask "is there a fire?" The moment something happens, it pushes an alert to wherever you've told it to. You configure the destination; the system fires it automatically when the event occurs.

**Message queue**
A deli counter with a ticket system. When 100 customers arrive at once, everyone takes a number. The counter works through tickets in strict order — no collisions, no skipped orders, no two people being served simultaneously at the same station.

**REST API**
A standard government form. Every request has a fixed format: what you want, where it lives, what you're sending. Predictable. Cacheable. Any client knows how to fill it out. The tradeoff: you sometimes get back more than you asked for.

**GraphQL**
A custom order form at a diner where you write exactly what you want — no default sides, no bundled extras. The kitchen returns exactly what's on the ticket, nothing more. More flexible. The kitchen needs a smarter cook and can't cache the way a standard menu can.

**Rate limiting**
A bouncer at a club who counts how many people come through the door per minute. No matter how many are waiting outside, only 100 get in per minute. Everyone else waits. If you're an important guest, you get a faster lane.

---

## Software Development

**Git branch**
A scribe who copies your entire manuscript into a private workroom before making any edits. They work in isolation — whatever they do in that room, the original in the main library is untouched. When their edits are approved, a librarian merges both manuscripts. If the edits were a disaster, the workroom copy is discarded. Nothing in the original library ever saw the mess.

**CI/CD pipeline**
A car assembly line with quality-control stations at every step. The code moves automatically through testing, linting, and build checks. If any station finds a defect, the line stops before the car reaches the customer — not after.

**Docker container**
A lunchbox that contains not just your meal but your plate, your fork, and the microwave to heat it up. Wherever you take it — your laptop, the cloud, your colleague's machine — it works exactly the same way.

**Environment variable**
A sticky note on the fridge that says "WiFi password: X". The app reads the sticky note instead of having the password baked into its source code. Change the sticky note, the app uses the new value. No code change, no deployment.

**Feature flag**
A light switch installed next to a new feature. The code is fully built and deployed. The switch controls whether it's on. You flip it on for 1% of users, watch what happens, and kill it in seconds if something breaks — no deployment, no rollback.

---

## AI & Machine Learning

**Model training**
A chef studying 10,000 recipes before their first day in the kitchen. They don't memorize each recipe — they build intuition: what flavors pair together, what techniques work at what temperature. Training is the studying. Inference is the cooking.

**Fine-tuning**
Taking that trained chef and giving them 200 recipes from your specific restaurant. They keep all their general cooking instincts but adapt to your menu, your customers, your kitchen's equipment.

**Embeddings**
A city map where similar things live in the same neighborhood. "Dog" and "puppy" are neighbors on the same block. "Dog" and "mortgage" are on opposite sides of the city. When you search, you find everything in the right neighborhood — even if the exact street address doesn't match.

**RAG (Retrieval-Augmented Generation)**
A lawyer who answers your question by first going to the library, pulling the three most relevant case files, reading them, and then responding — instead of answering purely from memory. More accurate. More current. Slower than guessing.

**Hallucination**
A confident intern who fills in the blanks they don't know with plausible-sounding details they invented. The tone is certain. The facts are wrong. The fix: give them the source documents (RAG) or double-check anything that sounds surprising.

---

## Product & Analytics

**A/B test**
Two menus in the same restaurant, given to different tables without telling anyone. Table A gets Menu 1. Table B gets Menu 2. You measure which table orders more dessert. The winner becomes the new menu for everyone.

**Feature flag** *(product framing)*
A dimmer switch on a new feature. You dial it from 0% to 100% gradually — 1% of users, then 5%, then 50%. You're watching for the moment the lights flicker before committing to full brightness.

**Funnel**
A coffee filter. Lots of water goes in at the top. Only some makes it through each stage. The drip rate at the bottom is your conversion. Most PM analysis is one question: which stage has the worst drip rate, and why?

**Churn**
Restaurant regulars who stop coming back. You don't always know why. Sometimes it's the food. Sometimes it's the price. Sometimes they just moved. The question is: did they leave because of something you could fix?
