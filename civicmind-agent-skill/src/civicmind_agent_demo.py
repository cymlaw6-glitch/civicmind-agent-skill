"""
CivicMind Agent Demo
A lightweight local demo that simulates a multi-agent intelligence workflow.

This demo does not call any external API. It is intended to demonstrate
workflow structure for GitHub review and token-plan application materials.
"""

from dataclasses import dataclass
from typing import List, Dict


@dataclass
class AgentResult:
    name: str
    output: str


class CivicMindDemo:
    def __init__(self, topic: str):
        self.topic = topic
        self.results: List[AgentResult] = []

    def run_agent(self, name: str, output: str):
        result = AgentResult(name=name, output=output)
        self.results.append(result)
        return result

    def run(self):
        self.run_agent(
            "Research Task Parser",
            f"Task type: industry / policy intelligence analysis. Topic: {self.topic}"
        )
        self.run_agent(
            "Information Collection Agent",
            "Collect policy files, news, reports, company materials and market signals."
        )
        self.run_agent(
            "Information Cleaning Agent",
            "Remove duplicates, low-quality commentary and weakly relevant fragments."
        )
        self.run_agent(
            "Source Credibility Agent",
            "Prioritize official documents, filings, company reports and institutional research."
        )
        self.run_agent(
            "Entity Extraction Agent",
            "Extract companies, policies, dates, regulators, funding events, products and risks."
        )
        self.run_agent(
            "Trend Reasoning Agent",
            "Infer policy direction, market demand, regulatory pressure and competitive intensity."
        )
        self.run_agent(
            "Risk Identification Agent",
            "Identify policy, compliance, business model, competition, funding and public opinion risks."
        )
        self.run_agent(
            "Strategy Generation Agent",
            "Generate role-specific recommendations for founders, investors and strategy teams."
        )
        self.run_agent(
            "Report Generation Agent",
            "Produce executive summary, evidence map, risk matrix and next actions."
        )
        self.run_agent(
            "Quality Evaluation Agent",
            "Check evidence support, uncertainty, logical consistency and missing information."
        )
        return self.results

    def print_report(self):
        print(f"# CivicMind Agent Demo Report: {self.topic}\n")
        for idx, result in enumerate(self.results, start=1):
            print(f"## {idx}. {result.name}")
            print(result.output)
            print()


if __name__ == "__main__":
    topic = "AI legal service industry entry analysis"
    demo = CivicMindDemo(topic)
    demo.run()
    demo.print_report()
