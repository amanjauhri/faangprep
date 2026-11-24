#!/usr/bin/env python3
"""Writes data/curriculum.json: the 60-day plan (titles, subtopics, problems, dates).
Run: python3 build/curriculum.py  (from the repo root)."""
import datetime as dt, json, os

START = dt.date(2026, 11, 25)  # Day 1 (Wednesday). Sundays are off.

PHASES = [(1, 12, "Foundations"), (13, 24, "Core patterns"), (25, 36, "Going deeper"),
          (37, 48, "Design & depth"), (49, 60, "Interview mode")]

# DSA: title | subtopics | problems "num Title"
DSA = """How to approach a coding interview + Big-O from scratch|What a coding interview really tests;The 4-step method: understand, plan, code, test;Big-O: how code slows down as input grows;Reading a loop to find its Big-O;Space complexity|217 Contains Duplicate
Arrays and hash maps|How arrays sit in memory;How a hash map finds things in O(1);The "have I seen this before?" pattern|1 Two Sum;242 Valid Anagram
Hashing: grouping and counting|Counting with a map;Choosing a good key;Bucket sort for top-K|49 Group Anagrams;347 Top K Frequent Elements
Prefix sums|What a running total is;Range sums in O(1);Prefix sum + hash map|238 Product of Array Except Self;560 Subarray Sum Equals K
Sets and sequences|Membership checks with a set;Finding where a sequence starts;Validating grids with sets|128 Longest Consecutive Sequence;36 Valid Sudoku
Week 1 review + first timed mock|How to run a mock on yourself;Self-review checklist;Patterns so far|121 Best Time to Buy and Sell Stock;169 Majority Element
Two pointers|Pointers from both ends;Sorted input is a signal;Skipping duplicates|125 Valid Palindrome;167 Two Sum II - Input Array Is Sorted;15 3Sum
Two pointers 2|Greedy pointer moves;Why moving the smaller side works|11 Container With Most Water;42 Trapping Rain Water
Sliding window|Fixed vs variable windows;Expand and shrink;Tracking what is inside the window|3 Longest Substring Without Repeating Characters;424 Longest Repeating Character Replacement
Sliding window 2|Frequency maps inside a window;The minimum-window technique|567 Permutation in String;76 Minimum Window Substring
Stacks|Last in, first out;Matching brackets;Stacks in Java (ArrayDeque)|20 Valid Parentheses;155 Min Stack;150 Evaluate Reverse Polish Notation
Monotonic stack + week 2 review|What "monotonic" means;Next greater element;When to reach for it|739 Daily Temperatures;853 Car Fleet
Binary search|Halving the search space;lo, hi, mid and off-by-one errors;One template that always works|704 Binary Search;74 Search a 2D Matrix
Binary search on the answer|Searching a range of possible answers;Writing a feasibility check|875 Koko Eating Bananas;1011 Capacity To Ship Packages Within D Days
Binary search on tricky inputs|Rotated arrays;Finding the sorted half|33 Search in Rotated Sorted Array;153 Find Minimum in Rotated Sorted Array;981 Time Based Key-Value Store
Linked lists|Nodes and pointers;Reversing a list;The dummy-head trick|206 Reverse Linked List;21 Merge Two Sorted Lists
Linked lists 2|Fast and slow pointers;Cycle detection;Reordering in place|141 Linked List Cycle;143 Reorder List;19 Remove Nth Node From End of List
LRU cache + week 3 review|Hash map + doubly linked list;O(1) get and put|146 LRU Cache;2 Add Two Numbers
Trees: the basics|Tree vocabulary;Recursion on trees;DFS orders: pre, in, post|226 Invert Binary Tree;104 Maximum Depth of Binary Tree;100 Same Tree
Trees: DFS patterns|Returning values up the tree;Height and diameter|543 Diameter of Binary Tree;110 Balanced Binary Tree;572 Subtree of Another Tree
Trees: BFS|Queues and level order;Seeing the tree level by level|102 Binary Tree Level Order Traversal;199 Binary Tree Right Side View
Binary search trees|The BST rule;In-order traversal is sorted;Validating a BST|98 Validate Binary Search Tree;230 Kth Smallest Element in a BST;235 Lowest Common Ancestor of a Binary Search Tree
Trees: hard problems|Building a tree from traversals;Maximum path sum|105 Construct Binary Tree from Preorder and Inorder Traversal;124 Binary Tree Maximum Path Sum
Heaps + week 4 review|What a heap is;Top-K with a heap;PriorityQueue in Java|703 Kth Largest Element in a Stream;215 Kth Largest Element in an Array;973 K Closest Points to Origin
Heaps 2|Two heaps for a running median;Scheduling with a heap|295 Find Median from Data Stream;621 Task Scheduler
Tries|Prefix trees;Insert, search, startsWith;Wildcard search|208 Implement Trie (Prefix Tree);211 Design Add and Search Words Data Structure
Intervals|Sort by start;Merging overlaps;Counting overlaps|56 Merge Intervals;57 Insert Interval;435 Non-overlapping Intervals
Backtracking|Choose, explore, un-choose;Subsets and permutations|78 Subsets;46 Permutations
Backtracking 2|Pruning;Combination sums;Searching a grid|39 Combination Sum;79 Word Search;22 Generate Parentheses
Graphs + week 5 review|Graph vocabulary;Adjacency lists;BFS vs DFS on grids|200 Number of Islands;695 Max Area of Island
Graphs 2|Multi-source BFS;Cloning a graph;Flowing from borders|994 Rotting Oranges;133 Clone Graph;417 Pacific Atlantic Water Flow
Topological sort|Dependencies as a graph;Kahn's algorithm;Detecting cycles|207 Course Schedule;210 Course Schedule II
Union-find and shortest paths|Union-find;Dijkstra's algorithm;Minimum spanning tree|684 Redundant Connection;743 Network Delay Time;1584 Min Cost to Connect All Points
Dynamic programming: the basics|What DP is;Recursion, then memo, then table|70 Climbing Stairs;198 House Robber;213 House Robber II
Dynamic programming 1D|Coin change;Word break;Palindromes|322 Coin Change;139 Word Break;5 Longest Palindromic Substring
Dynamic programming 2D + week 6 review|Grid DP;Longest common subsequence;Longest increasing subsequence|62 Unique Paths;1143 Longest Common Subsequence;300 Longest Increasing Subsequence
Knapsack and greedy|0/1 knapsack idea;Kadane's algorithm;When greedy is safe|416 Partition Equal Subset Sum;53 Maximum Subarray;55 Jump Game
Matrix and bit tricks|In-place matrix moves;Bit operations basics|48 Rotate Image;54 Spiral Matrix;136 Single Number;191 Number of 1 Bits
Design-style data structures|Combining structures for O(1) operations|380 Insert Delete GetRandom O(1);1396 Design Underground System
SQL for bank online tests|Joins;GROUP BY;Window functions|176 Second Highest Salary;184 Department Highest Salary;185 Department Top Three Salaries
Concurrency coding problems|Coordinating threads in code|1114 Print in Order;1115 Print FooBar Alternately
Mixed review + week 7 mock|Timed mixed set|1249 Minimum Remove to Make Valid Parentheses;528 Random Pick with Weight
Hard practice 1|Stacks and trees at hard level|84 Largest Rectangle in Histogram;297 Serialize and Deserialize Binary Tree
Hard practice 2|Heaps and binary search at hard level|23 Merge k Sorted Lists;4 Median of Two Sorted Arrays
Graph practice|BFS on words;Weighted graph queries|127 Word Ladder;399 Evaluate Division
Greedy practice|Grouping greedily;Interval greedy|846 Hand of Straights;452 Minimum Number of Arrows to Burst Balloons
String practice|String parsing;Custom sorting|151 Reverse Words in a String;692 Top K Frequent Words;937 Reorder Data in Log Files
Full mock loop + week 8 review|One coding round, one design round|Pick 2 unseen Mediums
Google focus|Google-style problems|1268 Search Suggestions System;17 Letter Combinations of a Phone Number
Meta focus|Meta-style problems|236 Lowest Common Ancestor of a Binary Tree;680 Valid Palindrome II
Amazon focus|Amazon-style problems|763 Partition Labels;138 Copy List with Random Pointer
Microsoft focus|Microsoft-style problems|8 String to Integer (atoi);73 Set Matrix Zeroes
Bank online test practice|HackerRank-style timed set|202 Happy Number;409 Longest Palindrome
Weak-spot review 1|Redo problems from your mistake log|Redo 3 from mistake log
Mock with a human|Peer or paid mock|2 unseen Mediums
Hard mix|DP and stack at hard level|72 Edit Distance;32 Longest Valid Parentheses
AI-enabled round practice|Multi-part problem with an AI assistant|One multi-part problem
Weak-spot review 2|Redo problems from your mistake log|Redo 3 from mistake log
Final mock|Full coding round|2 unseen Mediums
Wrap-up: pattern cheat sheet|All patterns on one page|-"""

