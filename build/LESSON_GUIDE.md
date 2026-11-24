# How to write a daily lesson

Every morning one new file, `data/lessons/day-NN.json`, is added. The FAANG Prep dashboard (`index.html`) renders it. `data/lessons/day-01.json` is the reference example: match its structure, depth and tone exactly.

## The reader
Aastha: about 8 years as a software engineer (TCS for client NCDEX, then about 6 years at JPMorgan, SDE1 to SDE3). Her stack: Java, Spring Boot, AWS (EKS, ECS, Lambda, Step Functions, Kinesis), Kafka, Airflow, Python/PySpark, Databricks, Oracle, Postgres, MySQL, Cassandra. Her key projects: the Income Attribution (IA) platform at JPMorgan (designed from scratch; a Kinesis-triggered PySpark pipeline on general-ledger refresh; a Spring Boot web app with pivot views for finance controllers; replaced a manual Excel process across Trading, Sales, Payments and Securities) and a netting engine (Airflow, Spring Boot, Kafka, Kubernetes, postings to SAP). She has not interviewed for 6 years. Interview language: Java. Targets: Google, Amazon, Microsoft, Meta, banks (UBS, Morgan Stanley, Nomura) and startups. She resigns around mid-January 2027.

## Interview first (most important)
Everything is preparation for interviews. Every track of every lesson must include `interview_angle` {asked_at, how_it_comes_up, strong_answer, pitfalls}: where this is asked (name companies: Google, Amazon, Microsoft, Meta, UBS, Morgan Stanley, Nomura, startups), how the question is actually phrased, what a strong answer sounds like, and the common mistakes. Explanations should keep pointing back to "this is what you'll say in the interview". Interview questions get model answers she can say out loud in 30–60 seconds. Where it fits, give her a line she can use about her own experience (the IA platform, the netting engine, Spring Boot on EKS, Kafka, Kinesis, Airflow), phrased honestly as "if you did X, say Y".

## Teaching style
- **Start from scratch, then build up.** She knows a lot, but it has been years since she prepared, so assume nothing. Every subtopic starts with the plain idea, then adds detail until it reaches interview level.
- **No unexplained jargon.** The first time a term appears, explain it in plain words (in the sentence, or in brackets). Add it to the day's glossary.
- **Structured, not a wall of text.** 3–6 subtopics per track, in a logical order. Each subtopic: a one-line summary (`in_one_line`), then 2–5 blocks. Prefer tables, steps and flows to long paragraphs. Paragraphs at most 3 short sentences.
- **Connect the dots.** `builds_on` names the earlier day(s) and idea this relies on; `next` says what the next lesson in the track does with it. The top-level `connections` list (2–4 items) links today's four tracks to each other.
- **Tie to her work** with a `callout` of tone `work` titled "From your JPMorgan work" when it genuinely fits (Spring Boot services, Kafka, Kinesis, Airflow, Cassandra/Oracle, the IA platform, the netting engine). Never invent facts about her projects; phrase as "if you have seen X, this is why".
- **Analogies** where they make a new idea click, kept short.
- Short sentences, everyday words, precise. British/Indian English spelling is fine. No emoji in text.

## Per track
- `dsa` (Coding patterns): explain the pattern from zero (what it is, the signal in a problem that tells you to use it, a Java template, Big-O). Then `problems`: every problem listed for the day in `data/curriculum.json`, each with statement, example, `how_to_think` (brute force first, then the improvement), 2–3 graded `hints`, a full `solution` (approach steps, correct and commented Java, time, space), optional `alternatives` (name/time/space/note) and `followups`. Check the Java against the example by hand. LeetCode URLs use the official slug: `https://leetcode.com/problems/<slug>/`.
- `java` (Java & Spring): explain the concept from zero, then how it works inside, a small realistic Java or Spring code example, common mistakes, and why interviewers ask it. 3–5 `interview_qa` with model answers.
- `design` (System design): build-up topics get the plain idea, a `flow` diagram, trade-offs in a table, failure modes. Full-design days walk through requirements → estimates → API → data model → high-level design (flow) → deep dives → trade-offs.
- `ai` (AI skills): plain explanation, why companies ask about it now, a hands-on exercise that includes checking the AI's output herself, and a copy-paste `prompt` for her Interview Coach chat. Remind her she can type QUIZ JAVA in that chat.
- Every track: `minutes` (dsa ~40, java ~15, design ~10–15, ai ~10; system-design days can make design ~30), `level` (Basics, Intermediate or Interview level, rising over the 60 days), `takeaways` (3–5), `resources` (2–3 real https links: official docs such as docs.oracle.com, dev.java, docs.spring.io, openjdk.org; Baeldung; System Design Primer; NeetCode; reputable articles). Only link pages you are confident exist.

## Day-level fields
`day`, `date` (YYYY-MM-DD), `phase` (copy from curriculum), `headline` (one line on what today is about), `intro` (2–3 sentences), `connections`, `tracks`, `glossary` (8–15 new terms with plain meanings; do not repeat terms from earlier days). The first interview question of each track appears in the Today page warm-up, so make it the most commonly asked one.

## Block types
`p` {text} · `steps` {items} · `list` {items} · `table` {head, rows} · `code` {code, lang} · `flow` {items:[{label, note}]} · `callout` {tone: tip|warn|work, title, text} · `compare` {items:[{title, points}]}. Text supports **bold** and `code` only. No HTML.

## Rules
- Follow the titles and problems in `data/curriculum.json` for the day; you may refine subtopics.
- Paraphrase sources; never copy more than a few words.
- Run `python3 build/validate.py data/lessons/day-NN.json data/news.json` and fix everything it reports before publishing.

## AI news (`data/news.json`)
Exactly 2 items (the dashboard shows them as small rows), from the last 7 days that matter to a software engineer job-hunting in big tech: AI in interviews and hiring, coding agents, major model releases, AI in banking. Each: date, tag (Hiring, Interviews, Models, Tools, Banking, Policy), a short headline, a 1-sentence summary, "why it matters for you" in 1 short sentence tied to her interviews, source name, real URL from your search results. Never invent news or links.
