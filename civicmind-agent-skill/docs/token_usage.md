# Token Usage Design

CivicMind Agent is designed as a high-token, long-context, multi-agent research workflow.

## Why It Requires High Token Budget

| Stage | Token Need |
|---|---|
| Source ingestion | Policy files, reports, filings and news materials can be very long. |
| RAG retrieval | Retrieved evidence must be placed into context for reasoning. |
| Source scoring | Each source requires metadata, summary and credibility analysis. |
| Entity extraction | Long source texts must be parsed into structured data. |
| Trend reasoning | Multi-step reasoning requires keeping prior facts in context. |
| Risk analysis | Risks require classification, severity scoring and trigger conditions. |
| Strategy generation | Output varies by user role and requires detailed recommendations. |
| Report generation | Full reports can be thousands of words. |
| Evaluation loop | Quality checks require rereading the report and evidence map. |

## Estimated Token Consumption Per Full Research Task

| Component | Estimated Tokens |
|---|---:|
| User query and research plan | 1,000 - 3,000 |
| Source snippets / RAG context | 20,000 - 80,000 |
| Extraction intermediate outputs | 5,000 - 15,000 |
| Credibility scoring | 3,000 - 10,000 |
| Trend reasoning | 5,000 - 20,000 |
| Risk matrix | 3,000 - 8,000 |
| Strategy recommendations | 3,000 - 10,000 |
| Final report | 5,000 - 20,000 |
| Quality review and revision | 5,000 - 15,000 |

A single complete task may require tens of thousands to hundreds of thousands of tokens depending on the number and length of sources. Batch research and RAG testing require substantially higher usage.