JAVA = """How Java runs: JDK, JRE, JVM, bytecode and the JIT
Memory basics: stack vs heap, references, primitives vs objects, autoboxing
Strings: immutability, the String pool, StringBuilder
OOP refresher: encapsulation, inheritance, polymorphism, abstraction
Abstract classes vs interfaces; composition over inheritance
Week 1 review: core Java quiz
equals() and hashCode(): the contract and why it matters
The Collections framework map: List, Set, Map, Queue
ArrayList vs LinkedList: how they work inside
HashMap internals: hashing, buckets, resizing, treeification
TreeMap, LinkedHashMap, Comparable vs Comparator
Generics and type erasure + week 2 review
Exceptions: checked vs unchecked, try-with-resources
Lambdas and functional interfaces
Streams API: map, filter, reduce, collectors
Modern Java: Optional, records, sealed classes, switch patterns
JVM memory areas: heap, stack, metaspace
Garbage collection basics + week 3 review
GC collectors (G1, ZGC), tuning and memory leaks
Threads 101: Thread, Runnable, lifecycle
synchronized and race conditions
volatile and the Java Memory Model
Deadlock, livelock, starvation
Week 4 review: concurrency basics quiz
ExecutorService and thread pools
Locks: ReentrantLock, ReadWriteLock, Condition
Concurrent collections: ConcurrentHashMap, BlockingQueue
CompletableFuture and async code
Atomics, CAS and producer-consumer
Virtual threads (Java 21) + week 5 review
Spring Core: IoC, dependency injection, bean scopes and lifecycle
Spring Boot: auto-configuration, starters, profiles
Spring MVC and REST: controllers, validation, error handling
Spring Data JPA and Hibernate: entities, lazy loading, N+1
@Transactional: propagation, isolation, rollback
Spring AOP and proxies + week 6 review
Spring Security: filter chain, JWT, OAuth2
Spring Kafka: consumers, retries, dead-letter topics
Caching (@Cacheable, Redis) and resilience (Resilience4j)
Testing Spring Boot: JUnit 5, Mockito, Testcontainers
SOLID part 1: Single Responsibility, Open/Closed
SOLID part 2: Liskov, Interface Segregation, Dependency Inversion + week 7 review
Design patterns 1: Singleton, Factory, Builder
Design patterns 2: Strategy, Observer, Template Method
Design patterns 3: Adapter, Decorator, Chain of Responsibility
Microservice patterns in Spring: gateway, saga, outbox
Observability in Spring Boot: Actuator, Micrometer, tracing
How to do a low-level design round + parking lot
LLD: thread-safe LRU cache and rate limiter
LLD: Splitwise
LLD: elevator system
LLD: BookMyShow (concurrent seat booking)
LLD: order book / matching engine
LLD: Amazon locker
Rapid-fire: 30 Java and Spring questions
Bank Java round: 25 core Java and Spring questions
Clean Spring Boot structure for take-home tasks
Weak-spot review: Java, Spring, LLD
Mock low-level design round
One-page Java and Spring cheat sheet"""

