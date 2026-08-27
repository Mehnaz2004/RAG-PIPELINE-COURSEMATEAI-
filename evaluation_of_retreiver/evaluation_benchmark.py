from datetime import datetime
from pathlib import Path

from vector_retriever import retrieve_vector
from hybrid_retriever import retrieve_hybrid


TOP_K = 5

TEST_CASES = [
    # ====== EXACT TECHNICAL TERM (4 cases) ======
    {
        "id": 1,
        "name": "Exact Python Concept: Polymorphism",
        "category": "exact_technical_term",
        "query": "What is polymorphism?",
        "user_id": "user_A",
        "expected_topic": "Python polymorphism",
        "notes": "Tests direct retrieval of a fundamental OOP concept.",
    },
    {
        "id": 2,
        "name": "Exact Python Concept: Inheritance",
        "category": "exact_technical_term",
        "query": "What is inheritance?",
        "user_id": "user_A",
        "expected_topic": "Python inheritance",
        "notes": "Tests retrieval of OOP inheritance concept.",
    },
    {
        "id": 3,
        "name": "Exact Python Concept: Modules",
        "category": "exact_technical_term",
        "query": "What is a Python module?",
        "user_id": "user_A",
        "expected_topic": "Python modules and imports",
        "notes": "Tests retrieval of module/import terminology.",
    },
    {
        "id": 4,
        "name": "Exact Python Concept: Classes",
        "category": "exact_technical_term",
        "query": "What is a Python class?",
        "user_id": "user_A",
        "expected_topic": "Python classes",
        "notes": "Tests direct class concept retrieval.",
    },

    # ====== KEYWORD / ACRONYM / TECHNICAL TOKEN (3 cases) ======
    {
        "id": 5,
        "name": "Keyword: Python Function",
        "category": "keyword_acronym",
        "query": "What does a Python function do?",
        "user_id": "user_A",
        "expected_topic": "Python functions",
        "notes": "Tests keyword-based matching for function concept.",
    },
    {
        "id": 6,
        "name": "Keyword: Flask Route",
        "category": "keyword_acronym",
        "query": "What is a route in Flask?",
        "user_id": "user_B",
        "expected_topic": "Flask routing",
        "notes": "Tests Flask-specific keyword retrieval.",
    },
    {
        "id": 7,
        "name": "Keyword: Python Dictionary",
        "category": "keyword_acronym",
        "query": "What is a dictionary?",
        "user_id": "user_A",
        "expected_topic": "Python dictionaries and data structures",
        "notes": "Tests retrieval of data structure terminology.",
    },

    # ====== PARAPHRASED QUERY (3 cases) ======
    {
        "id": 8,
        "name": "Paraphrased: Code Organization",
        "category": "paraphrased_query",
        "query": "How can Python code be structured so it can be reused across projects?",
        "user_id": "user_A",
        "expected_topic": "Python modules and reusability",
        "notes": "Semantic query testing module/import concepts without exact terminology.",
    },
    {
        "id": 9,
        "name": "Paraphrased: Building Web Applications",
        "category": "paraphrased_query",
        "query": "How do you create web pages that respond to user requests?",
        "user_id": "user_B",
        "expected_topic": "Flask web framework basics",
        "notes": "Tests semantic understanding of web routing without exact keyword.",
    },
    {
        "id": 10,
        "name": "Paraphrased: Object-Oriented Organization",
        "category": "paraphrased_query",
        "query": "How do you organize data and behaviors together in Python?",
        "user_id": "user_A",
        "expected_topic": "Classes and object-oriented programming",
        "notes": "Semantic query about OOP concepts without exact terminology.",
    },

    # ====== CONCEPTUAL / EXPLANATION QUERY (3 cases) ======
    {
        "id": 11,
        "name": "Conceptual: Purpose of Functions",
        "category": "conceptual_explanation",
        "query": "How do functions help organize a Python program?",
        "user_id": "user_A",
        "expected_topic": "Functions and program structure",
        "notes": "Tests retrieval of explanatory content about program organization.",
    },
    {
        "id": 12,
        "name": "Conceptual: Purpose of Flask",
        "category": "conceptual_explanation",
        "query": "What is the purpose of Flask?",
        "user_id": "user_B",
        "expected_topic": "Flask framework purpose and use cases",
        "notes": "Tests retrieval of framework overview and purpose.",
    },
    {
        "id": 13,
        "name": "Conceptual: Object-Oriented Design",
        "category": "conceptual_explanation",
        "query": "How does object-oriented programming help with writing better code?",
        "user_id": "user_A",
        "expected_topic": "OOP design principles and benefits",
        "notes": "Tests retrieval of conceptual explanations about OOP benefits.",
    },

    # ====== PROGRAMMING / API / CODE TERMINOLOGY (3 cases) ======
    {
        "id": 14,
        "name": "Programming: Import Statement",
        "category": "programming_api_terminology",
        "query": "What does an import statement do in Python?",
        "user_id": "user_A",
        "expected_topic": "Python imports and module loading",
        "notes": "Tests code-level terminology and mechanics.",
    },
    {
        "id": 15,
        "name": "Programming: Flask Decorators",
        "category": "programming_api_terminology",
        "query": "What is a decorator in Flask?",
        "user_id": "user_B",
        "expected_topic": "Python decorators and Flask usage",
        "notes": "Tests specific code construct terminology.",
    },
    {
        "id": 16,
        "name": "Programming: Object Attributes",
        "category": "programming_api_terminology",
        "query": "What are attributes of an object in Python?",
        "user_id": "user_A",
        "expected_topic": "Object attributes and instance variables",
        "notes": "Tests OOP terminology at code level.",
    },

    # ====== MULTI-DOCUMENT USER (3 cases) ======
    {
        "id": 17,
        "name": "Multi-Doc: Python Question for user_B",
        "category": "multi_document_user",
        "query": "What are Python exceptions?",
        "user_id": "user_B",
        "expected_topic": "Python exception handling (likely from Python.pdf)",
        "notes": "Tests that Python-related query correctly retrieves from Python.pdf when user has multiple docs.",
    },
    {
        "id": 18,
        "name": "Multi-Doc: Flask-Specific Question",
        "category": "multi_document_user",
        "query": "How do you handle HTTP requests in Flask?",
        "user_id": "user_B",
        "expected_topic": "Flask HTTP request handling (likely from Flask.pdf)",
        "notes": "Tests that Flask question retrieves from Flask.pdf when user has multiple docs.",
    },
    {
        "id": 19,
        "name": "Multi-Doc: General Web Development",
        "category": "multi_document_user",
        "query": "What is a web server?",
        "user_id": "user_B",
        "expected_topic": "Web server concepts (could be in either document)",
        "notes": "Tests retrieval relevance when concept may appear in multiple documents.",
    },

    # ====== EMPTY USER / NO DOCUMENTS (1 case) ======
    {
        "id": 20,
        "name": "Empty User: No Results Expected",
        "category": "empty_user",
        "query": "What is Python?",
        "user_id": "user_C",
        "expected_topic": "No results",
        "notes": "Verifies graceful handling of user with no indexed documents.",
    },
]


