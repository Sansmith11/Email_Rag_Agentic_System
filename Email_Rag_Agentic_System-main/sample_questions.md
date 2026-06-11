# Sample Questions, Expected Citations, and Agent Routing

## Thread Used

```text
T-0002
```

---

## Question 1

### Query

```text
What does the contract say?
```

### Expected Routing

```text
Entity Resolution Agent
→ Query Breakdown Agent
→ Attachment Retrieval
→ Citation Validator Agent
```

### Expected Citation

```text
sample_contract.txt
```

---

## Question 2

### Query

```text
What budget was approved?
```

### Expected Routing

```text
Entity Resolution Agent
→ Query Breakdown Agent
→ Attachment Retrieval
→ Citation Validator Agent
```

### Expected Citation

```text
sample_contract.txt
```

---

## Question 3

### Query

```text
When was the contract signed?
```

### Expected Routing

```text
Entity Resolution Agent
→ Query Breakdown Agent
→ Attachment Retrieval
→ Citation Validator Agent
```

### Expected Citation

```text
sample_contract.txt
```

---

## Question 4

### Query

```text
What does the document mention?
```

### Expected Routing

```text
Entity Resolution Agent
→ Query Breakdown Agent
→ Attachment Retrieval
→ Citation Validator Agent
```

### Expected Citation

```text
sample_contract.txt
```

---

## Question 5

### Query

```text
What are the issues discussed?
```

### Expected Routing

```text
Entity Resolution Agent
→ Query Breakdown Agent
→ Email Retrieval
→ Citation Validator Agent
```

### Expected Citation

```text
Email Message ID
```

---

## Question 6

### Query

```text
What tasks remain to be completed?
```

### Expected Routing

```text
Entity Resolution Agent
→ Query Breakdown Agent
→ Email Retrieval
→ Citation Validator Agent
```

### Expected Citation

```text
Email Message ID
```

---

## Question 7

### Query

```text
What are the issues and what tasks remain?
```

### Expected Routing

```text
Entity Resolution Agent
→ Query Breakdown Agent
→ Multiple Sub Queries
→ Retrieval
→ Citation Validator Agent
```

### Expected Citation

```text
Email Message ID
```

---

## Question 8

### Query

```text
What did we just discuss?
```

### Expected Routing

```text
Entity Resolution Agent
→ Query Breakdown Agent
→ Retrieval
→ Citation Validator Agent
```

### Expected Citation

```text
Conversation Context / Retrieved Source
```

---

# Graceful Failure Example

### Query

```text
What is the CEO salary?
```

### Expected Behavior

```text
No relevant information found.
```

### Expected Routing

```text
Entity Resolution Agent
→ Query Breakdown Agent
→ Retrieval
→ Citation Validator Agent
```

### Expected Citation

```text
None
```
