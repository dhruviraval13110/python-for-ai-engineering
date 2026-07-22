# Step 1: Repository Audit & Transformation Plan

This strategy transforms a student/hobbyist GitHub account into a **Principal AI Engineer Portfolio** aligned with hiring requirements at OpenAI, Anthropic, Google DeepMind, NVIDIA, Microsoft, Hugging Face, Meta AI, and top AI startups.

---

## 🔍 Audit Methodology & Evaluation Criteria

Every repository is evaluated against 5 criteria:
1. **Technical Depth**: Does it demonstrate PyTorch, Transformer architectures, RAG, Multi-Agent systems, or low-level MLOps?
2. **Production Quality**: Does it feature Docker, FastAPI, PyTest, Ruff linting, MyPy type checks, and CI/CD?
3. **Reproducibility**: Can a recruiter or staff engineer launch it in 1 command (`docker compose up`)?
4. **Recruiter Signal**: Does it directly map to open AI/ML Engineer job descriptions?
5. **Architectural Maturity**: Is the folder structure clean (`src/`, `tests/`, `docs/`, `examples/`)?

---

## 📊 Repository Classification & Action Matrix

| Original Repo | Current State | Classification | Action & Transformation Strategy | Targeted AI Role |
| :--- | :--- | :--- | :--- | :--- |
| `python-rent-calculator` | Basic Python expense script | **Refactor & Upgrade** | Transform into `ai-compute-cost-optimizer`: An AI Cloud & GPU Cost Optimization Engine utilizing constraint solvers, PyTorch VRAM estimation, and LLM API cost forecasting. | MLOps Engineer / Applied AI Engineer |
| `student-notes-app` | Simple web app | **Archive** | Move to `archive/` or make private. Lacks machine learning or AI depth. | N/A |
| `basic-ml-tutorials` | Notebook collection | **Merge & Re-architect** | Merge into `llm-fine-tuning-pipeline` or `deep-learning-benchmarks`. Convert raw `.ipynb` files into structured Python packages with PyTest. | ML Engineer / Research Engineer |
| `cv-face-detector` | Basic OpenCV script | **Refactor** | Refactor into `realtime-vision-edge-mlops`: Multi-object detection & tracking engine using YOLOv8, TensorRT acceleration, Triton inference server, and Streamlit UI. | Computer Vision Engineer |
| `simple-chatbot` | Basic OpenAI API wrapper | **Refactor** | Upgrade to `agentic-workflow-engine`: LangGraph-powered autonomous agent system with tool execution, memory, and Qdrant vector database. | Generative AI / LLM Engineer |
| `weather-script` | API script | **Delete** | Delete from public profile to reduce signal noise. | N/A |

---

## 🛠️ Detailed Refactoring Blueprint for `python-rent-calculator`

**From:** Basic single-file CLI script calculating shared rent.
**To:** `ai-compute-cost-optimizer` (Distributed GPU & LLM Cost Optimization Engine)

### Upgraded Architecture:
1. **Core Engine**: Pydantic v2 schemas calculating exact GPU VRAM requirements (KiB/MiB/GiB) for LLM inference (KV Cache, Batch Size, Sequence Length, Precision: FP32/FP16/BF16/INT8/INT4).
2. **Cost Solver**: LP/Integer Linear Programming optimizer using `SciPy`/`PuLP` to minimize cloud instance cost (AWS/GCP/Azure/Lambda Labs) given budget and latency constraints.
3. **FastAPI Service**: Production REST API endpoint `/api/v1/optimize-cost` with OpenAPI documentation and structured JSON logging.
4. **Production Stack**: FastAPI, Docker, PyTest, Ruff, MyPy, GitHub Actions CI/CD.