DESIGN = """What system design interviews test + client and server basics
The journey of a request: DNS, HTTP and HTTPS
Latency vs throughput, and the numbers to know
Scaling up vs scaling out; stateless services
Load balancers: L4 vs L7
Week 1 review: draw a basic web architecture
Caching basics
Cache strategies and invalidation
CDNs: serving content close to users
SQL vs NoSQL
Database indexes
Replication + week 2 review
Sharding and partitioning
Consistent hashing
CAP theorem and consistency models
Message queues and Kafka basics
Idempotency and exactly-once processing
API design: REST vs gRPC, pagination + week 3 review
Back-of-the-envelope estimation
Rate limiting algorithms
Microservices vs monolith; API gateway
Observability: logs, metrics, traces
Object storage and large files
The system design interview framework + full design: URL shortener
Unique ID generation
Distributed transactions: two-phase commit, sagas, outbox
Event sourcing and CQRS
Real-time: WebSockets, server-sent events, polling
Consensus and leader election
Full design: rate limiter + week 5 review
Bloom filters and probabilistic structures
Search and inverted indexes
Batch vs stream processing
Security basics: authentication, authorization, encryption
Disaster recovery and multi-region
Full design: payments and ledger + week 6 review
Distributed locks
Location search: geohash and quadtrees
Data warehouse vs lake vs lakehouse
Full design: notification system
Full design: news feed
Full design: AI assistant over documents (RAG)
Full design: job scheduler
Full design: real-time event pipeline
Full design: chat system
Full design: LLM chatbot at scale
Presenting your own project's design
Mock design round + scoring rubric
Google-style: collaborative document editing
Meta-style: live comments
Amazon-style: order checkout
Microsoft-style: file storage and sync
Bank-style: order matching and trade booking
Top-K and heavy hitters
Distributed cache
Startup-style: an MVP that can scale
Trade-off language interviewers want to hear
Redo your hardest design
Full mock design in 45 minutes
One-page system design cheat sheet"""

