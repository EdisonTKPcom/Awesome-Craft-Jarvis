#!/usr/bin/env python3
import csv
import urllib.parse as U
from pathlib import Path

ROOT = Path(__file__).resolve().parent
S = {
    r[0]: dict(stars=int(r[1]), forks=int(r[2]), lic=r[3], lang=r[4], push=r[5])
    for r in csv.reader((ROOT / "stats.tsv").open(), delimiter="\t")
}
LICNAME = {"NOASSERTION": "Custom", "none": "None", "OTHER": "Custom"}
AS = "2026-11-15"
ACTIVE_SINCE = "2026-10-16"

C = [
    (
        "Interface and HUD",
        [
            ("AnythingLLM", "Mintplex-Labs/anything-llm", "All-in-one self-hosted app for chatting with documents and local or remote models, with an OpenAI-compatible API."),
            ("big-AGI", "enricoros/big-AGI", "Local TypeScript suite, built with a web UI, for chatting with local and remote models and running productivity tools."),
            ("Jan", "janhq/jan", "Desktop app for running models fully offline on your computer. GitHub reports no standard SPDX licence, so read the repository before you use it."),
            ("Khoj", "khoj-ai/khoj", "Self-hostable personal assistant that can answer questions from your files and the web."),
            ("LibreChat", "LibreChat-AI/LibreChat", "Self-hosted chat UI, written in TypeScript and React, with agents, MCP support and many model backends."),
            ("LobeHub", "lobehub/lobehub", "Web and desktop chat UI, formerly published as Lobe Chat, for talking to local and remote models. GitHub reports no standard SPDX licence, so read the repository before you use it."),
            ("NextChat", "ChatGPTNextWeb/NextChat", "Cross-platform chat app, built with Next.js, React and Tauri, that can talk to Ollama and other model backends."),
            ("Open WebUI", "open-webui/open-webui", "Self-hosted web interface for Ollama and OpenAI-compatible servers. GitHub reports no standard SPDX licence. The project uses a source-available licence with extra branding terms, so read it before you rename or redistribute the interface."),
            ("textgen", "oobabooga/textgen", "Local desktop app for running LLMs, with text, vision, tool calling and an OpenAI-compatible API. Previously published as text-generation-webui."),
        ],
    ),
    (
        "Brain and runtimes",
        [
            ("AutoGen", "microsoft/autogen", "Programming framework for multi-agent applications. GitHub reports a CC-BY-4.0 licence, which is a Creative Commons licence rather than a typical OSI software licence. Read the repository before you use it."),
            ("Claude Agent SDK (Python)", "anthropics/claude-agent-sdk-python", "Official Python SDK from Anthropic for building agents with the Claude Agent SDK. Read Anthropic's documentation for authentication and usage requirements."),
            ("Claude Agent SDK (TypeScript)", "anthropics/claude-agent-sdk-typescript", "Official TypeScript SDK from Anthropic for the Claude Agent SDK. GitHub reports no SPDX licence, so read the repository before you use it."),
            ("CrewAI", "crewAIInc/crewAI", "Python framework for composing role-based autonomous agents that work together on a task."),
            ("LangGraph", "langchain-ai/langgraph", "Library for building stateful, resilient agents as graphs, from the LangChain team."),
            ("llama.cpp", "ggml-org/llama.cpp", "C/C++ library and CLI for running large language models locally on CPUs and GPUs."),
            ("LocalAI", "mudler/LocalAI", "Self-hosted OpenAI-compatible API that can run language, vision and audio models on your own hardware."),
            ("Ollama", "ollama/ollama", "Easy local runner and API for downloading and serving open models on your machine."),
            ("Open Interpreter", "openinterpreter/openinterpreter", "The Open Interpreter project, a local coding agent that can run open models and use tools on your machine."),
            ("Pydantic AI", "pydantic/pydantic-ai", "Python agent framework from the Pydantic team, with typed tools and support for several model providers."),
            ("smolagents", "huggingface/smolagents", "Small Python library from Hugging Face for building agents that write and run code as their actions."),
            ("vLLM", "vllm-project/vllm", "High-throughput inference and serving engine for large language models."),
        ],
    ),
    (
        "Speech to text",
        [
            ("faster-whisper", "SYSTRAN/faster-whisper", "Faster reimplementation of OpenAI Whisper transcription, built on CTranslate2."),
            ("sherpa-onnx", "k2-fsa/sherpa-onnx", "On-device speech toolkit with speech-to-text, text-to-speech and related tasks, using ONNX Runtime."),
            ("Vosk", "alphacep/vosk-api", "Offline speech recognition API that can run on servers, desktops and small devices such as a Raspberry Pi."),
            ("Whisper", "openai/whisper", "OpenAI's open-source speech recognition model and inference code, widely used as a local transcriber."),
            ("whisper.cpp", "ggml-org/whisper.cpp", "C/C++ port of Whisper for running speech recognition locally with no Python dependency."),
            ("WhisperX", "m-bain/whisperX", "Whisper-based transcription with word-level timestamps and speaker alignment."),
        ],
    ),
    (
        "Text to speech",
        [
            ("Chatterbox", "resemble-ai/chatterbox", "Open-source text-to-speech model and inference code from Resemble AI."),
            ("Coqui TTS (Idiap fork)", "idiap/coqui-ai-TTS", "Maintained community fork, hosted by Idiap, of the Coqui deep-learning text-to-speech toolkit. The original coqui-ai/TTS repository was last pushed on 2024-08-16."),
            ("F5-TTS", "SWivid/F5-TTS", "Open-source text-to-speech model and official inference code for F5-TTS."),
            ("Fish Speech", "fishaudio/fish-speech", "Open-source text-to-speech project. GitHub reports no standard SPDX licence, so read the repository, including any model terms, before you use it commercially."),
            ("Kokoro", "hexgrad/kokoro", "Lightweight open-source text-to-speech model and inference code. Last pushed on 2025-08-06."),
            ("Kokoro ONNX", "thewh1teagle/kokoro-onnx", "Local text-to-speech runtime that serves Kokoro models through ONNX Runtime."),
            ("Piper 1", "OHF-Voice/piper1-gpl", "Fast, local neural text-to-speech engine from the Open Home Foundation, the maintained successor to the archived rhasspy/piper project. The code is GPL-3.0."),
        ],
    ),
    (
        "Wake word",
        [
            ("Mycroft Precise", "MycroftAI/mycroft-precise", "Lightweight recurrent wake-word listener from the Mycroft project. Last pushed on 2023-11-25, so review whether it still meets your needs."),
            ("openWakeWord", "dscripka/openWakeWord", "Open-source wake-word and wake-phrase detection framework intended to be simple to train and run locally."),
            ("Porcupine", "Picovoice/porcupine", "On-device wake-word detection library. Read the licence before commercial use, including any terms that apply beyond the SPDX identifier GitHub reports."),
        ],
    ),
    (
        "Voice assistants",
        [
            ("Home Assistant", "home-assistant/core", "Open-source home automation platform, including a voice assistant that can run speech locally over the Wyoming protocol."),
            ("Leon", "leon-ai/leon", "Self-hosted personal assistant with a web interface, skills and a local-first design."),
            ("Linux Voice Assistant", "OHF-Voice/linux-voice-assistant", "Voice satellite for Home Assistant on Linux, using the ESPHome protocol, from the Open Home Foundation."),
            ("Mycroft", "MycroftAI/mycroft-core", "Archived core of the Mycroft voice assistant. Prefer OpenVoiceOS for current development. This snapshot last saw a push on 2024-09-08."),
            ("OpenVoiceOS", "OpenVoiceOS/ovos-core", "Active open-source voice assistant platform that continues the Mycroft core as a community fork."),
            ("Wyoming", "OHF-Voice/wyoming", "Peer-to-peer protocol and Python library used to connect local speech services to Home Assistant and other voice assistants."),
        ],
    ),
    (
        "Connections and MCP",
        [
            ("Composio", "ComposioHQ/composio", "Platform and open-source tooling that exposes a large set of third-party toolkits, including CRM, calendar, email and social APIs, to agents. Authorize each account yourself and keep tokens off Git."),
            ("FastMCP", "PrefectHQ/fastmcp", "Python framework, now maintained under Prefect, for building MCP servers and clients."),
            ("GitHub MCP Server", "github/github-mcp-server", "Official GitHub MCP server for letting an agent work with repositories and issues that you have authorized."),
            ("MCP Inspector", "modelcontextprotocol/inspector", "Official deterministic testing and inspection tools for MCP servers, useful when you are checking what a server is allowed to do. GitHub reports no standard SPDX licence, so read the repository before you use it."),
            ("MCP Python SDK", "modelcontextprotocol/python-sdk", "Official Python SDK for building Model Context Protocol servers and clients."),
            ("MCP Reference Servers", "modelcontextprotocol/servers", "Official reference MCP servers for connecting an agent to local files and to third-party services such as mail or chat, with your own credentials. GitHub reports no standard SPDX licence, so read the repository, including the licence of each bundled server, before you deploy one."),
            ("MCP TypeScript SDK", "modelcontextprotocol/typescript-sdk", "Official TypeScript SDK for building Model Context Protocol servers and clients. GitHub reports no standard SPDX licence, so read the repository before you use it."),
        ],
    ),
    (
        "Memory and knowledge",
        [
            ("Chroma", "chroma-core/chroma", "Open-source embedding database for storing and searching vectors used by assistants and RAG pipelines."),
            ("Faiss", "facebookresearch/faiss", "Library from Meta for efficient similarity search and clustering of dense vectors."),
            ("Graphiti", "getzep/graphiti", "Framework for building real-time knowledge graphs that agents can query as memory."),
            ("GraphRAG", "microsoft/graphrag", "Modular graph-based retrieval-augmented generation system from Microsoft."),
            ("LanceDB", "lancedb/lancedb", "Embedded multimodal retrieval library and vector store that can run next to an application."),
            ("Letta", "letta-ai/letta", "Platform for stateful agents with a long-term memory system, originally known as MemGPT."),
            ("LlamaIndex", "run-llama/llama_index", "Document processing and retrieval framework for connecting files and data sources to language models."),
            ("Mem0", "mem0ai/mem0", "Memory layer for AI agents that stores and retrieves long-term context across sessions."),
        ],
    ),
]

