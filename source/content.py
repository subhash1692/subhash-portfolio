"""Editable source content for Subhash's professional portfolio.
All representative case studies omit client-identifying implementation details.
"""
PROFILE = {
    "name": "Subhash",
    "title": "Principal / Lead Data Platform Architect",
    "email": "subhash1692@gmail.com",
    "github": "https://github.com/subhash1692",
    "linkedin": "https://www.linkedin.com/in/subhash-subhash-78b2a236/",
    "public_project": "https://github.com/subhash1692/azde-tfinfra-prj-template",
    "experience": "15+",
}

CASE_STUDIES = [
    {
        "slug": "enterprise-lakehouse",
        "number": "01",
        "category": "LAKEHOUSE ENGINEERING",
        "title": "From scattered sources to trusted data products.",
        "short": "A configuration-driven enterprise lakehouse pattern, designed for repeatable ingestion, reliable transformations, and governed consumption.",
        "chips": ["Azure Data Factory", "Databricks", "PySpark", "Delta Lake"],
        "accent": "mint",
        "lead": "Bringing new data domains online should not require reinventing an ingestion pipeline every time.",
        "context": "Enterprise data arrives from relational systems, document databases, file shares, and application APIs. Each source behaves differently, but the delivery platform still needs consistent scheduling, auditing, replay, and governance.",
        "responsibility": "I design both the reusable ingestion path and the transformations that turn source records into dependable analytical data. This includes source-specific adapters, common configuration, lakehouse transformations, and operational recovery patterns.",
        "approach": [
            ("Configure instead of duplicate", "Metadata-driven source definitions describe extraction modes, parameters, data quality rules, dependencies, and write strategies."),
            ("Build reliable incremental paths", "Full and incremental processing support deduplication, upserts, backfills, schema handling, and repeatable error recovery."),
            ("Separate stages by responsibility", "A medallion architecture organizes raw evidence, cleaned business entities, and modeled tables for downstream users."),
            ("Check correctness, not just execution", "Reconciliation checks compare volume, keys, aggregates, and expected change behavior before data is promoted."),
        ],
        "steps": ["Operational sources", "ADF / APIs", "ADLS + Delta", "Databricks processing", "Unity Catalog", "Analytics & applications"],
        "outcomes": ["Reusable source onboarding patterns", "Replayable and observable processing", "Governed, query-ready tables and semantic views"],
        "stack": "Azure Data Factory · ADLS Gen2 · Databricks · PySpark · Spark SQL · Delta Lake · Unity Catalog",
    },
    {
        "slug": "deployment-engineering",
        "number": "02",
        "category": "PLATFORM ENGINEERING & CI/CD",
        "title": "Deployment as a repeatable engineering system.",
        "short": "A release architecture that treats data workloads, permissions, applications, and infrastructure as reviewed, versioned assets.",
        "chips": ["Azure DevOps", "DABs", "Bicep / ARM", "Self-hosted agents"],
        "accent": "blue",
        "lead": "The difficult part of releasing a data platform is coordinating all the things that need to be true after deployment.",
        "context": "Modern data platforms mix notebooks, Python packages, SQL objects, permissions, ADF assets, Functions, deployment identities, and network-constrained infrastructure. A passing build alone does not prove a successful release.",
        "responsibility": "I build and maintain delivery workflows end-to-end: repository rules, linting and security checks, artifact packaging, environment configuration, self-hosted Linux agents, release pipelines, and production validation.",
        "approach": [
            ("Validate early", "Pull requests run focused linting, SQL/YAML checks, secret scans, restricted-file checks, and asset-bundle validation."),
            ("Build once; promote predictably", "Versioned wheels and deployment artifacts move through environments with explicit configuration and permissions."),
            ("Use declarative releases", "Databricks Asset Bundles, parameterized Azure deployments, and ordered idempotent SQL scripts define desired state."),
            ("Operate the runtime behind the runtime", "Provision and maintain self-hosted Azure DevOps deployment agents; perform scheduled quarterly Azure Data Factory Self-hosted Integration Runtime maintenance."),
        ],
        "steps": ["Pull request", "Quality gates", "Versioned artifacts", "Controlled promotion", "Verification", "Operational support"],
        "outcomes": ["Consistent releases across multiple environments", "Repeatable, auditable infrastructure and access changes", "Safer recovery when partial deployments fail"],
        "stack": "Azure DevOps · Databricks Asset Bundles · YAML · Python · Bash · Azure Bicep · ARM · Self-hosted agents · SHIR",
    },
    {
        "slug": "governance-access",
        "number": "03",
        "category": "GOVERNANCE & SELF-SERVICE",
        "title": "Make the safe path the easy path.",
        "short": "Identity, permissions, metadata, and controlled self-service built into the platform—not added after launch.",
        "chips": ["Unity Catalog", "Entra ID", "RBAC", "Key Vault"],
        "accent": "violet",
        "lead": "A platform is not usable just because resources were provisioned and a deployment reported success.",
        "context": "Cloud permissions, workspace membership, compute entitlements, storage access, and data grants are separate control planes. Misalignment leads to fragile onboarding and hard-to-diagnose production failures.",
        "responsibility": "I design domain and environment boundaries, automate Unity Catalog grants and related Azure permissions, and develop controlled provisioning and onboarding workflows for engineers, analysts, and data scientists.",
        "approach": [
            ("Separate access concerns", "Different identities and entitlements for deployment, workload execution, administration, and data consumption."),
            ("Review grants as code", "Catalog objects, external locations, and privileges are managed with idempotent, auditable scripts."),
            ("Enable bounded self-service", "Reusable templates and approval-aware workflows allow routine requests without persistent elevated access."),
            ("Verify the real outcome", "Access is tested as the intended user or service—not inferred from the success of a prior command."),
        ],
        "steps": ["Entra identities", "Azure RBAC", "Databricks workspace", "Unity Catalog", "Governed tables", "Approved consumers"],
        "outcomes": ["More consistent onboarding and access governance", "Auditable privilege and infrastructure changes", "Safer platform self-service and resource lifecycle management"],
        "stack": "Microsoft Entra ID · Managed Identity · Service Principals · Azure RBAC · Unity Catalog · Key Vault · Python · SQL",
    },
    {
        "slug": "production-genai",
        "number": "04",
        "category": "AI DATA PLATFORM ENGINEERING",
        "title": "Turn document AI prototypes into dependable jobs.",
        "short": "Configurable LLM extraction and classification pipelines with schema validation, retries, observability, and inference-cost discipline.",
        "chips": ["Python", "LLM endpoints", "JSON validation", "Databricks"],
        "accent": "amber",
        "lead": "An LLM demo becomes a platform capability only when it can be retried, audited, and run without wasting inference budget.",
        "context": "Document-processing workloads often encounter inconsistent outputs, network timeouts, rate limits, evolving field requirements, and uncertain rerun costs. Their outputs still need to integrate with governed analytical tables.",
        "responsibility": "I develop production-oriented document pipelines for classification, summarization, and structured field extraction, with per-use-case configuration and repeatable job packaging.",
        "approach": [
            ("Configuration per use case", "Prompts, model endpoints, extracted fields, and parsing rules are stored as controllable configuration."),
            ("Validate untrusted model output", "Schema checks, malformed-JSON handling, and explicit error states prevent silent downstream corruption."),
            ("Rerun only what changed", "Idempotency and processing-state checks avoid paying to reprocess documents unnecessarily."),
            ("Ship through the platform", "Python code and scheduled workflows are packaged, tested, and deployed with the same release disciplines as data jobs."),
        ],
        "steps": ["Documents", "Config + prompts", "LLM endpoint", "Schema checks", "Delta tables", "Downstream users"],
        "outcomes": ["Repeatable document processing with recoverable failures", "Structured data ready for governance and analytics", "Guardrails for inference cost and operational reliability"],
        "stack": "Python · REST APIs · LLM serving endpoints · Databricks jobs · Delta Lake · JSON schema checks · CI/CD",
    },
]