AI = """Using AI as your study coach (not a cheat sheet)
What an LLM is: tokens and next-word prediction
Context windows, temperature, and why answers vary
Prompting basics: role, context, constraints, examples
How AI shows up in 2026 interviews (Meta, Google, Amazon)
Week 1 review: an AI-assisted solve, start to finish
Hallucinations and how to verify AI output
Using AI to generate test cases
AI-assisted debugging
Embeddings: meaning as numbers
Vector databases and similarity search
RAG basics + week 2 review
Making RAG good: chunking, retrieval, re-ranking
Tool calling: how LLMs use APIs
Agents and MCP
Evals: measuring if an AI feature works
Structured outputs: reliable JSON from LLMs
Guardrails and prompt injection + week 3 review
Code comprehension with AI (Google's new round)
Thinking aloud while using AI
Spec-first prompting
AI coding agents: Copilot, Claude Code, Cursor
When not to use AI in an interview
First AI-enabled mock + week 4 review
Caching in LLM apps
LLM serving: latency, tokens per second, cost
Fine-tuning vs RAG vs prompting
The AWS GenAI stack: Bedrock, SageMaker, Amazon Q
Amazon's GenAI fluency questions
Second AI-enabled mock + week 5 review
Responsible AI in regulated finance
Reviewing code that AI wrote
Text-to-SQL and its risks
Your "how I use GenAI" interview story
Where GenAI fits in fintech systems
Week 6 review: AI concepts quiz
Model routing and fallbacks
Recommendations with embeddings
Orchestrating AI agent workflows
Adding LLM features to streaming pipelines
Exploring design trade-offs with AI
AI in system design: the RAG design day
Using AI to grade your mock
Learning a new codebase fast with AI
Building a feature with an AI coding agent
How banks govern AI use
How you would add AI to your IA platform
Week 8 review
Simulating Google's code comprehension round
Simulating Meta's AI-enabled round
GenAI fluency drill
Copilot in VS Code: a timed task
AI-specific behavioral questions
A personal drill built from your mistake log
Debriefing a mock with AI
AI news briefing for interviews
Take-home task with AI
Drafting your AI pitch
Final AI-enabled mock
Your 60-second AI pitch"""

def dates():
    d, out = START, []
    while len(out) < 60:
        if d.weekday() != 6:
            out.append(d)
        d += dt.timedelta(days=1)
    return out

def phase(n):
    return next(p for a, b, p in PHASES if a <= n <= b)

def main():
    dsa = [l.split("|") for l in DSA.strip().split("\n")]
    java = JAVA.strip().split("\n"); design = DESIGN.strip().split("\n"); ai = AI.strip().split("\n")
    assert len(dsa) == len(java) == len(design) == len(ai) == 60, (len(dsa), len(java), len(design), len(ai))
    days = []
    for i, d in enumerate(dates()):
        t, subs, probs = dsa[i]
        days.append({"day": i + 1, "date": d.isoformat(), "phase": phase(i + 1),
                     "dsa": {"title": t, "subtopics": [s for s in subs.split(";") if s],
                             "problems": [p for p in probs.split(";") if p and p != "-"]},
                     "java": {"title": java[i]}, "design": {"title": design[i]}, "ai": {"title": ai[i]}})
    out = {"start": START.isoformat(), "phases": [{"name": p, "from": a, "to": b} for a, b, p in PHASES], "days": days}
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    with open(os.path.join(root, "data", "curriculum.json"), "w") as f:
        json.dump(out, f, indent=1, ensure_ascii=False)
    print("Day 1", days[0]["date"], "Day 48", days[47]["date"], "Day 60", days[59]["date"])

if __name__ == "__main__":
    main()