INTRO = {
    "Interface and HUD": "Local and self-hosted chat interfaces and heads-up dashboards you can run on your own machine, including React and other web or desktop UIs.\n",
    "Brain and runtimes": "Model runtimes you can host locally, plus agent frameworks that can plan, call tools and keep a loop going. Several of these can also use a hosted API. Read each project's authentication docs; this list does not claim that any of them is free to run.\n",
    "Speech to text": "Local and self-hostable speech recognition tools, from Whisper and its faster ports to Vosk and on-device ONNX runtimes.\n",
    "Text to speech": "Local neural text-to-speech engines, including Kokoro, Piper, Coqui and other open models. Check model licences as well as the inference code.\n",
    "Wake word": "On-device detectors that can listen for a wake word or phrase before the rest of the assistant starts recording.\n",
    "Voice assistants": "Full voice-assistant stacks, including Home Assistant voice, the Wyoming protocol that replaced much of Rhasspy, Leon, and Mycroft's archived core with its OpenVoiceOS successor.\n",
    "Connections and MCP": "Connect an assistant only to accounts you control. Keep OAuth tokens and API keys in a local dotfolder, never in Git or in a page the browser can read. Start each server read-only, and switch on write access per server only when you need it.\n",
    "Memory and knowledge": "Stores and frameworks that let an assistant keep long-term context, including memory layers, knowledge graphs and vector databases.\n",
}