CAPABILITIES = [
    {"id":"01", "title":"Data platform architecture", "description":"Source-to-consumption design: ingestion, lakehouse patterns, semantic outputs, and resilient data contracts.", "tags":"ADF · Databricks · Delta · Iceberg"},
    {"id":"02", "title":"Platform delivery & automation", "description":"Reusable CI/CD, infrastructure as code, deployment agents, policies, testing, and release engineering.", "tags":"Azure DevOps · DABs · Bicep · Python"},
    {"id":"03", "title":"Governance that actually works", "description":"Identity-aware access, Unity Catalog, governed self-service, secure integrations, and explicit PII handling.", "tags":"Entra ID · RBAC · Unity Catalog"},
    {"id":"04", "title":"Production reliability & AI", "description":"Incident response, observability, performance and cost tuning, and operationally sound AI pipelines.", "tags":"Monitoring · PySpark · LLM pipelines"},
]

PRINCIPLES = [
    ("01", "Make it reproducible", "Environments, permissions, data transformations, and deployable assets should be repeatable from source control."),
    ("02", "Optimize for operators", "Recovery, lineage, logs, and clear ownership matter as much as the happy path."),
    ("03", "Prove data correctness", "A successful run is not a successful platform if the numbers are wrong."),
    ("04", "Build shared leverage", "Turn recurring engineering friction into useful libraries, templates, and self-service tooling."),
]
