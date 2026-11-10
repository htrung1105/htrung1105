<p align="center">
  <img src="assets/banner.svg" width="100%" alt="Nguyễn Lê Hoàng Trung. AI Engineer and AI Researcher. Retrieval systems, from the index to the API.">
</p>

<p align="center">
  <a href="https://htrung1105.github.io"><img alt="Portfolio" src="https://img.shields.io/badge/Portfolio-htrung1105.github.io-0f4c81?style=flat-square"></a>
  <a href="https://www.linkedin.com/in/trungnlh/"><img alt="LinkedIn" src="https://img.shields.io/badge/LinkedIn-trungnlh-0a66c2?style=flat-square"></a>
  <a href="https://doi.org/10.1007/978-981-92-2587-3_24"><img alt="Springer paper" src="https://img.shields.io/badge/Springer-SOICT%202025%20paper-5c6bc0?style=flat-square"></a>
</p>

<p align="center">
  <img alt="RAG and GraphRAG. LLM agents. Multimodal retrieval. Document OCR. Open to AI Engineer internships." src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=500&size=20&duration=2600&pause=900&color=2F81F7&center=true&vCenter=true&width=640&lines=RAG+and+GraphRAG+systems;LLM+agents+with+cited+answers;Multimodal+video+retrieval;Document+OCR;Open+to+AI+Engineer+internships">
</p>

Final-year Artificial Intelligence student at VNU-HCM University of Science. I build retrieval systems end to end: RAG and GraphRAG, LLM agents, and document OCR. I am looking for an AI Engineer internship.

<table>
  <tr>
    <td align="center" width="25%"><h3>353,746</h3>legal documents in the GraphRAG knowledge graph</td>
    <td align="center" width="25%"><h3>+30.2%</h3>OCR H-mean on NomNaOCR (0.731 to 0.952)</td>
    <td align="center" width="25%"><h3>Best Presentation</h3>SOICT 2025</td>
    <td align="center" width="25%"><h3>2nd Prize</h3>ICPC Southern Region 2024</td>
  </tr>
</table>

## Selected work

### [Vietnamese Legal GraphRAG](https://github.com/ductai05/VietLegalGraphRAG) · [demo video](https://www.youtube.com/watch?v=CkdYwaeIEU8)

Legal Q&A with structured citations and expiry warnings, built by a team of five. 353,746 documents become about 7.48 million chunks, searched through Elasticsearch and expanded through a Neo4j knowledge graph.

`Legal question` → `Hybrid search (BM25 + dense)` → `RRF and reranking` → `Neo4j graph expansion` → `LLM answer` → `Structured citations`

**My part:** the knowledge graph pipeline, hybrid retrieval and its evaluation scripts, the LangGraph agent service, and CI/CD.

### [KPTER: K-Pointer for Temporal Event Retrieval](https://doi.org/10.1007/978-981-92-2587-3_24)

Zero-shot event retrieval over video, combining OCR, ASR, semantic embeddings and object detection. Published in Springer CCIS vol. 2913 (SOICT 2025). Team WATLERE ranked Top 12 of 80+ at AI Challenge HCMC 2025.

**My part:** co-author with equal contribution. I worked on the multimodal indexing pipeline and the search backend and API.

### [Sino-Nom Historical OCR](https://github.com/ductai05/NLP-ChineseOCR)

Text detection for degraded Sino-Nom documents using a fine-tuned PP-OCRv5 model. H-mean rose from 0.731 to 0.952, with 0.966 precision on the NomNaOCR test set.

**My part:** the fine-tuning and evaluation notebooks.

### [TradingClaw](https://github.com/ductai05/TradingClaw)

A team-built trading assistant that runs against the Binance Testnet sandbox.

**My part:** the FastAPI backend, the gateway to the ML services (FinBERT, Kronos, Isolation Forest), Gemini integration, and per-request LLM token and cost logging.

## Tools

<p align="center">
  <img alt="Python, C++, PyTorch, FastAPI, PostgreSQL, Elasticsearch, Docker, GitHub Actions, Git, Linux" src="https://skillicons.dev/icons?i=python,cpp,pytorch,fastapi,postgres,elasticsearch,docker,githubactions,git,linux&perline=10">
</p>

<p align="center">Also: LangChain · LangGraph · GraphRAG · Neo4j · PaddlePaddle · SQL</p>

## Honors

- **Best Presentation Award**, SOICT 2025
- **2nd Prize**, ICPC Southern Region 2024, and contestant at the ICPC Vietnam National round
- **Consolation Prize**, Vietnamese National Olympiad in Informatics 2023

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/htrung1105/htrung1105/output/github-snake-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/htrung1105/htrung1105/output/github-snake.svg">
  <img alt="Animation of a snake eating the GitHub contribution graph" src="https://raw.githubusercontent.com/htrung1105/htrung1105/output/github-snake.svg" width="100%">
</picture>