RELATED = [
    ("Awesome Craft", "Awesome-Craft", "A curated list of open-source, self-hostable alternatives to popular SaaS tools."),
    ("Awesome Craft Agents", "Awesome-Craft-Agents", "A curated list of open-source chat apps, coding agents, self-hosted agent bots, workflow automation and image-generation UIs."),
    ("Awesome Craft AI", "Awesome-Craft-AI", "A curated list of open-source, self-hostable AI runtimes, servers, Hugging Face libraries and related infrastructure."),
    ("Awesome Craft BSC", "Awesome-Craft-BSC", "A curated list of verified open-source clients, SDKs, dev tools and protocol code for BNB Smart Chain and opBNB."),
    ("Awesome Craft CUDA", "Awesome-Craft-CUDA", "A curated list of open-source CUDA learning material, kernel libraries, tooling and portability projects."),
    ("Awesome Craft DeepSeek", "Awesome-Craft-DeepSeek", "A curated list of official DeepSeek repositories and open-source harnesses, serving engines, eval tools and fine-tuning stacks that work with DeepSeek models."),
    ("Awesome Craft DevOps", "Awesome-Craft-DevOps", "A curated list of open-source, self-hostable alternatives to popular DevOps and hosting SaaS tools."),
    ("Awesome Craft DNA", "Awesome-Craft-DNA", "A curated list of open-source tools for DNA, genomics and synthetic biology."),
    ("Awesome Craft Ethereum", "Awesome-Craft-Ethereum", "A curated list of verified open-source Ethereum clients, SDKs, dev frameworks, wallets and security tools."),
    ("Awesome Craft EV", "Awesome-Craft-EV", "A curated list of open-source software and hardware for electric vehicles and charging."),
    ("Awesome Craft Hardware", "Awesome-Craft-Hardware", "A curated list of open-source tools for PCB, FPGA, ASIC and chip design."),
    ("Awesome Craft Hyperliquid", "Awesome-Craft-Hyperliquid", "A curated list of verified open-source SDKs, node tools, analytics and community libraries for the Hyperliquid ecosystem."),
    ("Awesome Craft Malaysia", "Awesome-Craft-Malaysia", "A curated list of open-source tools useful to Malaysian SMEs, with verified MyInvois support called out separately."),
    ("Awesome Craft Mars", "Awesome-Craft-Mars", "A curated list of open-source tools and open data for Mars missions and settlement planning."),
    ("Awesome Craft Neuro", "Awesome-Craft-Neuro", "A curated list of open-source tools for brain-computer interfaces, electrophysiology and neurotechnology."),
    ("Awesome Craft Robotics", "Awesome-Craft-Robotics", "A curated list of open-source robotics software and hardware, including Microduck, Unitree SDKs, open humanoids, arms, simulation and middleware."),
    ("Awesome Craft Solana", "Awesome-Craft-Solana", "A curated list of verified open-source Solana clients, SDKs, frameworks, explorers and program libraries."),
    ("Awesome Craft Space", "Awesome-Craft-Space", "A curated list of open-source tools for spaceflight and rockets, covering orbit simulation, telemetry, launch data and more."),
    ("Awesome Craft Starlink", "Awesome-Craft-Starlink", "A curated list of open-source tools for Starlink and other LEO satellite internet systems."),
    ("Awesome Craft Web3", "Awesome-Craft-Web3", "A curated list of open-source DEX protocol code, self-custody software, indexers, frameworks and Blockchain infrastructure."),
]