def _format_result(document):
    """Extract and format a single retrieval result."""
    metadata = document.metadata
    return {
        "filename": metadata.get("filename", "Unknown"),
        "document_id": metadata.get("document_id", "Unknown"),
        "page": metadata.get("page", "Unknown"),
        "content": document.page_content[:500],
    }


def _print_test_header(test_case):
    """Print concise test case header to terminal."""
    print("\n" + "=" * 70)
    print(f"TEST {test_case['id']}: {test_case['name']}")
    print(f"Category: {test_case['category']}")
    print(f"Query: {test_case['query']}")
    print(f"User: {test_case['user_id']}")
    print("=" * 70)


def _print_retrieval_results(title, results):
    """Print retrieval results to terminal."""
    print(f"\n{title}")
    if not results:
        print("No results.")
        return

    for rank, result in enumerate(results, start=1):
        print(f"\n  {rank}. {result['filename']} (Page {result['page']})")


def _markdown_result_block(rank, result):
    """Generate Markdown for a single result."""
    return (
        f"### Rank {rank}\n\n"
        f"- Filename: {result['filename']}\n"
        f"- Document ID: {result['document_id']}\n"
        f"- Page: {result['page']}\n\n"
        f"**Content:**\n\n"
        f"> {result['content'].replace(chr(10), chr(10) + '> ')}\n\n"
    )


def _markdown_retrieval_section(retriever_name, results):
    """Generate Markdown retrieval section."""
    lines = [f"## {retriever_name} Retrieval\n"]

    if not results:
        lines.append("No results.\n")
    else:
        for rank, result in enumerate(results, start=1):
            lines.append(_markdown_result_block(rank, result))

    lines.append(f"### Manual Evaluation — {retriever_name}\n")
    lines.append("- Top 1 relevant: Not evaluated\n")
    lines.append("- Top 3 relevant: Not evaluated\n")
    lines.append("- Notes:\n")
    lines.append("\n---\n")

    return "".join(lines)


