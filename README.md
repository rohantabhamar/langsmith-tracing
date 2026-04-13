# LangSmith Tracing

LangSmith observability for LangChain and LangGraph pipelines.

## Files
| File | What it demonstrates |
|---|---|
| 1_simple_llm_call.py | Basic @traceable on a single LLM call |
| 2_sequential_chain.py | Tracing a sequential LangChain chain |
| 3_rag_v1–v4.py | RAG pipeline tracing across 4 versions |
| 4_agent.py | Agent run tracing with tool calls |
| 5_langgraph.py | Parallel fan-out LangGraph — 3 nodes run simultaneously, scores merged with operator.add, Pydantic structured output, full metadata + tags |

## Key patterns in 5_langgraph.py
- @traceable with name, tags, metadata per node
- Annotated[List[int], operator.add] for parallel score merging
- 3 parallel evaluator nodes → 1 aggregator
- Pydantic EvaluationSchema with Field() constraints
- run_name, tags, metadata passed in config

## Tech stack
LangSmith · LangGraph · LangChain · OpenAI GPT-4o-mini · Pydantic