def k(n):
    if n >= 1e6:
        return f"{n/1e6:.2f}M"
    if n >= 1000:
        return f"{n/1000:.1f}k"
    return str(n)


def anchor(n):
    return n.lower().replace(",", "").replace(" ", "-")


def fact(text):
    return f'<span class="ev-fact">{text}</span>'


def estimate(text):
    return f'<span class="ev-est">{text}</span>'


def safety_section():
    return """## Safety and operations

A local assistant can still leak secrets, send mail, change files or keep a microphone open. This section is guidance, not a setup guide, a security audit or legal advice.

- Keep API keys, OAuth tokens and service credentials in a local folder such as `~/.jarvis` (or another dotfolder on disk), with permissions limited to your user account. Never commit secrets, never put them in a public gist, and never ship them in a client-side bundle or a page the browser can read.
- Treat every connected MCP server and skill as read-only until you explicitly allow changes for that server. A calendar or mail server that can send or delete is a different risk from one that can only read.
- Provide `boot`, `stop` and `doctor` scripts (or the equivalent) so you can start the stack, shut it down, and run a PASS/FAIL health check without guessing at process state.
- Do not run an assistant, agent SDK or MCP host with permission checks disabled or in a bypass-permissions mode. If a tool cannot do its job without a bypass, do not run that tool until you understand and accept the specific permission it needs.
- Voice assistants and always-on microphones record audio in your home or office. Review what is stored, where it is processed (on the machine versus a remote API), and who can access the transcript.
- The MCP Inspector entry in Connections and MCP is one way to inspect what a server exposes before you grant it write access.

"""


def inspiration_section():
    return """## Inspiration

The category layout of this list (interface, brain, voice, connections, memory, and a safety section) was inspired by a public social post about running a JARVIS-style assistant on a local machine. The post is not a source of tools, claims or setup instructions, and this list does not reproduce its prompts, artwork or product pitches.

"""


def related_section():
    lines = [
        "## Related lists\n",
        "Other lists in the Awesome Craft series:\n",
    ]
    for name, repo, desc in RELATED:
        if not desc.endswith("."):
            desc += "."
        lines.append(f"- [{name}](https://github.com/EdisonTKPcom/{repo}) - {desc}")
    lines.append("")
    return "\n".join(lines) + "\n"


tools = [t for _, ts in C for t in ts]
missing = [t[1] for t in tools if t[1] not in S]
if missing:
    raise SystemExit(f"missing stats for: {missing}")