def _build_markdown(all_results, timestamp):
    """Build complete Markdown report."""
    lines = [
        "# StudyLensAI Retrieval Benchmark\n",
        "\n",
        "## Experiment Information\n",
        "\n",
        f"- Timestamp: {timestamp}\n",
        f"- Number of test cases: {len(all_results)}\n",
        "- Vector database: Chroma\n",
        "- Embedding model: sentence-transformers/all-MiniLM-L6-v2\n",
        "- Vector retriever: Chroma similarity search\n",
        "- Hybrid retriever: Vector search + BM25 + Reciprocal Rank Fusion\n",
        "- Results per query: Top 5\n",
        "\n",
    ]

    # Test cases
    for idx, result in enumerate(all_results, start=1):
        test = result["test_case"]
        lines.extend([
            f"# Test Case {idx}: {test['name']}\n",
            "\n",
            f"**Category:** {test['category']}\n",
            "\n",
            "**Query:**\n",
            "\n",
            f"> {test['query']}\n",
            "\n",
            f"**User:** {test['user_id']}\n",
            "\n",
            f"**Expected Topic:** {test['expected_topic']}\n",
            "\n",
            "**Purpose:**\n",
            "\n",
            f"{test['notes']}\n",
            "\n",
            "---\n",
            "\n",
            _markdown_retrieval_section("Vector", result["vector_results"]),
            "\n",
            _markdown_retrieval_section("Hybrid", result["hybrid_results"]),
            "\n",
        ])

    # Summary table
    lines.extend([
        "# Benchmark Summary\n",
        "\n",
        "## Test Categories\n",
        "\n",
        "| Category | Number of Tests | Vector Observation | Hybrid Observation |\n",
        "|---|---:|---|---|\n",
    ])

    # Count by category
    category_counts = {}
    for result in all_results:
        cat = result["test_case"]["category"]
        category_counts[cat] = category_counts.get(cat, 0) + 1

    category_labels = {
        "exact_technical_term": "Exact technical term",
        "keyword_acronym": "Keyword / acronym",
        "paraphrased_query": "Paraphrased query",
        "conceptual_explanation": "Conceptual explanation",
        "programming_api_terminology": "Programming/API terminology",
        "multi_document_user": "Multi-document retrieval",
        "empty_user": "Empty user",
    }

    for cat, label in category_labels.items():
        count = category_counts.get(cat, 0)
        if count > 0:
            lines.append(f"| {label} | {count} | | |\n")

    lines.extend([
        "\n",
        "# Overall Evaluation\n",
        "\n",
        "## Vector Retrieval Strengths\n",
        "\n",
        "_To be completed manually._\n",
        "\n",
        "## Hybrid Retrieval Strengths\n",
        "\n",
        "_To be completed manually._\n",
        "\n",
        "## Failure Cases\n",
        "\n",
        "_To be completed manually._\n",
        "\n",
        "## Final Decision\n",
        "\n",
        "_To be completed after reviewing all test cases._\n",
        "\n",
        "Possible final decisions may include:\n",
        "\n",
        "- Keep vector-only retrieval\n",
        "- Use hybrid retrieval\n",
        "- Improve hybrid retrieval\n",
        "- Add reranking later\n",
        "- Use different strategies depending on query type\n",
        "\n",
    ])

    return "".join(lines)


def main():
    """Run the retrieval benchmark."""
    all_results = []
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    for test_case in TEST_CASES:
        _print_test_header(test_case)

        vector_results = [
            _format_result(doc)
            for doc in retrieve_vector(test_case["query"], test_case["user_id"], TOP_K)
        ]
        hybrid_results = [
            _format_result(doc)
            for doc in retrieve_hybrid(test_case["query"], test_case["user_id"], TOP_K)
        ]

        _print_retrieval_results("VECTOR RESULTS:", vector_results)
        _print_retrieval_results("HYBRID RESULTS:", hybrid_results)

        all_results.append({
            "test_case": test_case,
            "vector_results": vector_results,
            "hybrid_results": hybrid_results,
        })

    # Save Markdown report
    output_directory = Path("evaluation_results")
    output_directory.mkdir(exist_ok=True)
    output_path = output_directory / f"retrieval_benchmark_{timestamp}.md"
    output_path.write_text(_build_markdown(all_results, timestamp), encoding="utf-8")

    print("\n" + "=" * 70)
    print("BENCHMARK COMPLETE")
    print("=" * 70)
    print(f"Test cases executed: {len(TEST_CASES)}")
    print(f"\nResults saved to:\n{output_path}")
    print("=" * 70)


if __name__ == "__main__":
    main()
