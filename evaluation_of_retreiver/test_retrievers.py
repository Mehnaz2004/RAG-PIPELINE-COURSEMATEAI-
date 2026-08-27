from datetime import datetime
from pathlib import Path

from hybrid_retriever import DEFAULT_CANDIDATE_K, retrieve_hybrid
from vector_retriever import retrieve_vector


TOP_K = 5

TEST_CASES = [
    {
        "name": "Exact technical terminology",
        "category": "Exact terminology",
        "query": "What is polymorphism?",
        "user_id": "user_A",
        "expected_topic": "Python polymorphism",
    },
    {
        "name": "Acronym or keyword",
        "category": "Acronym / keyword",
        "query": "What is an API?",
        "user_id": "user_B",
        "expected_topic": "API terminology",
    },
    {
        "name": "Natural language question",
        "category": "Paraphrased question",
        "query": "How does Python organize reusable code?",
        "user_id": "user_A",
        "expected_topic": "Python concepts",
    },
    {
        "name": "Concept explanation",
        "category": "Concept explanation",
        "query": "Explain the main idea behind Flask.",
        "user_id": "user_B",
        "expected_topic": "Flask concepts",
    },
    {
        "name": "Programming terminology",
        "category": "Programming / API terminology",
        "query": "What does a Python function do?",
        "user_id": "user_A",
        "expected_topic": "Python programming",
    },
    {
        "name": "User with no documents",
        "category": "Empty user scope",
        "query": "What is Python?",
        "user_id": "user_C",
        "expected_topic": "No results expected",
    },
]


def _result_data(document):
    metadata = document.metadata
    return {
        "filename": metadata.get("filename", "Unknown"),
        "document_id": metadata.get("document_id", "Unknown"),
        "page": metadata.get("page", "Unknown"),
        "content": document.page_content[:500],
    }


def _print_results(title, results):
    print(f"\n{title}\n")
    if not results:
        print("No results.")
        return

    for rank, result in enumerate(results, start=1):
        print(f"{rank}.")
        print(f"Filename: {result['filename']}")
        print(f"Document ID: {result['document_id']}")
        print(f"Page: {result['page']}")
        print(f"Content:\n{result['content']}\n")


def _markdown_results(results):
    if not results:
        return "No results.\n"

    sections = []
    for rank, result in enumerate(results, start=1):
        sections.append(
            f"### Rank {rank}\n\n"
            f"- Filename: {result['filename']}\n"
            f"- Document ID: {result['document_id']}\n"
            f"- Page: {result['page']}\n\n"
            f"**Content:**\n\n> {result['content'].replace(chr(10), chr(10) + '> ')}\n"
        )
    return "\n".join(sections)


def _build_markdown(evaluation_results, timestamp):
    lines = [
        "# StudyLensAI Retrieval Evaluation",
        "",
        "## Experiment Information",
        "",
        f"- Timestamp: {timestamp}",
        "- Vector database: Chroma",
        "- Embedding model: sentence-transformers/all-MiniLM-L6-v2",
        "- Vector retriever: Chroma similarity search",
        "- Hybrid retriever: Vector search + BM25 + Reciprocal Rank Fusion",
        f"- Final results per query: top {TOP_K}",
        f"- Candidate retrieval count: {DEFAULT_CANDIDATE_K}",
        "",
    ]

    for index, result in enumerate(evaluation_results, start=1):
        lines.extend([
            f"# Test {index}: {result['test_name']}",
            "",
            f"**Category:** {result['category']}",
            "",
            "**Query:**",
            f"> {result['query']}",
            "",
            f"**User ID:** {result['user_id']}",
            "",
            f"**Expected Topic:** {result['expected_topic']}",
            "",
            "---",
            "",
            "## Vector Retrieval Results",
            "",
            _markdown_results(result["vector_results"]),
            "",
            "---",
            "",
            "## Hybrid Retrieval Results",
            "",
            _markdown_results(result["hybrid_results"]),
            "",
            "---",
            "",
        ])

    lines.extend([
        "# Manual Evaluation Notes",
        "",
        "- Which retriever produced more relevant results?",
        "- Did hybrid improve exact terminology retrieval?",
        "- Did vector retrieval perform better for paraphrased queries?",
        "- Were there irrelevant results?",
        "- Were there duplicate or highly repetitive chunks?",
        "- Which approach would I choose based on this experiment?",
        "",
        "# Conclusion",
        "",
        "_To be completed after manual evaluation._",
        "",
    ])
    return "\n".join(lines)


def main():
    evaluation_results = []
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    for test_case in TEST_CASES:
        print("\n" + "=" * 60)
        print(f"TEST: {test_case['name']}")
        print(f"CATEGORY: {test_case['category']}")
        print(f"QUERY: {test_case['query']}")
        print(f"USER: {test_case['user_id']}")
        print(f"EXPECTED TOPIC: {test_case['expected_topic']}")
        print("=" * 60)

        vector_results = [
            _result_data(document)
            for document in retrieve_vector(
                test_case["query"], test_case["user_id"], TOP_K
            )
        ]
        hybrid_results = [
            _result_data(document)
            for document in retrieve_hybrid(
                test_case["query"], test_case["user_id"], TOP_K
            )
        ]

        _print_results("VECTOR RESULTS", vector_results)
        print("\n" + "-" * 60)
        _print_results("HYBRID RESULTS", hybrid_results)

        evaluation_results.append({
            "test_name": test_case["name"],
            "category": test_case["category"],
            "query": test_case["query"],
            "user_id": test_case["user_id"],
            "expected_topic": test_case["expected_topic"],
            "vector_results": vector_results,
            "hybrid_results": hybrid_results,
        })

    output_directory = Path("evaluation_results")
    output_directory.mkdir(exist_ok=True)
    output_path = output_directory / f"retrieval_evaluation_{timestamp}.md"
    output_path.write_text(
        _build_markdown(evaluation_results, timestamp),
        encoding="utf-8"
    )

    print("\n" + "=" * 60)
    print("EVALUATION COMPLETE")
    print("=" * 60)
    print(f"Results saved to: {output_path}")
    print("\nManually compare whether the retrieved chunks are relevant, whether hybrid improves exact terminology retrieval, and whether either retriever returns irrelevant or repetitive chunks.")


if __name__ == "__main__":
    main()