dupes = [repo for repo in [t[1] for t in tools] if [t[1] for t in tools].count(repo) > 1]
if dupes:
    raise SystemExit(f"duplicate repos: {sorted(set(dupes))}")

tot = sum(S[t[1]]["stars"] for t in tools)
forks = sum(S[t[1]]["forks"] for t in tools)
langs = sorted({S[t[1]]["lang"] for t in tools if S[t[1]]["lang"] not in ("", "none")})
active = sum(1 for t in tools if S[t[1]]["push"] >= ACTIVE_SINCE)

o = []
o.append(
    f"""<div align="center">

# Awesome Craft Jarvis [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> A curated list of open-source tools to run a personal JARVIS-style AI assistant locally, including dashboards, agent runtimes, voice, MCP connections and memory.

<img src="assets/craft-jarvis.svg" alt="Pixel-art heads-up display with a status ring, sidebar cards and a voice waveform, labelled CRAFT JARVIS" width="100%">

![Tools](https://img.shields.io/badge/tools-{len(tools)}-6366f1?style=for-the-badge)
[![Categories](https://img.shields.io/badge/categories-{len(C)}-0ea5e9?style=for-the-badge)](#contents)
[![Combined stars](https://img.shields.io/badge/combined_stars-{k(tot)}-f59e0b?style=for-the-badge&logo=github)](#-leaderboard)
[![Stars](https://img.shields.io/github/stars/EdisonTKPcom/Awesome-Craft-Jarvis?style=for-the-badge&color=22c55e)](https://github.com/EdisonTKPcom/Awesome-Craft-Jarvis/stargazers)
[![Last commit](https://img.shields.io/github/last-commit/EdisonTKPcom/Awesome-Craft-Jarvis?style=for-the-badge&color=ec4899)](https://github.com/EdisonTKPcom/Awesome-Craft-Jarvis/commits/main)

</div>

Open-source tools now cover most of a personal assistant stack you can run on your own machine: chat and HUD interfaces, local model runtimes and agent frameworks, speech input and output, connectors for accounts you already use, and memory stores. Every GitHub entry below was checked on {AS}. Check each project's licence before you deploy or sell anything built on it.

**Safety:** a local assistant can still leak secrets, send mail, change files or keep a microphone open. Keep credentials in a local dotfolder and out of Git, treat connected servers as read-only until you allow changes, and do not run tools with permission checks disabled. This list is not a setup guide, a security audit or legal advice.

## Contents
"""
)
o += ["- [Dashboard](#dashboard)"] + [f"- [{n}](#{anchor(n)})" for n, _ in C]
o += [
    "- [Safety and operations](#safety-and-operations)",
    "- [Inspiration](#inspiration)",
    "- [Related lists](#related-lists)",
    "- [Star history](#star-history)",
]
o.append("\n## Dashboard\n")
o.append(
    f"""<style>
.ev-fact{{border-bottom:3px solid #0f172a;padding-bottom:1px}}
.ev-goal{{border-bottom:3px dashed #0f172a;padding-bottom:1px}}
.ev-est{{border-bottom:3px dotted #0f172a;padding-bottom:1px}}
</style>

<table>
<tr>
<td align="center"><h2>{fact(str(len(tools)))}</h2>listed projects</td>
<td align="center"><h2>{fact(str(len(C)))}</h2>categories</td>
<td align="center"><h2>{estimate(k(tot))}</h2>combined GitHub stars</td>
<td align="center"><h2>{estimate(k(forks))}</h2>combined forks</td>
<td align="center"><h2>{estimate(f"{active}/{len(tools)}")}</h2>pushed in the last 30 days</td>
<td align="center"><h2>{fact(str(len(langs)))}</h2>languages</td>
</tr>
</table>

**Evidence tags**

<table>
<tr><th>Tag</th><th>Style</th><th>Meaning</th></tr>
<tr><td><span class="ev-fact">FACT</span></td><td>solid underline</td><td>A measured figure, with the source named.</td></tr>
<tr><td><span class="ev-goal">GOAL</span></td><td>dashed underline</td><td>A stated roadmap, price, ship date or plan, not a result.</td></tr>
<tr><td><span class="ev-est">ESTIMATE</span></td><td>dotted underline</td><td>A sum or count we computed from the facts.</td></tr>
</table>

This snapshot's dashboard has no GOAL figures. None of the dashboard numbers come from project roadmaps.

**Sources and method**

- Star counts, fork counts, licences, primary languages and last-push dates are {fact("FACT")} values from the GitHub REST API (`GET /repos/{{owner}}/{{repo}}`) on {AS}.
- Combined stars ({estimate(k(tot))}) and combined forks ({estimate(k(forks))}) are {estimate("ESTIMATE")}s: the arithmetic sum of those per-repository FACT counts, with no weighting and no unique-user deduplication. A person who stars two projects is counted twice.
- Pushed in the last 30 days ({estimate(f"{active}/{len(tools)}")}) is an {estimate("ESTIMATE")}: the number of listed repositories whose FACT `pushed_at` date is on or after {ACTIVE_SINCE}.
- Language and category counts, and the licence badges, are {estimate("ESTIMATE")}s of FACT fields. Star badges next to each entry update live and may differ from this snapshot.
"""
)
top = sorted(tools, key=lambda t: -S[t[1]]["stars"])[:10]
mx = S[top[0][1]]["stars"]
o.append(
    '### 🏆 Leaderboard\n\nStar counts in this table are FACT values from the snapshot. The bars are only a visual scale.\n\n<table>\n<tr><th>Rank</th><th>Project</th><th>Kind</th><th align="right">Stars</th><th></th></tr>'
)
kind = {t[1]: n for n, ts in C for t in ts}
for i, t in enumerate(top, 1):
    s = S[t[1]]["stars"]
    bar = "█" * max(1, round(s / mx * 20))
    medal = ["🥇", "🥈", "🥉"][i - 1] if i < 4 else i
    o.append(
        f'<tr><td align="center">{medal}</td><td><b>{t[0]}</b></td><td>{kind[t[1]]}</td><td align="right">{fact(k(s))}</td><td><code>{bar}</code></td></tr>'
    )
o.append("</table>\n")
o.append("\n### Stars by category\n")
o.append(
    "These category totals are ESTIMATE sums of the per-repository FACT star counts.\n\n```mermaid\npie showData\n    title Combined GitHub stars by category"
)
for n, ts in C:
    o.append(f'    "{n}" : {sum(S[t[1]]["stars"] for t in ts)}')
o.append("```\n")
lc = {}
for t in tools:
    L = LICNAME.get(S[t[1]]["lic"], S[t[1]]["lic"])
    lc[L] = lc.get(L, 0) + 1
o.append(
    "### Licences\n\n"
    + " ".join(
        f"![{L}](https://img.shields.io/badge/{U.quote(str(L).replace('-', '--'))}-{c}-64748b?style=flat-square)"
        for L, c in sorted(lc.items(), key=lambda x: -x[1])
    )
    + "\n\nThese badge counts are ESTIMATE tallies of the SPDX identifier GitHub returned for each repository. "
    + '"Custom" or "None" means GitHub could not match a standard SPDX licence. '
    + "Some projects also ship model or branding terms alongside the code, which are flagged in the entry. "
    + "Read each project licence before you use it commercially.\n"
)

for n, ts in C:
    o.append(f"## {n}\n")
    if n in INTRO:
        o.append(INTRO[n])
    for t in ts:
        desc = t[2]
        if not desc.endswith("."):
            desc += "."
        o.append(
            f"- [{t[0]}](https://github.com/{t[1]}) - {desc} ![Stars](https://img.shields.io/github/stars/{t[1]}?style=flat-square&label=%E2%AD%90)"
        )
    o.append("")
o.append(safety_section())
o.append(inspiration_section())
o.append(related_section())
o.append(
    "## Star history\n\n"
    "[![Star History Chart](https://api.star-history.com/chart?repos=EdisonTKPcom/Awesome-Craft-Jarvis&amp;type=Date)](https://www.star-history.com/#EdisonTKPcom/Awesome-Craft-Jarvis&Date)\n"
)
o.append(
    "## Contributing\n\nContributions welcome! Read the [contribution guidelines](contributing.md) first.\n\n"
    '<div align="center">\n\n'
    "If this list helped you find a tool, give it a ⭐ so others can find it.\n\n"
    "</div>\n"
)
(ROOT / "README.md").write_text("\n".join(o))
print(
    f"wrote README.md tools={len(tools)} stars={tot} "
    f"forks={forks} langs={len(langs)} active={active}/{len(tools)}"
)
for n, ts in C:
    print(f"  {n}: {len(ts)}  stars={sum(S[t[1]]['stars'] for t in ts)}")
